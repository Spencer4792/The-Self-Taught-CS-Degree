# Project and Portfolio Index


**160 hands-on projects across the book.**

Employers hire on proof, not claims. This is every build-it project in the book, in reading order, so you can grow a GitHub portfolio as you learn. Put the bigger ones in their own repositories with a clear README (see [15.4 Capstone and Portfolio Projects](15-Career/15.4-capstone-projects.md) for how to present them).

Tip: the six capstone briefs at the very bottom (in 15.4) are the projects most worth polishing for your job search. The chapter mini-projects are how you build the skill to ship them.

## Stage 0: Get set up

### [0.2 Programming Fundamentals (starting from zero)](00-Orientation/00.2-programming-fundamentals.md)
- Mini-project - a tiny function library
- Project 1 - Number-guessing game
- Project 2 - A terminal to-do list
- Project 3 - Temperature converter
- Project 4 - Tip calculator

## Stage 1: Foundations and the math

### [1.1 How Computers Represent Everything](01-Foundations/01.1-data-representation.md)
- Mini-project - a tiny hex viewer (like `xxd`)
- Mini-project #2 - a "number inspector" REPL

### [1.2 Boolean Logic and Digital Foundations](01-Foundations/01.2-boolean-logic.md)
- Mini-project - an 8-bit ALU simulator
- Mini-project #2 - a truth-table → minimal-circuit explorer

### [1.3 Discrete Math for Programmers](01-Foundations/01.3-discrete-math.md)
- Mini-project - a "proof helper" + Monte Carlo estimator
- Mini-project #2 - graph reachability and "is it a tree?" checker

### [18.1 Calculus for Computer Science](18-Math/18.1-calculus-for-cs.md)
- Mini-project - gradient descent from scratch on a multivariable function, and what training a model really is

### [18.2 Linear Algebra and Eigenvalues](18-Math/18.2-linear-algebra-and-eigenvalues.md)
- Mini-project part A - compress an image with truncated SVD
- Mini-project part A2 - the quality/size tradeoff plot
- Mini-project part B - PCA from scratch via eigendecomposition

### [1.4 Algorithmic Complexity and Big-O](01-Foundations/01.4-complexity-and-big-o.md)
- Mini-project - classify 4 mystery functions, then prove it
- Mini-project #2 - racing two algorithms for the same problem (the optimization arc)

## Stage 2: Core CS and programming craft

### [2.1 Arrays and Dynamic Arrays](02-Data-Structures/02.1-arrays.md)
- Mini-project: a typed dynamic array + benchmark vs. `list`
- Extra practice - a 2D matrix stored in a flat 1D array

### [2.2 Linked Lists](02-Data-Structures/02.2-linked-lists.md)
- Mini-project - a doubly linked list that backs an LRU cache
- Extra practice - a music-playlist doubly linked list

### [2.3 Stacks and Queues](02-Data-Structures/02.3-stacks-and-queues.md)
- Mini-project - an expression evaluator (shunting-yard + RPN)
- Extra practice - a browser history (two stacks)

### [2.4 Hash Tables](02-Data-Structures/02.4-hash-tables.md)
- Mini-project: a tiny key-value store + benchmarks
- Extra practice - a tiny inverted index for search

### [2.5 Trees and Binary Search Trees](02-Data-Structures/02.5-trees.md)
- Mini-project - an autocomplete engine built on a trie
- Extra practice - an expression tree (build, evaluate, pretty-print)

### [2.6 Heaps and Priority Queues](02-Data-Structures/02.6-heaps.md)
- Mini-project (a): a Dijkstra-ready priority scheduler
- Mini-project (b): streaming top-k with a size-k min-heap
- Extra practice - a `MedianFinder` stream class (two heaps)

### [2.7 Graphs and Their Representations](02-Data-Structures/02.7-graphs.md)
- Mini-project: model a road network and answer reachability
- Extra practice - a tiny social-network analyzer

### [3.1 Recursion and Divide and Conquer](03-Algorithms/03.1-recursion.md)
- Mini-project: a recursive file tree + a maze solver
- Mini-project: a recursive arithmetic expression evaluator

