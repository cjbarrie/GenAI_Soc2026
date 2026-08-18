# Generative AI in Sociology — 2026 Course Plan

This is the evolving single source of truth for the redesign. Detailed weekly content will be added only after the instructor approves a semester architecture.

## Current status

- **Phase 0 — Inspection:** Completed.
- **Phase 1 — Curriculum architecture:** Completed; the sociological-inference sequence was selected.
- **Phase 2 — Literature:** Approved at the level of sequence and reading functions. Final publication metadata and syllabus page ranges remain to be checked before the syllabus freeze.
- **Phase 3 — Assessment and coding progression:** Completed and approved. The design is recorded in `assessment/PHASE3_PROPOSAL.md`, `workbook/PROGRESSION.md`, and `syllabus/AI_USE_POLICY.md`.
- **Phase 4 — Visual system:** Completed. Direction A — Evidence & Society is approved and specified in `design/DESIGN_SYSTEM.md`.
- **Phase 5 — Pilot week:** Completed and approved for scaling through the instructor's decision to proceed to Phase 6.
- **Phase 6 — Scale:** Implemented across all 14 sessions. Workbooks, tasks, solutions, tests, reading guides, instructor notes, and decks are built; final technical and projection QA is in progress.
- **Phase 7 — Integration testing:** Not started.

## Confirmed constraints

- 14 scheduled Wednesday sessions, 9:30 a.m.–12:15 p.m.
- Approximately 5–10 NYU graduate sociology students.
- 60:40 balance between research methods and substantive sociology of AI.
- Middling technical depth; emphasize intelligibility of code and research design.
- Python data types taught through applied LLM examples.
- Approximately one anchor chapter section and two or three required papers per substantive week.
- Separate space may be given to qualitative methods and multimodal measurement.
- OpenRouter is the primary hosted-model gateway; local LLM operation receives extensive coverage.
- Existing Colabs are references, not templates that must be retained.
- Coding examples must proceed in small, inspectable steps with explicit inputs and outputs.
- Readings, lecture arguments, and computational work must be directly aligned.
- The course needs a visible semester-level learning arc.
- The old Blumer-centered interaction material will not be retained without a compelling link to current LLM research.
- The midterm will be take-home.
- November 25 will be a lower-stakes, attendance-flexible project or replication studio.

## Recurring course question

> What inference is the researcher trying to make, and what evidence would validate the use of an LLM for that inference?

## Proposed weekly record schema

Once an architecture is approved, each session will be recorded here with:

1. substantive question;
2. methodological domain;
3. learning objectives;
4. chapter anchor;
5. required and optional readings;
6. lecture argument;
7. worked computational example;
8. beginner coding task and tested solution;
9. validation and replication focus;
10. assessment connection;
11. slide/workbook/build status.

## Approved semester architecture

The course follows a **sociological-inference sequence**. The titles below are working questions, not final syllabus copy; readings and computational examples will be attached during the literature and assessment phases.

| Session | Date | Working question | Principal domain |
|---:|---|---|---|
| 1 | Sep 2 | What kind of research technology is an LLM? | Foundations, Python data, and course map |
| 2 | Sep 9 | What can an LLM output validly measure? | Annotation and measurement |
| 3 | Sep 16 | What does interpretation mean when an LLM assists qualitative research? | Qualitative analysis |
| 4 | Sep 23 | What counts as evidence across text, image, and audio? | Multimodal measurement |
| 5 | Sep 30 | Can generated media isolate a causal construct? | Treatment and stimulus generation |
| 6 | Oct 7 | What changes when the model becomes an interactant? | Conversational and personalized treatments |
| — | Oct 14 | No Wednesday meeting: NYU legislative Monday | — |
| 7 | Oct 21 | Whose attitudes and experiences do synthetic populations represent? | Silicon sampling and representation |
| 8 | Oct 28 | Can LLMs recover missing or unobserved social worlds? | Opinion prediction, validation, and limits |
| 9 | Nov 4 | How can micro-level interactions generate macro-level order? | Generative agent-based models I |
| 10 | Nov 11 | When can agent diversity and debate produce collective intelligence? | Generative agent-based models II; substantive sociology of AI |
| 11 | Nov 18 | Who—or what—produces research data in an agentic workflow? | Research agents, tools, and provenance |
| 12 | Nov 25 | What can we reproduce, and what remains opaque? | Low-stakes replication/project studio; attendance-flexible |
| 13 | Dec 2 | What culture, ideology, and hierarchy are encoded in models? | Auditing LLMs as objects of study |
| 14 | Dec 9 | What standards of evidence should govern LLM-assisted sociology? | Project symposium and course synthesis |

