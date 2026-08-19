# Course Redesign Decisions

This file records decisions for the collaborative redesign of **Generative AI in Sociology, Fall 2026**.

## 2026-08-18 — Phase 4 visual audit opened

- **Decision:** Treat the old Quarto/Reveal.js decks as sources of selected arguments and figures, not templates to restyle.
- **Rationale:** The audit found no common design system, highly uneven density, extensive code in lecture decks, inconsistent provenance, and a narrative frequently organized as paper-by-paper summary.
- **Implications:** Retain Quarto/Reveal.js as the likely delivery format, centralize the eventual theme, move extended code into the workbook, store sources outside visible slide copy, and rebuild figures when they materially improve explanation.
- **Proposed visual directions:** Evidence & Society (recommended), The Research Instrument, and Night Seminar.
- **Unresolved:** Instructor choice of visual direction before `design/DESIGN_SYSTEM.md` is created.

## 2026-08-18 — Evidence & Society visual direction approved

- **Decision:** Use Direction A — Evidence & Society for all 2026 lecture decks.
- **Rationale:** Instructor selection. The system gives sociology and computation equal visual status while remaining strong for projection, web viewing, and PDF export.
- **Implications:** Use a warm-paper editorial palette; Source Serif 4 for major questions, Source Sans 3 for teaching text, and IBM Plex Mono for code. Use a 16:9 Quarto/Reveal.js canvas, an asymmetric editorial grid, direct chart labels, claim-led titles, structured source notes, restrained animation, and a recurring claim/evidence/validation grammar.
- **Implementation:** The exact sizes, tokens, layouts, citation rules, accessibility requirements, and QA gate are defined in `design/DESIGN_SYSTEM.md`. Phase 5 will implement them in one pilot week before any other decks are built.
- **Pilot implementation:** Session 2, “Annotation and measurement,” is the representative pilot. It now includes a syllabus entry, reading guide, instructor notes, synthetic data, an executed workbook, a completion task and solution, a 29-slide deck, HTML/PDF exports, and automated checks. Instructor review remains the approval gate before Phase 6.

## 2026-08-18 — Literature sequence approved

- **Decision:** Proceed with the Phase 2 sociological-inference reading sequence and its stated reading functions.
- **Rationale:** Instructor approval after reviewing the literature-audit summary.
- **Implications:** Junsol Kim's work replaces the old Blumer-centered material in sessions on opinion prediction, societies of thought, and—provisionally—model consciousness/values. The old reading list is retained only according to the KEEP/REPLACE/MOVE TO OPTIONAL/DROP audit.
- **Unresolved:** Final page ranges and publication metadata checks before syllabus freeze.

## 2026-08-18 — Phase 3 opened

- **Decision:** Proceed to detailed assessment and coding-progression design.
- **Implications:** Working proposals now specify the beginner Python sequence, weekly coding trajectory, hosted/local environment, three grading models, take-home midterm structure, staged final project, and a task-specific AI-use policy.
- **Unresolved:** Assessment weights; AI permission on the analytical portions of the midterm; midterm verification procedure; final-project format; weekly grading mode; final approval of the supported-hybrid environment.

## 2026-08-18 — Assessment Model A and oral code assessment

- **Decision:** Use Assessment Model A, retaining its overall balance but dividing the midterm component into a 20% take-home submission and a 5% individual oral code walkthrough.
- **Rationale:** The instructor wants every student to demonstrate directly that they understand what each part of basic course code is doing. This addresses the principal weakness of the 2025 exercises without rewarding advanced syntax or memorized APIs.
- **Implications:** Each student completes a 10–12 minute walkthrough after the take-home midterm. With code visible, the student identifies inputs and types, explains every line or small block, predicts output and one modification, and connects the computation to its sociological and validation meaning. The walkthrough is independent work and permits no generative assistance.
- **Approved weights:** Weekly trace tasks 20%; take-home midterm 20%; oral code walkthrough 5%; final-project milestones 10%; final project package and presentation 35%; participation and reading preparation 10%.
- **Unresolved:** AI permission on the design/reproducibility portions of the take-home midterm; final-project form; weekly grading mode; final approval of the supported-hybrid environment.

## 2026-08-18 — Phase 3 assessment and environment decisions completed

