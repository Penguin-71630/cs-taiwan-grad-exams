"""Build one topic PDF from a source folder.

Source folder layout (Practice Exams/_src/<group>/<chapter>/<chapter> - <topic>/):
  manifest.json   unit metadata + questions (id, year, school, paper, qnum, url)
  <id>.md         hand transcription (Markdown + LaTeX math), one per question
  deskew.json     written by this script: detected skew angle per image

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


def md_to_typst(md_path):
    r = subprocess.run(
        ["pandoc", "--wrap=none", "-f", "markdown-fancy_lists-implicit_figures", "-t", "typst", str(md_path)],
        capture_output=True, text=True, check=True)
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
        lines.append(ln)
    return "\n".join(lines)


def tstr(s):
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def build(src, out_pdf):
    src = Path(src)
    man = json.loads((src / "manifest.json").read_text())
    skew_path = src / "deskew.json"
    skew = json.loads(skew_path.read_text()) if skew_path.exists() else {}
    qs = sorted(man["questions"], key=qkey)
    group = man["group"]
    title = f"{man['chapter']} - {man['topic']}"

    body = []
    for i, q in enumerate(qs, 1):
        md = src / f"{q['id']}.md"
        if not md.exists():
            raise SystemExit(f"missing transcription: {md}")
        img, w, h, info = prepare_image(q, skew)
        content = md_to_typst(md)
        src_line = f"{q['year']} 年　{q['school']}《{q['paper']}》　{q['qnum']}"
        note = f"原圖（已校正歪斜 {abs(info['angle']):.1f}°）" if info["corrected"] else "原圖"
        body.append(f"""
#question({i}, {tstr(src_line)}, {tstr(q['id'])})[
{content}
][
#figure-orig({tstr(str(img))}, {w}, {h}, {tstr(note)})
]
""")
    skew_path.write_text(json.dumps(skew, ensure_ascii=False, indent=1) + "\n")

    schools = "・".join(sorted({q["school"] for q in qs}, key=lambda s: SCHOOL_ORDER.get(s, 9)))
    doc = f"""
#let FONT = {FONTS[group]}
#set document(title: {tstr(title)})
#set page(paper: "a4", margin: (x: 2cm, top: 2cm, bottom: 2cm),
  footer: context [#set text(size: 8.5pt, fill: luma(110))
    #{tstr(title)} #h(1fr) #counter(page).display("1 / 1", both: true)])
#set text(font: FONT, size: 11pt, lang: "zh", region: "tw")
#show math.equation: set text(font: ("New Computer Modern Math", "Noto Serif TC"))
#set par(justify: true, leading: 0.75em, spacing: 0.9em)
// matrices / cases inside running text keep full (display) size, like LaTeX
#show math.mat: it => math.display(it)
#show math.cases: it => math.display(it)
#show raw: set text(font: ("DejaVu Sans Mono", "Noto Serif TC"), size: 9.5pt)
#show raw.where(block: true): it => block(width: 100%, fill: luma(246), inset: 7pt, radius: 2pt, it)
#show "[?]": it => text(fill: rgb("#c0392b"), weight: "bold", it)
#let blockquote(body) = block(inset: (left: 8pt), stroke: (left: 1.5pt + luma(170)), text(size: 9.5pt, fill: luma(70), body))
#let horizontalrule = line(length: 100%, stroke: 0.5pt + luma(170))

#let figure-orig(path, w, h, note) = {{
  let maxw = 17cm
  let maxh = 21cm
  let width = calc.min(maxw / 1cm, maxh / 1cm * w / h) * 1cm
  v(0.4em)
  block(width: 100%, breakable: false, {{
    text(size: 8.5pt, fill: luma(110), note)
    align(center, box(stroke: 0.4pt + luma(190), image(path, width: width)))
  }})
}}

#let question(n, src, qid, body, fig) = {{
  // header + transcription stay together so a header never dangles at a page bottom
  block(width: 100%, breakable: false, {{
    line(length: 100%, stroke: 0.8pt)
    v(-0.3em)
    grid(columns: (auto, 1fr, auto), column-gutter: 0.8em,
      text(weight: "bold", size: 12pt)[第 #n 題],
      align(horizon, text(weight: "bold")[#src]),
      align(horizon, text(size: 7.5pt, fill: luma(140), qid)))
    v(0.3em)
    body
  }})
  fig
  v(0.6em)
  text(size: 9pt, fill: luma(110))[作答區]
  v(4 * 1.8em)
}}

#align(center)[
  #text(size: 18pt, weight: "bold", {tstr(title)}) \\
  #v(0.2em)
  #text(size: 10pt, fill: luma(80))[{group}｜{man['subject']}｜{schools}｜民國 100–107 年｜共 {len(qs)} 題] \\
  #text(size: 8.5pt, fill: luma(120))[單元：{man['unit_key']}　・　題目來源：考古題題庫（tiku.ptsfu.org），以原圖為準；轉錄中標 [?] 處為原圖無法辨識]
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
