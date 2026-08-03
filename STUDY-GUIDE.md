# Study Guide: tracks, schedules, and how to actually finish

The book is large on purpose: it is a full computer science education. But you do not have to read all of it in order to get a job, and you do not have to read it at any particular speed. This guide gives you a few focused routes through the material, two sample schedules, the study habits that make it stick, and a short list of outside resources worth your time.

Pair this with three companion files:

- [SUMMARY.md](SUMMARY.md) is the full reading order, easiest to hardest.
- [PROGRESS.md](PROGRESS.md) is a checklist you tick off as you go.
- [CHECKPOINTS.md](CHECKPOINTS.md) tells you when you are actually ready to move to the next stage.

---

## How to choose a route

If your only goal is a first job, do not try to read all 106 chapters before applying. Pick a track below, finish it, build the projects, and start applying while you keep learning. You become hireable well before you finish the whole book. The full path is there for real depth and for the long game, not as a gate you must clear before you are allowed to apply.

Three things are true of every track:

1. **Everyone does the Core.** Setup, programming fundamentals, problem solving, data structures, algorithms, and git. This is non-negotiable. It is what interviews test and what every job uses.
2. **Everyone does the Career stage.** Interviews and a portfolio are how the skill turns into an offer. Start that practice early, not at the end.
3. **The track decides the middle.** What you add between the Core and the Career stage depends on the kind of job you want.

---

## Track A: Fastest path to a first software job

The smallest set that makes you a credible junior software engineer. Aim a few months of consistent work, then start applying while you continue.

**Core (do these first, in order)**

- [0.1 Setup and Tooling](00-Orientation/00.1-setup-and-tooling.md), [0.2 Programming Fundamentals](00-Orientation/00.2-programming-fundamentals.md), [0.3 Problem-Solving](00-Orientation/00.3-problem-solving.md)
- [1.1 Data Representation](01-Foundations/01.1-data-representation.md), [1.2 Boolean Logic](01-Foundations/01.2-boolean-logic.md), [1.3 Discrete Math](01-Foundations/01.3-discrete-math.md), [1.4 Big-O](01-Foundations/01.4-complexity-and-big-o.md)
- All of [Part 2: Data Structures](02-Data-Structures) and [Part 3: Algorithms](03-Algorithms)
- [4.1 Python Deep Dive](04-Programming-Mastery/04.1-python-deep-dive.md), [4.2 Files, Regex, OS](04-Programming-Mastery/04.2-files-regex-os.md)
- [11.1 Git Deep Dive](11-Version-Control/11.1-git-and-github.md), [11.2 Git Tutorial](11-Version-Control/11.2-git-hands-on-tutorial.md)

**Add (enough breadth to pass interviews and build one real app)**

- [5.1 Memory](05-Systems/05.1-memory.md), [5.2 Concurrency](05-Systems/05.2-concurrency.md) (read for understanding, do not over-study)
- [6.1 TCP/IP](06-Networking/06.1-tcp-ip.md), [6.2 HTTP, DNS, TLS](06-Networking/06.2-http-dns-tls.md)
- [7.1 SQL](07-Databases/07.1-relational-and-sql.md), [7.2 Indexing and Transactions](07-Databases/07.2-design-indexing-transactions.md)
- [8.1 Frontend](08-Web/08.1-frontend.md), [8.2 Backend and APIs](08-Web/08.2-backend-apis.md), [8.3 Auth](08-Web/08.3-auth-and-permissions.md)
- [9.1 Scalability](09-System-Design/09.1-scalability-fundamentals.md), [9.2 Caching and CDNs](09-System-Design/09.2-caching-and-cdn.md), [9.3 Load Balancing](09-System-Design/09.3-load-balancing-proxies.md)
- [10.1 Docker](10-Cloud-DevOps/10.1-docker.md), [10.3 CI/CD](10-Cloud-DevOps/10.3-cicd-and-deployment.md)
- [27.1 Clean Code and Design Patterns](27-Software-Engineering/27.1-clean-code-and-design-patterns.md), [27.2 Testing and Architecture](27-Software-Engineering/27.2-testing-and-architecture.md)
- [12.3 Web App Security](12-Security/12.3-web-app-security.md)

