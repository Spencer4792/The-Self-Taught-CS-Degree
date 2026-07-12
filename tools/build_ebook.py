#!/usr/bin/env python3
"""Build EPUB (and optionally PDF) editions of the book from SUMMARY.md order.

Usage:
  python3 tools/build_ebook.py epub                 -> dist/cs-mastery.epub
  python3 tools/build_ebook.py tex                  -> dist/cs-mastery.tex (for PDF)
  python3 tools/build_ebook.py stage-tex <N>        -> dist/stage-<N>.tex

Requires pandoc. PDF additionally requires xelatex (run it on the .tex output).
Mermaid diagrams are replaced with a pointer to the web edition (ASCII art
in the chapters already covers most of them).
"""
import re, sys, subprocess, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
DIST = ROOT / "dist"
SITE = "https://spencer4792.github.io/The-Self-Taught-CS-Degree/"

def parse_summary():
    stages, cur = [], None
    for ln in (ROOT / "SUMMARY.md").read_text(encoding="utf-8").split("\n"):
        m_sec = re.match(r"^# (?!Summary)(.+)$", ln.strip())
        m_item = re.match(r"^-?\s*\[([^\]]+)\]\(([^)]+\.md)\)$", ln.strip())
        if m_sec:
            cur = (m_sec.group(1), [])
            stages.append(cur)
        elif m_item and cur is not None:
            cur[1].append((m_item.group(1), m_item.group(2)))
    return stages

def transform(text):
    """Prepare one chapter's markdown for ebook conversion."""
    out, in_fence, fence_lang, buf = [], False, None, []
    for ln in text.split("\n"):
        s = ln.lstrip()
        if not in_fence and s.startswith("```"):
            in_fence, fence_lang, buf = True, s[3:].strip().lower(), [ln]
            continue
        if in_fence:
            buf.append(ln)
            if s.startswith("```") and len(buf) > 1:
                in_fence = False
                if fence_lang == "mermaid":
                    out.append(f"*(Interactive diagram in the [web edition]({SITE}).)*")
                else:
                    out.extend(buf)
            continue
        # demote headings one level (stages become chapters' parents)
        if re.match(r"^#{1,5} ", ln):
            ln = "#" + ln
        # chapter-to-chapter links -> plain emphasis (targets don't exist in ebook)
        ln = re.sub(r"\[([^\]]+)\]\((?!https?://)[^)]*\.md[^)]*\)", r"*\1*", ln)
        ln = re.sub(r"\[([^\]]+)\]\(#[^)]*\)", r"*\1*", ln)
        out.append(ln)
    return "\n".join(out)

def concat(stages):
    parts = ["---",
             'title: "The Self-Taught CS Degree"',
             'author: "Spencer Hales"',
             f'date: ""',
             "lang: en",
             "---", ""]
    for stage_title, chapters in stages:
        parts.append(f"# {stage_title}\n")
        for _, path in chapters:
            p = ROOT / path
            if p.exists():
                parts.append(transform(p.read_text(encoding="utf-8")))
                parts.append("")
    return "\n".join(parts)

def pdf_sanitize(md):
    # xelatex with DejaVu lacks astral-plane emoji; keep the codepoint readable
    return md.replace("\U0001F600", "[U+1F600]")

PDF_VARS = ["-V", "mainfont=DejaVu Serif", "-V", "monofont=DejaVu Sans Mono",
            "-V", "sansfont=DejaVu Sans", "-V", "geometry:margin=2.2cm",
            "-V", "fontsize=10pt", "-V", "documentclass=report",
            "--toc", "--toc-depth=2", "--pdf-engine=xelatex"]

def run_pandoc(md_text, out_path, fmt):
    DIST.mkdir(exist_ok=True)
    src = DIST / "_book.md"
    src.write_text(md_text, encoding="utf-8")
    if fmt == "epub":
        cmd = ["pandoc", str(src), "-o", str(out_path), "--toc", "--toc-depth=2",
               "--epub-chapter-level=2", "--metadata", "title=The Self-Taught CS Degree"]
    else:  # tex
        cmd = ["pandoc", str(src), "-s", "-o", str(out_path), "--top-level-division=part"] + \
              [a for a in PDF_VARS if a != "--pdf-engine=xelatex"]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print(r.stderr[-3000:])
        sys.exit(1)
    print(f"wrote {out_path}")

if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "epub"
    stages = parse_summary()
    if mode == "epub":
        run_pandoc(concat(stages), DIST / "cs-mastery.epub", "epub")
    elif mode == "tex":
        run_pandoc(pdf_sanitize(concat(stages)), DIST / "cs-mastery.tex", "tex")
    elif mode == "stage-tex":
        n = int(sys.argv[2])
        run_pandoc(pdf_sanitize(concat([stages[n]])), DIST / f"stage-{n}.tex", "tex")
    else:
        sys.exit("unknown mode")
