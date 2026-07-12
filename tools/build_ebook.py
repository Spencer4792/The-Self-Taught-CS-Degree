#!/usr/bin/env python3
"""Build EPUB and PDF editions of the book from SUMMARY.md order.

Each chapter is parsed SEPARATELY through pandoc's AST (matching how the
website and GitHub render them), filtered (mermaid fallbacks, internal-link
handling), and only then assembled. Concatenating raw markdown is unsafe:
fence-state can leak across chapter boundaries.

Usage:
  python3 tools/build_ebook.py frags     # parse+filter all chapters -> dist/_frag/
  python3 tools/build_ebook.py epub      # frags -> dist/cs-mastery.epub
  python3 tools/build_ebook.py tex       # frags -> dist/cs-mastery.tex (then run xelatex twice)

Requires pandoc; PDF additionally requires xelatex with DejaVu fonts.
"""
import re, sys, json, subprocess, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
DIST = ROOT / "dist"
FRAG = DIST / "_frag"
SITE = "https://spencer4792.github.io/The-Self-Taught-CS-Degree/"

# ---------------------------------------------------------------- summary
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

# ---------------------------------------------------------------- AST filter
def _walk(node):
    if isinstance(node, list):
        return [_walk(x) for x in node]
    if not isinstance(node, dict):
        return node
    t = node.get("t")
    if t == "CodeBlock":
        (_, classes, _), _code = node["c"]
        if "mermaid" in classes:
            return {"t": "Para", "c": [{"t": "Emph", "c": [
                {"t": "Str", "c": "(Interactive diagram in the web edition: "},
                {"t": "Str", "c": SITE}, {"t": "Str", "c": ")"}]}]}
        return node
    if t == "Link":
        attr, inlines, (url, _title) = node["c"]
        if not url.startswith(("http://", "https://", "mailto:")):
            return {"t": "Emph", "c": _walk(inlines)}
        return {"t": "Link", "c": [attr, _walk(inlines), [url, _title]]}
    node = dict(node)
    if "c" in node:
        node["c"] = _walk(node["c"])
    return node

def build_frags():
    FRAG.mkdir(parents=True, exist_ok=True)
    n = 0
    for _, chapters in parse_summary():
        for _, path in chapters:
            src = ROOT / path
            slug = path.replace("/", "__")
            out = FRAG / (slug + ".json")
            if out.exists() and out.stat().st_mtime > src.stat().st_mtime:
                continue
            r = subprocess.run(["pandoc", "-f", "markdown", "-t", "json", str(src)],
                               capture_output=True, text=True, check=True)
            doc = json.loads(r.stdout)
            doc["blocks"] = _walk(doc["blocks"])
            out.write_text(json.dumps(doc), encoding="utf-8")
            n += 1
    print(f"filtered {n} chapters -> {FRAG}")

def convert_frag(path, to, extra=()):
    r = subprocess.run(["pandoc", "-f", "json", "-t", to, str(path), *extra],
                       capture_output=True, text=True, check=True)
    return r.stdout

# --- PDF-only: long inline code can't break inside \texttt{...}; split it
#     into chunks joined by \allowbreak so TeX can wrap between them.
def _split_code_text(text, width=22):
    chunks, cur = [], ""
    for ch in text:
        cur += ch
        if len(cur) >= width and ch in ',;&=/:)]}_.- ':
            chunks.append(cur); cur = ""
        elif len(cur) >= width + 14:      # no natural break point found
            chunks.append(cur); cur = ""
    if cur: chunks.append(cur)
    return chunks

def _walk_pdf(node):
    if isinstance(node, list):
        out = []
        for x in node:
            if isinstance(x, dict) and x.get("t") == "Code" and len(x["c"][1]) > 30:
                attr, text = x["c"]
                pieces = _split_code_text(text)
                for k, piece in enumerate(pieces):
                    if k:
                        out.append({"t": "RawInline", "c": ["latex", "\\allowbreak{}"]})
                    out.append({"t": "Code", "c": [attr, piece]})
            else:
                out.append(_walk_pdf(x))
        return out
    if isinstance(node, dict):
        node = dict(node)
        if "c" in node:
            node["c"] = _walk_pdf(node["c"])
        return node
    return node

