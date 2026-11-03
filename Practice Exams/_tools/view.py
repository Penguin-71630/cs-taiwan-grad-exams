"""Prepare question images for transcription (no typst/pandoc needed).

Usage: python3 view.py OUT_DIR ID [ID ...]
For each id: downloads the original (cache: ~/.cache/tiku/orig, or TIKU_CACHE), applies the same
deskew rule as build.py (rotate when |angle| >= 0.75 deg), and writes
  OUT_DIR/<id>.png             the image build.py crops figures from (view this to transcribe)
  OUT_DIR/<id>-grid.png        same image with a 0.05 grid labelled in fractions of width/height,
                               for reading `<!-- fig x0 y0 x1 y1 -->` coordinates
Images taller than 1100 px are also written as overlapping slices <id>-partK.png / -partK-grid.png
(grid labels stay fractions of the WHOLE image), so nothing is shrunk when viewed.
"""
import os, sys, urllib.request
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, os.path.dirname(__file__))
from deskew import estimate  # noqa: E402

CACHE = Path(os.environ.get("TIKU_CACHE", Path.home() / ".cache" / "tiku"))
UA = "Mozilla/5.0 (practice-workbook builder)"
THRESHOLD = 0.75
MAX_PX = 2000  # build.py downsizes to this before cropping; fractions are scale-free
SLICE, OVERLAP = 1100, 120
try:
    FONT = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 18)
except OSError:
    FONT = ImageFont.load_default()


def fetch(qid):
    orig = CACHE / "orig" / f"{qid}.webp"
    if not orig.exists():
        orig.parent.mkdir(parents=True, exist_ok=True)
        req = urllib.request.Request(f"https://img.ptsfu.org/{qid}.webp", headers={"User-Agent": UA})
        orig.write_bytes(urllib.request.urlopen(req, timeout=60).read())
    return orig


def prepared(qid):
    im = Image.open(fetch(qid)).convert("RGB")
    ang = estimate(im)
    if abs(ang) >= THRESHOLD:
        im = im.rotate(ang, resample=Image.BICUBIC, expand=True, fillcolor=(255, 255, 255))
    return im, ang


def grid(im, y_off=0, full_h=None):
    full_h = full_h or im.height
    g = im.copy()
    d = ImageDraw.Draw(g)
    for k in range(1, 20):
        x = round(k * 0.05 * g.width)
        d.line([(x, 0), (x, g.height)], fill=(255, 0, 0) if k % 2 == 0 else (255, 170, 170), width=1)
        if k % 2 == 0:
            d.text((x + 2, 2), f"{k * 0.05:.1f}", fill=(200, 0, 0), font=FONT)
    for k in range(1, 20):
        y = round(k * 0.05 * full_h) - y_off
        if 0 <= y < g.height:
            d.line([(0, y), (g.width, y)], fill=(0, 0, 255) if k % 2 == 0 else (170, 170, 255), width=1)
            d.text((2, y + 2), f"{k * 0.05:.2f}", fill=(0, 0, 200), font=FONT)
    return g


def main():
    out = Path(sys.argv[1]); out.mkdir(parents=True, exist_ok=True)
    for qid in sys.argv[2:]:
        im, ang = prepared(qid)
        im.save(out / f"{qid}.png")
        grid(im).save(out / f"{qid}-grid.png")
        parts = 1
        if im.height > SLICE:
            y, parts = 0, 0
            while y < im.height:
                parts += 1
                c = im.crop((0, y, im.width, min(im.height, y + SLICE)))
                c.save(out / f"{qid}-part{parts}.png")
                grid(c, y, im.height).save(out / f"{qid}-part{parts}-grid.png")
                if y + SLICE >= im.height:
                    break
                y += SLICE - OVERLAP
        print(f"{qid}: {im.width}x{im.height}, skew {ang:+.2f}{' (corrected)' if abs(ang) >= THRESHOLD else ''}"
              + (f", {parts} slices" if parts > 1 else ""))


if __name__ == "__main__":
    main()
