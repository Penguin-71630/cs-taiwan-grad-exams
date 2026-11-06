"""Build compact Tier answer PDFs alongside tiers.json.

Usage: TIKU_FONTS=$HOME/fonts python3 _tools/answers.py --out ~/tiers/out
Generate tiers.json first with _tools/tiers.py --out using the same directory.
"""
import argparse
from functools import lru_cache
import json
from pathlib import Path
import re
import subprocess
import sys

import typst

from build import FONT_DIRS, FONTS, md_to_typst, numbering, tstr

PE = Path(__file__).resolve().parents[1]
ADIR = PE / "_src" / "_a"
MARKS = {"official": "官", "drive": "詳", "devin": "自"}


@lru_cache(maxsize=None)
def read_answer(qid):
    path = ADIR / f"{qid}.md"
    try:
        text = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return "", "（缺）", True
    lines = text.splitlines()
    marker = re.fullmatch(r"<!-- src: (official|drive|devin) -->", lines[0] if lines else "")
    if not marker:
        raise ValueError(f"{path}: invalid src marker")
    body = "\n".join(lines[1:]).strip()
    if not body:
        raise ValueError(f"{path}: empty answer")
    return f"【{MARKS[marker.group(1)]}】", md_to_typst(body).strip(), False


def build_answers(title, topics, out):
    group = title.split(" - Tier ")[0]
    body = []
    missing = []
    count = 0
    previous_part = None
    for topic in topics:
        rel = Path(topic["pdf"]).relative_to(PE.name)
        manifest = json.loads((PE / "_src" / rel.with_suffix("") / "manifest.json").read_text())
        part = topic.get("part")
        if part and part != previous_part:
            body.append(f'#block(sticky: true, above: 0.5em, below: 0.2em)[#text(size: 11pt, weight: "bold", {tstr(part)})]')
        previous_part = part
        heading = f"{topic['chapter']} - {topic['topic']}"
        body.append(f'#block(sticky: true, above: 0.5em, below: 0.2em)[#text(size: 9pt, weight: "bold", {tstr(heading)})]')
        for n, q, _ in numbering(manifest):
            mark, answer, absent = read_answer(q["id"])
            if absent:
                missing.append(q["id"])
            label = f"第 {n} 題（{q['year']} {q['school']}《{q['paper']}》{q['qnum']}）{mark}"
            body.append(f'#block(width: 100%, above: 0pt, below: 0pt)[#text(weight: "bold", {tstr(label)}) {answer}\n]')
            count += 1
    doc = f'''#set document(title: {tstr(title + " 解答")})
#set page(paper: "a4", margin: (x: 1.2cm, y: 1.2cm),
  footer: context align(center, text(size: 7pt, counter(page).display("1"))))
#set text(font: {FONTS[group]}, size: 9pt, lang: "zh", region: "tw", top-edge: "ascender", bottom-edge: "descender")
#set par(justify: false, leading: 0.45em, spacing: 0pt)
#let ident = sym.equiv
#show math.equation: set text(font: ("New Computer Modern Math", "Noto Serif TC"))
#show math.mat: it => math.display(it)
#show math.cases: it => math.display(it)
#show raw: set text(font: ("DejaVu Sans Mono", "Noto Serif TC"), size: 8pt)
#show "[?]": it => text(fill: rgb("#c0392b"), weight: "bold", it)
#let blockquote(body) = block(inset: (left: 6pt), text(size: 8pt, fill: luma(70), body))
#let horizontalrule = line(length: 100%, stroke: 0.5pt + luma(170))
#text(size: 12pt, weight: "bold", {tstr(title + " 解答")})
#v(0.3em)
#columns(2, gutter: 0.7cm)[
{chr(10).join(body)}
]
'''
    source = out / f"{title} 解答.typ"
    source.write_text(doc, encoding="utf-8")
    pdf = source.with_suffix(".pdf")
    typst.compile(str(source), output=str(pdf), root="/", font_paths=FONT_DIRS)
    print(f"{pdf.name}: {count} answers, {len(missing)} missing ({len(set(missing))} unique IDs)")
    return count, missing


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=Path.home() / "tiers" / "out")
    args = parser.parse_args(argv)
    out = args.out.expanduser().resolve()
    try:
        tiers = json.loads((out / "tiers.json").read_text())
        read_answer.cache_clear()
        total, missing = 0, []
        for title, topics in tiers.items():
            count, absent = build_answers(title, topics, out)
            total += count
            missing.extend(absent)
    except (OSError, ValueError, subprocess.CalledProcessError) as exc:
        print(f"ERROR {exc}", file=sys.stderr)
        return 1
    print(f"Total: {total} answers, {len(missing)} missing occurrences, {len(set(missing))} unique missing IDs")
    return 0


if __name__ == "__main__":
    sys.exit(main())
