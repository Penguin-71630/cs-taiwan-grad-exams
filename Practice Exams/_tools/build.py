"""Build one topic PDF from a source folder.

Source layout:
  _src/<group>/<chapter>/<chapter> - <topic>/manifest.json
                  unit metadata + questions (id, year, school, paper, qnum, url)
  _src/_q/<id>.md hand transcription (Markdown + LaTeX math), one per question, shared by
                  every unit the question is tagged with.
                  A line `<!-- fig x0 y0 x1 y1 -->` (fractions of the deskewed original image)
                  embeds that crop of the original -- used only for figures/diagrams,
                  which are never redrawn.
  _src/_q/deskew.json  detected skew angle per image (only images that figures are cropped from)

Images are downloaded to a cache dir (default ~/.cache/tiku, override with TIKU_CACHE);
originals in <cache>/orig are never modified, corrected copies go to <cache>/fixed.

Usage: python build.py SRC_DIR OUT_PDF
"""
import json, os, re, subprocess, sys, urllib.request
from pathlib import Path

sys.path.insert(0, os.path.dirname(__file__))
from deskew import estimate  # noqa: E402
from PIL import Image  # noqa: E402
import typst  # noqa: E402

MAX_PX = 2000
THRESHOLD = 0.75  # degrees; only obvious skew is corrected
FONT_DIRS = [os.environ.get("TIKU_FONTS", "/root/fonts")]
CACHE = Path(os.environ.get("TIKU_CACHE", Path.home() / ".cache" / "tiku"))
UA = "Mozilla/5.0 (practice-workbook builder)"

FONTS = {
    "計系": '("Times New Roman", "Noto Serif TC")',
    "資演": '("New Computer Modern", "Noto Serif TC")',
    "數學": '("New Computer Modern", "Noto Serif TC")',
    "英文": '("Times New Roman", "Noto Serif TC")',
}
SCHOOL_ORDER = {"台大": 0, "清大": 1, "交大": 2}


def qkey(q):
    m = re.search(r"\d+", q["qnum"])
    return (q["year"], SCHOOL_ORDER.get(q["school"], 9), q["paper"], int(m.group()) if m else 0, q["qnum"])


def fetch(q):
    orig = CACHE / "orig" / f"{q['id']}.webp"
    if not orig.exists():
        orig.parent.mkdir(parents=True, exist_ok=True)
        req = urllib.request.Request(q["url"], headers={"User-Agent": UA})
        data = urllib.request.urlopen(req, timeout=60).read()
        orig.write_bytes(data)
    return orig


def prepare_image(q, skew):
    orig = fetch(q)
    out = CACHE / "fixed" / f"{q['id']}.jpg"
    im = Image.open(orig).convert("RGB")
    if q["id"] not in skew:
        ang = estimate(im)
        skew[q["id"]] = {"angle": ang, "corrected": abs(ang) >= THRESHOLD}
    info = skew[q["id"]]
    if not out.exists():
        out.parent.mkdir(parents=True, exist_ok=True)
        if info["corrected"]:
            im = im.rotate(info["angle"], resample=Image.BICUBIC, expand=True, fillcolor=(255, 255, 255))
        if max(im.size) > MAX_PX:  # ~300 dpi at the 17 cm text width is plenty for print
            r = MAX_PX / max(im.size)
            im = im.resize((round(im.width * r), round(im.height * r)), Image.LANCZOS)
        im.save(out, quality=88, optimize=True)
    w, h = Image.open(out).size
    return out, w, h, info


FIG_RE = re.compile(r"^<!--\s*fig\s+([\d.]+)\s+([\d.]+)\s+([\d.]+)\s+([\d.]+)\s*-->[ \t]*$", re.M)