**Finish with the whole [Career stage](15-Career)** and build at least Capstone Project 1 (full-stack CRUD + auth, deployed).

Skip for now: calculus and linear algebra, physics, semiconductors, theory of computation, compilers, distributed systems, AI and ML, business, infrastructure. They make you better but are not required to get hired. Come back for them.

---

## Track B: Web / full-stack developer

Track A, but go deeper on the product-building chapters and build two web apps.

Add to Track A: the rest of [Part 7: Databases](07-Databases), all of [Part 9: System Design](09-System-Design), [10.2 Kubernetes](10-Cloud-DevOps/10.2-kubernetes.md) and [10.4 AWS](10-Cloud-DevOps/10.4-aws.md), [13.1 Observability](13-Observability/13.1-observability.md), and [26.1 Distributed Systems Foundations](26-Distributed-Systems/26.1-foundations.md). Build Capstone Projects 1 and 2.

---

## Track C: Data / machine learning

Track A's Core, plus the math and data spine, with data projects instead of a second web app.

Add to the Core: [18.1 Calculus](18-Math/18.1-calculus-for-cs.md), [18.2 Linear Algebra and Eigenvalues](18-Math/18.2-linear-algebra-and-eigenvalues.md), all of [Part 16: Data](16-Data) (statistics, pandas, visualization, performance), [7.1 SQL](07-Databases/07.1-relational-and-sql.md), [14.1 ML Foundations](14-ML-DL/14.1-ml-foundations.md), [14.2 Deep Learning](14-ML-DL/14.2-deep-learning.md), [20.2 ML Engineering and MLOps](20-AI/20.2-ml-engineering-and-mlops.md), and [20.3 Generative AI and LLMs](20-AI/20.3-generative-ai-and-llms.md). Build Capstone Project 3 (pipeline to model to dashboard).

---

## Track D: Semiconductor equipment and process engineering

For readers heading into the fab world (field service, equipment engineering, CMP process engineering) rather than a pure software seat. The CS core still pays for itself daily: fab tools are computers with pumps attached, and the engineers who can script, analyze data, and read the control software are the ones who advance fastest.

Add to Track A's Core: [18.1 Calculus](18-Math/18.1-calculus-for-cs.md), [16.1 Statistics and Probability](16-Data/16.1-statistics-and-probability.md), [19.1 Physics for CS](19-Physics/19.1-physics-for-cs.md), [5.2 Concurrency](05-Systems/05.2-concurrency.md), all of [Part 17: Semiconductors](17-Semiconductors) (17.5 and 17.7 especially), all of [Part 30: Fab Engineering](30-Fab-Engineering), and the C++ track in reading order ([29.1](29-Cpp/29.1-cpp-for-python-programmers.md), [29.5](29-Cpp/29.5-classes-and-object-layout.md), [29.2](29-Cpp/29.2-memory-and-object-lifetime.md), [29.6](29-Cpp/29.6-templates-and-compile-time-cpp.md), [29.3](29-Cpp/29.3-allocators-arenas-cache.md), [29.7](29-Cpp/29.7-concurrency-atomics-memory-model.md), [29.4](29-Cpp/29.4-industrial-embedded-cpp.md)). For the portfolio, polish the virtual-tool DOE from [30.4](30-Fab-Engineering/30.4-cmp-process-engineering.md), the qual-marathon analyzer from [30.5](30-Fab-Engineering/30.5-field-service-and-tool-install.md), and the run-to-run controller from [17.7](17-Semiconductors/17.7-fab-equipment-and-tool-software.md): together they read as "this person already thinks like a process engineer."

---

## The whole thing

If you want the complete education and not just the job, just follow [SUMMARY.md](SUMMARY.md) top to bottom. The tracks above are subsets of that exact order.

