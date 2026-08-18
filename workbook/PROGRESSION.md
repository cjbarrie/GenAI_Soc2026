# Workbook and Coding Progression — Phase 3 Proposal

**Status:** Approved Phase 3 learning progression. This specifies the learning progression; it does not yet build the notebooks.

## Pedagogical contract

Every worked example will display the same five-part trace:

1. **Research question:** what sociological quantity, process, or claim is at issue?
2. **Input:** show the exact Python object and its type before sending or transforming it.
3. **Transformation:** execute one short, named operation at a time.
4. **Output:** print the raw result before parsing, summarizing, or plotting it.
5. **Check:** compare the output with human data, a rule-based baseline, a second run/model, or a predeclared expectation.

Students predict the output before important cells run. Notebooks use short cells, visible intermediate values, plain Python before compact pandas operations, and small assertions that explain failures. Live calls are never required to understand the example: each notebook ships with a small cached response.

## Student-facing semester map

The workbook landing page will show four cumulative strands.

| Course movement | Research capability | Python capability | Validation habit |
|---|---|---|---|
| Sessions 1–4: Observe | Turn social material into inspectable records and measurements | Types, collections, indexing, loops, functions, JSON | Inspect inputs; compare with human labels and source evidence |
| Sessions 5–6: Intervene | Generate fixed and conversational treatments | Combinations, randomization, conditionals, state | Check construct fidelity and treatment exposure |
| Sessions 7–10: Simulate | Represent people, distributions, and interaction processes | Aggregation, nested records, update functions, repeated runs | Validate at multiple levels; probe sensitivity and contamination |
| Sessions 11–14: Delegate and audit | Use tools/agents while preserving evidence; study models as social objects | File I/O, deduplication, provenance, configuration, reusable functions | Reproduce, document dependence, and bound claims |

## Python foundations

The foundations unit is self-contained and available before Session 1. It should take a complete beginner roughly six to eight hours in small blocks; experienced students can use a diagnostic to skip material they already know.

| Unit | Concepts | Applied LLM/research object | Check for understanding |
|---|---|---|---|
| 0. Running code | Notebook cells, expressions, comments, `print`, reading errors | Inspect a cached model response | Change one value and predict which output changes |
| 1. Values and types | Strings, integers, floats, booleans, `None`, variables, `type` | Prompt text, token counts, temperature, success flags, missing data | Identify the type and meaning of each field |
| 2. Collections | Lists, dictionaries, indexing, slicing, nesting | Message lists and structured research records | Retrieve a user message and add a metadata field |
| 3. Decisions | Comparisons, Boolean logic, `if`/`elif`/`else` | Accept, flag, or reject a parsed label | Explain which branch runs for three examples |
| 4. Repetition | `for` loops, accumulation, counting, filtering | Loop through coded excerpts | Build a label-frequency dictionary by hand |
| 5. Functions | Arguments, return values, scope, docstrings | A small output-validation function | Test valid, invalid, and missing output |
| 6. Research data | Text, CSV, JSON, lists of dictionaries, introductory pandas | Load human labels and cached LLM records | Trace one row from disk to summary |
| 7. Algorithms for research | Counting, matching, sorting, deduplication, grouping, maxima/minima, decomposition | Join annotations to source texts; retain provenance | Compare a transparent loop with a compact implementation |

Each unit ends with 2–4 executable checks and a “read this error” box. Foundations deliberately omit classes, decorators, asynchronous programming, package design, and ML mathematics.

## Hosted and local model environments

### Approved supported hybrid