### [3.2 Sorting Algorithms](03-Algorithms/03.2-sorting.md)
- Mini-project: measured growth vs. theoretical curves

### [3.3 Searching](03-Algorithms/03.3-searching.md)
- Mini-project - four interview classics, one toolbox
- Mini-project - the "binary search on the answer" toolkit (one skeleton, three siblings)

### [3.4 Graph Algorithms](03-Algorithms/03.4-graph-algorithms.md)
- Mini-project: a tiny city route planner
- Mini-project: a social network analyzer

### [3.5 Dynamic Programming](03-Algorithms/03.5-dynamic-programming.md)
- Mini-project: a tiny `diff` tool
- Mini-project: a grid path optimizer

### [3.6 Greedy Algorithms and Backtracking](03-Algorithms/03.6-greedy-and-backtracking.md)
- Mini-project
- Mini-project - Meeting Room Scheduler

### [4.1 Python Deep Dive (the data model)](04-Programming-Mastery/04.1-python-deep-dive.md)
- Mini-project - a retry decorator library (data model, all together)
- Mini-project 2 - a tiny immutable `Money` type (the data model for real)

### [4.2 Files, Regex and the Operating System](04-Programming-Mastery/04.2-files-regex-os.md)
- Mini-project A - the Downloads folder organizer
- Mini-project B - a log-file parser with regex
- Mini-project C - a duplicate-file finder (automate something annoying)

### [4.3 Web Scraping and Talking to APIs](04-Programming-Mastery/04.3-scraping-and-apis.md)
- Mini-project A - GitHub API → cached report
- Mini-project B - a polite static-site scraper
- Mini-project C - a weather CLI on a free, no-key API (great first API project)

### [11.1 Git and GitHub Deep Dive](11-Version-Control/11.1-git-and-github.md)
- Mini-project: Git disaster-recovery lab
- Mini-project 2: simulate a two-person team (conflicts, reviews, hotfixes)

### [11.2 Git Hands-On Tutorial](11-Version-Control/11.2-git-hands-on-tutorial.md)
- Mini-project - "Simulate a team"

## Stage 3: Under the hood (systems, architecture, networking, theory)

### [5.1 Memory: the Stack, the Heap and Pointers](05-Systems/05.1-memory.md)
- Mini-project: visualize a recursive call stack + measure cache-friendly vs cache-unfriendly traversal
- Mini-project: a leak detector and a refcount/cycle observatory
- Mini-project: a memory-aware data-structure showdown

### [5.2 Processes, Threads, Concurrency and Parallelism](05-Systems/05.2-concurrency.md)
- Mini-project: concurrent web-fetcher - sequential vs threads vs async
- Mini-project: a thread-safe producer/consumer pipeline with a bounded queue
- Mini-project: an async web crawler with a bounded semaphore

### [5.3 Operating System Concepts](05-Systems/05.3-operating-systems.md)
- Mini-project: extend the shell
- Mini-project: a process & system monitor (a mini `top`)
- Mini-project: a CPU scheduler simulator (FCFS / SJF / RR / Priority)

### [25.1 Computer Architecture](25-Architecture/25.1-computer-architecture.md)
- Mini-project - sum an array, count cycles, then add a cache model

### [25.2 Assembly Programming](25-Architecture/25.2-assembly-programming.md)
- Mini-project - write `factorial` in assembly, then compare the compiler's version

### [6.1 The Internet and the TCP/IP Stack](06-Networking/06.1-tcp-ip.md)
- Mini-project: multi-client chat server with `selectors`
- Mini-project: a tiny port scanner + a message-framed protocol

### [6.2 HTTP, DNS and TLS](06-Networking/06.2-http-dns-tls.md)
- Mini-project: a from-scratch HTTP/1.1 server on raw sockets
- Mini-project: a caching DNS-over-HTTP resolver + an HTTP request/response inspector

### [6.3 WebSockets, Polling, RPC and FTP](06-Networking/06.3-websockets-rpc-polling.md)
- Mini-project: a live "ticker" dashboard over WebSockets (with long-polling fallback)
- Mini-project: a transport benchmark - short polling vs long polling vs SSE