## Architectural notes

- The take-home midterm will sit near the transition from measurement/intervention to representation, with precise timing to be set in Phase 3.
- Replication, validation, and transparency are recurring practices throughout the semester, not topics deferred entirely to Session 12 or 14.
- Junsol Kim's work is a strong candidate for Sessions 8 and 10 and possibly Session 13; placement depends on the systematic literature audit.
- Session 14 can accommodate short presentations or research-design clinics for a cohort of 5–10 while preserving time for synthesis.

## Phase 3 approved design

- Every computational example uses a visible research question → input → transformation → raw output → check sequence.
- The beginner Python foundations unit covers values and types, collections, logic, loops, functions, research data, and transparent research algorithms.
- Each session has one 10–25 minute task with 2–4 checks, a commented solution, and a reading-linked interpretation.
- The approved environment is a supported hybrid: canonical Jupyter notebooks runnable locally, a Colab fallback, the official OpenRouter Python SDK for hosted calls, cached outputs for all required work, and Ollama as the default local runtime.
- Assessment Model A is approved: weekly trace tasks 20%, take-home midterm 20%, individual oral code walkthrough 5%, project milestones 10%, final project package/presentation 35%, and participation/reading preparation 10%.
- The proposed take-home midterm falls across the October 14 legislative-week break and assesses code tracing, limited repair, research-design diagnosis, and reproducibility. Every student then completes a 10–12 minute oral walkthrough explaining a short code extract line by line, predicting its output and one modification, and connecting it to the research design.
- AI use is permitted with responsibility and disclosure. Students remain responsible for every claim and line of code and must demonstrate understanding in the oral walkthrough.
- Weekly coding tasks receive completion marks only, with an opportunity to complete missing elements within one week.
- The final project is a sociological research design and presentation, staged through an inferential-target note, validation clinic, November 25 replication/progress record, December 9 presentation, and final research-design package during the exam period.

## Phase 6 implementation matrix

Every session now has a syllabus record, reading guide, instructor notes, executable workbook, completion task, commented solution, automated test, and Reveal.js deck. Session 2 is the approved 29-slide pilot; the other sessions use the scaled deck template. The canonical file pattern is `sessionXX` within each artifact directory.

| Sessions | Student workbook routine | Reading/code link | Oral-understanding check | Build status |
|---|---|---|---|---|
| 1 | research record from Python values | claims about LLMs as research technologies become record fields and checks | explain each value, type, key, and return value | Built and executed |
| 2 | annotation and measurement pipeline | construct validity motivates labels, comparisons, and disagreement checks | trace the pilot function line by line | Pilot approved; built and executed |
| 3–4 | qualitative themes and multimodal records | interpretive and multimodal claims become evidence-link and normalization rules | name the input structure and explain each transformation | Built and executed |
| 5–6 | generated and conversational treatments | causal claims become treatment and exposure records | distinguish assignment, treatment, response, and output | Built and executed |
| 7–8 | synthetic representation and prediction | representational claims become group summaries and target-specific scores | explain grouping, averaging, and inferential limits | Built and executed |
| 9–10 | agent updates and collective outcomes | emergence claims become explicit update and comparison rules | trace one agent and one interaction round | Built and executed |
| 11–12 | provenance and replication | transparency claims become provenance tables and replication comparisons | explain what each recorded field permits a researcher to audit | Built and executed |
| 13–14 | model audits and evidence standards | substantive claims become factorial comparisons and claim audits | defend what the code establishes and what it cannot establish | Built and executed |

Across the scaled materials, every code example follows the same novice-facing sequence: research target → exact input and Python type → named operation → output → substantive interpretation → check → limitation. Code that would be too dense for projection is split across slides; the complete version remains in the workbook with a worked trace and an oral rehearsal prompt.
