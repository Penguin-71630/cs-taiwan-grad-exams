import argparse
import json
import re
import subprocess
import sys


def list_folder(folder_id):
    result = subprocess.run(
        ["curl", "-fsSL", f"https://drive.google.com/drive/folders/{folder_id}"],
        capture_output=True, text=True, check=True,
    )
    match = re.search(r"window\['_DRIVE_ivd'\]\s*=\s*'(.*?)';", result.stdout, re.S)
    if not match:
        raise RuntimeError(f"could not parse Drive folder {folder_id}")
    raw = match.group(1)
    decoded = re.sub(
        r"\\x([0-9a-fA-F]{2})",
        lambda item: chr(int(item.group(1), 16)),
        raw,
    ).replace(r"\/", "/").replace(r"\'", "'")
    data = json.loads(decoded)
    return [(item[0], item[2], item[3]) for item in (data[0] or [])]


def walk(folder_id, prefix="", allowed=None):
    entries = list_folder(folder_id)
    for item_id, name, mime in entries:
        if mime.endswith("folder"):
            if allowed is not None and item_id not in allowed:
                continue
            next_prefix = allowed[item_id] if allowed is not None else name
            path = "/".join(part for part in (prefix, next_prefix) if part)
            walk(item_id, path)
        elif name != "_DS_Store":
            path = "/".join(part for part in (prefix, name) if part)
            print(f"{path}\t{item_id}")


def main():
    parser = argparse.ArgumentParser(
        usage="drive_ls.py <folder_id> [subpath_name] [--subfolder ID:PREFIX ...]"
    )
    parser.add_argument("folder_id")
    parser.add_argument("subpath_name", nargs="?", default="")
    parser.add_argument(
        "--subfolder", action="append", default=[], metavar="ID:PREFIX",
        help="restrict the root listing to these child folders and prefix their paths",
    )
    args = parser.parse_args()
    allowed = {}
    for value in args.subfolder:
        folder_id, prefix = value.split(":", 1)
        allowed[folder_id] = prefix
    walk(args.folder_id, args.subpath_name, allowed if allowed else None)


if __name__ == "__main__":
    try:
        main()
    except (RuntimeError, ValueError, subprocess.CalledProcessError) as error:
        print(error, file=sys.stderr)
        raise SystemExit(1)
