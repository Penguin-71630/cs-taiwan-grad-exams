"""Export the 計系、資演、數學 question bank as an Obsidian vault."""
import argparse
import datetime
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build import CACHE, FIG_RE, crop_figures, normalize_paragraph, prepare_image, qkey  # noqa: E402

PE = Path(__file__).resolve().parents[1]
SRC = PE / "_src"
Q_DIR = SRC / "_q"
ANSWER_DIR = SRC / "_a"
INDEX_DIR = SRC / "_index"
DESKEW_PATH = Q_DIR / "deskew.json"
SKEW = json.loads(DESKEW_PATH.read_text()) if DESKEW_PATH.exists() else {}
GROUPS = ("計系", "資演", "數學")
SOURCE_RE = re.compile(r"^\s*<!--\s*src\b.*?-->\s*$")
ANSWER_LABEL_RE = re.compile(r"^(?:\([A-E]\)\s*)+$")
OPTION_TOKEN_RE = re.compile(r"\(([A-Ea-e])\)\s*")
SCORE_MARKER_RE = re.compile(r"^\s*(?:\[([^\]]+)\]|\(([^()]*)\)|【([^】]*)】)\s*")
NUMBER_PREFIX_RE = re.compile(
    r"^\s*(?:"
    r"(?P<arabic>\d+)\\?\.\s*"
    r"|\((?P<parenthesized>\d+)\)\s*"
    r"|\*\*\((?P<boldroman>[IVXLCDM]+)\)\*\*\s*"
    r"|\((?P<roman>[IVXLCDM]+)\)\s*"
    r")",
    re.IGNORECASE,
)
SUBPART_RE = re.compile(r"\(([a-z])\)$", re.IGNORECASE)
INLINE_PROTECTED_RE = re.compile(r"(`[^`]*`|\$(?!\$)[^$\n]*\$(?<!\\))")


def safe_component(value):
    return value.replace(":", "：").replace("/", "／").replace("\\", "＼")


def roman_value(value):
    values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0
    previous = 0
    for char in reversed(value.upper()):
        current = values[char]
        result += -current if current < previous else current
        previous = max(previous, current)
    return result


def problem_range(q):
    raw = q["qnum"].upper()
    numbers = [int(number) for number in re.findall(r"\d+", raw)]
    if numbers:
        start = numbers[0]
        end = numbers[-1] if re.search(r"\d\s*[-–~]\s*(?:Q\s*)?\d", raw) and len(numbers) > 1 else start
    else:
        roman = re.search(r"Q([IVXLCDM]+)$", raw)
        if not roman:
            raise ValueError(f"cannot determine printed question number for {q['id']}: {q['qnum']}")
        start = end = roman_value(roman.group(1))
    return start, end


def problem_label(q):
    start, end = problem_range(q)
    return str(start) if start == end else f"{start} ~ {end}"


def order_key(q):
    base = qkey(q)
    start, _ = problem_range(q)
    return (*base[:3], start, base[-1])


def read_index():
    questions = {}
    for path in sorted(INDEX_DIR.glob("q-*.tsv")):
        for line_number, line in enumerate(path.read_text().splitlines(), 1):
            if not line.strip():
                continue
            fields = line.split("|", 5)
            if len(fields) < 5:
                raise ValueError(f"invalid index row {path}:{line_number}")
            qid, year, school, paper, qnum = fields[:5]
            question = {
                "id": qid,
                "year": int(year),
                "school": school,
                "paper": paper,
                "qnum": qnum,
            }
            previous = questions.get(qid)
            if previous and previous != question:
                raise ValueError(f"conflicting index metadata for {qid}: {previous} / {question}")
            questions[qid] = question
    return questions


