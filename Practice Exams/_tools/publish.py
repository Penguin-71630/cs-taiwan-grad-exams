"""Build every topic whose questions are all transcribed and whose PDF is missing or stale,
verify it against its manifest, and commit each topic separately; then push once.

Usage: python publish.py [--no-push]
"""
import json, os, subprocess, sys
from pathlib import Path

sys.path.insert(0, os.path.dirname(__file__))
from build import build  # noqa: E402
from check import pdf_text  # noqa: E402
import re  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
REPO = ROOT.parent
QDIR = ROOT / "_src" / "_q"
BRANCH = "claude/cloud-credit-test-dhu8yn"
TRAILER = ("\n\nCo-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>\n"
           "Claude-Session: https://claude.ai/code/session_01SnDy9j9kHdRMiHxdZ7c83s")


def git(*a, check=True):
    return subprocess.run(["git", "-C", str(REPO), *a], capture_output=True, text=True, check=check)


def main():
    built, failed = [], []
    tools_mtime = max(p.stat().st_mtime for p in (ROOT / "_tools").glob("*.py"))
    for man_path in sorted(p for p in (ROOT / "_src").glob("*/*/*/manifest.json") if not p.parts[-4].startswith("_")):
        src = man_path.parent
        man = json.loads(man_path.read_text())
        mds = [QDIR / f"{q['id']}.md" for q in man["questions"]]
        if not all(m.exists() for m in mds):
            continue
        rel = src.relative_to(ROOT / "_src")
        pdf = ROOT / rel.parent / f"{src.name}.pdf"
        newest = max([man_path.stat().st_mtime, tools_mtime] + [m.stat().st_mtime for m in mds])
        if pdf.exists() and pdf.stat().st_mtime >= newest:
            continue
        try:
            n = build(src, pdf)
            txt = pdf_text(pdf)
            heads = {int(x) for x in re.findall(r"第 ?(\d+) ?題", txt)}
            flat = txt.replace("\n", "")
            if heads != set(range(1, n + 1)) or any(q["id"] not in flat for q in man["questions"]):
                raise RuntimeError(f"check failed: headers {sorted(heads)} for {n} questions")
        except Exception as e:  # keep going; report at the end
            failed.append(f"{rel}: {e}")
            continue
        git("add", str(pdf), str(src), *[str(m) for m in mds], str(QDIR / "deskew.json"))
        if git("diff", "--cached", "--quiet", check=False).returncode != 0:
            git("commit", "-q", "-m", f"Practice Exams: {man['group']}/{man['chapter']} - {man['topic']} ({n} 題)" + TRAILER)
            built.append(f"{rel} ({n})")
    print(f"committed {len(built)} topic(s)")
    for b in built:
        print("  +", b)
    for f in failed:
        print("  FAILED", f)
    if built and "--no-push" not in sys.argv:
        for i in range(4):
            r = git("push", "-u", "origin", BRANCH, check=False)
            if r.returncode == 0:
                print("pushed")
                break
            print("push failed:", r.stderr.strip()[-300:])
            import time; time.sleep(2 ** (i + 1))


if __name__ == "__main__":
    main()