- **AI use:** Retain the tone and substance of the 2025 LaTeX policy. Generative AI use is permitted with responsibility and disclosure across coursework; students remain responsible for and must understand every claim and line of code. Material assistance requires a short disclosure. Methodological use requires a fuller research record. The oral code walkthrough is completed without live AI assistance.
- **Final project:** Use a self-designed LLM-related sociological research design and class presentation, similar to 2025. Require a minimal prototype or input/output trace where feasible, but not a completed empirical paper. Within the 35% final component, the design is worth 25 percentage points and the presentation 10.
- **Weekly work:** Award completion marks only. Incomplete elements can be supplied within one week; do not numerically grade code sophistication or polish.
- **Environment:** Approve the supported hybrid: canonical Jupyter notebooks runnable in local Jupyter/VS Code, Colab fallback, official OpenRouter SDK for hosted calls, cached outputs for required work, and Ollama as the default local runtime with LM Studio as the GUI alternative.
- **Implications:** Phase 3 is complete. These decisions govern the pilot week and eventual syllabus/workbook implementation.

## 2026-08-18 — Repository root

- **Decision:** Use `GenAI_Soc2026` as the new course repository root.
- **Rationale:** The directory is intentionally separate from the read-only 2025 repository and already contains the anchor chapter.
- **Implications:** All new materials will be created here. The original `GenAI_Soc` repository will not be modified.
- **Unresolved:** Final location of the chapter PDF within the repository; Git initialization and proposed directory structure await approval.

## 2026-08-18 — Course logistics

- **Decision:** The seminar meets Wednesdays, 9:30 a.m.–12:15 p.m., in Fall 2026.
- **Rationale:** Instructor confirmation.
- **Implications:** The NYU calendar provides 14 Wednesday meetings from September 2 through December 9. October 14 is a legislative Monday and therefore not a Wednesday meeting; November 25 remains a teaching day under the published university calendar.
- **Decision:** Plan for a small seminar of approximately 5–10 NYU graduate sociology students.
- **Implications:** Activities can use whole-class discussion, pairs, and individual code walkthroughs rather than elaborate sectioning. Every student should be able to explain at least one computational decision aloud, and presentation time need not drive the entire final meeting.

## 2026-08-18 — Semester architecture

- **Decision:** Organize the course around the sociological-inference sequence (Architecture B), not a chapter-domain sequence.
- **Rationale:** This gives students a clearer intellectual arc and better realizes the 60:40 methods/substantive balance.
- **Implications:** Sessions will be framed by questions about measurement, interpretation, intervention, representation, emergence, agentic research, model culture, and standards of evidence. Chapter domains remain visible as methodological anchors, but they do not determine the order or titles of the course.

## 2026-08-18 — Midterm format

- **Decision:** Use a take-home midterm.
- **Rationale:** A take-home format better supports careful interpretation of code and research-design reasoning than a timed class exercise.
- **Implications:** The midterm should assess code reading, input/output tracing, methodological diagnosis, and validation design. It should not primarily reward writing code from memory. Exact release date, deadline, weight, and policy on LLM use remain to be designed in Phase 3.

## 2026-08-18 — Thanksgiving-eve session

- **Decision:** Make Wednesday, November 25 a lower-stakes session because many students will be away.
- **Rationale:** Attendance and concentration are likely to be atypical immediately before Thanksgiving.
- **Implications:** Do not place indispensable new substantive content or a high-stakes assessment in this slot. Use an accessible hybrid/asynchronous replication or project studio with a small, recoverable deliverable.

## 2026-08-18 — Intellectual balance

- **Decision:** Target a 60:40 balance between LLMs as research methods and substantive sociology of AI.
- **Rationale:** The course should remain methodologically useful while becoming more substantively sociological.
- **Implications:** Substantive questions should be integrated into method weeks and also receive dedicated space. The course should not become either an API practicum or a generic sociology-of-technology seminar.

## 2026-08-18 — Technical depth

- **Decision:** Use a middling level of technical detail: enough for students to understand what code does, without turning the course into an ML architecture class.
- **Rationale:** Students need conceptual control over workflows and code while remaining focused on sociological inference.
- **Implications:** The introduction will explain tokens, inference, sampling, messages, models, tools, and relevant architecture conceptually. Equations and implementation details will appear only when they clarify code or inference.

## 2026-08-18 — Python foundations

- **Decision:** “Different input types” primarily means Python data types, taught through applied LLM examples.
- **Rationale:** Students need transferable programming fluency rather than a detached inventory of types.
- **Implications:** Strings, numbers, booleans, `None`, lists, dictionaries, and nested structures will be introduced through prompts, messages, model configuration, structured outputs, and research records.

## 2026-08-18 — Reading load

- **Decision:** Retain approximately the existing reading load: chapter section(s) plus roughly two or three required papers per substantive week, with selected optional readings.
- **Rationale:** The overall load is appropriate, but readings need stronger alignment with lectures and code.
- **Implications:** Literature selection will be rebuilt from first principles and each required paper must have an explicit pedagogical function.