### [23.1 Automata and Formal Languages](23-Theory-of-Computation/23.1-automata-and-languages.md)
- Mini-project - build a tiny regex engine ("I just built grep")

### [23.2 Computability and Complexity](23-Theory-of-Computation/23.2-computability-and-complexity.md)
- Mini-project - a TM that runs programs + a SAT solver used by reduction

## Stage 4: Working with data

### [16.1 Statistics and Probability for Data Science](16-Data/16.1-statistics-and-probability.md)
- Mini-project 2 - the CLT & confidence-interval coverage lab

### [16.2 Data Wrangling with pandas and NumPy](16-Data/16.2-data-wrangling-pandas-numpy.md)
- Mini-project 1 - messy dataset → clean tidy analysis
- Mini-project 2 - time-series resampling & rolling-feature lab

### [16.3 Data Visualization](16-Data/16.3-data-visualization.md)
- Mini-project: a multi-view analytics dashboard + a D3 enter/update/exit chart

## Stage 5: Building and shipping real software

### [27.2 Testing, Software Architecture and Engineering Practices](27-Software-Engineering/27.2-testing-and-architecture.md)
- Mini-project - ship a real feature, TDD + layers + ADR

### [7.1 Relational Databases and SQL](07-Databases/07.1-relational-and-sql.md)
- Mini-project: An analytics schema and the questions it answers
- Mini-project #2: A bookstore schema from scratch

### [7.2 Schema Design, Indexing and Transactions](07-Databases/07.2-design-indexing-transactions.md)
- Mini-project: normalize a mess and prove the speedup
- Mini-project 2: diagnose and fix three slow queries

### [7.3 NoSQL, DynamoDB and Embedded Databases](07-Databases/07.3-nosql-dynamodb-sqlite.md)
- Mini-project: same app, relational vs. DynamoDB single-table
- Mini-project 2: session store + rate limiter + leaderboard in Redis

### [7.4 Sharding, Partitioning and Replication](07-Databases/07.4-sharding-partitioning-replication.md)
- Mini-project: design the data tier for a high-write app
- Mini-project (second): a tiny sharded key-value store in Python
- Mini-project (second, design variant): the data tier for global multi-tenant Anneava

### [8.1 Frontend Fundamentals](08-Web/08.1-frontend.md)
- Mini-project: a React dashboard card that fetches an API and renders a chart
- Mini-project 2: a debounced search / autocomplete component (React + TypeScript)

### [8.2 Backend and API Design](08-Web/08.2-backend-apis.md)
- Mini-project: a JSON API end to end (FastAPI + Postgres)
- Mini-project 2: a paginated, filterable, versioned `/v1/users` API with idempotency and a structured error envelope

### [8.3 Authentication and Permissions](08-Web/08.3-auth-and-permissions.md)
- Mini-project: add real auth to the FastAPI service (8.2)
- Mini-project 2: refresh-token rotation with reuse detection

### [9.1 Scalability Fundamentals](09-System-Design/09.1-scalability-fundamentals.md)
- Mini-project: full capacity estimate for a realistic service

### [9.2 Caching and CDNs](09-System-Design/09.2-caching-and-cdn.md)
- Mini-project: cache a slow function and measure the win (with stampede protection)

### [9.3 Load Balancing and Proxies](09-System-Design/09.3-load-balancing-proxies.md)
- Mini-project: nginx as reverse proxy + load balancer over 3 app instances

### [9.4 Rate Limiting](09-System-Design/09.4-rate-limiting.md)
- Mini-project: per-user token-bucket limiter on an API, rejecting bursts

### [9.5 Message Queues and Async](09-System-Design/09.5-message-queues.md)
- Mini-project: async job pipeline (web enqueue → worker, with retries + DLQ)

### [9.6 Designing Real Systems](09-System-Design/09.6-designing-systems.md)
- Mini-project: design a rate-limited public API end to end (interview-style write-up)

