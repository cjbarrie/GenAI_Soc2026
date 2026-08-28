# Workbook and Coding Progression — Phase 3 Proposal

**Status:** Implemented dual-route progression. Weeks 1–13 have aligned runnable notebooks and task files; Weeks 8–13 remain provisional as full literature-led chapters.

## Pedagogical contract

Every worked example will display the same five-part trace:

1. **Research question:** what sociological quantity, process, or claim is at issue?
2. **Input:** show the exact Python object and its type before sending or transforming it.
3. **Transformation:** execute one short, named operation at a time.
4. **Output:** print the raw result before parsing, summarizing, or plotting it.
5. **Check:** compare the output with human data, a rule-based baseline, a second run/model, or a predeclared expectation.

Students predict the output before important cells run. Notebooks use short cells, visible intermediate values and plain Python before compact operations. Weeks 1–2 make both a live OpenRouter call and a live Ollama call. Students choose either route in Weeks 3–7, compare both again in Week 8, and then continue with either route. Recorded outputs remain available only as an outage contingency.

### Zero-Python course-book rule

The student course book contains a separate Python page for every coding week. That page, rather than a separate notebook, contains the complete core exercise. Each new idea is introduced in its own short code block. Immediately before the block, the page names the exact input and its Python type. Immediately after it, the page explains every line and symbol, prints the expected output, and states what the output means for the research question. Exercises begin with runnable code and ask students to change one clearly identified value or line; they do not begin with an incomplete function or unexplained placeholder. The downloadable `.py` task is an exact copy of the Python-page exercise, not an advanced extension. Optional notebook material must be labelled as optional and must not quietly become part of the completion criteria.

The Python progression is organized around the parts of an LLM routine rather than around generic programming exercises. Week 1 first makes two genuine calls, then uses their request and return objects to introduce strings, variables, lists, dictionaries, indexing, SDK attributes, string methods, integers, Booleans, `print`, `type` and `len`. Week 2 reuses these ideas for a codebook and label comparisons. Weeks 3–7 add route selection, JSON, multimodal inputs, call parameters, conversation state and schemas. Week 8 introduces the first loop around a call. Week 9 introduces the first student-defined function. Weeks 10–13 reuse those ideas for simulation, tools, reproducibility and a small audit grid. Compact code is not a learning objective.

### Planned interactive for the final workbook

