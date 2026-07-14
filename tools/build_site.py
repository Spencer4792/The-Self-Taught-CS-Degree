#!/usr/bin/env python3
"""Build the book as a static website from SUMMARY.md.

Usage: python3 tools/build_site.py [output-dir] [--strict]   (default: book-site/)

--strict passes mkdocs build --strict, turning any warning (broken links,
missing nav targets) into a build failure. CI uses this as a link gate.

Parses SUMMARY.md (the curriculum order), generates a Material for MkDocs
config, stages the markdown into a temp docs dir, and builds. Requires:
    pip install mkdocs-material pymdown-extensions

To browse with working search, serve it:  python3 -m http.server -d book-site
"""
import re, sys, shutil, subprocess, pathlib, tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
_args = [a for a in sys.argv[1:] if not a.startswith("--")]
OUT = pathlib.Path(_args[0]) if _args else ROOT / "book-site"
STRICT = "--strict" in sys.argv

def parse_summary():
    """Return nav structure: list of (section_title, [(title, path), ...])."""
    nav, section = [], None
    front = []
    for ln in (ROOT / "SUMMARY.md").read_text(encoding="utf-8").split("\n"):
        m_sec = re.match(r"^# (?!Summary)(.+)$", ln.strip())
        m_item = re.match(r"^-?\s*\[([^\]]+)\]\(([^)]+\.md)\)$", ln.strip())
        if m_sec:
            section = (m_sec.group(1), [])
            nav.append(section)
        elif m_item:
            title, path = m_item.group(1), m_item.group(2)
            if section is None:
                front.append((title, path))
            else:
                section[1].append((title, path))
    return front, nav

def yml_escape(s):
    return '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'

def main():
    front, nav = parse_summary()
    stage = pathlib.Path(tempfile.mkdtemp(prefix="booksite_"))
    docs = stage / "docs"
    docs.mkdir()

    # stage every md file referenced plus any md the chapters link to, and all dirs
    for d in ROOT.iterdir():
        if d.is_dir() and re.match(r"\d", d.name):
            shutil.copytree(d, docs / d.name)
    for extra in ("STUDY-GUIDE.md", "PROGRESS.md", "PROJECTS.md",
                  "CHECKPOINTS.md", "SUMMARY.md", "LICENSE"):
        p = ROOT / extra
        if p.exists():
            shutil.copy(p, docs / p.name)
    # ship the Anki deck so the README's download link works on the site
    if (ROOT / "study").exists():
        (docs / "study").mkdir(exist_ok=True)
        for f in (ROOT / "study").glob("*.*"):
            if f.suffix in (".apkg", ".tsv"):
                shutil.copy(f, docs / "study" / f.name)
    # README becomes the site index; rewrite links pointing at it
    if (ROOT / "README.md").exists():
        shutil.copy(ROOT / "README.md", docs / "index.md")
    for md in docs.rglob("*.md"):
        t = md.read_text(encoding="utf-8")
        t2 = t.replace("(README.md)", "(index.md)").replace("(../README.md)", "(../index.md)")
        if t2 != t:
            md.write_text(t2, encoding="utf-8")

    lines = [
        "site_name: CS Mastery",
        "site_description: A from-scratch computer science curriculum",
        "use_directory_urls: false",
        "theme:",
        "  name: material",
        "  palette:",
        "    - scheme: default",
        "      toggle: {icon: material/brightness-7, name: Dark mode}",
        "    - scheme: slate",
        "      toggle: {icon: material/brightness-4, name: Light mode}",
        "  features:",
        "    - navigation.sections",
        "    - navigation.top",
        "    - search.suggest",
        "    - content.code.copy",
        "markdown_extensions:",
        "  - admonition",
        "  - tables",
        "  - pymdownx.superfences:",
        "      custom_fences:",
        "        - name: mermaid",
        "          class: mermaid",
        "          format: !!python/name:pymdownx.superfences.fence_code_format",
        "  - pymdownx.highlight",
        "  - toc:",
        "      permalink: true",
        "      # GitHub-identical anchors so in-book #links work in both renderers",
        "      slugify: !!python/object/apply:pymdownx.slugs.slugify",
        "        kwds: {case: lower}",
        "plugins:",
        "  - search",
        "nav:",
        "  - Home: index.md",
    ]
    for title, path in front:
        if path == "README.md":
            continue  # already mapped to Home/index.md
        lines.append(f"  - {yml_escape(title)}: {path}")
    for sec_title, items in nav:
        lines.append(f"  - {yml_escape(sec_title)}:")
        for title, path in items:
            lines.append(f"      - {yml_escape(title)}: {path}")
    (stage / "mkdocs.yml").write_text("\n".join(lines) + "\n", encoding="utf-8")

    if OUT.exists():
        shutil.rmtree(OUT)
    cmd = ["mkdocs", "build", "-f", str(stage / "mkdocs.yml"),
           "-d", str(OUT.resolve())]
    if STRICT:
        cmd.append("--strict")
    r = subprocess.run(cmd, capture_output=True, text=True)
    print(r.stdout or "", r.stderr or "", sep="")
    shutil.rmtree(stage)
    if r.returncode != 0:
        sys.exit(1)
    n = sum(1 for _ in OUT.rglob("*.html"))
    print(f"Built {n} pages -> {OUT}")
    print(f"Serve with: python3 -m http.server -d {OUT.name}")

if __name__ == "__main__":
    main()