### [26.1 Distributed Systems Foundations](26-Distributed-Systems/26.1-foundations.md)
- Mini-project: a small distributed key-value store with quorums

### [26.2 Consensus and Replication](26-Distributed-Systems/26.2-consensus-and-replication.md)
- Mini-project: Raft with injected failures across N nodes

### [10.1 Docker and Containerization](10-Cloud-DevOps/10.1-docker.md)
- Mini-project: app + Postgres + Redis with `docker compose`
- Mini-project 2: a multi-service dev environment with hot-reload, override files, and a Makefile

### [10.2 Kubernetes](10-Cloud-DevOps/10.2-kubernetes.md)
- Mini-project: full manifest set for a 2-service app + config/secrets + HPA
- Mini-project 2: zero-downtime rollout you can *prove*, plus a CronJob

### [10.3 CI/CD, Staging and Deployments](10-Cloud-DevOps/10.3-cicd-and-deployment.md)
- Mini-project: full CI/CD for the FastAPI+Docker app with a staging gate and a canary/blue-green plan
- Mini-project 2: a release-and-rollback pipeline you can rehearse

### [10.4 AWS: S3, Lambda, Serverless and Core Services](10-Cloud-DevOps/10.4-aws.md)
- Mini-project: architect NYX Finance's analytics app (ingest → store → serve)
- Mini-project 2: a static site on S3 + CloudFront with HTTPS, plus a contact-form Lambda

### [12.1 Cryptography and Encryption](12-Security/12.1-cryptography.md)
- Mini-project - Encrypted + Authenticated File Vault
- Mini-project #2 - Hybrid "encrypt to a public key" envelope (for sharing)

### [12.2 Network Security](12-Security/12.2-network-security.md)
- Mini-project - "Harden this server" checklist applied to a fresh cloud VM
- Mini-project #2 - Build a 3-tier segmented network locally with Docker
- Mini-project #3 - Defense-in-depth case study: hardening the NYX Finance stack end to end

### [12.3 Web Application Security and the OWASP Top 10](12-Security/12.3-web-app-security.md)
- Mini-project - Before/After security review of an insecure FastAPI app

### [12.4 Hands-On with Burp Suite](12-Security/12.4-burp-suite.md)
- Mini-project - Structured authorized assessment of local Juice Shop
- Mini-project #2 - "Prove my own app is server-side secure" harness (DVWA + a tiny FastAPI of mine)
- Mini-project #3 - A repeatable defensive proxy harness in CI (mitmproxy + my own app)

### [13.1 Logging, Metrics and Tracing](13-Observability/13.1-observability.md)
- Mini-project - Build an observable service
- Mini-project #2 - Local Prometheus + Grafana stack with a load generator and a real burn-rate alert
- Mini-project #3 - Full local stack: app + Prometheus (with rules) + Grafana + Jaeger, traced end to end

### [16.4 Performance Optimization and Profiling](16-Data/16.4-performance-optimization.md)
- Mini-project: take a slow program from baseline to 10 - 100× faster

## Stage 6: Machine learning and AI

### [14.1 Machine Learning Foundations](14-ML-DL/14.1-ml-foundations.md)
- Mini-project: end-to-end classification on a real dataset
- Mini-project 2: build k-means and PCA from scratch, then watch the bias - variance curve

### [14.2 Deep Learning with PyTorch and TensorFlow](14-ML-DL/14.2-deep-learning.md)
- Mini-project: time-series forecaster in PyTorch, end to end
- Mini-project 2: gradient-check your from-scratch backprop, then a CNN on MNIST

### [20.1 Artificial Intelligence (the classical foundations)](20-AI/20.1-artificial-intelligence.md)
- Mini-project - an unbeatable game AI with a clean writeup

### [20.2 Machine Learning Engineering and MLOps](20-AI/20.2-ml-engineering-and-mlops.md)
- Mini-project - a model, end to end

### [20.3 Generative AI and Large Language Models](20-AI/20.3-generative-ai-and-llms.md)
- Mini-project - "Chat with my documents" (end-to-end RAG)