The final Session 1 workbook should use [AnimatedLLM](https://animatedllm.github.io/) immediately before the first API example. Students should work through its text-generation animation and identify: (1) the current context, (2) the next-token probability distribution, (3) the selected token, and (4) how that token becomes part of the next input. This belongs in the student workbook as a short guided activity, not in the Session 1 lecture slides.

Before the first live calls in Week 1, the course distinguishes the **model**, **service**, **API**, and **SDK** in plain language. Week 1 compares OpenRouter as a hosted routing service with an Ollama-served local model. Students identify which parts of the research request stay the same and which parts change when the access route changes.

The first OpenRouter example in Week 1 is assembled across separate cells rather than presented as one unexplained block: prompt string; message list; client call; response object; first choice; returned message; returned text. Each cell states its input, operation, output and research meaning. The extraction path (`response.choices[0].message.content`) is unpacked one step at a time. The Ollama call uses the identical prompt while making the different call and response path explicit.

## Student-facing semester map

The workbook landing page will show four cumulative strands.

| Course movement | Research capability | Python capability | Validation habit |
|---|---|---|---|
| Sessions 1–4: Evidence, measurement and interpretation | Turn social material into inspectable records and measurements | Prompt strings, message lists, calls, returned text, JSON and multimodal records | Inspect inputs; compare model returns with human labels and source evidence |
| Sessions 5–6: Experiments and research encounters | Generate fixed and conversational treatments | Call parameters, structured records, conversation lists and `.append()` | Check construct fidelity and what respondents actually encounter |
| Sessions 7–10: Synthetic populations and social simulation | Represent people, distributions and interaction processes | Structured outputs, loops and small functions with explicit parameters | Validate at multiple levels; probe sensitivity and contamination |
| Sessions 11–13: Research agents, replication and model audits | Use tools while preserving evidence; study models as social objects | Tool records, function returns, saved settings and repeated parameter grids | Reproduce, document dependence and bound claims |

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
- Teach the official [`openrouter`](https://openrouter.ai/docs/client-sdks/python/overview) and [`ollama`](https://github.com/ollama/ollama-python) Python clients directly in Week 1. Do not hide the prompt, message list, call or response extraction inside a helper until functions are introduced in Week 9.
- Read `OPENROUTER_API_KEY` from the environment or notebook secret store. The shared key is never printed, saved in notebooks, or committed. It should have a spending cap, model/provider allowlists, and privacy guardrails.
- Ship recorded raw responses as a contingency. Live OpenRouter and Ollama calls are the normal path in Weeks 1–2; a student may use a recorded return when access fails and must explain that substitution in the recording.
- Use Ollama as the default command-line local runtime because it supplies a simple local API. Provide LM Studio as the GUI alternative and llama.cpp as an optional advanced path. The course examples record the runtime, model artifact/tag, quantization when available, parameters, and retrieval date.

### Local-LLM support sequence

The local material is a continuing strand rather than a single installation handout:

1. **Before term:** hardware and disk-space decision tree; Apple Silicon, Windows, Linux, and “hardware not suitable” paths; safe download/removal instructions.
2. **Session 1:** make one hosted and one local call; introduce open versus closed weights, model files, runtimes and why “local” is a deployment claim rather than a quality claim.
3. **Session 2:** use both routes as annotators and distinguish route disagreement, prompt instability and disagreement with a human reference.
4. **Session 3:** privacy clinic using synthetic interview data; explain why identifiable field data should not be sent to the shared gateway.
5. **Sessions 3–7:** use the chosen route each week for JSON, constrained generation, conversation state and structured probability outputs. Students may repeat the same task with the other route for comparison.
6. **Session 8:** compare local and hosted population predictions without treating either as a gold standard.
7. **Session 12:** reproduce an earlier result from an exact local artifact where feasible; contrast this with a routed hosted model.

The guide will cover model selection, memory versus parameter count, context and memory costs, quantization, CPU/GPU tradeoffs, download provenance, licenses, privacy limits, energy/cost tradeoffs, API serving, upgrades, cleanup, and troubleshooting. Students without suitable machines will use cached output and an instructor demonstration; hardware ownership will not affect assessment.

## Weekly beginner tasks

Each task uses one small LLM routine and adds one or two Python ideas. Students receive complete setup code and make one named change. Completion depends on the narrated explanation of inputs, operations, outputs and methodological meaning—not on abstraction, efficiency or video editing.

| Session | Beginner task | Inputs → output | Python reinforcement | Reading-to-code connection | Validation check |
|---:|---|---|---|---|---|
| 1 | Make the first two model calls, then inspect their objects | Trust statement + scale → identical message → hosted and local raw returns | Strings, lists, dictionaries, indexing, SDK attributes, methods, integers, Booleans, `print`, `type`, `len` | Separates a proposed score from a valid measure of trust | Explain every value, both routes and the missing validation evidence |
| 2 | Use two LLMs as annotators | Housing comment + codebook → two labels → human comparison | Lists, dictionaries, indexing, equality comparisons | Turns annotation into a visible dual-route routine | Distinguish model disagreement, prompt instability and human disagreement |
| 3 | Request a structured theme suggestion | Two excerpts → JSON request → model return → parsed `theme`, `evidence_id`, `question` | `json.loads`, keys, lists of dictionaries | Connects model suggestions back to source excerpts | Verify that the cited excerpt exists and supports the interpretation |
| 4 | Constrain a model to observable description | Ordered observation strings → constrained request → observation/inference fields | Nested message content and structured fields | Makes the distinction between seeing and interpreting operational | Identify recognition or theory that entered despite the constraint |
| 5 | Generate and compare treatment candidates | Frame string + shared facts + generation settings → candidate text | Keyword arguments such as `model`, `temperature`, `max_tokens` | Shows how an LLM widens a treatment pool without validating it | Change only the frame parameter; inspect semantic confounds |
| 6 | Generate one adaptive probe | Interview history list → appended participant answer → model-generated next question | Conversation lists, `.append()`, ordered state | Makes the model's role in the interview encounter visible | Check whether the probe follows the answer without introducing a cause |
| 7 | Request a probability distribution | Exact survey item + population instruction → JSON-schema response → seven probabilities | Structured outputs, `json.loads`, list retrieval, `sum` | Makes aggregate synthetic prediction machine-readable | Check range and total; compare with human data separately |
| 8 | Repeat a structured prediction across cases | Short profile list → repeated model calls → matched human/model records | First visible `for` loop around an LLM call | Distinguishes individual, aggregate and subgroup validation targets | Calculate only the target named in the claim |
| 9 | Put an LLM call inside one update function | Agent state + neighbour message + threshold → next state | First student-edited function; explicit parameters and `return` | Separates actor attributes, interaction input and update rule | Change one parameter and explain the resulting state change |
| 10 | Repeat an interaction under two conditions | Agent list + network/interaction parameter → repeated outcomes | Function calls, loops and result lists | Links micro interaction rules to claims about emergence | Compare runs and retain the conditions that produced each result |
| 11 | Inspect one research-agent tool record | Research question → tool request → returned source/claim record | Function arguments, returned dictionaries and provenance fields | Makes long-horizon delegation auditable one step at a time | Reject a claim without a resolvable source and recorded transformation |
| 12 | Re-run one saved routine | Saved prompt, model and parameters → second return → discrepancy record | Named parameters, reusable function call and record comparison | Turns replication dependence into visible code and metadata | Separate prompt, model, provider and stochastic differences |
| 13 | Run a small parameter audit | Models × prompt frames → structured returns and condition records | Nested loops introduced only here; parameter grid | Connects patterned outputs to bounded audit claims | Describe an observed difference without assigning its social cause |
| 14 | Project presentations | No coding task | — | Students present and receive feedback on the final research design | — |

## Standard 165-minute meeting rhythm

This is the default, varied slightly when discussion warrants it:

- 9:30–10:00 — instructor framing, sociological background and the question linking the readings;
- 10:00–10:50 — class discussion of the readings;
- 10:50–11:00 — break;
- 11:00–12:05 — guided walkthrough of the coding exercise;
- 12:05–12:15 — questions, recording/submission reminder and preparation.

The coding walkthrough pauses after input construction, message construction, the model call, the raw return, parsing and validation. Students explain the input and output of each operation before the instructor moves on.

## Workbook evidence of completion

A completed weekly submission is one short screen recording with audio. It shows:

1. the input and Python type entering each operation;
2. the prompt/messages and the model access route;
3. the call and the returned object or cached contingency;
4. any extraction, parsing or check and its output;
5. the named change and the resulting difference;
6. a spoken connection to one reading and one explicit limit.

Recordings are uploaded to a dedicated NYU Box folder. The instructor will insert the folder link before term. Production quality is irrelevant; audible understanding is the criterion.