def read_manifest_questions():
    index = read_index()
    groups_by_id = defaultdict(set)
    urls_by_id = {}
    for group in GROUPS:
        for path in sorted((SRC / group).glob("*/*/manifest.json")):
            manifest = json.loads(path.read_text())
            for q in manifest["questions"]:
                qid = q["id"]
                if qid not in index:
                    raise ValueError(f"{qid} in {path} is missing from _src/_index/q-*.tsv")
                groups_by_id[qid].add(group)
                if q.get("url"):
                    urls_by_id[qid] = q["url"]

    counts_by_paper = defaultdict(Counter)
    for qid, groups in groups_by_id.items():
        q = index[qid]
        key = (q["year"], q["school"], q["paper"])
        for group in groups:
            counts_by_paper[key][group] += 1

    group_order = {group: position for position, group in enumerate(GROUPS)}
    questions = []
    for qid, groups in groups_by_id.items():
        q = dict(index[qid])
        if len(groups) == 1:
            q["group"] = next(iter(groups))
        else:
            key = (q["year"], q["school"], q["paper"])
            q["group"] = max(
                groups,
                key=lambda group: (counts_by_paper[key][group], -group_order[group]),
            )
        q["url"] = urls_by_id.get(qid)
        source = Q_DIR / f"{qid}.md"
        if not source.exists():
            raise ValueError(f"missing transcription: {source}")
        q["text"] = source.read_text()
        q["paragraphs"] = [
            paragraph
            for paragraph in re.split(r"\n\s*\n", q["text"].strip())
            if paragraph.strip()
        ]
        q["normalized"] = [normalize_paragraph(paragraph) for paragraph in q["paragraphs"]]
        q["is_mc"] = is_multiple_choice(qid)
        questions.append(q)
    return questions, groups_by_id


def is_multiple_choice(qid):
    answer = ANSWER_DIR / f"{qid}.md"
    if not answer.exists():
        return False
    lines = answer.read_text().splitlines()
    marker = next((i for i, line in enumerate(lines) if SOURCE_RE.fullmatch(line)), None)
    if marker is None:
        return False
    body = [
        line.strip().rstrip("\\").strip()
        for line in lines[marker + 1:]
        if line.strip().rstrip("\\").strip()
    ]
    return bool(body) and all(ANSWER_LABEL_RE.fullmatch(line) for line in body)


def leading_match(left, right):
    count = 0
    while count < min(len(left), len(right)) and left[count] == right[count]:
        count += 1
    return count


def adjacent_questions(previous, current):
    previous_start, previous_end = problem_range(previous)
    current_start, _ = problem_range(current)
    if current_start == previous_end + 1:
        return True
    if current_start != previous_end:
        return False
    previous_part = SUBPART_RE.search(previous["qnum"])
    current_part = SUBPART_RE.search(current["qnum"])
    return bool(
        previous_part
        and current_part
        and ord(current_part.group(1).lower()) == ord(previous_part.group(1).lower()) + 1
    )


def stem_groups(paper_questions):
    groups = []
    current = []
    for q in paper_questions:
        if current:
            duplicate = any(leading_match(old["normalized"], q["normalized"]) == len(q["normalized"])
                            for old in current)
            shared = leading_match(current[0]["normalized"], q["normalized"])
            if (
                shared >= 1
                and shared < len(q["paragraphs"])
                and not duplicate
                and adjacent_questions(current[-1], q)
            ):
                current.append(q)
                continue
            groups.append(current)
        current = [q]
    if current:
        groups.append(current)
    return groups


def score_value(value):
    return bool(re.search(r"(?:%|％|分|\bpoints?\b|\bpts?\.?\b)", value, re.IGNORECASE))


def strip_question_numbers(text, q):
    start, end = problem_range(q)
    expected = set(range(start, end + 1))
    output = []
    scores = []
    seen_expected_number = False
    seen_other_number = False
    in_code = False
    for line in text.splitlines():
        if line.strip().startswith("```"):
            in_code = not in_code
            output.append(line)
            continue
        match = NUMBER_PREFIX_RE.match(line)
        prefix_length = 0
        if match and not in_code:
            arabic = match.group("arabic")
            parenthesized = match.group("parenthesized")
            roman = match.group("boldroman") or match.group("roman")
            roman_qnum = re.search(r"Q([IVXLCDM]+)$", q["qnum"].upper())
            number = (
                int(arabic or parenthesized)
                if arabic or parenthesized
                else roman_value(roman) if roman and roman_qnum else None
            )
            if number is not None:
                if number in expected:
                    prefix_length = match.end()
                    seen_expected_number = True
                elif not seen_expected_number and not seen_other_number:
                    prefix_length = match.end()
                    seen_other_number = True
        if prefix_length:
            line = line[prefix_length:]
            score_match = SCORE_MARKER_RE.match(line)
            if score_match:
                marker = next((value for value in score_match.groups() if value is not None), "")
                if score_value(marker):
                    scores.append(marker.strip())
                    line = line[score_match.end():]
        output.append(line)
    return "\n".join(output), scores


