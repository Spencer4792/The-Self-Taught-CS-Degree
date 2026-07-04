import pathlib, subprocess, sys, json

import re, pathlib

def blocks(path):
    out, cur, lang, in_f = [], [], None, False
    for ln in path.read_text(encoding="utf-8").split("\n"):
        s = ln.strip()
        if not in_f and s.startswith("```"):
            in_f, lang, cur = True, s[3:].strip().lower(), []
        elif in_f and s.startswith("```"):
            in_f = False
            if lang in ("python", "py"): out.append("\n".join(cur))
        elif in_f:
            cur.append(ln)
    return out

def runnable(b):
    if re.search(r"^\s*\.\.\.", b, re.M): return False
    if any(k in b for k in ("input(", "while True:", "plt.show()")): return False
    return True


root = pathlib.Path(__file__).resolve().parent.parent
import json as _j
done = set()
try:
    for _ln in open('qa-results.jsonl'):
        _r = _j.loads(_ln); done.add((_r['file'], _r['block']))
except FileNotFoundError:
    pass
out = open('qa-results.jsonl', 'a')
import sys as _s
files = [p for d in _s.argv[1:] for p in sorted((root / d).glob('*.md'))]
for p in files:
    bs = blocks(p)
    ns_src = ''
    for i, b in enumerate(bs):
        rec = {'file': str(p.relative_to(root)), 'block': i}
        if (rec['file'], rec['block']) in done:
            if rec.get('status') != 'FAIL': pass
            continue
        if not runnable(b):
            rec['status'] = 'SKIP'
        else:
            try:
                import time as _t
                trial = ns_src + '\n\n' + b
                t0 = _t.time()
                r = subprocess.run([sys.executable, '-c', trial], capture_output=True, text=True, timeout=6)
                el = _t.time() - t0
                if r.returncode == 0:
                    if el < 3.0: ns_src = trial
                    rec['status'] = 'OK'
                else:
                    r2 = subprocess.run([sys.executable, '-c', b], capture_output=True, text=True, timeout=6)
                    if r2.returncode == 0:
                        rec['status'] = 'OK'
                    else:
                        err = (r2.stderr or r.stderr).strip().split('\n')[-1][:250]
                        rec['status'] = 'DEP' if ('ModuleNotFoundError' in err or 'ImportError' in err) else 'FAIL'
                        rec['error'] = err
            except subprocess.TimeoutExpired:
                rec['status'] = 'TIMEOUT'
        out.write(json.dumps(rec) + '\n'); out.flush()
out.close()
print('DONE')