## 2026-08-18 — Qualitative and multimodal methods

- **Decision:** Qualitative methods and multimodal measurement may receive separate sessions.
- **Rationale:** Each involves distinct epistemological, validation, and implementation problems.
- **Implications:** Semester architectures should protect space for both rather than treating multimodality as a short extension of text classification.

## 2026-08-18 — Programming environment and model access

- **Decision:** Do not preserve the old Colab notebooks by default. Rebuild computational materials from scratch where useful. Use OpenRouter as the principal hosted-model gateway and teach the OpenRouter SDK. Provide extensive guidance for running local LLMs.
- **Rationale:** The old notebooks did not reliably produce understanding, one gateway reduces account friction, and local models are important for access, privacy, cost, and reproducibility.
- **Implications:** Use the official Python package (`openrouter`) and its lean client interface for hosted calls. Examples should use a thin course configuration layer, central model identifiers, cached outputs, and provider-neutral research records. Hosted and local paths should share the same conceptual interface where practical. A shared course key must never be committed or embedded in notebooks; it should be distributed privately, capped, restricted where practical, and rotated if exposed.
- **Unresolved:** Whether the primary student environment should be browser-hosted notebooks, local Jupyter/VS Code, a managed course environment, or a supported hybrid; policy for distributing and rotating the shared OpenRouter credential.

## 2026-08-18 — Coding pedagogy

- **Decision:** Slow the coding progression substantially. Break code into explicit steps and explain inputs, transformations, and outputs. Make readings and code speak directly to each other.
- **Rationale:** The 2025 exercises did not reliably demonstrate that students completed or understood the code, and the pace was too fast.
- **Implications:** Each worked example will use short cells or blocks, concrete state inspection, prediction-before-execution prompts, small checks/tests, and a visible connection to a claim or validation problem from the readings. Weekly tasks must be narrower than the old multi-part labs.

## 2026-08-18 — Course-level orientation

- **Decision:** Give students a clearer map of what they will encounter and learn across the semester.
- **Rationale:** Students wanted a stronger sense of the course’s broader arc.
- **Implications:** The syllabus, opening session, workbook landing page, and recurring weekly framing will show the progression of methods, substantive questions, coding skills, and assessments.

## 2026-08-18 — Interactionist material

- **Decision:** Do not retain the old Blumer-centered material by default.
- **Rationale:** The instructor does not find it sufficiently compelling unless tied to genuinely new LLM research.
- **Implications:** A substantive session may instead focus on AI as an epistemic/social actor, collective intelligence, internal “societies of thought,” or human–AI influence. Junsol Kim’s recent work is a priority candidate. Final placement awaits literature review and architecture approval.

## 2026-08-18 — Phase 6 scaling standard

- **Decision:** Approval to proceed to Phase 6 constitutes approval of the Session 2 pilot as the scaling baseline.
- **Decision:** Every scaled workbook and deck must teach code through six explicit questions: What is the research target? What exactly is the input? What Python type is it? What operation is performed? What output is returned? What does that output mean for the sociological claim?
- **Rationale:** Students need to be able to narrate the code, not merely run it. A small cohort and the approved oral component make spoken explanation an enforceable course norm.
- **Implementation:** Workbooks include prediction pauses, worked traces, assertions explained in ordinary language, reading-linked limitations, and oral rehearsal prompts. Projected code is split across slides when necessary; complete code remains in the workbook. All required exercises can run from cached or synthetic data without spending model credits.
- **Decision:** The supported hybrid environment is now implemented with canonical local Jupyter notebooks, a Colab fallback, OpenRouter for hosted calls, and Ollama as the default local runtime, with a separate extensive local-LLM guide.

## 2026-08-19 — Phase 7 release standard

- **Decision:** Treat line-by-line comprehensibility as a release requirement, not an optional annotation layer. Every generated workbook now includes a Python-mechanics guide, actual argument values and types immediately before the worked function call, a printed return value, an interpreted check, and an optional extension clearly separated from the completion task.
- **Decision:** Keep `openai/gpt-5.2` as the centrally configured hosted model and Ollama `gemma4` as the documented local example after checking their official listings on August 19, 2026. Model availability must be rechecked before teaching.
- **Decision:** Use the Sociological Science article page for Alvero et al. in student-facing links because the correct DOI currently redirects through a broken journal route; retain the DOI in the bibliography.
- **Decision:** A course release requires all notebooks to execute, all tests and integration scripts to pass, every deck to render and pass geometry/visual review, rendered HTML to pass desktop/mobile checks, bibliography records to match Crossref where available, and all student-facing links to resolve or be explicitly classified as access-restricted.