def strip_hard_break(line):
    line = line.rstrip()
    if line.endswith("\\") and not line.endswith("\\\\"):
        return line[:-1].rstrip()
    return line


def escape_obsidian_patterns(line):
    parts = INLINE_PROTECTED_RE.split(line)
    for index in range(0, len(parts), 2):
        part = parts[index]
        def escape(match):
            content, suffix = match.groups()
            if "|" in content or suffix:
                return f"\\{{{content}\\}}{suffix or ''}"
            return match.group(0)

        part = re.sub(r"(?<!\\)\{([^{}\n]+)\}(\([^()\n]+\))?", escape, part)
        parts[index] = part
    return "".join(parts)


def normalize_markdown(text):
    lines = text.splitlines()
    output = []
    in_code = False
    in_math = False
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("```"):
            output.append(line)
            in_code = not in_code
            continue
        if in_code:
            output.append(line)
            continue
        if stripped == "$$":
            output.append(line)
            in_math = not in_math
            continue
        if in_math:
            output.append(line)
            continue
        inline_display = re.fullmatch(r"\s*\$\$(.+?)\$\$\s*", line)
        if inline_display:
            output.extend(["$$", inline_display.group(1), "$$"])
            continue
        line = strip_hard_break(line)
        output.append(escape_obsidian_patterns(line))
    return "\n".join(output).strip()


def option_contents(line):
    line = strip_hard_break(line).strip()
    matches = list(OPTION_TOKEN_RE.finditer(line))
    if not matches or matches[0].start() != 0:
        return []
    letters = [match.group(1).lower() for match in matches]
    if len(matches) > 1 and len(set(letters)) == len(letters) and letters == sorted(letters):
        return [
            f"({match.group(1)}) "
            f"{line[match.end():matches[index + 1].start()].strip()}"
            if index + 1 < len(matches)
            else f"({match.group(1)}) {line[match.end():].strip()}"
            for index, match in enumerate(matches)
        ]
    first = matches[0]
    return [f"({first.group(1)}) {line[first.end():].strip()}"]


def crop_and_embed(q, text, attachments_dir, figure_counts):
    if not FIG_RE.search(text):
        return text, 0
    image, _, _, _ = prepare_image(q, SKEW)
    cropped, calls = crop_figures(q, text, image)
    base = f"資工考研 100 - 107 考古題：{q['group']}"
    problem = problem_range(q)[0]
    for index, token in enumerate(calls):
        crop_path = CACHE / "crop" / f"{q['id']}-{index}.jpg"
        if not crop_path.exists():
            raise FileNotFoundError(f"figure crop not found: {crop_path}")
        paper_suffix = f" {safe_component(q['paper'])}" if q["paper_multi"] else ""
        figure_key = (
            q["group"],
            q["school"],
            q["year"],
            q["paper"] if q["paper_multi"] else "",
            problem,
        )
        figure_counts[figure_key] += 1
        figure_number = figure_counts[figure_key]
        filename = (
            f"{safe_component(q['school'])} {q['year']}{paper_suffix} "
            f"Problem {problem}{f'-{figure_number}' if figure_number > 1 else ''}.png"
        )
        target = attachments_dir / base / filename
        target.parent.mkdir(parents=True, exist_ok=True)
        with Image.open(crop_path) as cropped_image:
            cropped_image.save(target, format="PNG")
        embed = f"![[{base}/{filename}]]"
        if token not in cropped:
            raise ValueError(f"figure placeholder lost for {q['id']}: {token}")
        cropped = cropped.replace(token, embed)
    return cropped, len(calls)