def crop_figures(q, md_text, img_path):
    """Replace fig directives with placeholders; return (md, {placeholder: typst call})."""
    calls = {}

    def sub(m):
        k = len(calls)
        x0, y0, x1, y1 = map(float, m.groups())
        im = Image.open(img_path)
        box = (round(x0 * im.width), round(y0 * im.height), round(x1 * im.width), round(y1 * im.height))
        out = CACHE / "crop" / f"{q['id']}-{k}.jpg"
        out.parent.mkdir(parents=True, exist_ok=True)
        c = im.crop(box)
        c.save(out, quality=90, optimize=True)
        token = f"FIGCROP{k}XX"
        # keep the figure at the scale it has on the original page (page width -> 17 cm)
        calls[token] = f"#fig-crop({tstr(str(out))}, {c.width}, {c.height}, {x1 - x0:.3f})"
        return token

    return FIG_RE.sub(sub, md_text), calls


TILDE = "\ue000"  # stands in for a literal "\~" while pandoc runs


def md_to_typst(md_text):
    # pandoc 3.1 writes a literal "~" unescaped, and typst reads "~" as a non-breaking space
    md_text = md_text.replace("\\~", TILDE)
    r = subprocess.run(
        ["pandoc", "--wrap=none", "-f", "markdown-fancy_lists-implicit_figures", "-t", "typst"],
        input=md_text, capture_output=True, text=True, check=True)
    # plain monochrome code for printing: drop the language tag so typst does not colour it
    out = re.sub(r"^```\w+$", "```", r.stdout, flags=re.M)
    # pandoc does not escape typst list markers at line start ("2. ...", "+ ...", "- ...")
    # \mathbf in LaTeX is bold *upright*; typst's bold() keeps italics
    out = re.sub(r"(?<![\w.])bold\(([^()]*)\)", r"upright(bold(\1))", out)
    lines, in_code = [], False
    for ln in out.split("\n"):
        if ln.startswith("```"):
            in_code = not in_code
        elif not in_code:
            ln = re.sub(r"^(\d+)\. ", r"\1\\. ", ln)
            ln = re.sub(r"^([+-]) ", r"\\\1 ", ln)
        lines.append(ln.replace(TILDE, "~" if in_code or ln.startswith("```") else "\\~"))
    return "\n".join(lines)


