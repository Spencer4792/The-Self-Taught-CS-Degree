# Stage Checkpoints: are you ready to move on?

Reading a chapter and understanding a chapter are different things, and the gap is where self-study quietly goes wrong. At the end of each stage, come here. Each checkpoint has two parts:

- **Can you, from memory?** A short list of things a person who finished the stage should be able to do or explain without looking. If any item is fuzzy, go back to that chapter. That is not failure; that is the checkpoint doing its job.
- **Prove it.** One small build-or-explain challenge. If you can do it without copying from the chapter, you own the material.

Be honest with yourself here. The whole point of this book is real understanding, and the only person these checkpoints protect is you.

---

## Checkpoint 0: after Get set up

**Can you, from memory?**

- Open a terminal and navigate the filesystem (`pwd`, `ls`, `cd`), create and delete files and folders.
- Explain what the shell, the Python interpreter, and a virtual environment each are, in one sentence each.
- Write, save, and run a `.py` file that takes input and prints output.
- Use variables, conditionals, loops, functions, and the four core containers (list, tuple, dict, set).
- Read a traceback and find the line that caused the error.

**Prove it.** Without looking anything up, write a small terminal program (for example a number-guessing game or a tip calculator), run it, and fix any errors yourself. Commit it to a fresh git repository.

---

## Checkpoint 1: after Foundations and the math

**Can you, from memory?**

- Convert a number between binary, decimal, and hex, and explain two's complement.
- Build any boolean function from logic gates and explain why a NAND gate is enough on its own.
- State what a derivative and a gradient are, and why gradient descent walks downhill.
- Explain what an eigenvector is in plain words and why it matters.
- Give the Big-O of a loop or a recursive function and explain what Big-O actually measures.

**Prove it.** Take a short piece of code and state its time and space complexity with a one-paragraph justification. Separately, implement gradient descent on a simple function and show it reaching the minimum.

---

## Checkpoint 2: after Core CS

This is the most important checkpoint in the book. It is what technical interviews test.

**Can you, from memory?**

- Implement, from scratch, a dynamic array, a linked list, a stack, a queue, a hash table, a binary search tree, and a heap, and state the time complexity of each operation.
- Write recursion with a correct base case, and explain the call stack.
- Implement and explain binary search, a sort that is O(n log n), BFS, and DFS.
- Recognize when a problem calls for two pointers, a sliding window, a hash map, or dynamic programming.
- Use git confidently: branch, merge, resolve a conflict, and open a pull request.

**Prove it.** Implement a hash table from scratch with tests, then solve three interview-style problems (one easy, one medium, one harder) and state the complexity of each solution out loud as if in an interview.

---

## Checkpoint 3: after Under the hood

**Can you, from memory?**

- Explain the difference between the stack and the heap, and what a pointer is.
- Explain a race condition and one way to prevent it, and what the GIL is.
- Trace what happens, layer by layer, when you type a URL and press enter.
- Describe the fetch-decode-execute cycle and why caches make programs faster.
- Explain what a finite automaton and a Turing machine are, and what the halting problem says.

**Prove it.** Write a small concurrent program (for example fetching several URLs at once) and explain why your approach is correct. Separately, simulate a simple finite automaton in code.

---

## Checkpoint 4: after Working with data

**Can you, from memory?**

- Compute and interpret mean, variance, and a confidence interval, and explain what a p-value is and is not.
- Explain the central limit theorem in plain words.
- Load, clean, filter, group, and join data with pandas, and explain vectorization versus a Python loop.
- Choose an appropriate chart for a given question and say why.

**Prove it.** Take a messy dataset, clean it into a tidy form, answer two real questions about it with a groupby and a join, and produce one honest chart that communicates a finding.

---

## Checkpoint 5: after Building and shipping real software

**Can you, from memory?**

- Design a normalized relational schema, write JOIN and GROUP BY queries, and explain what an index and a transaction do.
- Build a REST API with proper status codes, validation, and authentication.
- Explain caching, load balancing, and rate limiting, and sketch a scalable system at a high level.
- Containerize an app with Docker and describe a CI/CD pipeline.
- Name three code smells, three SOLID principles, and write a test before the code (TDD).

**Prove it.** Build and deploy a small full-stack app with a database, an authenticated API, tests, and a Dockerfile. This is Capstone Project 1 and it belongs on your resume.

---

## Checkpoint 6: after Machine learning and AI

**Can you, from memory?**

- Explain the bias-variance tradeoff and how you detect and fix overfitting.
- Derive or clearly explain gradient descent and backpropagation.
- Choose the right evaluation metric for a problem and say why accuracy can lie.
- Explain how a transformer's attention works at a high level, and what RAG is.
- Describe what turns a notebook model into a production ML system (serving, monitoring, drift).

**Prove it.** Train a model end to end on a real dataset with a proper train/validation/test split, evaluate it honestly, and either serve it behind a small API or build a simple retrieval-augmented question answerer.

---

## Checkpoint 7: after the advanced and specialized tracks

This stage is a buffet, so the checkpoint is simple: for each chapter you chose to do, can you explain its core idea to someone else and point to the small thing you built in it? If yes, it counts. If you only read it, go back and build the project. Reading is not knowing.

A good sign you are done with a chapter here: you could give a five-minute whiteboard talk on it without notes.

---

## Checkpoint 8: ready to apply

This is not about more knowledge. It is about evidence and readiness.

**Can you check every box?**

- You have two or three projects on GitHub, each with a clear README, that you can demo and discuss in depth.
- At least one project is deployed and reachable by a link.
- You can solve a medium interview problem while talking through your reasoning and stating complexity.
- You can walk through a basic system design out loud using a clear framework.
- You have STAR-method answers ready for the common behavioral questions.
- Your resume states impact with numbers, and your LinkedIn and GitHub are presentable.
- You have applied to real jobs and done at least one mock interview.

**Prove it.** Do a full mock interview (coding, plus a short system design or project deep-dive, plus two behavioral questions) with another person, and act on their feedback. Then send applications. You are ready. Keep learning while you interview.
