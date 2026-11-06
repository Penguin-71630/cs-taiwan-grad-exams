import argparse, json, glob, sys, os, tempfile
from pathlib import Path
import typst
from pypdf import PdfWriter, PdfReader
PE = Path(__file__).resolve().parents[1]
REPO = PE.parent
sys.path.insert(0, str(PE / "_tools"))
from plan import unit_order
from build import FONTS
sys.path.insert(0, str(Path(__file__).parent))
from scoring import page as scoring_page
N = lambda s: s.replace("／", "/").strip()
parser = argparse.ArgumentParser()
parser.add_argument("--out", type=Path, default=Path.home() / "tiers" / "out")
args = parser.parse_args()
OUT = args.out.expanduser().resolve()
OUT.mkdir(parents=True, exist_ok=True)
mans = {}
for mf in glob.glob(str(PE / "_src/*/*/*/manifest.json")):
    p = Path(mf); g = p.parts[-4]
    d = json.load(open(mf))
    mans.setdefault((g, N(d["chapter"])), []).append(d)
fontdir = os.environ["TIKU_FONTS"]
promotions = json.load(open(PE / "_src/_index/tier-promote.json"))
def esc(s): return s.replace("\\", "\\\\").replace('"', '\\"')
summary = {}
tiers_index = {}
tempdir = tempfile.TemporaryDirectory(prefix="tiers-")
TMP = Path(tempdir.name)
for g in ("計系", "資演", "數學"):
    allm = [m for (gg, _), ms in mans.items() if gg == g for m in ms]
    cand = sorted((m for m in allm if m["topic"] != "其他主題"),
                  key=lambda m: (-len(m["questions"]), m["chapter"], unit_order(m["unit_key"])))
    tot = sum(len(m["questions"]) for m in cand); cum = 0; tier_of = {}
    for m in cand:
        tier_of[id(m)] = "1" if cum < 0.5 * tot else "2" if cum < 0.85 * tot else "3"
        cum += len(m["questions"])
    for m in allm:
        tier_of.setdefault(id(m), "3")
    for ch, tp in promotions[g]:
        hit = [m for m in allm if m["chapter"] == ch and (m["topic"] == tp if tp in ("全章", "其他主題", "Binary Tree", "B Tree", "Rank", "Subspace", "Johnson") else m["topic"].startswith(tp))]
        assert len(hit) == 1, (g, ch, tp, [m["topic"] for m in hit])
        tier_of[id(hit[0])] = "1"
    if g == "數學":
        for k in tier_of: tier_of[k] = {"1": "1", "2": "1", "3": "2"}[tier_of[k]]
    for t in ("1", "2", "3"):
        title = f"{g} - Tier {t}"
        if not any(tier_of[id(m)] == t for m in allm):
            (OUT / f"{title}.pdf").unlink(missing_ok=True); continue
        PARTS = {"計系": ["計算機組織", "作業系統"], "數學": ["離散數學", "線性代數"]}.get(g, [None])
        part_of = lambda m: m["subject"].split("、")[0] if PARTS[0] else None
        parts = []
        for P in PARTS:
            byc = {}
            for m in allm:
                if tier_of[id(m)] == t and part_of(m) == P: byc.setdefault(m["chapter"], []).append(m)
            items = []
            for ch, ms in byc.items():
                ms.sort(key=lambda m: (m["topic"] == "其他主題", -len(m["questions"]), unit_order(m["unit_key"])))
                items.append((ch, ms))
            items.sort(key=lambda it: -sum(len(m["questions"]) for m in it[1] if m["topic"] != "其他主題"))
            if items: parts.append((P, items))
        chs = [it for _, items in parts for it in items]
        assert sum(len(ms) for _, ms in chs) == sum(tier_of[id(m)] == t for m in allm)
        summary[title] = [(P, [(ch, [(m["topic"], len(m["questions"])) for m in ms]) for ch, ms in items]) for P, items in parts]
        rows = []
        for P, items in parts:
            if P:
                rows.append("  table.hline(stroke: 0.7pt),")
                rows.append(f'  table.cell(colspan: 2, align: center, inset: (y: SIZEY))[#text(weight: "bold", "{P}")],')
                rows.append("  table.hline(stroke: 0.7pt),")
            for i, (ch, ms) in enumerate(items):
                if i: rows.append("  table.hline(stroke: 0.4pt + luma(120)),")
                for m in ms:
                    name = m["topic"] if m["topic"] not in ("其他主題", "全章") else f"{ch} - {m['topic']}"
                    rows.append(f'  "{esc(name)}", [{len(m["questions"])} 題],')
        R = sum(len(ms) for _, ms in chs) + 1 + 1.3 * sum(1 for P, _ in parts if P)
        size = max(7.5, min(11.0, 650 / (R * 1.85)))
        rows = [r.replace("SIZEY", f"{size*0.45:.1f}pt") for r in rows]
        cover = f'''#set page(paper: "a4", margin: (x: 2cm, y: 1.5cm))
#set text(font: {FONTS[g]}, lang: "zh", region: "tw")
#set document(title: "{esc(title)}")
#align(center + horizon)[
  #text(size: 30pt, weight: "bold", "{esc(title)}")
  #v(0.4em)
  #text(size: 14pt, fill: luma(60), "台清交 100 － 107 年資工所考古題")
  #v(1.4em)
  #set text(size: {size:.1f}pt)
  #table(columns: 2, stroke: none, align: (left, right), column-gutter: 2.5em,
    inset: (x: 0.3em, y: {size*0.4:.1f}pt),
  table.hline(stroke: 1.2pt),
  table.header([*知識點*], [*題數*]),
{chr(10).join(rows) if parts[0][0] else "  table.hline(stroke: 0.7pt)," + chr(10) + chr(10).join(rows)}
  table.hline(stroke: 1.2pt),
  )
]
'''
        cp = TMP / f"cover-{g}-{t}.typ"; cp.write_text(cover)
        cpdf = TMP / f"cover-{g}-{t}.pdf"; cpdf.write_bytes(typst.compile(str(cp), font_paths=[fontdir]))
        w = PdfWriter()
        w.append(str(cpdf), outline_item=None)
        w.add_outline_item("封面", 0)
        sp = TMP / f"scoring-{g}.typ"; sp.write_text(scoring_page(g, FONTS[g]))
        spdf = TMP / f"scoring-{g}.pdf"; spdf.write_bytes(typst.compile(str(sp), font_paths=[fontdir]))
        w.append(str(spdf), outline_item=None)
        w.add_outline_item("計分方式", 1)
        pos = {}
        toc = []
        for P, items in parts:
            for ch, ms in items:
                for m in ms:
                    pos[id(m)] = len(w.pages)
                    pdf = PE / g / m["chapter"] / f"{m['chapter']} - {m['topic']}.pdf"
                    w.append(str(pdf), outline_item=None)
                    toc.append({
                        "part": P,
                        "chapter": m["chapter"],
                        "topic": m["topic"],
                        "pdf": str(pdf.relative_to(REPO)),
                    })
        for P, items in parts:
            top = w.add_outline_item(P, pos[id(items[0][1][0])]) if P else None
            for ch, ms in items:
                parent = w.add_outline_item(ch, pos[id(ms[0])], parent=top)
                for m in ms:
                    w.add_outline_item(m["topic"], pos[id(m)], parent=parent)
        out = OUT / f"{title}.pdf"
        w.write(str(out))
        tiers_index[title] = toc
        print(title, len(chs), "chapters,", sum(len(x[1]) for x in chs), "topics,", len(w.pages), "pages,", round(out.stat().st_size/1e6,1), "MB")

tempdir.cleanup()
json.dump(summary, open(OUT / "summary.json", "w"), ensure_ascii=False, indent=1)
json.dump(tiers_index, open(OUT / "tiers.json", "w"), ensure_ascii=False, indent=1)