def process_question_text(q, text, attachments_dir, figure_counts):
    text, scores = strip_question_numbers(text, q)
    text, image_count = crop_and_embed(q, text, attachments_dir, figure_counts)
    options = []
    lines = []
    for line in text.splitlines():
        parsed_options = option_contents(line) if q["is_mc"] else []
        if parsed_options:
            options.extend(parsed_options)
            lines.extend(f"- [ ] {option}" for option in parsed_options)
        else:
            lines.append(line)
    text = normalize_markdown("\n".join(lines))
    return text, scores, options, image_count


def quote_block(text):
    if not text:
        return []
    return [f"> {line}" if line else ">" for line in text.splitlines()]


def note_location(out, questions, papers_by_folder):
    q = questions[0]
    multi = len(papers_by_folder[(q["group"], q["school"], q["year"])]) > 1
    q["paper_multi"] = multi
    folder = f"{safe_component(q['school'])} {q['year']}"
    if multi:
        folder += f" {safe_component(q['paper'])}"
    directory = out / "資工所考古題" / q["group"] / folder
    start = problem_range(questions[0])[0]
    end = problem_range(questions[-1])[1]
    note_range = str(start) if start == end else f"{start} ~ {end}"
    title = f"{q['school']} {q['year']} {q['group']}"
    if multi:
        title += f" {q['paper']}"
    title += f" - Problem {note_range}"
    return directory / f"Problem {note_range}.md", title


def record_for_group(out, group, attachments_dir, papers_by_folder, figure_counts):
    first = group[0]
    shared_count = (
        min(leading_match(first["normalized"], q["normalized"]) for q in group[1:])
        if len(group) > 1 else 0
    )
    if shared_count == len(first["paragraphs"]):
        shared_count = 0
    is_group = len(group) > 1
    content_parts = []
    option_groups = []
    scores_for_single = []
    image_count = 0
    if is_group:
        first_full = "\n\n".join(first["paragraphs"])
        first_full, count = crop_and_embed(first, first_full, attachments_dir, figure_counts)
        image_count += count
        first_paragraphs = [
            paragraph for paragraph in re.split(r"\n\s*\n", first_full.strip()) if paragraph.strip()
        ]
        shared_raw = "\n\n".join(first_paragraphs[:shared_count])
        shared_raw, shared_scores = strip_question_numbers(shared_raw, first)
        shared_text = normalize_markdown(shared_raw)
        if shared_text:
            content_parts.append(shared_text)
        first_unique = "\n\n".join(first_paragraphs[shared_count:])
        processed, scores, options, count = process_question_text(
            first, first_unique, attachments_dir, figure_counts
        )
        # Figures in the first question were already cropped with the shared stem.
        # Avoid a second crop pass while retaining all previously replaced embeds.
        image_count += count
        content_parts.append(f"**Problem {problem_label(first)}**")
        first_scores = shared_scores + scores
        if first_scores:
            content_parts.extend(f"> Score: {score}" for score in first_scores)
        if processed:
            content_parts.append(processed)
        if first["is_mc"]:
            option_groups.append((problem_label(first), options))
        for group_index, q in enumerate(group[1:], 1):
            matches = [
                leading_match(old["normalized"], q["normalized"])
                for old in group[:group_index]
            ]
            drop = max(matches, default=0)
            if drop >= len(q["paragraphs"]):
                drop = 0
            unique = "\n\n".join(q["paragraphs"][drop:])
            processed, scores, options, count = process_question_text(
                q, unique, attachments_dir, figure_counts
            )
            image_count += count
            content_parts.append(f"**Problem {problem_label(q)}**")
            content_parts.extend(f"> Score: {score}" for score in scores)
            if processed:
                content_parts.append(processed)
            if q["is_mc"]:
                option_groups.append((problem_label(q), options))
    else:
        text = "\n\n".join(first["paragraphs"])
        processed, scores_for_single, options, image_count = process_question_text(
            first, text, attachments_dir, figure_counts
        )
        content_parts.append(processed)
        if first["is_mc"]:
            option_groups.append((problem_label(first), options))

    path, title = note_location(out, group, papers_by_folder)
    return {
        "path": path,
        "title": title,
        "questions": group,
        "content": "\n\n".join(part for part in content_parts if part),
        "shared_stem": is_group,
        "single_scores": scores_for_single,
        "option_groups": option_groups,
        "image_count": image_count,
    }


