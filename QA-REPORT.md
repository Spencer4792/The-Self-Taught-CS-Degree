# Code-Block QA Report

Generated 2026-07-04 by running every fenced Python block in the book (blocks run
cumulatively per file, so later blocks can use earlier definitions). Re-run any time with
`python3 tools/run_code_blocks.py <chapter-dir> [...]`.

## Summary

| Result | Blocks | Meaning |
|---|---|---|
| OK | 714 | Ran clean |
| FAIL | 179 | Raised an error (see breakdown — most are presentation style, not bugs) |
| DEP | 96 | Imports a library not installed in the test sandbox (fastapi, boto3, sklearn, redis, torch, ...) |
| TIMEOUT | 9 | Exceeded 6 s (benchmarks, thread demos — expected) |
| SKIP | 71 | Intentionally non-runnable (`...` placeholders, `input()`, `while True`, `plt.show()`) |

## Real bug found and fixed

- **05-Systems/05.1-memory.md** — the weakref example declared
  `__slots__ = ("name", "_parent")`, which makes `weakref.ref(parent)` raise
  `TypeError: cannot create weak reference to 'Node' object`. Added `"__weakref__"` to
  the slots tuple and corrected the printed-output comment. Verified it now runs.

(Earlier polish waves on ch 00–03 fixed ~10 more executable bugs: wrong asserts, vacuous
tests, incorrect expected outputs. Those are already committed.)

## FAIL breakdown — mostly not bugs

| Error class | Count | Interpretation |
|---|---|---|
| NameError | 91 | Mostly harness artifacts: a block uses a definition from an earlier block the harness dropped (it excludes slow/failed blocks from the cumulative context). A minority may be genuinely missing definitions — worth an eye during prose passes. |
| IndentationError | 36 | Snippet-style blocks: an indented method body meant to be read inside a class from a previous block. Fine for a book; not runnable standalone. |
| Network errors | ~20 | `requests`/`urllib`/socket calls to real or local services. Expected offline failures. |
| argv/usage errors | ~11 | CLI scripts that need `python script.py <args>`. Expected. |
| SyntaxError | 5 | REPL transcripts (`>>>` prompts) and cheat-sheet pseudo-code with `...`. Presentation style, not bugs. `'return' outside function` (12.3) = Flask handler bodies shown without the route decorator context. |
| IndexError | 6 | Five in 04.4-automation-projects (likely `sys.argv[1]` without args — verify during the ch-04 prose pass); one in 04.2. |
| KeyError | 2 | `os.environ["API_KEY"]` / `"GITHUB_TOKEN"` — expected without env vars. |
| FileNotFoundError | 4 | Examples reading local files that ship with the reader's project, not the repo. |

## Follow-ups for the remaining prose waves

1. ~~04.4 IndexError blocks~~ DONE (2026-07-10): all five (plus 04.2's wordcount) now
   print a clean usage line via a `SystemExit` guard instead of a traceback, and each
   carries a usage comment.
2. ~~NameError-heavy files~~ DONE (2026-07-10): triaged all 102 NameErrors; 24 were
   real. Fixed with minimal imports/stubs (08.3, 12.3, 16.4, 16.5, 04.1) or explicit
   prose framing (07.2 sketches, 20.4 pseudocode, 24.2 now credits its 24.1 classes).
   Also fixed: a forward reference to `heapsort` in 02.6, a `cProfile.run` scoping
   gotcha in 16.4 (switched to `runctx`), two Flask handler bodies in 12.3 wrapped in
   their route context, and an invalid one-line `try/except/finally` in 28.1.
3. ~~REPL fencing~~ PARTIAL (2026-07-10): 01.1's two REPL transcripts re-fenced as
   ` ```pycon `. Remaining REPL/pseudo blocks elsewhere still fence as python.

## Per-file issue counts (FAIL + TIMEOUT + DEP)

25 12-Security/12.3-web-app-security.md · 18 08-Web/08.2-backend-apis.md ·
16 04-Programming-Mastery/04.4-automation-projects.md · 16 08-Web/08.3-auth-and-permissions.md ·
15 04-Programming-Mastery/04.3-scraping-and-apis.md · 14 24-Compilers/24.2-interpreters-and-vms.md ·
10 16-Data/16.3-data-visualization.md · 9 each: 04.2, 05.1, 05.2, 13.1, 16.1, 16.4 ·
8 27-Software-Engineering/27.2 · 7 07-Databases/07.3 · 6 each: 02.6, 16.2 ·
5 20-AI/20.2 · 4 each: 00.2, 01.4, 02.5, 03.2, 04.1, 05.3, 06.2, 09.4, 10.4, 14.2, 24.1 ·
3 each: 06.3, 12.4, 14.1, 27.1, 28.1 · 2 each: 01.1, 07.2, 09.2, 10.1, 12.1, 16.5, 17.1, 20.4 ·
1 each: 00.1, 02.7, 03.6, 06.1, 07.4, 09.3, 19.1, 20.1, 20.3

Files heavy in DEP (fastapi/boto3/etc.) are expected to score high here — that reflects
the sandbox, not the book.
