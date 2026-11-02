"""Render a PDF to a montage PNG for visual spot checks. Usage: python preview.py PDF OUT_DIR [dpi] [cols]"""
import sys, subprocess, glob, os
from PIL import Image
pdf, out = sys.argv[1], sys.argv[2]
dpi = sys.argv[3] if len(sys.argv) > 3 else "60"
cols = int(sys.argv[4]) if len(sys.argv) > 4 else 6
os.makedirs(out, exist_ok=True)
for f in glob.glob(os.path.join(out, "p-*.png")):
    os.remove(f)
subprocess.run(["pdftoppm", "-r", dpi, "-png", pdf, os.path.join(out, "p")], check=True)
ims = [Image.open(f) for f in sorted(glob.glob(os.path.join(out, "p-*.png")))]
w, h = ims[0].size
rows = (len(ims) + cols - 1) // cols
m = Image.new("RGB", (w * cols, h * rows), "white")
for i, im in enumerate(ims):
    m.paste(im, ((i % cols) * w, (i // cols) * h))
m.save(os.path.join(out, "montage.png"))
print(len(ims), "pages")
