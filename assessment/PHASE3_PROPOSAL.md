# Assessment Design — Phase 3 Proposal

**Status:** Approved Phase 3 assessment design.

## Audit of the 2025 scheme

The 2025 course assigned 30% to weekly labs/exercises, 30% to participation, and 40% to a self-designed final project and presentation. It had three strengths: regular hands-on work, a substantial independent application, and a norm of explaining code aloud. It also left three important gaps:

- no mid-course check of individual code comprehension or research-design reasoning;
- a very large and weakly specified participation component;
- weekly notebooks could be completed by running cells without producing compact evidence that the student understood inputs, outputs, or errors.

The redesign should retain frequent practice and an independent project while creating more diagnostic, staged evidence.

## Common assessment architecture

All three models below use the same components.

### Weekly trace tasks

Ten best submissions from Sessions 1–13; Session 12 is automatically low-stakes and can replace a missed task. Weekly work receives completion marks only. A task is complete when it contains the prediction, working code, interpreted check, and reading-linked claim. Work that does not yet contain all four elements can be completed and resubmitted within one week; it is not assigned a numerical quality score.

### Midterm project proposal

**Proposed timing:** release after Session 6 on October 7 and submit before Session 7 on October 21. The legislative-week break gives students time without displacing a teaching session.

**Proposed length:** 1,200–1,500 words, plus references and a short appendix if needed.

**Proposed structure**

1. **Research question and motivation:** state the sociological question and the claim the proposed study would seek to support.
2. **Focused literature position:** identify the relevant debate or gap without requiring an exhaustive review.
3. **Evidence and design:** specify data, sampling or case selection, unit of analysis, inferential target, and proposed comparison.
4. **Role of the LLM:** explain the model's specific task and distinguish it from researcher judgment.
5. **Worked example:** show one input → operation → expected output → researcher check using cached, synthetic or illustrative material.
6. **Validation, failure and ethics:** identify likely failures, appropriate checks, and issues of privacy, consent, representation, access or ownership.
7. **Reproducibility and development:** state what will be saved and what must happen next before the final submission.

The proposal is the first substantial stage of the final project. It does not ask students to complete a full LLM-assisted study, conduct an exhaustive literature review, reproduce transformer architecture, or write an API workflow from memory.

### Individual oral code walkthrough

Each student completes a 10–12 minute individual walkthrough shortly after submitting the proposal. The student is shown a short, non-technical code extract drawn from a common weekly task or, where suitable, the proposal's worked example and must explain it completely in plain language.

The walkthrough asks the student to:

1. identify the input objects and their Python types;
2. explain each line or small block, including how important variables change;
3. state the resulting output before the code is run;
4. predict what would change after one small modification;
5. connect the computation to the sociological quantity or validation problem it represents.

This is an understanding assessment, not a syntax quiz. Students are not expected to recall package APIs, write code on a blank screen, or use technical vocabulary when an accurate plain-language explanation is available. The code remains visible throughout. Generative assistance is not used during the walkthrough. A live remote or equivalent accessible format will be available where needed.

**Five-point rubric:** inputs and types (1); complete line-by-line trace (2); output/change prediction (1); research meaning and validation (1).

### Staged final project: research design and presentation

The final is a self-designed, LLM-related sociological research project, similar in spirit to the 2025 assignment. Its two principal assessed products are a research design and a class presentation. Students should demonstrate a minimal input/output or proof of concept where feasible, but they are not required to complete a full empirical paper or obtain definitive findings.

**Milestones**

- **October 28:** short response-to-feedback note explaining how the midterm proposal will be revised.
- **November 11:** five-minute design clinic plus validation plan and one minimal input/output trace.
- **November 25:** optional synchronous/asynchronous replication and project studio; submit a recoverable discrepancy/progress record.
- **December 9:** 10–12 minute project presentation plus questions and structured peer feedback.
- **During the December 16–22 exam period:** final research-design package: research question and sociological motivation; inferential target; data and sampling plan; proposed LLM workflow; minimal input/output trace or prototype where feasible; validation strategy; failure modes and ethics; reproducibility record; a brief AI-use disclosure; and an account of how the design changed after proposal feedback.

The 35% final-project component is assessed as research design (25 percentage points) and presentation (10 percentage points). Criteria are: sociological importance; match between claim and design; transparent proposed implementation; validation; substantive interpretation; reproducibility; and communication. Code sophistication is not an independent virtue.

### Participation and reading preparation

Participation should be evidenced through small, varied contributions: a reading question, peer explanation of a code block, validation critique, or project feedback. Speaking frequency alone should not determine the mark. Students may submit a short written contribution when access or absence makes oral participation difficult.

## Three coherent grading models

### Model A — Balanced evidence (approved)

| Component | Weight |
|---|---:|
| Weekly trace tasks | 20% |
| Midterm project proposal | 20% |
| Individual oral code walkthrough | 5% |
| Final project milestones | 10% |
| Final project package and presentation | 35% |
| Participation and reading preparation | 10% |

**Rationale:** produces direct individual evidence of code comprehension, reduces the old participation weight, and preserves a substantial final project. The oral component tests explanation and tracing rather than technical sophistication.

### Model B — Practice and revision

| Component | Weight |
|---|---:|
| Weekly trace tasks | 30% |
| Midterm project proposal | 20% |
| Final project milestones | 10% |
| Final project package and presentation | 30% |
| Participation and reading preparation | 10% |

**Tradeoff:** best for novice coders because repeated practice and revision carry more weight; the final project has less room to distinguish ambitious independent work.

### Model C — Research apprenticeship

| Component | Weight |
|---|---:|
| Weekly trace tasks | 15% |
| Midterm project proposal | 20% |
| Final project milestones | 15% |
| Final project package and presentation | 40% |
| Participation and reading preparation | 10% |

**Tradeoff:** makes proposal, validation, and replication stages central and resembles a graduate research workshop; it places more grade pressure on one research trajectory.

## AI-use policy: permitted with responsibility and disclosure

The course retains the voice and principle of the 2025 policy: AI can augment learning and research, but it can also substitute for the difficult work through which understanding develops. Use is permitted across weekly tasks, the midterm project proposal, and the final project. Students remain responsible for every submitted claim and line of code and must be able to explain their work fully.

Material AI assistance requires a brief disclosure naming the tool or model, what it was used for, what was incorporated, and how the student checked it. When an LLM is part of the research method, the full research record additionally preserves prompts, outputs, settings, dates, provider or local runtime, transformations, and validation decisions. The individual oral code walkthrough is completed without live AI assistance and directly verifies understanding.

The approved student-facing wording is maintained in `syllabus/AI_USE_POLICY.md`.

## Environment implications for assessment

- Grade logic and interpretation, not access to a powerful laptop or expensive model.
- All assessed tasks must work from cached output.
- Hosted calls use the shared, capped OpenRouter key distributed outside the repository; local execution is an option or explicit comparison, never an equipment requirement.
- A student may use local Jupyter/VS Code or the Colab fallback, but the submitted artifact and checks are identical.
- Project data containing identifiable or sensitive material require a separate data-handling plan and cannot be sent through the shared course key.

## Implementation decisions

- Model A is approved, including the individual oral code walkthrough.
- AI use is permitted with responsibility and disclosure; students must understand and be able to explain submitted work.
- The final project consists principally of a sociological research design and presentation, with a minimal prototype where feasible.
- Weekly tasks receive completion marks only.
- The supported-hybrid environment is approved.
