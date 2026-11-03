"""Write the figure crops a transcription asks for, so they can be checked by eye.

Usage: python3 crop_preview.py OUT_DIR ID [ID ...]
Reads _src/_q/<id>.md, applies each `<!-- fig x0 y0 x1 y1 -->` to the prepared image (same deskew
rule as build.py) and writes OUT_DIR/<id>-fig<k>.png.
"""
import os, re, sys
from pathlib import Path

sys.path.insert(0, os.path.dirname(__file__))
from view import prepared  # noqa: E402

QDIR = Path(__file__).resolve().parent.parent / "_src" / "_q"
FIG_RE = re.compile(r"^<!--\s*fig\s+([\d.]+)\s+([\d.]+)\s+([\d.]+)\s+([\d.]+)\s*-->[ \t]*$", re.M)

out = Path(sys.argv[1]); out.mkdir(parents=True, exist_ok=True)
for qid in sys.argv[2:]:
    boxes = [tuple(map(float, m.groups())) for m in FIG_RE.finditer((QDIR / f"{qid}.md").read_text())]
    if not boxes:
        print(f"{qid}: no figures"); continue
    im, _ = prepared(qid)
    for k, (x0, y0, x1, y1) in enumerate(boxes):
        c = im.crop((round(x0 * im.width), round(y0 * im.height), round(x1 * im.width), round(y1 * im.height)))
        c.save(out / f"{qid}-fig{k}.png")
        print(f"{qid}-fig{k}.png {c.width}x{c.height}")
