# Transcribing questions (for parallel transcription agents)

You transcribe a list of question images into `Practice Exams/_src/_q/<ID>.md`. You do NOT build PDFs
(no pandoc/typst needed): the lead merges your branch and typesets everything.

## Steps

```bash
cd "Practice Exams"
python3 _tools/view.py /tmp/v ID1 ID2 ...      # downloads + deskews; writes <ID>.png and <ID>-grid.png (and -partK slices if tall)
```

For each ID, one at a time:

1. Open `/tmp/v/<ID>.png` (or its `-partK.png` slices, in order) with your image viewer at full size. Transcribe
   from the image only. Never use the question bank's text summary or any other source.
2. If the question has a figure / diagram / circuit / plot / complex drawing, open `<ID>-grid.png` to read crop coordinates (see Figures).
3. Write `_src/_q/<ID>.md` directly (one file per ID).

When all are written:

```bash
python3 _tools/lint_q.py ID1 ID2 ...           # must print "0 with errors"; fix every ERROR, judge each WARN
python3 _tools/crop_preview.py /tmp/c ID ...    # for every ID with a fig line: open each crop and check it
```

A crop must contain the whole figure (labels, axes, captions belonging to it) and as little body text as
possible. Fix the coordinates and re-run until every crop is right.

## Content rules

- Transcribe exactly what is printed: the same wording, numbering, point values, and language (Chinese stays
  Chinese, English stays English). Keep typos as printed. For an obvious misprint, add a line `> 註：…` after the question.
- Do not transcribe repeated page headers/footers such as 「【不可使用計算機】」, page numbers, or exam-paper titles.
- Do not transcribe exam-wide answering, scoring, or general exam instructions (such as answer-sheet directions, question-type/scoring rules, or general calculation/rounding notes). Keep the question's own point marker and actual problem content.
- Transcribe shared stems as printed in each question. The build deduplicates matching leading paragraphs within the same exam and adds a reference to the first printed question; repeated options or content in the middle of a question are not deduplicated.
- If you cannot read something with certainty, write `[?]` in its place (e.g. `x[?]3`, or `[?]` for a whole
  word). Never guess. `[?]` is printed in red so the reader knows to check the original.
- Start with the question number as printed, escaped so it is not a Markdown list: `13\. [2%] Let …`, `6\. (18 points) …`.
- If one image contains several questions or a shared stem, transcribe everything in the image.

## Markdown / LaTeX conventions (pandoc Markdown → typst)

- Math: inline `$…$`, display `$$…$$` on its own line. LaTeX inside: `\frac`, `\begin{bmatrix}…\end{bmatrix}`,
  `\begin{cases}…\end{cases}`, `\text{…}`, `\mathrm`, `\mathbf`, `\log`, `\Theta`, `\lfloor … \rfloor`, etc.
  Every `$` must be paired. A literal dollar sign in prose is `\$`.
- Sub-items (a)(b)(c) / (1)(2) and multiple-choice options: one per line, each line except the last ends with `\`
  (hard line break). A blank line starts a new paragraph.

  ```
  (A) $O(n)$\
  (B) $O(n \log n)$\
  (C) $O(n^2)$
  ```
- A range tilde must be written `\~` (e.g. `21\~23`, `P0\~P4`). A bare `~` is pandoc subscript syntax (`x~i~`); use
  `$x_i$` for math subscripts, `H~2~O`-style only for real text subscripts.
- A literal `@` outside code must be written `\@` (typst treats `@x` as a reference and the build fails).
- Blanks to fill: `\_\_\_\_\_\_\_\_`.
- Bold/italic as printed: `**…**`, `*…*`.
- Code / assembly / pseudocode: a fenced ``` block, no language tag, indentation as printed.
- Tables: Markdown pipe tables (`|:---|---:|`) when the table is a plain grid of text; empty cells allowed.
  A table with merged cells, drawings, or that is part of a figure: crop it as a figure instead.
- Do not use Markdown headings (`#`), images (`![]()`), or HTML.

## Figures

Never redraw figures and never describe them in words. Embed a crop of the original instead, on its own line where the figure appears:

```
<!-- fig x0 y0 x1 y1 -->
```

`x0 y0 x1 y1` are fractions (0–1, 2–3 decimals) of the WHOLE `<ID>.png` width and height (left, top, right, bottom).
Read them from `<ID>-grid.png`: red vertical lines every 0.05 of the width (labelled every 0.1), blue horizontal lines
every 0.05 of the height (all labelled; on slices the labels are still fractions of the whole image).
Leave a small margin around the figure. Put figure text such as labels inside the crop, not in the transcription.

Example (from `201a71b418`):

````
2\. (9%) Suppose out of order execution is adopted in a pipeline design. The figure below gives a generic pipeline architectures with out-of-order pipeline design.

(a) Explain the needed work in the reservation station and reorder buffer, respectively, in order to support out of order execution. (4%)

(b) … to avoid the "Power-off \@multiplier" instruction to be moved in front of the set of multiply instructions. (5%)

```
mul.d   $f2, $f4, $f6
Power-Off  @multiplier
```

<!-- fig 0.185 0.545 0.89 1.0 -->
````

More examples of finished transcriptions are everywhere in `_src/_q/` (e.g. `m_335c2a4fe61c6def.md` recurrence with
cases, `m_1841e4b34949a0eb.md` matrix, `m_00ba249a92884934.md` tables, `31ec680c51.md` figure).

## Git

Only add the `_src/_q/<ID>.md` files of your assigned IDs. Do not touch any other file (not `deskew.json`,
manifests, PDFs, tools, README). Commit on a new branch off `claude/cloud-credit-test-dhu8yn` and push it.
