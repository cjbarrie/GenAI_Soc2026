# Generative AI in Sociology — 2026 Course Plan

This is the evolving single source of truth for the redesign. Detailed weekly content will be added only after the instructor approves a semester architecture.

## Current status

- **Phase 0 — Inspection:** Completed.
- **Phase 1 — Curriculum architecture:** Completed; the sociological-inference sequence was selected.
- **Phase 2 — Literature:** Approved at the level of sequence and reading functions. Final publication metadata and syllabus page ranges remain to be checked before the syllabus freeze.
- **Phase 3 — Assessment and coding progression:** Completed and approved. The design is recorded in `assessment/PHASE3_PROPOSAL.md`, `workbook/PROGRESSION.md`, and `syllabus/AI_USE_POLICY.md`.
- **Phase 4 — Visual system:** Completed. Direction A — Evidence & Society is approved and specified in `design/DESIGN_SYSTEM.md`.
- **Phase 5 — Pilot week:** Completed and approved for scaling through the instructor's decision to proceed to Phase 6.
- **Phase 6 — Scale:** Completed. Across all 14 sessions, workbooks, tasks, solutions, tests, reading guides, instructor notes, and decks are built and executed.
- **Phase 7 — Integration testing:** Completed August 19, 2026. The release passed notebook execution, tests, structural integration, citation and link checks, secret scanning, slide capture, visual review, and desktop/mobile HTML QA. See `docs/PHASE7_VERIFICATION.md`.

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
- The midterm will be a take-home project proposal that develops directly into the final project.
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
| 3 | Sep 16 | What can an LLM contribute to qualitative interpretation? | Qualitative analysis |
| 4 | Sep 23 | What part of social experience becomes evidence? | Situated, sensory, and multimodal observation |
| 5 | Sep 30 | Can generated media isolate a causal construct? | Treatment and stimulus generation |
| 6 | Oct 7 | What changes when a model starts asking the questions? | AI-assisted and AI-led interviewing |
| — | Oct 14 | No Wednesday meeting: NYU legislative Monday | — |
| 7 | Oct 21 | Whose attitudes and experiences do synthetic populations represent? | Silicon sampling and representation |
| 8 | Oct 28 | Can LLMs recover missing or unobserved social worlds? | Opinion prediction, validation, and limits |
| 9 | Nov 4 | How can micro-level interactions generate macro-level order? | Generative agent-based models I |
| 10 | Nov 11 | When can agent diversity and debate produce collective intelligence? | Generative agent-based models II; substantive sociology of AI |
| 11 | Nov 18 | Who—or what—produces research data in an agentic workflow? | Research agents, tools, and provenance |
| 12 | Nov 25 | What can we reproduce, and what remains opaque? | Low-stakes replication/project studio; attendance-flexible |
| 13 | Dec 2 | What culture, ideology, and hierarchy are encoded in models? | Auditing LLMs as objects of study |
| 14 | Dec 9 | Project presentations | No new reading, lecture content or weekly task |

## Architectural notes

- The midterm project proposal will sit near the transition from measurement/intervention to representation and establish the student's final-project question and design.
- Replication, validation, and transparency are recurring practices throughout the semester, not topics deferred entirely to Session 12 or 14.
- Sessions 3, 6, and 7 now form a deliberate qualitative-data sequence: **interpret a corpus → co-produce a corpus through interaction → simulate a population**. Session 3 includes only a short bridge on AI-moderated data provenance; Session 6 gives AI-assisted and AI-moderated interviewing sustained treatment; Session 7 retains synthetic respondents and representation.
- Junsol Kim's work is a strong candidate for Sessions 8 and 10 and possibly Session 13; placement depends on the systematic literature audit.
- Session 14 is reserved entirely for 10–12 minute student project presentations and questions. It contains no new readings, lecture content, code walkthrough or weekly task.

## Phase 3 approved design