def tstr(s):
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def build(src, out_pdf):
    src = Path(src)
    man = json.loads((src / "manifest.json").read_text())
    qdir = src.parents[2] / "_q"
    skew_path = qdir / "deskew.json"
    skew = json.loads(skew_path.read_text()) if skew_path.exists() else {}
    qs = sorted(man["questions"], key=qkey)
    group = man["group"]
    title = f"{man['chapter']} - {man['topic']}"

    body = []

    def render_question(i, q):
        md = qdir / f"{q['id']}.md"
        if not md.exists():
            raise SystemExit(f"missing transcription: {md}")
        md_text = md.read_text()
        calls = {}
        if FIG_RE.search(md_text):
            img, _, _, _ = prepare_image(q, skew)
            md_text, calls = crop_figures(q, md_text, img)
        content = md_to_typst(md_text)
        for token, call in calls.items():
            if token not in content:
                raise SystemExit(f"figure placeholder lost for {q['id']}")
            content = content.replace(token, call)
        src_line = f"{q['year']} 年　{q['school']}《{q['paper']}》　{q['qnum']}"
        return f"""
#question({i}, {tstr(src_line)}, {tstr(q['id'])})[
{content}
]
"""

    if "sections" in man:
        by_id = {q["id"]: q for q in qs}
        printed = {}
        for section in man["sections"]:
            refs = sorted({printed[qid] for qid in section["ids"] if qid in printed})
            heading = f'#text(size: 12pt, weight: "bold", {tstr(section["topic"])})'
            if refs:
                ref_text = "另見：第 " + "、".join(map(str, refs)) + " 題"
                heading += f'\n#v(0.15em)\n#text(size: 8pt, fill: luma(120), {tstr(ref_text)})'
            body.append(f"""
#block(sticky: true, width: 100%)[
{heading}
#v(0.35em)
]
""")
            section_qs = []
            section_seen = set()
            for qid in section["ids"]:
                if qid in printed or qid in section_seen or qid not in by_id:
                    continue
                section_seen.add(qid)
                section_qs.append(by_id[qid])
            for q in sorted(section_qs, key=qkey):
                n = len(printed) + 1
                body.append(render_question(n, q))
                printed[q["id"]] = n
    else:
        for i, q in enumerate(qs, 1):
            body.append(render_question(i, q))
    skew_path.write_text(json.dumps(skew, ensure_ascii=False, indent=1) + "\n")

    schools = "・".join(sorted({q["school"] for q in qs}, key=lambda s: SCHOOL_ORDER.get(s, 9)))
    years = sorted({q["year"] for q in qs})
    year_label = f"民國 {'、'.join(map(str, years))} 年" if group == "英文" else "民國 100–107 年"
    subtitle = f"收錄 {len(man['sections'])} 個主題" if "sections" in man else man["unit_key"]
    doc = f"""
#let FONT = {FONTS[group]}
#set document(title: {tstr(title)})
#set page(paper: "a4", margin: (x: 1.5cm, top: 1.8cm, bottom: 1.8cm),
  footer: context [#set text(size: 8pt, fill: luma(110))
    #{tstr(title)} #h(1fr) #counter(page).display("1 / 1", both: true)])
#set text(font: FONT, size: 10pt, lang: "zh", region: "tw")
#show math.equation: set text(font: ("New Computer Modern Math", "Noto Serif TC"))
#set par(justify: true, leading: 0.75em, spacing: 0.9em)
// matrices / cases inside running text keep full (display) size, like LaTeX
#show math.mat: it => math.display(it)
#show math.cases: it => math.display(it)
#show raw: set text(font: ("DejaVu Sans Mono", "Noto Serif TC"), size: 8.5pt)
#show raw.where(block: true): it => block(width: 100%, inset: (left: 1.2em, y: 4pt), it)
#show "[?]": it => text(fill: rgb("#c0392b"), weight: "bold", it)
#let blockquote(body) = block(inset: (left: 8pt), stroke: (left: 1.5pt + luma(170)), text(size: 8.5pt, fill: luma(70), body))
#let horizontalrule = line(length: 100%, stroke: 0.5pt + luma(170))

// a figure cropped from the original scan (figures are embedded, never redrawn)
#let fig-crop(path, w, h, frac) = {{
  let maxh = 18cm
  let width = calc.min(18 * frac, maxh / 1cm * w / h) * 1cm
  block(width: 100%, align(center, image(path, width: width)))
}}

#let question(n, src, qid, body) = {{
  // Short questions stay together; long questions can flow, with their headers kept attached.
  let head = block(sticky: true, width: 100%, {{
    line(length: 100%, stroke: 0.8pt)
    v(-0.3em)
    grid(columns: (auto, 1fr, auto), column-gutter: 0.8em,
      text(weight: "bold", size: 11pt)[第 #n 題],
      align(horizon, text(weight: "bold")[#src]),
      align(horizon, text(size: 7pt, fill: luma(140), qid)))
    v(0.3em)
  }})
  context {{
    let h = measure(block(width: 18cm, {{ head; body }})).height
    block(width: 100%, breakable: h > 12cm, {{ head; body }})
  }}
  // blank space for working / answers (about 2 lines)
  v(2 * 1.8em)
}}

#align(center)[
  #text(size: 16pt, weight: "bold", {tstr(title)}) \\
  #v(0.2em)
  #text(size: 9pt, fill: luma(80))[{group}｜{man['subject']}｜{schools}｜{year_label}｜共 {len(qs)} 題] \\
  #text(size: 8pt, fill: luma(120), {tstr(subtitle)})
]
#v(0.8em)
{''.join(body)}
"""
    typ = CACHE / "typ" / (re.sub(r"[^\w.-]+", "_", title) + ".typ")
    typ.parent.mkdir(parents=True, exist_ok=True)
    typ.write_text(doc)
    Path(out_pdf).parent.mkdir(parents=True, exist_ok=True)
    typst.compile(str(typ), output=str(out_pdf), root="/", font_paths=FONT_DIRS)
    return len(qs)


if __name__ == "__main__":
    n = build(sys.argv[1], sys.argv[2])
    print(f"built {sys.argv[2]} with {n} questions")
