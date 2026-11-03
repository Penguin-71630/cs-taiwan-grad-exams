"""Lightweight checks on transcriptions (Python only; no pandoc/typst needed).

Usage: python3 lint_q.py ID [ID ...]      (exit 1 if any ERROR)
Checks _src/_q/<id>.md outside code blocks / inline code:
  ERROR  file missing or empty; a `=== ` line; Markdown image `![...]`
  ERROR  bare `~` (write `\~`; `x~i~` subscripts are fine); bare `@` (write `\@`); odd number of unescaped `$`
  ERROR  malformed fig line or coords not 0 <= x0 < x1 <= 1, 0 <= y0 < y1 <= 1
  WARN   HTML other than the fig comment; line starting with `#`; unbalanced { } inside math
"""
import re, sys
from pathlib import Path

QDIR = Path(__file__).resolve().parent.parent / "_src" / "_q"
FIG_RE = re.compile(r"^<!--\s*fig\s+([\d.]+)\s+([\d.]+)\s+([\d.]+)\s+([\d.]+)\s*-->[ \t]*$")


def strip_inline_code(s):
    return re.sub(r"(`+)(.+?)\1", "", s)


def lint(qid):
    errs, warns = [], []
    f = QDIR / f"{qid}.md"
    if not f.exists() or not f.read_text().strip():
        return [f"missing or empty {f.name}"], []
    text = f.read_text()
    in_code, dollars, prose = False, 0, []
    for n, raw in enumerate(text.split("\n"), 1):
        if raw.startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        if raw.startswith("=== "):
            errs.append(f"L{n}: bundle separator left in file")
        if raw.lstrip().startswith("<!--"):
            m = FIG_RE.match(raw.strip())
            if not m:
                errs.append(f"L{n}: malformed fig/comment line: {raw.strip()}")
            else:
                x0, y0, x1, y1 = map(float, m.groups())
                if not (0 <= x0 < x1 <= 1 and 0 <= y0 < y1 <= 1):
                    errs.append(f"L{n}: fig coords out of range: {raw.strip()}")
            continue
        s = strip_inline_code(raw)
        if "![" in s:
            errs.append(f"L{n}: Markdown image (use <!-- fig --> crops)")
        if re.search(r"(?<!\\)~", re.sub(r"(?<!\\)~[^\s~]+~", "", s)):
            errs.append(f"L{n}: bare ~ (write \\~)")
        if re.search(r"(?<!\\)@", s):
            errs.append(f"L{n}: bare @ (write \\@)")
        if re.search(r"</?[a-zA-Z][a-zA-Z0-9]*(\s[^>]*)?/?>", s) and not re.search(r"\$[^$]*<[^$]*\$", s):
            warns.append(f"L{n}: HTML-looking tag")
        if s.startswith("#"):
            warns.append(f"L{n}: line starts with # (heading)")
        dollars += len(re.findall(r"(?<!\\)\$", s))
        prose.append(s)
    if in_code:
        errs.append("unclosed ``` code block")
    if dollars % 2:
        errs.append(f"odd number of unescaped $ ({dollars})")
    for m in re.finditer(r"\$\$?(.+?)\$\$?", "\n".join(prose), re.S):
        body = re.sub(r"\\[{}]", "", m.group(1))
        if body.count("{") != body.count("}"):
            warns.append(f"unbalanced braces in math: {m.group(1)[:60]!r}")
    return errs, warns


def main():
    bad = 0
    for qid in sys.argv[1:]:
        errs, warns = lint(qid)
        for e in errs:
            print(f"ERROR {qid} {e}")
        for w in warns:
            print(f"WARN  {qid} {w}")
        bad += bool(errs)
    print(f"{len(sys.argv) - 1} checked, {bad} with errors")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