def render_note(records, today):
    first = records[0]
    title = first["title"]
    note = [
        "---",
        f"date: {today}",
        "publish:",
        "description:",
        "---",
        f"> [!note] {title}",
    ]
    is_group_note = any(record["shared_stem"] for record in records)
    if len(records) == 1 and not is_group_note:
        for score in first["single_scores"]:
            note.append(f"> > Score: {score}")
        note.append(">")
        note.extend(quote_block(first["content"]))
    else:
        note.append(">")
        for record in records:
            note.extend(quote_block(record["content"]))

    note.append("")
    for record in records:
        for label, options in record["option_groups"]:
            if not options:
                continue
            if len(record["questions"]) > 1 or len(records) > 1:
                note.append(f"**Problem {label}**")
            note.extend(f"- [ ] {option}" for option in options)
            if options:
                note.append("")
    return "\n".join(note).rstrip() + "\n"


def export(out):
    questions, groups_by_id = read_manifest_questions()
    attachments_dir = out / "_Attachments"
    attachments_dir.mkdir(parents=True, exist_ok=True)
    papers_by_folder = defaultdict(set)
    for q in questions:
        papers_by_folder[(q["group"], q["school"], q["year"])].add(q["paper"])
    for q in questions:
        q["paper_multi"] = len(papers_by_folder[(q["group"], q["school"], q["year"])]) > 1

    paper_questions = defaultdict(list)
    for q in questions:
        paper_questions[(q["group"], q["year"], q["school"], q["paper"])].append(q)

    records_by_path = defaultdict(list)
    expected_ids = set()
    figure_counts = Counter()
    for paper in paper_questions.values():
        ordered = sorted(paper, key=order_key)
        for group in stem_groups(ordered):
            record = record_for_group(
                out, group, attachments_dir, papers_by_folder, figure_counts
            )
            records_by_path[record["path"]].append(record)
            expected_ids.update(q["id"] for q in group)

    if expected_ids != set(groups_by_id):
        missing = sorted(set(groups_by_id) - expected_ids)
        extra = sorted(expected_ids - set(groups_by_id))
        raise ValueError(f"question coverage mismatch: missing={missing}, extra={extra}")

    note_count = 0
    grouped_note_count = 0
    image_count = 0
    exported_ids = Counter()
    for path, records in records_by_path.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(render_note(records, datetime.date.today().isoformat()))
        note_count += 1
        grouped_note_count += sum(record["shared_stem"] for record in records)
        image_count += sum(record["image_count"] for record in records)
        for record in records:
            for q in record["questions"]:
                exported_ids[q["id"]] += 1

    repeated = sorted(qid for qid, count in exported_ids.items() if count != 1)
    if repeated or set(exported_ids) != expected_ids:
        raise ValueError(f"IDs must appear in exactly one note: repeated={repeated}")
    for path in out.rglob("*"):
        if ":" in str(path):
            raise ValueError(f"ASCII colon in output path: {path}")

    multi_paper_folders = []
    for (group, school, year), papers in sorted(papers_by_folder.items()):
        if len(papers) > 1:
            multi_paper_folders.extend(
                f"{group}/{safe_component(school)} {year} {safe_component(paper)}"
                for paper in sorted(papers)
            )
    multi_group_ids = sum(len(groups) > 1 for groups in groups_by_id.values())
    multiple_choice_count = sum(q["is_mc"] for q in questions)
    print(f"Notes: {note_count}")
    print(f"IDs: {len(exported_ids)}")
    print(f"題組 notes: {grouped_note_count}")
    print(f"MC questions: {multiple_choice_count}")
    print(f"Images: {image_count}")
    print(f"Multi-group IDs: {multi_group_ids}")
    print("Multi-paper folders:")
    for folder in multi_paper_folders:
        print(f"  {folder}")
    print(f"Vault: {out}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=Path.home() / "obsidian-out")
    args = parser.parse_args()
    out = args.out.expanduser().resolve()
    if out == PE.resolve() or PE.resolve() in out.parents:
        parser.error("--out must be outside the repository")
    export(out)


if __name__ == "__main__":
    main()
