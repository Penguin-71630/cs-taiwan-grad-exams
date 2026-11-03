"""Estimate skew of scanned question images; write corrected copies only when skew is obvious.

Usage: python deskew.py ORIG_DIR OUT_DIR [--threshold 0.75]
Originals are never modified. Prints a JSON report {id: angle}.
"""
import sys, os, json, glob
import numpy as np
from PIL import Image

def estimate(im):
    g = im.convert("L")
    scale = 1000 / max(g.size)
    if scale < 1:
        g = g.resize((int(g.width * scale), int(g.height * scale)))
    a = np.asarray(g, dtype=np.float32)
    ink = (a < 128).astype(np.uint8) * 255
    src = Image.fromarray(ink)
    best, best_score = 0.0, -1
    for ang in np.arange(-4, 4.001, 0.1):
        r = np.asarray(src.rotate(ang, resample=Image.BILINEAR, expand=False), dtype=np.float32)
        prof = r.sum(axis=1)
        score = float(np.var(np.diff(prof)))
        if score > best_score:
            best, best_score = float(ang), score
    return round(best, 2)

def main():
    src, out = sys.argv[1], sys.argv[2]
    th = float(sys.argv[sys.argv.index("--threshold") + 1]) if "--threshold" in sys.argv else 0.75
    os.makedirs(out, exist_ok=True)
    rep = {}
    for f in sorted(glob.glob(os.path.join(src, "*.webp"))):
        qid = os.path.basename(f)[:-5]
        im = Image.open(f).convert("RGB")
        ang = estimate(im)
        fixed = abs(ang) >= th
        dst = os.path.join(out, qid + ".png")
        if fixed:
            im = im.rotate(ang, resample=Image.BICUBIC, expand=True, fillcolor=(255, 255, 255))
        im.save(dst, optimize=True)
        rep[qid] = {"angle": ang, "corrected": fixed}
    print(json.dumps(rep, ensure_ascii=False, indent=1))

if __name__ == "__main__":
    main()
