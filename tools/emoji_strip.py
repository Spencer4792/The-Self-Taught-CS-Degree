#!/usr/bin/env python3
"""Strip emojis from chapters. Table cells: checkmark/cross -> Yes/No.
Elsewhere: checkmark/cross -> plain unicode tick/x; decorative emoji removed.
Whitelist: U+1F600 in 01.1 (Unicode encoding examples). Usage: python3 tools/emoji_strip.py [--dry]
"""
import re, sys, pathlib

EMOJI = re.compile(
    "[\U0001F000-\U0001FAFF✅❌✨⭐⚠❗❓❤"
    "⬆⬇\U0001F004️‍\U0001F1E6-\U0001F1FF]"
)
KEEP_1F600 = "01.1-data-representation.md"

def clean_line(ln, is_table):
    if is_table:
        ln = ln.replace("✅", "Yes").replace("❌", "No")
        ln = ln.replace("⚠️", "Partial").replace("⚠", "Partial")
    else:
        ln = ln.replace("✅", "✓").replace("❌", "✗")
    ln = EMOJI.sub("", ln)
    # tidy: leftover double spaces outside leading indent, trailing space
    m = re.match(r"^(\s*)(.*)$", ln)
    body = re.sub(r"  +", " ", m.group(2)) if not is_table else m.group(2)
    return (m.group(1) + body).rstrip()

def process(path, dry):
    text = path.read_text(encoding="utf-8")
    out, changed = [], 0
    for ln in text.split("\n"):
        keep = ""
        if path.name == KEEP_1F600:
            ln = ln.replace("\U0001F600", "\x00")  # protect
        if EMOJI.search(ln):
            is_table = ln.lstrip().startswith("|")
            new = clean_line(ln, is_table)
            if new != ln:
                changed += 1
            ln = new
        ln = ln.replace("\x00", "\U0001F600")
        out.append(ln)
    if changed and not dry:
        path.write_text("\n".join(out), encoding="utf-8")
    return changed

if __name__ == "__main__":
    dry = "--dry" in sys.argv
    root = pathlib.Path(__file__).resolve().parent.parent
    total = files = 0
    for p in sorted(root.rglob("*.md")):
        c = process(p, dry)
        if c:
            files += 1
            total += c
            print(f"{c:4d}  {p.relative_to(root)}")
    print(f"\n{'DRY RUN: would change' if dry else 'Changed'} {total} lines in {files} files")