# ---------------------------------------------------------------- EPUB
def build_epub():
    parts = ["<html><body>"]
    for stage_title, chapters in parse_summary():
        parts.append(f"<h1>{stage_title}</h1>")
        for _, path in chapters:
            frag = FRAG / (path.replace("/", "__") + ".json")
            html = convert_frag(frag, "html")
            # chapter's own H1 stays; shift to h1 is already the case
            parts.append(html)
    parts.append("</body></html>")
    big = DIST / "_book.html"
    big.write_text("\n".join(parts), encoding="utf-8")
    out = DIST / "cs-mastery.epub"
    subprocess.run(["pandoc", "-f", "html", str(big), "-o", str(out),
                    "--toc", "--toc-depth=2", "--epub-chapter-level=1",
                    "--metadata", "title=The Self-Taught CS Degree",
                    "--metadata", "author=Spencer Hales"], check=True)
    print(f"wrote {out}")

# ---------------------------------------------------------------- PDF (tex)
HEADER = r"""
\usepackage{fvextra}
\DefineVerbatimEnvironment{Highlighting}{Verbatim}{breaklines,breakanywhere,fontsize=\small,commandchars=\\\{\}}
\RecustomVerbatimEnvironment{verbatim}{Verbatim}{breaklines,breakanywhere,fontsize=\footnotesize}
\usepackage{etoolbox}
\AtBeginEnvironment{longtable}{\footnotesize}
\usepackage[htt]{hyphenat}
\emergencystretch=3em
\usepackage{xurl}
\usepackage{newunicodechar}
\newfontfamily\glyphfb{DejaVu Sans}
""" + "\n".join(
    r"\newunicodechar{%s}{{\glyphfb %s}}" % (c, c)
    for c in "✓✗ℂ∎∥≪≫⊨⋈①②③④⑤⑥⑦⑧⑨⟺")

def build_tex():
    # get a standalone preamble from pandoc itself
    dummy = DIST / "_dummy.md"
    # the dummy must exercise highlighting + tables so pandoc's standalone
    # template emits the Shaded/Highlighting macros and longtable support
    dummy.write_text("x\n\n```python\nx = 1\n```\n\n| a | b |\n|---|---|\n| 1 | 2 |\n", encoding="utf-8")
    hdr = DIST / "_header.tex"
    hdr.write_text(HEADER, encoding="utf-8")
    shell = subprocess.run(
        ["pandoc", str(dummy), "-s", "-t", "latex", "--toc", "--toc-depth=2",
         "-H", str(hdr), "--top-level-division=chapter",
         "-V", "documentclass=report", "-V", "mainfont=DejaVu Serif",
         "-V", "monofont=DejaVu Sans Mono", "-V", "sansfont=DejaVu Sans",
         "-V", "geometry:margin=2.2cm", "-V", "fontsize=10pt",
         "-V", "title=The Self-Taught CS Degree", "-V", "author=Spencer Hales",
         "-V", "colorlinks=true"],
        capture_output=True, text=True, check=True).stdout
    preamble = shell.split("\\begin{document}")[0]
    post = shell.split("\\begin{document}")[1]
    front = post.split("\\tableofcontents")[0] + "\\tableofcontents\n\\setcounter{tocdepth}{1}\n"

    body = []
    for stage_title, chapters in parse_summary():
        safe = stage_title.replace("&", "\\&").replace("%", "\\%").replace("#", "\\#")
        body.append("\\part{%s}" % safe)
        for _, path in chapters:
            frag = FRAG / (path.replace("/", "__") + ".json")
            doc = json.loads(frag.read_text(encoding="utf-8"))
            doc["blocks"] = _walk_pdf(doc["blocks"])
            tmp = FRAG / "_pdf_tmp.json"
            tmp.write_text(json.dumps(doc), encoding="utf-8")
            # --no-highlight: colored tokens become unbreakable macro args in
            # LaTeX; plain verbatim + fvextra can wrap long lines anywhere
            tex = convert_frag(tmp, "latex", ["--top-level-division=chapter", "--no-highlight"])
            body.append(tex.replace("\U0001F600", "[U+1F600]"))
    out = DIST / "cs-mastery.tex"
    out.write_text(preamble + "\\begin{document}" + front + "\n".join(body) +
                   "\n\\end{document}\n", encoding="utf-8")
    print(f"wrote {out}  (run: cd dist && xelatex cs-mastery.tex, twice)")

if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "epub"
    DIST.mkdir(exist_ok=True)
    if mode == "frags":
        build_frags()
    elif mode == "epub":
        build_frags(); build_epub()
    elif mode == "tex":
        build_frags(); build_tex()
    else:
        sys.exit("unknown mode: frags | epub | tex")
