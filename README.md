# The Self-Taught CS Degree

### Everything you'd learn in a computer science bachelor's, from your first line of code to your first job offer.

You start at "what is a program," and you finish with the data structures, systems knowledge, real projects, and interview preparation that actually get people hired. Every concept is built from the ground up, with runnable code and a project in every chapter. No degree, no bootcamp, and no prior experience required.

[![Checks, build, and deploy](https://github.com/Spencer4792/The-Self-Taught-CS-Degree/actions/workflows/deploy-site.yml/badge.svg)](https://github.com/Spencer4792/The-Self-Taught-CS-Degree/actions/workflows/deploy-site.yml)

**📖 Read it as a website: [spencer4792.github.io/The-Self-Taught-CS-Degree](https://spencer4792.github.io/The-Self-Taught-CS-Degree/)** — full-text search, sidebar navigation in curriculum order, rendered diagrams, dark mode. It rebuilds automatically from this repo.

*Created and maintained by Spencer Hales. Free and open under the [MIT License](LICENSE).*

---

## What this is

This is a full computer science education in one place, designed as a single path you can follow from your first line of code to your first job offer. It does not assume a degree, a bootcamp, or any background at all. It begins by explaining what a program even is, and it ends with coding interviews, system design, a portfolio of real projects, and a job-search playbook.

The destination is concrete: **your first entry-level software or data job.** Everything in here is aimed at the two things that get you there, real understanding and proof you can build. Along the way you pick up the same foundations a computer science degree gives you, often explained more plainly.

The approach is simple and it never changes:

- **Build from the ground up.** Every idea is built from nothing. We write the simple version from scratch before reaching for any library, so there are no black boxes. The goal is the kind of understanding that lets you actually implement a thing, not just name it.
- **Learn by doing.** Every chapter has code you run yourself, exercises with worked solutions, and a mini-project you can put on GitHub. Reading is not enough. You build.
- **Go deep, not just wide.** When math shows up, we derive it and make it intuitive instead of asking you to take it on faith.

It is written in a friendly, direct voice, like a knowledgeable instructor walking you through the material at a whiteboard.

> **Where it ends:** the final stage, Landing the Job (Part 15), is dedicated to [coding interviews](15-Career/15.1-coding-interviews.md), [system design interviews](15-Career/15.2-system-design-interviews.md), [behavioral prep, resume and job-search strategy](15-Career/15.3-behavioral-resume-jobsearch.md), and [capstone portfolio projects](15-Career/15.4-capstone-projects.md). Start that practice early and keep it warm the whole way through.

---

## How to navigate this repository

Whether you are teaching yourself from scratch, filling gaps after a degree, or switching into the field, the path is the same. Here is how to move through it:

- **Read on the website or in the repo.** The [website](https://spencer4792.github.io/The-Self-Taught-CS-Degree/) is the same content with search and navigation; the repo is where you clone, run the code, and do the exercises. Most people read on the site and work in a local clone.
- **Follow the order.** [SUMMARY.md](SUMMARY.md) lists every chapter in the exact order to read them, from easiest to hardest. The same progression, with stage descriptions, is in the Learning Path below. The numbered folders are just stable labels for storage, so read by the path, not by folder order.
- **Read with your hands.** Every chapter has runnable code (mostly Python) and exercises with worked solutions. Type the code out and run it. That is the whole point. To run the examples, create a virtual environment and `pip install -r requirements.txt`. The heavy machine-learning libraries live in `requirements-ml.txt`, so install those only when you reach Parts 14, 19, and 20.
- **Dip into the reference.** The [cheat sheets](28-Appendix/28.1-cheat-sheets.md) and [glossary](28-Appendix/28.2-glossary.md) are meant to stay open in a tab.
- **Drill with flashcards.** [study/cs-mastery.apkg](study/cs-mastery.apkg) is an Anki deck built from every chapter's "Teach it back" section plus the glossary: 880 cards in per-part subdecks. Import it into [Anki](https://apps.ankiweb.net/) and review as you finish each chapter. (Regenerate anytime with `python3 tools/build_anki.py`.)
- **Read offline.** `python3 tools/build_ebook.py epub` produces an EPUB for e-readers, and `python3 tools/build_ebook.py tex` plus two `xelatex` passes produces the full ~1,800-page PDF (requires pandoc; PDF also needs TeX). Mermaid diagrams link back to the web edition; everything else, including the ASCII diagrams and all code, is in the book itself.
- **Plan and stay on track.** Use the [Study Guide](STUDY-GUIDE.md) to pick a route (fastest path to a job, web, or data/ML) and a schedule, the [Progress Tracker](PROGRESS.md) to check off chapters, the [Project Index](PROJECTS.md) to build a portfolio as you go, and the [Stage Checkpoints](CHECKPOINTS.md) to confirm you are ready before moving on.

The material is licensed under the [MIT License](LICENSE), so you can use, copy, and adapt it freely. Corrections and improvements are very welcome.

---

## How to use this book

**Read it with your hands, not just your eyes.** Every chapter has code you should type out (not copy-paste, *type it*) and run, plus exercises with worked solutions and a mini-project. Don't skip them. Passive reading is exactly the trap this book is built to help you avoid.

**The rules this book follows:**

1. **No black boxes.** Before reaching for a library, the book builds the simple version from scratch, so you can always explain roughly what a tool does underneath.
2. **Math gets derived, not asserted.** When a complexity bound or a formula shows up, we show *why*.
3. **Every concept gets code.** If you can't write it, you don't really understand it, so every idea comes with runnable code.
4. **Build something.** Each chapter ends with a project you can put on GitHub.
5. **Explain it back.** Each chapter closes with a "teach it back" prompt. If you can't explain it simply, that is the signal to go back.

**Every chapter has the same rhythm:** a beginner "Start here" on-ramp, the theory and math, a "Build it" from-scratch implementation, a mini-project, a "Common mistakes" box, an "On the job / interview angle" callout, and an "Exercises" section with fully worked solutions, closing with "Teach it back."

---

## The Learning Path - follow this order

This is the spine of the book: **everything arranged from easiest to hardest, as a natural progression where each stage unlocks the next**, basically a self-paced CS degree. If you just want a roadmap, follow the stages top to bottom. (A flat by-subject index is at the bottom for reference.) The folder numbers are just storage labels; *this ordering is the real curriculum.*

> **Honest pacing:** the whole path is a multi-year journey if you do the projects (and the projects are the point). That is fine. Depth is the entire goal. A reasonable rhythm is one chapter every couple of days, building the capstone projects (Part 15) as you go.

### Stage 0 - Get set up (Week 0)
*Start here even if you think you know it. Zero prior coding assumed.*
- [0.1 Setup & Tooling, the command line, Python, PyCharm, git](00-Orientation/00.1-setup-and-tooling.md)
- [0.2 Programming Fundamentals (starting from zero)](00-Orientation/00.2-programming-fundamentals.md)
- [0.3 Problem-Solving & Computational Thinking](00-Orientation/00.3-problem-solving.md)

### Stage 1 - Foundations: how computers work + the math (degree year 1)
*The bedrock. The math here (calculus, linear algebra) is what later makes ML and physics click instead of feeling like magic.*
- [1.1 How Computers Represent Everything](01-Foundations/01.1-data-representation.md)
- [1.2 Boolean Logic & Digital Foundations](01-Foundations/01.2-boolean-logic.md)
- [1.3 Discrete Math for Programmers](01-Foundations/01.3-discrete-math.md)
- [18.1 Calculus for Computer Science](18-Math/18.1-calculus-for-cs.md)
- [18.2 Linear Algebra & Eigenvalues](18-Math/18.2-linear-algebra-and-eigenvalues.md)
- [1.4 Algorithmic Complexity & Big-O (rigorous)](01-Foundations/01.4-complexity-and-big-o.md)

### Stage 2 - Core CS: data structures, algorithms & real programming craft (degree year 1 - 2)
*The heart of the degree and of every interview. Build every structure from scratch.*
- [2.1 Arrays & Dynamic Arrays](02-Data-Structures/02.1-arrays.md)
- [2.2 Linked Lists](02-Data-Structures/02.2-linked-lists.md)
- [2.3 Stacks & Queues](02-Data-Structures/02.3-stacks-and-queues.md)
- [2.4 Hash Tables](02-Data-Structures/02.4-hash-tables.md)
- [2.5 Trees & Binary Search Trees](02-Data-Structures/02.5-trees.md)
- [2.6 Heaps & Priority Queues](02-Data-Structures/02.6-heaps.md)
- [2.7 Graphs & Their Representations](02-Data-Structures/02.7-graphs.md)
- [3.1 Recursion & Divide and Conquer](03-Algorithms/03.1-recursion.md)
- [3.2 Sorting Algorithms](03-Algorithms/03.2-sorting.md)
- [3.3 Searching](03-Algorithms/03.3-searching.md)
- [3.4 Graph Algorithms](03-Algorithms/03.4-graph-algorithms.md)
- [3.5 Dynamic Programming](03-Algorithms/03.5-dynamic-programming.md)
- [3.6 Greedy Algorithms & Backtracking](03-Algorithms/03.6-greedy-and-backtracking.md)
- [4.1 Python Deep Dive (the data model)](04-Programming-Mastery/04.1-python-deep-dive.md)
- [4.2 Files, Regex & the Operating System](04-Programming-Mastery/04.2-files-regex-os.md)
- [4.3 Web Scraping & Talking to APIs](04-Programming-Mastery/04.3-scraping-and-apis.md)
- [4.4 Automation Mini-Projects](04-Programming-Mastery/04.4-automation-projects.md)
- [11.1 Git & GitHub Deep Dive (branching, rebasing, cherry-pick)](11-Version-Control/11.1-git-and-github.md)
- [11.2 Git Hands-On Tutorial (do it with me)](11-Version-Control/11.2-git-hands-on-tutorial.md)

### Stage 3 - Under the hood: systems, architecture, networking & theory (degree year 2)
*How the machine and the internet actually work, the layer most self-taught devs skip and regret, plus the formal theory of what computation even is.*
- [5.1 Memory: the Stack, the Heap & Pointers](05-Systems/05.1-memory.md)
- [5.2 Processes, Threads, Concurrency & Parallelism](05-Systems/05.2-concurrency.md)
- [5.3 Operating System Concepts](05-Systems/05.3-operating-systems.md)
- [25.1 Computer Architecture](25-Architecture/25.1-computer-architecture.md)
- [25.2 Assembly Programming](25-Architecture/25.2-assembly-programming.md)
- [6.1 The Internet & the TCP/IP Stack](06-Networking/06.1-tcp-ip.md)
- [6.2 HTTP, DNS & TLS](06-Networking/06.2-http-dns-tls.md)
- [6.3 WebSockets, Polling, RPC & FTP](06-Networking/06.3-websockets-rpc-polling.md)
- [23.1 Automata & Formal Languages](23-Theory-of-Computation/23.1-automata-and-languages.md)
- [23.2 Computability & Complexity (Turing machines, halting, P vs NP)](23-Theory-of-Computation/23.2-computability-and-complexity.md)

### Stage 4 - Working with data (degree year 2 - 3)
*The data skills employers want, now on a rigorous footing. Needs the Stage 1 math.*
- [16.1 Statistics & Probability for Data Science](16-Data/16.1-statistics-and-probability.md)
- [16.2 Data Wrangling with pandas & NumPy](16-Data/16.2-data-wrangling-pandas-numpy.md)
- [16.3 Data Visualization (Matplotlib, Plotly, D3, Recharts, Chart.js)](16-Data/16.3-data-visualization.md)

### Stage 5 - Building & shipping real software (degree year 3)
*Going from writing code to building, deploying, securing, and operating a real product. Learn the engineering craft (27) alongside the stack; clean code and tests make everything else here easier.*
- [27.1 Clean Code, SOLID & Design Patterns](27-Software-Engineering/27.1-clean-code-and-design-patterns.md)
- [27.2 Testing, Software Architecture & Engineering Practices](27-Software-Engineering/27.2-testing-and-architecture.md)
- [7.1 Relational Databases & SQL](07-Databases/07.1-relational-and-sql.md)
- [7.2 Schema Design, Indexing & Transactions](07-Databases/07.2-design-indexing-transactions.md)
- [7.3 NoSQL, DynamoDB & Embedded Databases](07-Databases/07.3-nosql-dynamodb-sqlite.md)
- [7.4 Sharding, Partitioning & Replication](07-Databases/07.4-sharding-partitioning-replication.md)
- [8.1 Frontend Fundamentals](08-Web/08.1-frontend.md)
- [8.2 Backend & API Design (REST, GraphQL, FastAPI)](08-Web/08.2-backend-apis.md)
- [8.3 Authentication & Permissions](08-Web/08.3-auth-and-permissions.md)
- [9.1 Scalability Fundamentals: Latency, Throughput, QPS, Availability](09-System-Design/09.1-scalability-fundamentals.md)
- [9.2 Caching & CDNs](09-System-Design/09.2-caching-and-cdn.md)
- [9.3 Load Balancing & Proxies](09-System-Design/09.3-load-balancing-proxies.md)
- [9.4 Rate Limiting](09-System-Design/09.4-rate-limiting.md)
- [9.5 Message Queues & Async (Kafka, RabbitMQ, SQS)](09-System-Design/09.5-message-queues.md)
- [9.6 Designing Real Systems (putting it together)](09-System-Design/09.6-designing-systems.md)
- [26.1 Distributed Systems Foundations (clocks, ordering, consistency, CAP)](26-Distributed-Systems/26.1-foundations.md)
- [26.2 Consensus & Replication (Raft, Paxos, 2PC)](26-Distributed-Systems/26.2-consensus-and-replication.md)
- [10.1 Docker & Containerization](10-Cloud-DevOps/10.1-docker.md)
- [10.2 Kubernetes](10-Cloud-DevOps/10.2-kubernetes.md)
- [10.3 CI/CD, Staging & Deployments](10-Cloud-DevOps/10.3-cicd-and-deployment.md)
- [10.4 AWS: S3, Lambda, Serverless & Core Services](10-Cloud-DevOps/10.4-aws.md)
- [12.1 Cryptography & Encryption](12-Security/12.1-cryptography.md)
- [12.2 Network Security: Firewalls & TLS in Practice](12-Security/12.2-network-security.md)
- [12.3 Web Application Security & the OWASP Top 10](12-Security/12.3-web-app-security.md)
- [12.4 Hands-On with Burp Suite](12-Security/12.4-burp-suite.md)
- [13.1 Logging, Metrics & Tracing (Grafana, ELK, Splunk, SLI/SLO)](13-Observability/13.1-observability.md)
- [16.4 Performance Optimization & Profiling (+ an HPC primer)](16-Data/16.4-performance-optimization.md)

### Stage 6 - Intelligence: machine learning & AI (degree year 3 - 4)
*The deep end. Pays off everything from Stage 1's math through Stage 5's engineering.*
- [14.1 Machine Learning Foundations (math + scikit-learn)](14-ML-DL/14.1-ml-foundations.md)
- [14.2 Deep Learning with PyTorch & TensorFlow](14-ML-DL/14.2-deep-learning.md)
- [20.1 Artificial Intelligence (the classical foundations)](20-AI/20.1-artificial-intelligence.md)
- [20.2 Machine Learning Engineering & MLOps](20-AI/20.2-ml-engineering-and-mlops.md)
- [20.3 Generative AI & Large Language Models (how they actually work)](20-AI/20.3-generative-ai-and-llms.md)
- [20.4 Agentic AI: Creating & Implementing Agents](20-AI/20.4-agentic-ai.md)

### Stage 7 - Going deep & wide: advanced & specialized tracks (degree year 4 / electives)
*Pick by curiosity and goals. Compilers builds on Stage 3's automata/architecture; semiconductors needs Stage 1 (logic) + Stage 3 (architecture); physics needs the Stage 1 math.*
- [24.1 Lexing, Parsing & Abstract Syntax Trees](24-Compilers/24.1-lexing-parsing-asts.md)
- [24.2 Interpreters, Type Systems & a Bytecode VM](24-Compilers/24.2-interpreters-and-vms.md)
- [19.1 Physics for Computer Scientists: Mechanics & Electromagnetism](19-Physics/19.1-physics-for-cs.md)
- [19.2 Modern Physics & a Quantum Computing Primer](19-Physics/19.2-modern-physics-and-quantum-computing.md)
- [17.1 Semiconductor Physics: From Sand to Switches](17-Semiconductors/17.1-semiconductor-physics.md)
- [17.2 The Transistor & Digital Logic in Silicon](17-Semiconductors/17.2-transistor-and-logic.md)
- [17.3 From Transistors to Chips: Architecture & Memory](17-Semiconductors/17.3-from-transistors-to-chips.md)
- [17.4 Chip Design Flow & Hardware Description Languages](17-Semiconductors/17.4-chip-design-flow-and-hdl.md)
- [17.5 Semiconductor Manufacturing: How Chips Are Made](17-Semiconductors/17.5-semiconductor-manufacturing.md)
- [17.6 The Industry & Landing an Entry-Level Semiconductor Job](17-Semiconductors/17.6-semiconductor-careers.md)
- [16.5 Beyond Python: Go, C++, R & Node.js](16-Data/16.5-beyond-python-languages.md)
- [22.1 Mac Minis, Home Labs & Building Server Farms](22-Infrastructure/22.1-mac-minis-and-server-farms.md)
- [21.1 Building & Structuring a Software Company](21-Business/21.1-software-company.md)

### Stage 8 - Landing the job (run alongside Stages 5 - 7)
*Start the coding-interview practice during Stage 2 and keep it warm; do the rest as you near applying.*
- [15.1 Cracking the Coding Interview (the patterns)](15-Career/15.1-coding-interviews.md)
- [15.2 System Design Interviews (entry-level)](15-Career/15.2-system-design-interviews.md)
- [15.3 Behavioral Interviews, Resume & the Job Search](15-Career/15.3-behavioral-resume-jobsearch.md)
- [15.4 Capstone & Portfolio Projects](15-Career/15.4-capstone-projects.md)

### Appendix - keep these open in a tab the whole way through
*Reference material, not a stage. Dip in whenever you need a fast lookup or a definition.*
- [28.1 Cheat Sheets (git, bash, SQL, regex, Python, Docker, kubectl, Big-O…)](28-Appendix/28.1-cheat-sheets.md)
- [28.2 Glossary (A-Z of every key term, linked to its chapter)](28-Appendix/28.2-glossary.md)

---

## Reference: all parts by subject

<details>
<summary>Click to expand the flat, by-subject index (folder order)</summary>

**Part 0, Orientation & Setup:** [0.1](00-Orientation/00.1-setup-and-tooling.md) · [0.2](00-Orientation/00.2-programming-fundamentals.md) · [0.3](00-Orientation/00.3-problem-solving.md)
**Part 1, CS Foundations:** [1.1](01-Foundations/01.1-data-representation.md) · [1.2](01-Foundations/01.2-boolean-logic.md) · [1.3](01-Foundations/01.3-discrete-math.md) · [1.4](01-Foundations/01.4-complexity-and-big-o.md)
**Part 2, Data Structures:** [2.1](02-Data-Structures/02.1-arrays.md) · [2.2](02-Data-Structures/02.2-linked-lists.md) · [2.3](02-Data-Structures/02.3-stacks-and-queues.md) · [2.4](02-Data-Structures/02.4-hash-tables.md) · [2.5](02-Data-Structures/02.5-trees.md) · [2.6](02-Data-Structures/02.6-heaps.md) · [2.7](02-Data-Structures/02.7-graphs.md)
**Part 3, Algorithms:** [3.1](03-Algorithms/03.1-recursion.md) · [3.2](03-Algorithms/03.2-sorting.md) · [3.3](03-Algorithms/03.3-searching.md) · [3.4](03-Algorithms/03.4-graph-algorithms.md) · [3.5](03-Algorithms/03.5-dynamic-programming.md) · [3.6](03-Algorithms/03.6-greedy-and-backtracking.md)
**Part 4, Programming Mastery & Automation:** [4.1](04-Programming-Mastery/04.1-python-deep-dive.md) · [4.2](04-Programming-Mastery/04.2-files-regex-os.md) · [4.3](04-Programming-Mastery/04.3-scraping-and-apis.md) · [4.4](04-Programming-Mastery/04.4-automation-projects.md)
**Part 5, Computer Systems & OS:** [5.1](05-Systems/05.1-memory.md) · [5.2](05-Systems/05.2-concurrency.md) · [5.3](05-Systems/05.3-operating-systems.md)
**Part 6, Networking:** [6.1](06-Networking/06.1-tcp-ip.md) · [6.2](06-Networking/06.2-http-dns-tls.md) · [6.3](06-Networking/06.3-websockets-rpc-polling.md)
**Part 7, Databases & Storage:** [7.1](07-Databases/07.1-relational-and-sql.md) · [7.2](07-Databases/07.2-design-indexing-transactions.md) · [7.3](07-Databases/07.3-nosql-dynamodb-sqlite.md) · [7.4](07-Databases/07.4-sharding-partitioning-replication.md)
**Part 8, Web Development & APIs:** [8.1](08-Web/08.1-frontend.md) · [8.2](08-Web/08.2-backend-apis.md) · [8.3](08-Web/08.3-auth-and-permissions.md)
**Part 9, System Design & Scalability:** [9.1](09-System-Design/09.1-scalability-fundamentals.md) · [9.2](09-System-Design/09.2-caching-and-cdn.md) · [9.3](09-System-Design/09.3-load-balancing-proxies.md) · [9.4](09-System-Design/09.4-rate-limiting.md) · [9.5](09-System-Design/09.5-message-queues.md) · [9.6](09-System-Design/09.6-designing-systems.md)
**Part 10, Cloud, Containers & DevOps:** [10.1](10-Cloud-DevOps/10.1-docker.md) · [10.2](10-Cloud-DevOps/10.2-kubernetes.md) · [10.3](10-Cloud-DevOps/10.3-cicd-and-deployment.md) · [10.4](10-Cloud-DevOps/10.4-aws.md)
**Part 11, Version Control:** [11.1](11-Version-Control/11.1-git-and-github.md)
**Part 12, Security & Cybersecurity:** [12.1](12-Security/12.1-cryptography.md) · [12.2](12-Security/12.2-network-security.md) · [12.3](12-Security/12.3-web-app-security.md) · [12.4](12-Security/12.4-burp-suite.md)
**Part 13, Observability:** [13.1](13-Observability/13.1-observability.md)
**Part 14, Machine Learning & Deep Learning:** [14.1](14-ML-DL/14.1-ml-foundations.md) · [14.2](14-ML-DL/14.2-deep-learning.md)
**Part 15, Landing the Job:** [15.1](15-Career/15.1-coding-interviews.md) · [15.2](15-Career/15.2-system-design-interviews.md) · [15.3](15-Career/15.3-behavioral-resume-jobsearch.md) · [15.4](15-Career/15.4-capstone-projects.md)
**Part 16, Data, Visualization & Performance:** [16.1](16-Data/16.1-statistics-and-probability.md) · [16.2](16-Data/16.2-data-wrangling-pandas-numpy.md) · [16.3](16-Data/16.3-data-visualization.md) · [16.4](16-Data/16.4-performance-optimization.md) · [16.5](16-Data/16.5-beyond-python-languages.md)
**Part 17, Semiconductors & Hardware:** [17.1](17-Semiconductors/17.1-semiconductor-physics.md) · [17.2](17-Semiconductors/17.2-transistor-and-logic.md) · [17.3](17-Semiconductors/17.3-from-transistors-to-chips.md) · [17.4](17-Semiconductors/17.4-chip-design-flow-and-hdl.md) · [17.5](17-Semiconductors/17.5-semiconductor-manufacturing.md) · [17.6](17-Semiconductors/17.6-semiconductor-careers.md)
**Part 18, Mathematics for CS:** [18.1](18-Math/18.1-calculus-for-cs.md) · [18.2](18-Math/18.2-linear-algebra-and-eigenvalues.md)
**Part 19, Physics:** [19.1](19-Physics/19.1-physics-for-cs.md) · [19.2](19-Physics/19.2-modern-physics-and-quantum-computing.md)
**Part 20, AI, ML Engineering & Agents:** [20.1](20-AI/20.1-artificial-intelligence.md) · [20.2](20-AI/20.2-ml-engineering-and-mlops.md) · [20.3](20-AI/20.3-generative-ai-and-llms.md) · [20.4](20-AI/20.4-agentic-ai.md)
**Part 21, The Business of Software:** [21.1](21-Business/21.1-software-company.md)
**Part 22, Infrastructure & Self-Hosting:** [22.1](22-Infrastructure/22.1-mac-minis-and-server-farms.md)
**Part 23, Theory of Computation:** [23.1](23-Theory-of-Computation/23.1-automata-and-languages.md) · [23.2](23-Theory-of-Computation/23.2-computability-and-complexity.md)
**Part 24, Compilers & Interpreters:** [24.1](24-Compilers/24.1-lexing-parsing-asts.md) · [24.2](24-Compilers/24.2-interpreters-and-vms.md)
**Part 25, Computer Architecture & Assembly:** [25.1](25-Architecture/25.1-computer-architecture.md) · [25.2](25-Architecture/25.2-assembly-programming.md)
**Part 26, Distributed Systems:** [26.1](26-Distributed-Systems/26.1-foundations.md) · [26.2](26-Distributed-Systems/26.2-consensus-and-replication.md)
**Part 27, Software Engineering:** [27.1](27-Software-Engineering/27.1-clean-code-and-design-patterns.md) · [27.2](27-Software-Engineering/27.2-testing-and-architecture.md)
**Part 11 (cont.), Git tutorial:** [11.2](11-Version-Control/11.2-git-hands-on-tutorial.md)
**Appendix:** [28.1 Cheat Sheets](28-Appendix/28.1-cheat-sheets.md) · [28.2 Glossary](28-Appendix/28.2-glossary.md)

</details>

---

## How the stages map to where you want to go

This curriculum is built to take you from **absolute beginner to properly deep**, and to a job, without ever hand-waving:

- **Stages 0-2** build the foundations most self-taught developers feel shaky on, including the calculus and linear algebra (eigenvalues, SVD) that make everything later make sense.
- **Stages 3-5** turn you into someone who can build, ship, scale, secure, and operate real software end to end.
- **Stage 6** is the intelligence layer: classical ML and deep learning on a firm mathematical footing, then production MLOps, then how LLMs actually work and how to build **agentic AI** systems.
- **Stage 7** is where you go deep and wide on whatever you are curious about: **physics** and quantum computing, the full **semiconductor** stack (with a researched guide to breaking into that industry), other programming languages, **building server farms and Mac-mini infrastructure**, and **running a software company**.
- **Stage 8** is the bridge to employment: interviews, portfolio, and the job search, kept warm the whole way through.

Let's build the deep understanding. Start at [Stage 0](00-Orientation/00.1-setup-and-tooling.md).
