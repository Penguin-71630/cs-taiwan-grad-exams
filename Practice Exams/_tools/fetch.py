"""Download originals for a source folder into the cache and write PNG views for transcription.
Usage: python fetch.py SRC_DIR VIEW_DIR"""
import json, sys, os
from pathlib import Path
sys.path.insert(0, os.path.dirname(__file__))
from build import fetch
from PIL import Image
man = json.loads((Path(sys.argv[1]) / "manifest.json").read_text())
out = Path(sys.argv[2]); out.mkdir(parents=True, exist_ok=True)
for q in man["questions"]:
    p = fetch(q)
    im = Image.open(p).convert("RGB")
    im.save(out / f"{q['id']}.png")
    print(q["id"], im.size)