- Every computational example uses a visible research question → input → transformation → raw output → check sequence.
- The beginner Python foundations unit covers values and types, collections, logic, loops, functions, research data, and transparent research algorithms.
- Each session has one 10–25 minute task with 2–4 checks, a commented solution, and a reading-linked interpretation.
- The approved environment is a supported hybrid: canonical Jupyter notebooks runnable locally, a Colab fallback, the official OpenRouter Python SDK for hosted calls, cached outputs for all required work, and Ollama as the default local runtime.
- Assessment Model A is approved: weekly trace tasks 20%, midterm project proposal 20%, individual oral code walkthrough 5%, project milestones 10%, final project package/presentation 35%, and participation/reading preparation 10%.
- The midterm project proposal falls across the October 14 legislative-week break and is the first substantial stage of the final project. It specifies the sociological question, focused literature position, evidence and design, role of the LLM, one worked example, validation, ethics, reproducibility and next steps. Every student then completes a separate 10–12 minute oral walkthrough explaining a short code extract line by line, predicting its output and one modification, and connecting it to the research design.
- AI use is permitted with responsibility and disclosure. Students remain responsible for every claim and line of code and must demonstrate understanding in the oral walkthrough.
- Weekly coding tasks receive completion marks only, with an opportunity to complete missing elements within one week.
- The final project is a sociological research design and presentation, staged through an inferential-target note, validation clinic, November 25 replication/progress record, December 9 presentation, and final research-design package during the exam period.

## Phase 6 implementation matrix

Every session now has a syllabus record, reading guide, instructor notes, executable workbook, completion task, commented solution, automated test, and Reveal.js deck. Session 2 was originally the 29-slide visual-system pilot and was subsequently rebuilt as a 64-slide literature-led session; its collaborative workflow and beginner-facing standards now guide the remaining weekly revisions. The canonical file pattern is `sessionXX` within each artifact directory.

| Sessions | Student workbook routine | Reading/code link | Oral-understanding check | Build status |
|---|---|---|---|---|
| 1 | research record from Python values | claims about LLMs as research technologies become record fields and checks | explain each value, type, key, and return value | Built and executed |
| 2 | annotation and measurement pipeline | construct validity motivates labels, comparisons, and disagreement checks | trace the focal functions and research record line by line | Literature-led rebuild approved; built, executed, rendered, and visually reviewed |
| 3 | qualitative themes | interpretive claims become source-trace, counterexample, alternative, and memo requirements | trace the focal functions and explain why computational completeness is not interpretive validity | Literature-led rebuild approved; built, executed, rendered, and visually reviewed |
| 4 | ordered multimodal situations | Collins's situational theory and video-data methods become ordered moment records, source links, adjacent comparisons, and alignment warnings | narrate previous/current loop state, exact returned changes, research meaning, and limit | Literature-led rebuild approved; aligned artifacts built, executed, rendered, and visually reviewed |
| 5 | generated treatments | causal claims become candidate, rejection-reason, provenance, and pool-comparison records | distinguish stimulus construction, validation, assignment, and outcome | Literature-led rebuild approved; aligned artifacts built, executed, rendered, and under final visual review |
| 6 | realized interview paths | interview claims become protocol, exact-turn, probe-source, probe-link, and topic records | trace `enumerate`, source branches, append, and the returned audit; state why it is not a quality score | Literature-led rebuild approved; aligned artifacts built, executed, tested, rendered, and repaired through instructor visual review |
| 7–8 | synthetic representation and prediction | representational claims become group summaries and target-specific scores | explain grouping, averaging, and inferential limits | Built and executed |
| 9–10 | agent updates and collective outcomes | emergence claims become explicit update and comparison rules | trace one agent and one interaction round | Built and executed |
| 11–12 | provenance and replication | transparency claims become provenance tables and replication comparisons | explain what each recorded field permits a researcher to audit | Built and executed |
| 13–14 | model audits and evidence standards | substantive claims become factorial comparisons and claim audits | defend what the code establishes and what it cannot establish | Built and executed |

Across the scaled materials, every code example follows the same novice-facing sequence: research target → exact input and Python type → named operation → output → substantive interpretation → check → limitation. Code that would be too dense for projection is split across slides; the complete version remains in the workbook with a worked trace and an oral rehearsal prompt.

## Standing slide-review requirement

Every future rebuild and every reopened earlier session must use `docs/SLIDE_REVIEW_CHECKLIST.md`. Sessions 1–5 require a retrospective audit for source fidelity, citation consistency, terminology, narrative transitions, instructor voice, image geometry and beginner-code provenance. Sessions 7–14 must pass the same checks before instructor review.