### [20.4 Agentic AI: Creating and Implementing Agents](20-AI/20.4-agentic-ai.md)
- Mini-project - a tool-using research agent (end to end)

## Stage 7: Going deep and wide (advanced and specialized)

### [24.1 Lexing, Parsing and Abstract Syntax Trees](24-Compilers/24.1-lexing-parsing-asts.md)
- Mini-project: statements, blocks, control flow, and a pretty-printer

### [24.2 Interpreters, Type Systems and a Bytecode VM](24-Compilers/24.2-interpreters-and-vms.md)
- Mini-project: a mini-language REPL with two backends

### [19.1 Physics for Computer Scientists](19-Physics/19.1-physics-for-cs.md)
- Mini-project - a 2D physics sandbox with gravity and collisions

### [19.2 Modern Physics and a Quantum Computing Primer](19-Physics/19.2-modern-physics-and-quantum-computing.md)
- Mini-project - measure a Bell state 10,000 times and see the correlations

### [17.1 Semiconductor Physics: From Sand to Switches](17-Semiconductors/17.1-semiconductor-physics.md)
- Mini-project - full diode-circuit explorer

### [17.2 The Transistor and Digital Logic in Silicon](17-Semiconductors/17.2-transistor-and-logic.md)
- Mini-project - design a CMOS gate for a Boolean function and verify it

### [17.3 From Transistors to Chips: Architecture and Memory](17-Semiconductors/17.3-from-transistors-to-chips.md)
- Mini-project - a clock-driven traffic-light FSM

### [17.4 Chip Design Flow and Hardware Description Languages](17-Semiconductors/17.4-chip-design-flow-and-hdl.md)
- Mini-project - design + verify a 4-function ALU

### [17.5 Semiconductor Manufacturing](17-Semiconductors/17.5-semiconductor-manufacturing.md)
- Mini-project - a Python "fab economics" model
- Mini-project 2 - node shrink × die growth × yield, all interacting

### [17.6 The Industry and Landing an Entry-Level Semiconductor Job](17-Semiconductors/17.6-semiconductor-careers.md)
- Mini-project - my personalized 90-day roadmap, portfolio plan & resume rewrite

### [16.5 Beyond Python: Go, C++, R and Node.js](16-Data/16.5-beyond-python-languages.md)
- Mini-project: word-frequency counter in Python, Go, and Node

### [22.1 Mac Minis, Home Labs and Building Server Farms](22-Infrastructure/22.1-mac-minis-and-server-farms.md)
- Build it - mini-project (a): a single hardened headless server
- Build it - mini-project (b): a 3-year cost model in Python
- Build it - mini-project (c): a 3-node cluster
- Mini-project - wire it all together (capstone)

### [21.1 Building and Structuring a Software Company](21-Business/21.1-software-company.md)
- Mini-project A: cap table + dilution model
- Mini-project B: runway calculator + fundraise trigger
- Mini-project C: one-page business model + GTM

## Stage 8: Landing the job

### [15.1 Cracking the Coding Interview (the patterns)](15-Career/15.1-coding-interviews.md)
- Mini-project - Build your Pattern Playbook + cheat sheet

### [15.2 System Design Interviews (entry-level)](15-Career/15.2-system-design-interviews.md)
- Mini-project - Reusable answer template + checklist

### [15.3 Behavioral Interviews, Resume and the Job Search](15-Career/15.3-behavioral-resume-jobsearch.md)
- Mini-project - A job-search operating system

### [15.4 Capstone and Portfolio Projects](15-Career/15.4-capstone-projects.md)
- Six capstone project briefs (increasing ambition)
- Project 1 - Full-stack CRUD + Auth app (the must-have)
- Project 2 - A "Twitter-lite" / social or content app (full-stack, a notch up)
- Project 3 - Data/ML project: pipeline → model → dashboard (plays to my strengths)
- Project 4 - A systems project: mini key-value store (or web server)
- Project 5 - A rate-limited API gateway / backend service (systems + web)
- Project 6 - "Automate something real" (pragmatism that signals seniority)
- Mini-project - Pick one and build the full plan + repo scaffold