---

## Two sample schedules

Pick the pace you can actually sustain. Consistency beats intensity. Three focused hours, four days a week, will carry you further than occasional all-nighters.

### 12-month steady plan (about 2 chapters per week)

| Months | Focus |
|---|---|
| 1 | Stage 0 and Stage 1 (setup, fundamentals, how computers work, the math) |
| 2 to 3 | Stage 2 (data structures, algorithms, Python, git). Start interview practice now. |
| 4 | Stage 3 (systems, architecture, networking, theory) |
| 5 | Stage 4 (data) |
| 6 to 7 | Stage 5 (databases, web, system design, cloud, security, observability, software engineering) |
| 8 | Stage 6 (machine learning and AI) |
| 9 to 10 | Stage 7 (your choice of advanced and specialized tracks) |
| 11 to 12 | Stage 8 polish, build and deploy capstones, apply, interview |

### 6-month job-focused plan (Track A, about 4 chapters per week)

| Weeks | Focus |
|---|---|
| 1 to 2 | Stage 0 and Stage 1 |
| 3 to 7 | Data structures and algorithms (do interview reps the whole time) |
| 8 to 9 | Python, git, a bit of systems and networking |
| 10 to 12 | Databases and web (build Capstone 1 here) |
| 13 to 15 | System design basics, Docker and CI/CD, clean code and testing, web security |
| 16 to 20 | Interview prep in earnest, finish and deploy the capstone, write the resume |
| 21 to 24 | Apply widely, do mock interviews, iterate |

Whatever plan you pick, start applying before you feel ready. The last 20 percent of readiness comes from interviewing.

---

## Study habits that actually work

- **Type the code, do not copy it.** Muscle memory and the small errors you fix are where the learning lives.
- **Do the mini-project.** A chapter is not done until you have built its project. See [PROJECTS.md](PROJECTS.md).
- **Use the checkpoints.** Before leaving a stage, pass its checkpoint in [CHECKPOINTS.md](CHECKPOINTS.md). If you cannot, go back. That is the system working, not failing.
- **Teach it back.** Every chapter ends with a "teach it back" prompt. If you cannot explain it simply, out loud, you do not own it yet.
- **Space your repetition.** Revisit older topics briefly and often rather than cramming once. Interview patterns especially need regular reps, not a single pass.
- **Build in public.** Push your projects to GitHub as you go. A green commit history and a few real repos are worth more than any certificate.
- **One thing at a time.** Finish a stage before starting the next. Breadth without depth is the exact trap this book is built to avoid.

---

## A short, honest list of outside resources

This book is meant to stand on its own, but a few outside resources are genuinely worth your time. Use them to practice and to hear a second voice on hard topics, not as a replacement.

**Practice and interviews**

- A coding-practice site for daily reps (for example LeetCode or its friendlier guided cousins). Work by pattern, the way [15.1](15-Career/15.1-coding-interviews.md) lays out, not at random.
- The "System Design Primer" open-source repository on GitHub, as a companion to [Part 9](09-System-Design).
- Mock interviews with a peer or a free mock-interview platform. Nothing exposes gaps faster.

**Books worth owning (read alongside the matching part)**

- A data-structures-and-algorithms reference for extra problems and proofs.
- "Designing Data-Intensive Applications" for databases and distributed systems ([Part 7](07-Databases), [Part 26](26-Distributed-Systems)).
- "Crafting Interpreters" if you love [Part 24](24-Compilers) and want to go further.
- "Hands-On Machine Learning" as a second pass on [Part 14](14-ML-DL) and [Part 20](20-AI).

**Free video courses for tricky intuition**

- 3Blue1Brown's series on linear algebra, calculus, and neural networks pairs beautifully with [Part 18](18-Math) and [Part 14](14-ML-DL).
- MDN Web Docs (developer.mozilla.org) is the reference for everything in [Part 8](08-Web).

Availability and exact titles change over time, so search for the current version. The point is the topic, not any single link.