- Canonical materials are ordinary `.ipynb` notebooks, runnable in local JupyterLab or VS Code. A Colab launch path remains available as a fallback, not as a separate version of the course.
- Use one pinned Python environment (provisionally Python 3.11) with `uv`; provide a plain `requirements.txt` export for students who need `pip`.
- Teach the official [`openrouter`](https://openrouter.ai/docs/client-sdks/python/overview) Python SDK directly in the first hosted-model examples. After students understand the request and response objects, a thin course helper may centralize model identifiers, caching, and research metadata.
- Read `OPENROUTER_API_KEY` from the environment or notebook secret store. The shared key is never printed, saved in notebooks, or committed. It should have a spending cap, model/provider allowlists, and privacy guardrails.
- Ship cached raw responses for all required exercises. Live calls are a replaceable step, not a prerequisite for completing the logic or validation task.
- Use Ollama as the default command-line local runtime because it supplies a simple local API. Provide LM Studio as the GUI alternative and llama.cpp as an optional advanced path. The course examples record the runtime, model artifact/tag, quantization when available, parameters, and retrieval date.

### Local-LLM support sequence

The local material is a continuing strand rather than a single installation handout:

1. **Before term:** hardware and disk-space decision tree; Apple Silicon, Windows, Linux, and “hardware not suitable” paths; safe download/removal instructions.
2. **Session 1:** open versus closed weights; model files, runtimes, quantization, and why “local” is a deployment claim rather than a quality claim.
3. **Session 2:** run the same classification record from cached output, OpenRouter, and a local model; compare schemas and latency.
4. **Session 3:** privacy clinic using synthetic interview data; explain why identifiable field data should not be sent to the shared gateway.
5. **Session 7:** full local lab: choose a model that fits available memory, start/stop the server, call it from Python, inspect logs, and diagnose common failures.
6. **Session 8:** compare local and hosted population predictions without treating either as a gold standard.
7. **Session 12:** reproduce an earlier result from an exact local artifact where feasible; contrast this with a routed hosted model.

The guide will cover model selection, memory versus parameter count, context and memory costs, quantization, CPU/GPU tradeoffs, download provenance, licenses, privacy limits, energy/cost tradeoffs, API serving, upgrades, cleanup, and troubleshooting. Students without suitable machines will use cached output and an instructor demonstration; hardware ownership will not affect assessment.

## Weekly beginner tasks

Each task is scoped for roughly 10–25 minutes after the worked example. It introduces no more than two new programming ideas, includes a commented solution, 2–4 tests, and one optional extension.

| Session | Beginner task | Inputs → output | Python reinforcement | Reading-to-code connection | Validation check |
|---:|---|---|---|---|---|
| 1 | Build one research record | Prompt string + settings dictionary + cached response → nested record | Types, lists, dictionaries | Davidson–Karell’s research-use map becomes a documented call | Assert required metadata fields exist; identify what remains unknown |
| 2 | Count classification errors | Human/model label pairs → confusion counts and one metric function | Loops, conditionals, counters, functions | Stuhler et al. and Chae–Davidson’s measurement errors become observable | Inspect false positives/negatives, not accuracy alone |
| 3 | Link themes to evidence | Codebook dictionary + excerpts + proposed labels → evidence table | Dictionaries, filtering, functions | Than et al.’s coding workflow meets Ibrahim–Voyer/Nguyen–Welch’s reflexivity debate | Reject any theme without a supporting source quotation |
| 4 | Normalize multimodal records | Small text/image/audio metadata records → one common list of dictionaries | Nested data, missing values, simple file paths | Law–Roberto and Maranca et al. motivate modality-specific evidence | Flag missing modality-specific fields; do not equate common schema with common validity |
| 5 | Construct a treatment set | Two lists of intended/nuisance attributes → factorial treatment records | Nested loops or `itertools`, booleans | Dafoe’s information equivalence becomes a design constraint | Filter variants that violate a predeclared fidelity rule |
| 6 | Log a conversation | Initial state + three turns → ordered turn records and exposure summary | `if`, loops, state dictionaries, append | Conversational persuasion papers become dynamic treatment records | Distinguish assignment from experienced content |
| 7 | Compare group distributions | Human and synthetic response records → group means and within-group spread | Grouping, accumulation, missing data | Boelaert and Wang et al.’s flattening claim becomes a statistic | Show a case with similar means but different variance |
| 8 | Score several inferential targets | Human/synthetic tables → individual, aggregate, association, and effect summaries | Small metric functions, matching records | Kim–Lee, Xie et al., and Ashokkumar et al. require different validation targets | Prevent one metric from standing in for all targets |
| 9 | Implement one ABM update | Agent states + neighbor list + explicit rule → next state | Functions, loops, dictionaries, copying state | Macy–Willer and Chuang et al. clarify actor/rule/process distinctions | Test synchronous versus accidental in-place updating |
| 10 | Vary interaction structure | Agent opinions + two network structures → repeated group outcomes | Nested loops, reusable functions, seeds | Ashery et al., the critique/reply, and Kim et al. connect interaction structure to emergence claims | Compare multiple runs and perform a simple contamination probe |
| 11 | Preserve provenance | Agent-collected source records → deduplicated claim/source table | File/URL fields, sets, deduplication, sorting | The AI Scientist and transparency editorial motivate traceable delegation | Reject claims without a resolvable source and recorded transformation |
| 12 | Compare replication records | Cached/live/local results + configurations → discrepancy report | JSON serialization, hashing, comparison functions | GUIDE-LLM and Barrie–Palmer–Spirling become an executable audit | Explain whether discrepancy is stochastic, model, provider, or workflow dependence |
| 13 | Run a factorial audit | Model/language/frame/paraphrase conditions → grouped output differences | Product construction, loops, grouping | Waight, Buyl, and Kim et al. connect output differences to bounded causal claims | Separate observed difference from explanation of its cause |
| 14 | Audit a project claim | One project research record → missing-evidence checklist | Reuse functions and nested records | Course synthesis: claim → target → evidence → failure mode | Rewrite one claim to match the evidence actually available |

## Standard 165-minute meeting rhythm

This is a default, varied when discussion or student work warrants it:

- 9:30–9:42 — retrieval prompt and semester-map location
- 9:42–10:15 — reading-led sociological problem and disagreement
- 10:15–10:38 — methodological argument and worked study anatomy
- 10:38–10:48 — break
- 10:48–11:20 — live code walkthrough with prediction before execution
- 11:20–11:45 — paired beginner task
- 11:45–12:05 — validation diagnostic and comparison with the reading
- 12:05–12:15 — exit record: claim, evidence, uncertainty, next skill

No uninterrupted instructor coding segment should normally exceed 12 minutes. The walkthrough pauses after input construction, the model/transformation step, raw output, parsing, and validation.

## Workbook evidence of completion

A completed weekly submission contains only four small artifacts:

1. the student’s prediction before running the focal cell;
2. the task function or loop;
3. passing checks plus one interpreted failure or disagreement;
4. a 100–150 word claim/evidence note tied to a required reading.

This is intentionally harder to fake through blind execution and easier to assess than a long undifferentiated notebook.
