# Writing answers (for parallel answer agents)

You write short answers for a list of question IDs into `Practice Exams/_src/_a/<ID>.md`. You do NOT build PDFs.
The reader is a student doing timed mock exams who only wants the final answer to check against (no worked solutions).

## Inputs your brief gives you

- The question IDs (usually whole exam papers: same year, school, paper).
- Official answer keys for some IDs (from `_src/_index/keys-交大.tsv`), already mapped to IDs by the lead.
- Google Drive file IDs of any solutions for those papers (handwritten photos, PDFs, 網友討論 docx), from `_src/_index/drive-answers.tsv`.

## Steps

```bash
cd "Practice Exams"
pip install gdown                               # once
python3 -m gdown <drive-file-id> -O /tmp/d/<name>   # each Drive file listed in your brief
python3 _tools/view.py /tmp/v ID1 ID2 ...       # original question images (optional; the transcription is usually enough)
```

For each ID:

1. Read `_src/_q/<ID>.md` (the transcription). If it has `[?]` or a figure, look at `/tmp/v/<ID>.png` too.
2. Work out the answer yourself first.
3. Compare with the official key (if given) and with any Drive solution for that question.
4. Write `_src/_a/<ID>.md`.

When done: `python3 _tools/lint_a.py ID1 ID2 ...` must report 0 errors. Commit only `_src/_a/*.md` on your own branch and push.

## File format

```
<!-- src: official -->
(B)(D)
```

- Line 1 is exactly one of `<!-- src: official -->`, `<!-- src: drive -->`, `<!-- src: devin -->`:
  - `official`: the official key for this question exists and you copied it. Always copy the official key, even if you disagree. If you disagree, add a line `> 註：…` with your answer and a one-line reason.
  - `drive`: no official key; a Drive solution covers it and, after checking, you agree with it.
  - `devin`: you solved it yourself (no source, or the Drive solution was wrong; if wrong, add `> 註：Drive 詳解作 …，應為 …`).
- Then the answer, as short as possible, in the question's language (Chinese question → Chinese, English → English):
  - Multiple choice: the options, e.g. `(C)` or `(A)(B)(E)`. Normalize lowercase option labels to uppercase.
  - Several sub-questions: one per line ending with `\`, e.g. `(a) 12\` / `(b) $O(n \log n)$`.
  - Numeric / fill-in: the final value with units; formulas in `$…$` LaTeX as in the transcriptions.
  - Proofs: one line with the key idea, or `證明略`.
  - Drawings, code, explanations: one or two lines with the essential result (final tree in parenthesized form, Gantt order, the key line of code, the key reason).
- If you are not sure, or sources conflict and you cannot settle it, write your best answer followed by `[?]` and a short reason, e.g. `(B) [?] 官方答案無此題，(B)(C) 皆可辯`. Never present a guess as certain.
- No explanations beyond that. Never copy long text from Drive solutions.

## Official key formats

`keys-交大.tsv` has a header (`題目ID`, `答案`, `來源檔`). Copy the complete answer, including these forms:

- Grouped keys such as `Q21: (C); Q22: (A)` become one numbered answer per line:
  ```
  Q21: (C)\
  Q22: (A)
  ```
- `或` separates accepted alternatives: `(A)或(C)或(A)(C)` means A alone, C alone, or both. Do not collapse alternatives into one selection.
- `均給分` means full credit regardless of selection (including no selection); copy the listed options and suffix, e.g. `(A)(B)(C)(D)(E)均給分`.

The linter ignores whitespace, trailing `\`, and `> 註：` lines when comparing official answers. For grouped answers, newlines and semicolons are equivalent. Keep question numbers and the order of letters and alternatives exactly as in the key. Every ID with an official key must use `src: official`.

Run `python3 _tools/lint_a.py` to check existing answers, or add `--all` to also report missing non-English answers.

## Correctness

- Every numeric answer (CPU time, AMAT, page faults, scheduling waiting time, recurrences, determinants, eigenvalues, counting, …) must be checked by a short Python computation or brute force before you write it. Do not commit the scripts.
- Read the whole question, including the shared stem of a 題組 (it may be in an earlier question of the same paper; find it in the `_q` files with the same year/school/paper in `_src/_index/q-*.tsv`).
- For select-all-that-apply questions, decide each option separately.
