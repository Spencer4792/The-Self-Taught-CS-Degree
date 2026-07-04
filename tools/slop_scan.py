#!/usr/bin/env python3
"""Scan chapters for AI-writing tics. Usage: python3 tools/slop_scan.py [dir ...]"""
import re, sys, pathlib, collections

PATTERNS = {
    'stock-phrase': re.compile(r"(?i)\b(here's the thing|the whole game|the whole story|the whole point|in your bones|with your own hands|the mental hook|that's the proof|no black boxes|crucially|delve|the entire reason|let's make sure you (actually )?believe|earn(ed)? (the|this) chapter|burn(ed)? in(to)?\b)"),
    'hype': re.compile(r"(?i)\b(superpower|magic(al)?\b|insanely?\b|beautiful(ly)?|stunning|blazing|gorgeous|genuinely|the flex|crown jewel|mind[- ]blowing)"),
    'punchy-frag': re.compile(r"(?:^|\. )(That's it\.|There it is\.|Terrible\.|Slick\.|Done\.|Boom\.|Simple as that\.|Full stop\.)"),
    'comma-splice': re.compile(r", (it|this|that|they|you|we)('s| is| are| was| were)? (just|the|a|an|not|why|how|what)\b"),
    'bold-heavy': None,   # computed per line
    'emphasis-contrast': re.compile(r"_[a-z]+_,? not _[a-z]+_|\*[a-z]+\*,? not \*[a-z]+\*"),
}

def scan(paths):
    per_file = collections.defaultdict(collections.Counter)
    hits = collections.defaultdict(list)
    for p in paths:
        in_f = False
        for i, ln in enumerate(p.read_text(encoding='utf-8').split('\n'), 1):
            s = ln.lstrip()
            if s.startswith('```') or s.startswith('~~~'):
                in_f = not in_f; continue
            if in_f: continue
            for name, pat in PATTERNS.items():
                if pat is None:
                    if ln.count('**') >= 6:   # 3+ bold spans on one line
                        per_file[p][name] += 1; hits[p].append((i, name, ln.strip()[:100]))
                elif pat.search(ln):
                    per_file[p][name] += 1; hits[p].append((i, name, ln.strip()[:100]))
    return per_file, hits

if __name__ == '__main__':
    root = pathlib.Path(__file__).resolve().parent.parent
    dirs = sys.argv[1:] or [d.name for d in sorted(root.iterdir()) if d.is_dir() and d.name[0].isdigit()]
    files = [p for d in dirs for p in sorted((root / d).glob('*.md'))]
    per_file, hits = scan(files)
    tot = collections.Counter()
    for p, c in sorted(per_file.items(), key=lambda kv: -sum(kv[1].values())):
        tot.update(c)
        print(f"{sum(c.values()):4d}  {p.relative_to(root)}  {dict(c)}")
    print(f"\nTOTAL {sum(tot.values())} hits in {len(per_file)} files: {dict(tot)}")
    if '--lines' in sys.argv:
        print()
        for p in sorted(hits):
            print(f"== {p.relative_to(root)}")
            for i, name, txt in hits[p]:
                print(f"  L{i} [{name}] {txt}")
