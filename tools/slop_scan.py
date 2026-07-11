#!/usr/bin/env python3
"""Scan chapters for AI-writing tics.

Usage: python3 tools/slop_scan.py [dir ...] [--lines] [--all]

Default mode runs the high-signal detectors (stock phrases, hype words,
punchy fragments, prose em-dashes, emojis) and exits 1 on any hit, so it
works as a regression gate: `python3 tools/slop_scan.py && echo clean`.

--all additionally runs the noisy advisory detectors (comma-splice,
bold-heavy, emphasis-contrast). Those are informational; they flag
structural conventions and legitimate prose too, so review by hand.
--lines prints each offending line.
"""
import re, sys, pathlib, collections

PATTERNS = {
    'stock-phrase': re.compile(r"(?i)\b(here's the thing|the whole game|the whole story|the whole point|in your bones|with your own hands|the mental hook|that's the proof|no black boxes|crucially|delve|the entire reason|let's make sure you (actually )?believe|earn(ed)? (the|this) chapter|burn(ed)? in(to)?\b)"),
    'hype': re.compile(r"(?i)\b(superpower|magic(al)?\b|insanely?\b|beautiful(ly)?|stunning|blazing|gorgeous|genuinely|the flex|crown jewel|mind[- ]blowing)"),
    'punchy-frag': re.compile(r"(?:^|\. )(That's it\.|There it is\.|Terrible\.|Slick\.|Done\.|Boom\.|Simple as that\.|Full stop\.)"),
    'em-dash': re.compile(r"—"),
    'emoji': re.compile("[\U0001F300-\U0001FAFF✅❌✨⭐]"),
}
ADVISORY = {
    'comma-splice': re.compile(r", (it|this|that|they|you|we)('s| is| are| was| were)? (just|the|a|an|not|why|how|what)\b"),
    'bold-heavy': None,   # computed per line
    'emphasis-contrast': re.compile(r"_[a-z]+_,? not _[a-z]+_|\*[a-z]+\*,? not \*[a-z]+\*"),
}
# Legitimate uses that would otherwise trip a detector. A line matching any
# of these is skipped for the named detector only.
WHITELIST = {
    'hype': re.compile(r"(?i)(beautifulsoup|magic (number|string|constant|value|method)s?|\"magic\"|'magic'|`magic`|magic GUID|MAGIC)"),
    'stock-phrase': re.compile(r"(?i)(burn(ed)?-in|burn in the (die|chip|silicon))"),
    'emoji': re.compile("\U0001F600"),  # U+1F600 is subject matter in 01.1 Unicode examples
}

def scan(paths, patterns):
    per_file = collections.defaultdict(collections.Counter)
    hits = collections.defaultdict(list)
    for p in paths:
        in_f = False
        for i, ln in enumerate(p.read_text(encoding='utf-8').split('\n'), 1):
            s = ln.lstrip()
            if s.startswith('```') or s.startswith('~~~'):
                in_f = not in_f; continue
            if in_f: continue
            for name, pat in patterns.items():
                if name == 'em-dash' and s.startswith('|'):
                    continue  # em-dash as an empty table cell is fine
                wl = WHITELIST.get(name)
                if wl and wl.search(ln):
                    continue
                if pat is None:
                    if ln.count('**') >= 6:   # 3+ bold spans on one line
                        per_file[p][name] += 1; hits[p].append((i, name, ln.strip()[:100]))
                elif pat.search(ln):
                    per_file[p][name] += 1; hits[p].append((i, name, ln.strip()[:100]))
    return per_file, hits

if __name__ == '__main__':
    root = pathlib.Path(__file__).resolve().parent.parent
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    dirs = args or [d.name for d in sorted(root.iterdir()) if d.is_dir() and d.name[0].isdigit()]
    files = [p for d in dirs for p in sorted((root / d).glob('*.md'))]
    patterns = dict(PATTERNS)
    if '--all' in sys.argv:
        patterns.update(ADVISORY)
    per_file, hits = scan(files, patterns)
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
    gate = sum(v for k, v in tot.items() if k in PATTERNS)
    sys.exit(1 if gate else 0)
