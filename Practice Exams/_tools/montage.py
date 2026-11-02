"""Stack question images (with id labels) into viewing sheets for transcription.

Usage: python montage.py OUT_DIR ID [ID ...]
Downloads missing originals into the cache, then writes sheet-01.png, sheet-02.png, ... each at
most 1600 px wide and 2000 px tall. A tall image gets a sheet (or several slices) of its own.
Prints which ids are on which sheet.
"""
import os, sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, os.path.dirname(__file__))
from build import fetch  # noqa: E402

W, H, LABEL = 1600, 2000, 34
out = Path(sys.argv[1]); out.mkdir(parents=True, exist_ok=True)
for f in out.glob("sheet-*.png"):
    f.unlink()
try:
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 24)
except OSError:
    font = ImageFont.load_default()

pieces = []  # (label, image)
for qid in sys.argv[2:]:
    im = Image.open(fetch({"id": qid, "url": f"https://img.ptsfu.org/{qid}.webp"})).convert("RGB")
    if im.width > W:
        im = im.resize((W, round(im.height * W / im.width)), Image.LANCZOS)
    if im.height <= H - LABEL:
        pieces.append((qid, im))
    else:  # slice tall pages with a small overlap so no line is cut unseen
        step, k, y = H - LABEL - 60, 1, 0
        while y < im.height:
            pieces.append((f"{qid} (part {k})", im.crop((0, y, im.width, min(im.height, y + H - LABEL)))))
            y += step; k += 1

sheets, cur, h = [], [], 0
for lab, im in pieces:
    need = im.height + LABEL + 10
    if cur and h + need > H:
        sheets.append(cur); cur, h = [], 0
    cur.append((lab, im)); h += need
if cur:
    sheets.append(cur)
for i, sh in enumerate(sheets, 1):
    hh = sum(im.height + LABEL + 10 for _, im in sh)
    canvas = Image.new("RGB", (W, hh), "white")
    d = ImageDraw.Draw(canvas)
    y = 0
    for lab, im in sh:
        d.rectangle([0, y, W, y + LABEL - 4], fill=(255, 235, 150))
        d.text((8, y + 4), lab, fill="black", font=font)
        canvas.paste(im, (0, y + LABEL)); y += im.height + LABEL + 10
    canvas.save(out / f"sheet-{i:02d}.png")
    print(f"sheet-{i:02d}.png: " + ", ".join(lab for lab, _ in sh))
