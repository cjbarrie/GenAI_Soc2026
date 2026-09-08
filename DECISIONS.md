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
- **Initial pilot implementation:** Session 2, “Annotation and measurement,” was first built as a 29-slide representative pilot. That version established the visual system but was superseded by the literature-led Session 2 rebuild recorded below.

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

## 2026-08-27 — Midterm becomes the final-project proposal

- **Decision:** Replace the Python-oriented take-home midterm with a short project proposal worth the same 20%.
- **Rationale:** A proposal gives students a useful intermediate product and lets feedback improve the final research design. Requiring a complete LLM-assisted study at midterm would be disproportionate to the course's breadth and timetable.
- **Implications:** The proposal states the sociological question, focused literature position, evidence and design, proposed role of the LLM, one worked input/output/validation example, likely failures, ethical issues, reproducibility plan and next steps. It is not a completed study or exhaustive literature review. The 5% oral walkthrough remains a separate check that students understand the basic code they use. Later milestones now document revision after proposal feedback.

## 2026-08-27 — Core Python exercises move into the course book

- **Decision:** Assume zero prior Python knowledge. Put every required coding exercise in full on a dedicated weekly Python page rather than requiring students to infer the task from a notebook or `.py` file.
- **Rationale:** Earlier examples combined too many operations and introduced functions, comprehensions, generators or nested records before students understood basic values and control flow.
- **Implications:** The readings-and-slides page remains focused on the week's literature and lecture. Its adjacent Python page names each block's input and type, explains every line and symbol, prints the expected output, and states its research meaning and limit. The assessed block begins as runnable code and asks for one bounded modification. Downloadable materials repeat or extend the page without replacing its explanation.

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
- **Decision:** Keep `openai/gpt-5.2` as the centrally configured hosted model and use the smaller multimodal Ollama tag `gemma4:e2b-it-qat` as the provisional local model. Both identifiers must be rechecked two weeks before teaching.
- **Decision:** Use the Sociological Science article page for Alvero et al. in student-facing links because the correct DOI currently redirects through a broken journal route; retain the DOI in the bibliography.
- **Decision:** A course release requires all notebooks to execute, all tests and integration scripts to pass, every deck to render and pass geometry/visual review, rendered HTML to pass desktop/mobile checks, bibliography records to match Crossref where available, and all student-facing links to resolve or be explicitly classified as access-restricted.

## 2026-08-19 — Session 1 lessons for all subsequent weeks

- **Voice:** Write slide titles and body copy in the instructor's direct, explanatory voice. Titles should say plainly what the slide is doing or what students need to understand. Avoid polished slogans, compressed abstractions, and copywriting formulations such as “the course begins where the output ends” or “four verbs locate what.” Read every deck aloud during review; if a line would sound unnatural in class, rewrite it.
- **Paper introductions:** Make it immediately obvious when a slide is discussing a paper. Show a legible, consistently framed image of the paper or publisher page where this helps students recognize the source, then state the paper's question, evidence, and relevance in ordinary language. Paper images must be visibly rendered, intentionally cropped, and checked at 1280 × 720; never allow a figure, typology, title, or citation to be cut off.
- **Readings and code:** Do not place readings and computation in separate tracks. Each focal paper should motivate a research decision, failure mode, or validation check that reappears in the worked code. Each worked example should return to the corresponding substantive claim.
- **Beginner model-access sequence:** Before showing OpenRouter syntax, distinguish the model, model service, API, and SDK. Compare a direct provider API, a routing service such as OpenRouter, and a locally served model through Ollama. Explain that one routing SDK is useful because much of the request structure can remain stable across hosted models, while Ollama offers a local route with different implications for privacy, cost, hardware, and reproducibility.
- **Beginner code sequence:** Introduce one object or operation at a time. For each block, name the exact input, its Python type, the operation, the raw output and its type, and what the result means for the research task. Explain strings, integers, floats, Booleans, `None`, dictionaries, lists, imports, environment variables, client construction, method calls, named arguments, and nested response access before presenting a complete call. Never assume that students already understand indexing, dot notation, assignment, quotation marks, or the difference between the string `"0"` and the integer `0`.
- **Examples:** Use small applied sociological tasks rather than decontextualized questions or requests for definitions. The Session 1 anchor example asks a model to score a survey-style statement for social trust on a 0–2 scale. It then uses the apparently simple output to introduce coding, construct definition, scale rules, parsing, validation against human-coded cases, and the limits of the resulting claim.
- **Pacing:** Split complete programs across multiple slides and rebuild them only after students have seen each component. Keep projected code short and readable, insert prediction pauses, and give students time to explain code aloud. The desired test is whether a beginner can describe what every line receives, does, and returns—not whether the cell runs successfully.
- **Interactive placement:** Keep AnimatedLLM as a guided activity in the final Session 1 workbook, immediately before the first API example. Do not include it in the lecture deck unless a later revision gives it a clear argumentative role. Do not use Transformer Explorer.
- **Visual QA:** Rendering is part of authorship. For each deck, inspect all slides containing paper images, figures, screenshots, tables, code, and citations in the rendered HTML—not only in source. Compare related paper screenshots for consistent framing and scale, and capture targeted screenshots again after any crop, font-size, or content change.
- **Scaling rule:** Session 1 is now the reference for tone, beginner explanation, code pacing, paper presentation, and rendered-slide QA. Reuse its teaching logic in later weeks, but do not mechanically reuse its layouts or examples.

## 2026-08-19 — Session 2 literature-led rebuild

- **Core question:** Organize the session around when an LLM-produced label can be used as a sociological measure, using one synthetic study of public comments on a rezoning proposal throughout.
- **Evidence sequence:** Move from construct definition to prompt stability, reference-label provenance, patterned errors, and downstream consequences. Barrie, Palaiologou, and Törnberg's Prompt Stability Scoring paper is the central reliability reading; Stuhler, Dang Ton, and Ollion motivates the promptbook; Egami et al. supplies a bounded downstream-inference extension.
- **Asides:** Use Schroeder, Roy, and Kabbara briefly to show that model-assisted human labels are not necessarily independent reference data. Pair it with Agarwal, Naaman, and Vashistha to show that the source text itself may already be a human–model product. Record both `reference_source` and `text_production_mode` in the research record.
- **Coding progression:** Preserve the Session 1 beginner standard. Introduce strings, dictionaries, lists, f-strings, JSON parsing, loops, conditionals, sets, and counters one operation at a time. Every block identifies its input and type, output and type, and research meaning. Students use a supplied PSS helper rather than implementing Krippendorff's alpha.
- **Delivery:** Use cached synthetic model responses as the required path; direct APIs, OpenRouter, and Ollama are compared as interchangeable access routes whose provenance still has to be recorded. The completion task remains narrow and is assessed for completion, followed by ordinary-language explanation practice.
- **Deck scope:** The first literature-led rebuild contained 58 slides. The opening revision expands the deck to 64 slides so that annotation history, example provenance, and substantive stakes are established before the focal result. The deck remains paced for the full 165-minute meeting, including a break and prediction/discussion pauses. Paper images, figures, code, tables, and citations are checked in the rendered 1280 × 720 deck.

## 2026-08-19 — Session 2 opening revision

- **Decision:** Do not open an annotation session with an unexplained accuracy-versus-estimate puzzle. First establish the lineage from human coding to supervised classifiers to prompted LLMs, and explain why annotation labels become consequential variables in later analysis.
- **Example provenance:** Before displaying any result, state visibly that the rezoning comments, reference labels, cached classifier labels, and prompt-variant labels are instructor-authored synthetic course materials. They demonstrate validation mechanics and provide no evidence about a real hearing, population, or named LLM.
- **Slide intention:** Each early slide must state the point students should take from its evidence. The opening accuracy slide now identifies the two directional errors and explains directly why 10/12 agreement coexists with a support estimate of 6/12 rather than 4/12.

## 2026-08-19 — What worked in the Session 2 collaboration

- **Work from literature to teaching design:** The productive order was literature audit → synthesis of the methodological lessons → 165-minute session architecture → slide/workbook build → rendered review. This prevented the deck from becoming a sequence of paper summaries or a code demonstration looking for an argument.
- **Establish continuity before novelty:** The session became clearer once it explained human coding and supervised classification before LLM annotation. Future weeks should begin with the established sociological or methodological practice that the LLM workflow extends, changes, or challenges.
- **Give the example a provenance before using it:** Students should know whether an example is empirical, adapted, simulated, or instructor-authored before seeing its results. Synthetic data are useful because they permit carefully chosen failure cases, but the deck must state visibly what was constructed and what the example cannot establish.
- **Make slides intelligible without the talk track:** A slide should communicate its evidence, intended inference, and relevance even before the instructor elaborates. Do not use a puzzle, metric, quotation, code block, or paper image until the nouns, source, comparison, and stakes have been established.
- **Use one cumulative research problem:** The synthetic rezoning study allowed construct definition, prompt stability, provenance, patterned error, precision/recall, and downstream inference to accumulate around the same cases. Future sessions should prefer one main research problem over several disconnected demonstrations.
- **Let readings perform distinct jobs:** Stuhler supplied the promptbook and task-dependence logic; Barrie et al. supplied the stability diagnostic; Schroeder and Agarwal/Naaman complicated provenance; Egami et al. carried error into the downstream claim. A paper belongs in the core deck only when its specific job is clear.
- **Connect readings directly to objects in code:** Codebook rules became a dictionary, prompt variants became named records, stability became casewise comparison plus a supplied helper, and annotation error became explicit Boolean branches and counters. This alignment made the code an implementation of the methodological argument rather than a parallel exercise.
- **Keep technical ambition below explanation ambition:** The most successful code was basic Python attached to a consequential research decision. Students use a supplied PSS implementation and explain its input and output; they do not reproduce Krippendorff's alpha. Future sessions should reserve complexity for ideas, not syntax.
- **Treat screenshots as evidence, not decoration:** Paper and chapter images worked when the paper was clearly named, the crop ended at a complete visual or paragraph, and adjacent text stated the research question and takeaway. Every screenshot must be checked at presentation size after cropping.
- **Use rendered review as an editorial stage:** Contact sheets exposed narrative gaps, while full-size checks exposed clipping and overly dense slides. User review of the actual HTML—not only the source—produced substantive improvements to wording, sequencing, and provenance.
- **Carry forward the instructor's voice:** Direct titles such as “An LLM changes who applies the rules, not why the rules are needed” worked better than slogans or compressed abstractions. Week 3 should continue using explicit, speakable sentences and should explain what each slide is doing.
- **Week 3 process:** Repeat the same staged workflow for qualitative analysis: audit the relevant literature first, synthesize what LLM assistance changes about interpretation, agree the cumulative example and session architecture, then rebuild the reading guide, slides, workbook, and task before final rendered QA.

## 2026-08-20 — Qualitative interpretation, AI interviewing, and synthetic respondents

- **Decision:** Keep Session 3 centered on how an LLM participates in interpreting an existing qualitative corpus. Begin with familiarization, initial and focused coding, constant comparison, memo-writing, theme development, and iterative return to the material before introducing an LLM-generated suggestion.
- **Decision:** Give AI-assisted and AI-moderated interviewing substantial treatment in Session 6, where the model is already conceptualized as an interactant. Compare human interviewing, an AI copilot that suggests probes, controlled adaptive interviewing, and fully AI-moderated text or voice interviewing.
- **Decision:** Keep synthetic respondents and persona interviews in Session 7. Do not present plausible model-generated testimony as evidence about a human population.
- **Rationale:** Session 3 became clearer once the human analytic process supplied the benchmark. The central computational limitation is not merely missing provenance: a Python record or separate model call does not reproduce the analyst's accumulated familiarity, remembered comparisons, developing hunches, and iterative reinterpretation.
- **Session 3 implementation:** Use the mutual-aid corpus to distinguish retrieval, coding, theming, and interpretation; trace a generated suggestion back to passages; compare supporting and deviant cases; and record alternatives and researcher memos. Mention Jack, Cooper, and Flower only in a clearly labeled closing aside. Do not build AI-moderated interviewing into the cumulative example.
- **Session 6 implementation:** Use the AI-interview literature as a major application of model-as-interactant. Candidate core roles are Geiecke and Jaravel or Wuttke et al. for scale and controlled comparison; Jack, Cooper, and Flower or Cuevas et al. for depth and interactional critique; and Liu et al. for hybrid interviewer support. Retain conversational persuasion as a second application rather than the entire week.
- **Session 7 implementation:** Distinguish AI interviewer/human respondent, human interviewer/AI respondent, and AI interviewer/AI respondent. Use participant-authenticity and accessibility work to avoid surveillance-based solutions to AI-assisted participant responses.
- **Course progression:** Describe the three-week conceptual movement as **interpret a corpus → co-produce a corpus → simulate a population**.

## 2026-08-24 — Adaptive survey design in Session 5

- **Decision:** Teach Yamil Velez's published crowdsourced adaptive survey method after the fixed text and image treatment examples.
- **Scope:** Show how participant open-ended responses become structured items, pass toxicity and redundancy filters, enter a shared question bank, and are prioritized by an adaptive algorithm.
- **Boundary:** Describe this as adaptive survey design, not a free-form AI interview. Session 6 retains the fuller treatment of turn-by-turn probing and interviewer effects.
- **Implementation consequence:** The Session 5 Python exercise remains a fixed cached pool so beginners can understand candidate records, rules, rejection reasons, and pool comparison. The Velez case shows the additional provenance that adaptive instruments require.

## 2026-08-20 — Required weekly build process for Sessions 4–14

- **Decision:** Use the stage-gated process recorded in `docs/WEEKLY_BUILD_PROCESS.md`: audit → literature review → methodological synthesis → session architecture → aligned build → rendered editorial review → testing → stored lessons.
- **Decision:** Do not begin final slides before the literature direction, synthesis, cumulative example, and session architecture have been reviewed.
- **Rationale:** The collaborative revisions of Sessions 1–3 showed that premature slide construction produces thin context, disconnected readings and code, unexplained examples, and avoidable rebuilding.
- **Implication:** Each week receives a durable literature audit, synthesis, architecture, and post-review decision record. Later revisions must consult those records before changing the session's scope or restoring previously rejected material.

## 2026-08-21 — Session 4 aligned build

- **Core question:** “What part of social experience becomes evidence?” The session studies what happens within a confrontation that allows violence to begin or enables it to remain nonviolent.
- **Sociological lineage:** Begin with Simmel on the senses, Mead on the social act, Goffman on the interaction order, conversation analysis on sequence, Emerson–Fretz–Shaw on fieldnotes, and Goodwin on professional vision. Collins enters as a development within this observational tradition, not as the beginning of situational sociology.
- **Cumulative example:** Use one non-graphic instructor-authored synthetic confrontation with a shared opening and paired escalation/de-escalation endings. Every visual, transcript, observation note, participant recollection, and model-style output is labeled synthetic. The example cannot establish intention, responsibility, theoretical validity, or a population pattern.
- **Reading jobs:** Collins motivates reconstruction of the situational pathway and the barrier of confrontational tension/fear. Nassauer supplies comparison across violent and nonviolent outcomes. Nassauer and Legewie supply event boundaries, units, camera position, synchronization, coding, validity, and ethics. Legewie, Nassauer, and Kühne extend the argument from reconstruction to sampling and generalization.
- **World-model placement:** ImageBind and V-JEPA 2 are taught after students understand the human observation problem. Shared representation, recognition, description, transcription, prediction, and planning are distinguished from sociological explanation. Bisk et al. keeps embodied and social experience in view.
- **Python progression:** Replace the old generic record-normalization task with `trace_sequence`. Students reuse dictionaries, lists, loops, conditionals, append, and functions; the new idea is maintaining previous/current state across an ordered list. The output records structured adjacent changes and transcript alignment warnings while explicitly refusing a causal label.
- **Assessment:** The completion-marked task asks for exact output prediction, two small missing branches, passing checks, comparison of both endings, one oral loop explanation, a 100–150 word reading connection, and AI-use disclosure.
- **Visual system:** Use the existing Evidence & Society theme, verified paper/chapter page images, and one coherent generated storyboard. Paper images must be identified as papers or chapters and explained through question, material, finding, and teaching role.

## 2026-08-21 — Session 4 narrative revision after rendered review

- **Narrative order:** Establish the sociological observation tradition before introducing the confrontation. The sequence is now Simmel → Mead → Goffman → conversation analysis → fieldnotes → Goodwin, followed by a clearly labeled constructed case, Collins's situational argument, video-method decisions, model operations, sampling, and Python.
- **Visible roadmap:** Show students the five-part route at the start: observation → case → records → models → Python. Section slides repeat this logic so that new material answers a question already established.
- **Paper slides:** Every focal source states why it appears at that point in the class. Goodwin now explains how coding and highlighting organize observation; the next slide connects that argument directly to video codes and dictionary keys.
- **Voice:** Prefer sentences the instructor could plausibly say aloud. Remove compressed contrasts and production-sounding formulations such as “not clerical tidying,” “operations, not warrants,” “inspectable record,” and “inferential task.”
- **Image treatment:** Never stretch a storyboard cell to a wide slide frame. Preserve the source aspect ratio, center each cell, and inspect both single and paired layouts at 1280 × 720.
- **Future-week rule:** A contact sheet is necessary but insufficient. Read the sequence of titles as a lecture, then inspect the roadmap, every paper introduction, each transition into a new literature, all reused images, and representative code slides at full size.

## 2026-08-21 — What worked and failed in the Session 4 collaboration

### What failed

- **The approved architecture did not automatically produce a coherent lecture.** The first build contained the right authors and concepts, but introduced the confrontation before explaining why Simmel, Mead, Goffman, conversation analysis, fieldnotes, and Goodwin were needed. The later return to that lineage therefore felt like a detour rather than a cumulative argument.
- **The slide sequence relied too much on the talk track.** Individual slides contained accurate material, but the title sequence did not tell students where the class was going or why the next source appeared. A paper image and a summary of its argument were not enough to establish its teaching purpose.
- **Goodwin was present but under-motivated.** “Professional vision” was introduced as an interesting paper rather than as the bridge between socially organized observation, video coding, and the fields chosen for a Python dictionary.
- **The instructor's voice drifted again during a long build.** Phrases such as “synchronization is a substantive issue, not clerical tidying,” “operations, not warrants,” and “inspectable research record” were compressed and polished in a way that would sound unnatural in the room. Earlier voice decisions had been recorded but were not enforced consistently at the sentence level.
- **The initial visual check tested fit more successfully than fidelity.** The storyboard stayed within slide bounds, but CSS forced each portrait-shaped panel into a wide frame. An overflow check could not detect that the people and scene had been stretched.
- **A contact sheet alone did not reveal every problem.** It showed broad consistency, but not whether a paper's purpose was clear, whether an image retained its proportions, or whether a phrase would sound strange when spoken.

### What worked

- **A visible five-part roadmap clarified the whole session:** observation → case → records → models → Python. The section order then repeated that route rather than asking students to infer it.
- **Putting the sociological lineage before the case gave each author a specific job.** Simmel supplies sensory position; Mead supplies action and response; Goffman supplies encounter organization; conversation analysis supplies order and overlap; fieldnotes make selection visible; Goodwin explains how trained coding practices organize observation.
- **Introducing the confrontation after the checklist made it an application rather than an interruption.** Collins could then sharpen a question students already knew how to observe, while Nassauer and video methodology specified the comparison and research design.
- **The revised Goodwin pair worked because the first slide states why the paper is present and the second applies coding, highlighting, and representation to the course objects.** The later dictionary slide explicitly returns to this connection.
- **Direct titles improved the lecture voice.** “Timing can change the interpretation of the sequence” and “The first `if` statement handles the first item” are clearer than abstract oppositions and can be said naturally in class.
- **Aspect-ratio-preserving crops fixed the storyboard.** Single and paired images are centered at their source proportions rather than enlarged to fill an arbitrary wide box.
- **Rendered review became an editorial loop.** The useful sequence was title-outline review → contact sheet → full-size checks of roadmap, paper slides, transitions, images, and code → wording and layout revision → rerender → targeted reinspection.

### What to carry into later weeks

- Before building slides, write the title sequence alone and check that each title answers why the next slide is needed.
- Give every paper a visible “why it is here” statement or an equally explicit connection to the cumulative research problem.
- Review voice by reading visible copy aloud; a stored style rule is not enough.
- Check image fidelity as well as clipping and overflow. Never infer that an image is correct merely because it fits inside the slide.
- Treat the roadmap and section transitions as part of the teaching argument, especially in a session spanning several literatures and technical operations.

### What remains specific to this session

- The precise Simmel → Mead → Goffman → conversation analysis → fieldnotes → Goodwin order belongs to a class about situated observation; later weeks should use the relevant established practice rather than copy this lineage.
- A case may sometimes open a session effectively. The problem here was not “example first” in the abstract, but introducing the confrontation before students knew what the subsequent theoretical material would help them do.
- The paired protest endings are a deliberately synthetic device for teaching situational comparison. They should not become the default example structure elsewhere in the course.

## 2026-08-21 — Session 5 aligned build

- **Core question:** Can generated media isolate a causal construct? The class follows two paid-parental-leave frames from theoretical definition through candidate production, manual review, and a Python decision record.
- **Sociological lineage:** Music Lab, a confederate status experiment, factorial surveys, and the motherhood-penalty study establish that sociologists have long constructed interfaces, performances, vignettes, and matched cases as treatments.
- **Central distinction:** A condition is a theoretical category; a stimulus is one material representation of it. Construction, validation, assignment, and estimation remain separate stages.
- **Cumulative example:** Use twelve instructor-authored synthetic messages. Keep the synthetic provenance visible and do not describe the illustrative ratings as a pretest.
- **Python progression:** One candidate dictionary enters a list; a separate rules dictionary records researcher choices; independent `if` statements accumulate every rejection reason; a second function compares retained pools. The code records decisions but does not confer construct validity.
- **Assessment:** The completion-marked task uses four cached candidates and two bounded `.append()` gaps. Students predict output, run checks, connect one decision to a reading, disclose AI use, and prepare to explain each line orally.
- **Visual rule:** Use actual paper pages and figures at their original aspect ratios. Every focal paper must have a visible teaching job rather than appearing as an unexplained screenshot.

## 2026-08-24 — Session 5 voice revision

- **Problem found in the rendered deck:** The lecture contained the right material but still used compressed planning language in visible copy, including “our route,” “causal design,” “generated candidates,” “research history,” “production conditions,” and “different research meanings.” These phrases described the structure from outside rather than sounding like an instructor explaining the material to students.
- **Revision:** Rewrite titles as sentences that could be spoken naturally in class. Say what students are about to look at or do: “We will check the first message by hand,” “What else changes between these two messages?”, and “The Python applies the same checks to every message.”
- **Code-slide rule:** Explain the actual value, object, and action in a complete sentence. Avoid label sequences such as “input / output / research meaning / limit” in visible slide copy, even when those elements still guide the teaching design.
- **Future check:** Search every completed deck for abstract noun clusters, slogan-like contrasts, roadmap labels, and production-language terms. Then read the title sequence aloud as a seminar before rendering.

## 2026-08-24 — Session 5 full implementation after slide review

- **Rebuild rather than pad sparse slides:** The revised deck uses 76 content slides with varied structures—source crops, message comparisons, tables, rating scales, candidate galleries, provenance maps, and code traces. Each sequence now establishes the example, identifies the decision at stake, and states what the evidence permits.
- **Begin with concrete treatment carriers:** Vignettes, matched applications, confederates, and interfaces are each defined through a sociological example before the focal papers are developed.
- **Return to original sources:** Emerson, Yancey, and Chai's original article now introduces the neighbourhood-vignette example. Wallander remains a methods reading rather than being cited as the source of Emerson's study.
- **Published framing case (revised 2026-08-24):** Bloemraad, Silva, and Voss's 2016 *Social Forces* article replaces the unpublished McManaway dissertation. The deck uses the published article's rights, economics, and family framing contests and Figure 3; the synthetic candidate pool is now organized around those three domains.
- **Use causal-inference language for semantic differences:** Intended frame wording is marked separately from policy detail, warmth, certainty, and other possible confounds. Random assignment identifies the effect of the complete assigned message, not the isolated effect of the researcher's condition label.
- **Define candidate, starting pool, retained pool, pretest, rating scale, and response distribution before using them:** A single message score is explicitly distinguished from a pool mean across messages and a participant-response distribution from a real pretest.
- **Correct the teaching-data provenance:** Candidate texts are cached LLM outputs lightly edited by the instructor. Perception scores and flags are instructor-authored mock annotations—not LLM judgments and not human pretest data. Python calculates word counts from the displayed text; researcher-chosen rules remain separate inputs.
- **Keep the code faithful to the research process:** The workbook and helper calculate `word_count` from `text.split()`, preserve all rejection reasons, copy the calculated count into retained records, and compare mock annotations only after individual screening. Every code block states its input, type, operation, output, source, and limit in beginner language.
- **Room discussion rather than pair instructions:** Slides ask the class to interrogate a shared example. The take-home exercise remains individual and completion-marked, with oral explanation used to verify understanding.
- **Verification:** Session 5 tests pass; the workbook's code cells execute in sequence; JSON files validate; Quarto renders the HTML successfully. Direct visual inspection of the refreshed HTML remains the final instructor review gate.

## 2026-08-24 — Session 5 publisher-source and legibility correction

- **Use the supplied article, not an access preview:** The Emerson slide now shows the published *American Sociological Review* title page and a separate, readable extract of the wording respondents heard. The earlier JSTOR metadata/login preview is not used.
- **Use the final publication when it is available:** LinkedOut now uses the typeset *Quarterly Journal of Economics* article and its published online appendix rather than images from the CRC discussion paper.
- **Split dense source figures instead of shrinking them:** The seven-stage LinkedOut image pipeline is shown in two adjacent crops. The rating instrument is also divided into intended characteristics and possible confounds, allowing students to read the actual questions.
- **Source screenshots must do explanatory work:** Each crop is introduced by a direct title and followed by a sentence explaining what the source shows and why it matters for treatment construction.

## 2026-08-24 — What worked in the Session 5 collaboration

### What initially failed

- The first build chose McManaway's dissertation because it offered a convenient framing design, but convenience was not enough. The source was unpublished, substantively arbitrary for this course, and difficult to present as an authoritative sociological experiment.
- Several screenshots passed basic file and geometry checks while still failing editorially. Article text ended halfway through a paragraph, and splitting the LinkedOut pipeline across two crops cut arrows, faces, and stages at the slide boundary.
- The deck alternated between sparse one-sentence slides and overloaded evidence slides. The LinkedOut rating-form slide asked students to parse too many questions and scales at once.
- Schwitter and LinkedOut began to repeat the same broad lesson about candidate generation and validation because each paper had not been given a sufficiently distinct job.
- The Python slides explained individual syntax but did not state their overall research task often enough. Students could follow `.append()` or an `if` statement without yet knowing that the program was only applying stated rules to saved records.
- Repeated local revisions left the architecture and supporting documents temporarily behind the rendered deck. Alignment must be restored after any substantive change to the example or literature.

### What improved the session

- Replacing the dissertation with Bloemraad, Silva, and Voss's published *Social Forces* article gave the example a clear sociological question, exact published treatments, interpretable heterogeneous results, and a defensible reason for appearing in the course.
- The replacement was carried through the dataset, workbook, task, solution, tests, syllabus, reading guide, instructor notes, literature synthesis, bibliography, and slides. It became one research design rather than a slide-only citation swap.
- Reviewing numbered slides against the source images exposed problems that rendering success could not detect. Crops improved when they ended after a complete abstract, treatment list, figure, or experimental stage rather than at a convenient pixel height.
- The LinkedOut section became clearer after replacing severed pipeline crops and an overloaded rating form with one complete published figure and one plain comparison of intended and nuisance ratings.
- Velez's crowdsourced adaptive surveys were integrated by removing repeated LinkedOut material rather than simply adding another aside. The transition now has one clear job: fixed candidate pool → evolving question bank → turn-by-turn interviewing in Session 6.
- Naming the boundary mattered. Velez is taught as adaptive survey design rather than described loosely as a free-form AI interview.
- The Python section improved when it began with its narrow research task, explicitly stated what it does not do, traced the changing value of `reasons` for one candidate, and gave the two returned lists distinct research meanings.
- Shortening titles after the narrative revision made them easier to read aloud without returning to slogan-like phrasing.

### Lessons to carry into Session 6

1. Start from a source hierarchy: peer-reviewed published work first; use working papers only when recency or uniqueness justifies them and label their status.
2. Assign every paper one teaching job and decide what it replaces before adding it to the deck.
3. Inspect screenshot boundaries for semantic completeness as well as geometry. Never end mid-paragraph, mid-figure, mid-arrow, or mid-experimental stage.
4. State the computational procedure's research job before explaining syntax. Then trace exact values through one complete iteration.
5. Distinguish forms of adaptation precisely: an evolving shared item bank, participant-specific tailoring, and turn-by-turn conversational probing create different data and inferential problems.
6. After any substantive redesign, realign the architecture and student-facing materials before calling the week complete.
7. Preserve the successful sequence: literature audit → synthesis → narrative arc → source images → beginner-code mapping → rendered editorial review.

## 2026-08-24 — Session 6 literature-led implementation

- **Overall argument:** Do not ask whether AI is generally a good interviewer. First specify what the interview is meant to establish, what discretion the interviewer has, what relationship produces the answer, and which path the participant actually received.
- **What came before:** Chicago life records add temporal and contextual adequacy; Merton and Kendall add specificity without direction; standardized interviewing adds procedural comparability; repair distinguishes fixed wording from shared meaning; Oakley and Bourdieu make the relationship part of data production; Jerolmack and Khan bound claims made from interview accounts; CASI shows that automation and mode effects predate LLMs.
- **Contemporary papers:** Geiecke and Jaravel make the scalable AI-led case; Wuttke identifies interviewer-type effects under random assignment; Jack and Cuevas show why completion, richness, human judgment and participant experience should not be collapsed; Panfilova makes model variation visible. Hackenburg is a short transfer to conversation as treatment rather than the week's organizing subject.
- **Cumulative example:** Two fully synthetic seminar-participation interviews share the same fixed opener and closing protocol question. Their adaptive paths diverge toward intellectual worth versus status and the interaction order. The target is participants' accounts and interpretations, not observed participation behaviour.
- **Python job:** `audit_interview` reconstructs the realized path from cached turns. It counts roles and question sources, preserves topics in first-seen order, and stores every adaptive probe with the turn it responds to. It does not call a model or score depth, rapport, accuracy, or validity.
- **Beginner explanation:** Every code slide shows the input being read, the line or branch, state before and after, and the research meaning. The new idea is `enumerate`; dictionaries, lists, conditionals, append and functions are reused.
- **Visual/editorial rules:** Use source images at original aspect ratio with `object-fit: contain`; show full figures or semantically complete crops; never use login, library-access or publisher-error previews. Vary transcripts, tables, split paper layouts, process steps and code-state layouts. Titles should say plainly what the slide is doing.
- **Verification:** The 58-slide Quarto deck renders successfully, all referenced images exist, the notebook executes against the cached data, and the Session 6 solution tests pass. The in-app browser blocks local `file:` inspection, so the rendered HTML remains available for the instructor's final visual review rather than claiming browser-based inspection that did not occur.

## 2026-08-25 — Session 6 source, voice and narrative revision

- **Opening:** The opening judgment is now answered explicitly. Interview A better supports a claim about how this participant defines intellectual worth; Interview B is shorter but introduces “not confident.” Neither is universally better, and the three morning questions now follow directly from that judgment.
- **Foundational criteria:** The criteria are anchored in Merton and Kendall, Fowler and Mangione, Oakley, Bourdieu, Jerolmack and Khan, and the earlier life-history tradition. The deck distinguishes exact criteria from instructor synthesis and uses the supplied published Merton and Kendall PDF.
- **Source rule:** Use a full visible citation when a paper first appears. Do not use login pages, bot-protection screens, publisher errors or preprints as article images. Use an exact quotation or ask for the published PDF instead. Apply this citation-format audit to Sessions 1–5 during their next revision.
- **Screenshots:** Crop to the exact table, paragraph, protocol or figure being discussed. The Tourangeau and Smith slide now shows Table 3 rather than an unrelated later table; Geiecke and Jaravel shows only the relevant panel; Cuevas and Panfilova use tighter semantic crops.
- **Contemporary arc:** The sequence is now system arrangement → access/privacy → local/remote trade-offs → published implementations → kinds of validation evidence. The Liu “copilot” is described as an envisioned support design, not a deployed commercial product.
- **Voice:** Text and voice are separated technically. The deck records microphone audio → STT → text interviewer → TTS → audible question, explains the exact input and output of each call, and treats voice, pace, model, provider and instructions as part of the interview design.
- **Closing:** The Hackenburg/Yin persuasion transfer was removed. The lecture returns to the opening pair before the cumulative example and Python, so the code now follows the methodological answer instead of delaying it.
- **Bourdieu source correction:** The published PDF now sits in `literature/source_pdfs/session06/`. The Bourdieu slide shows the complete note 2 from p. 34 and highlights its full first sentence. This replaces the shortened text-only quotation and preserves the rest of Bourdieu's claim about objective structures shaping both the recorded interaction and the researcher's interaction with participants.
- **Jerolmack and Khan evidence sequence:** The earlier one-slide summary is now four slides built from the published article. The deck defines the attitudinal fallacy in the authors' text, works through LaPiere's 251 encounters and the Dean–Whyte budgeting example, and then shows the authors' explicit account of what interviews can establish. Highlighted source crops are paired with plain-language interpretation, so the claim boundary is demonstrated rather than merely asserted.
- **Explain named system components before reporting results:** The Cuevas design now uses the paper's actual Figure 2 and a separate slide defining the fixed baseline, Dynamic Prober and Member Checker in terms of exactly what participants received. Do not expect students to infer a system design from author-created labels, and never substitute prose that refers to a figure for the figure itself.

## 2026-08-25 — What the Session 6 instructor review repaired

### Narrative and teaching arc

- The opening interview comparison initially asked for a judgment without supplying a clear answer or explaining what evidence supported that answer.
- The three questions for the morning were useful but were not connected clearly enough to the opening comparison.
- Several transitions were missing or delayed, including the move between foundational interviewing traditions, the move from interview accounts to Jerolmack and Khan, and the return to the opening pair.
- CAPI, CASI and audio-CASI appeared without enough explanation of what changed for the participant or why mode mattered for the argument.
- Some contemporary papers and technical sections arrived as additions rather than answers to a question created by the previous section.
- The final repair made the sequence cumulative: purpose of interviewing → older interviewing traditions → relationship and claim limits → earlier computer-assisted modes → AI-assisted and AI-led systems → evaluation evidence → return to the opening example → Python audit.

### Foundations and source anchoring

- Early criteria and comparison tables looked authoritative without being anchored closely enough in foundational literature.
- Merton and Kendall needed the supplied published PDF, exact criteria and readable source passages.
- Oakley and Bourdieu were initially reduced to large claims on sparse slides. Both required fuller citations, more explanation and direct source evidence.
- Bourdieu's quotation needed checking against the complete note in the published PDF; the slide now shows and highlights the full relevant passage.
- Jerolmack and Khan initially received one thin summary slide. The revised sequence defines the attitudinal fallacy and demonstrates it through the LaPiere and Dean–Whyte examples before stating what interviews can still establish.
- Statements such as “this solves the problem” were replaced with claims that match the more qualified arguments in the sources.

### Study designs, systems and findings

- Tourangeau and Smith needed a proper introduction, full citation, the actual substantive finding and the correct table.
- Liu et al. was described with vague phrases such as “support imagined by interview researchers.” The repair states that it is an exploratory interview study of 16 researchers' views about possible support and concerns, not a test of a deployed copilot.
- The deck originally used unexplained system labels and did not always say who made the next-question decision.
- Cuevas's design was compressed into three sentences. “Dynamic Prober” and “Member Checker” were undefined, and the screenshot showed prose referring to Figure 2 rather than Figure 2. The repair shows the actual design figure and defines exactly what participants received in all three conditions.
- Panfilova's controlled benchmark needed a shorter explanation, a clear statement that the respondent was simulated and a citation that remained fully on screen.
- Findings were revised to distinguish operational success, participant experience, conversational quality, qualitative richness and evidence about behavior.

### Technology and beginner explanation

- The deck needed a clearer account of text and voice as different technical pipelines and a direct explanation of speech-to-text and text-to-speech inputs and outputs.
- Privacy coverage had to follow raw audio, transcripts, prompts, provider routing, retention and ownership rather than stop at a platform's prompt-storage statement.
- Local and remote systems needed concrete discussion of latency, hardware, model size and maintenance.
- Python slides needed to state the overall research job, the provenance of dictionaries and annotations, the exact values entering each step and the limits of the returned audit.
- The code was revised to map onto the human interviewing process while making clear that it does not evaluate rapport, depth, truth or validity.

### Voice and visible copy

- Repeated phrases sounded generated or compressed: “the answer becomes input to another decision,” “trade external transfer for hardware and maintenance,” “realized interview path,” and other abstract oppositions.
- Visible production language such as “This is an instructor synthesis…” distracted from the substantive point and was removed.
- “The paper is about what researchers wanted and feared” was replaced with a straightforward description of the Liu study's design and limits.
- Redundant captions, including “A system can work as software and still need substantial methodological revision,” were removed when they merely repeated the slide title.
- Titles and body copy were rewritten as sentences the instructor could plausibly say aloud.

### Visual design and citations

- All tables needed a closing bottom rule.
- A blank slide and several sparse or overloaded slides required restructuring.
- Screenshots sometimes showed the wrong page, the wrong table, a preprint, a login prompt, text about a figure rather than the figure, or a crop ending mid-sentence.
- Essential figures, quotations and paper text needed larger crops and highlighted passages.
- Citations needed one standard format, a full first reference, shorter repeated references and placement that kept the complete DOI on screen.
- Render and overflow checks found geometric problems but could not detect weak narrative, incorrect evidence, stretched images, unreadable text or unnatural wording. Full-size source comparison and aloud review are now mandatory.

### Standing action

- `docs/SLIDE_REVIEW_CHECKLIST.md` is now the required pre-delivery self-review for future weeks.
- Apply the same checklist retrospectively whenever Sessions 1–5 are reopened, even when the requested edit appears local.
- Sessions 7–14 must pass the checklist before they are presented for instructor review.

## APSA chapter source and section map (2026-08-27)

- The canonical course copy of Barrie et al. (2026), “AI and Research Methods,” is the standalone APSA Preprints chapter PDF at `coursebook/downloads/readings/ai-and-research-methods-barrie-et-al-2026.pdf`.
- Student-facing chapters link directly to that local PDF, so it remains downloadable from the published course book. They also link to DOI `10.33774/apsa-2026-h59kk` as the stable external record.
- Do not use the former APSA full-report URL ending in `Lee-TF-APSA-AI-Report-2026-Tucker-Persily.pdf`; it no longer resolves.
- The verified chapter runs from §10.1 through §10.7. It contains no §10.8 or §10.9. Weekly assignments must name the actual relevant section rather than repeating a generic or inferred section range.

## Beginner Python completion tasks (2026-08-27)

- Weekly completion tasks assess whether students can trace and explain a short research routine. They do not assess fluency, abstraction or efficient Python.
- For developed Weeks 1–7, the downloadable `.py` file must reproduce the linear exercise printed in the chapter. It must not introduce a harder task through incomplete functions, `__main__` guards, assertions, test harnesses or multi-stage metrics.
- The required pattern is: run a complete block, inspect the stated output, change one named input, run it again and explain the methodological consequence.
- Students should understand the five parts of an LLM routine—input, prompt/messages, model call, returned text and researcher check. The course may supply setup and live-call lines; students are not required to engineer wrappers around them.
- `scripts/check_coursebook.py` now rejects function or class definitions and `__main__` guards in the developed weekly task files.

## Class rhythm and narrated coding submissions (2026-08-27)

- The normal meeting has three substantive parts: instructor framing first, discussion of the readings in the middle and a guided coding walkthrough at the end.
- The weekly coding submission is a short screen recording with audio, uploaded to a dedicated NYU Box folder whose link will be added later.
- Students must show the original run and one named change and explain the input, operation and output of every block. They must also explain a methodological limit and connect it to a reading. Video editing and code elegance are not assessed.
- Weeks 1–2 use real OpenRouter and Ollama calls. Students choose either route in Weeks 3–7 and compare both again in Week 8; recorded responses are an access contingency.
- Python is introduced through the parts of an LLM routine: strings and messages, returned objects, JSON and structured outputs, generation parameters, conversation state, loops, and then small functions with explicit parameters from Week 9.
- The skeletal Weeks 8–13 must retain this arc when their literature, slides and chapters are developed. Week 14 remains presentation-only.

## Week 14 is presentation week (2026-08-27)

- Week 14 is reserved entirely for student project presentations, questions and brief feedback.
- It introduces no new reading, lecture content, slides, notebook, coding walkthrough or weekly completion task.
- The student-facing page contains only the presentation format, what to bring and the reminder that the final research-design package is submitted during the examination period.
- Obsolete Session 14 teaching artifacts were removed. `scripts/check_coursebook.py` now fails if a Session 14 task, reading guide, slide deck, solution or workbook is reintroduced.

## Dual-route Python and LLM strand implemented (2026-08-27)

- Local JupyterLab or VS Code is canonical. Colab remains an OpenRouter-only fallback because it cannot normally reach Ollama on a student's computer.
- The supported clients are the official `openrouter` and `ollama` Python packages. The central model defaults are `openai/gpt-5.2` and `gemma4:e2b-it-qat`; both identifiers must be retested two weeks before term.
- Weeks 1–2 show separate complete OpenRouter and Ollama calls. Weeks 3–7 retain both explicit `if/else` branches and let the student choose `ROUTE`. Week 8 requires a small dual-route loop. No student-defined function appears before Week 9.
- Each routine starts with a sociological input and visibly proceeds through messages, route, call, raw return, parsed output and methodological check. The Python page, notebook and task use the same assessed routine for developed Weeks 1–7.
- Weeks 8–13 have runnable coding prototypes, but their course-book pages remain bare outlines until their literature reviews, slides and full chapters are collaboratively developed.
- The setup clinic, diagnostic script and preflight notebook check both routes without displaying the key. Students with unsuitable hardware complete the early local calls on a paired or instructor machine without penalty.
- `data/dual_route_recorded_outputs.json` supplies clearly labelled outage fixtures. Live calls remain normal; fixtures do not masquerade as current model evidence.
- Weekly completion remains a narrated screen recording in which the student explains every operation's input and output, the named change and one methodological limit.

## Weekly recording deadline and submission guide (2026-09-08)

- Weekly recordings are due by 5:00 p.m. Eastern on the Tuesday before the next class.
- `coursebook/recording-and-submission.qmd` is the single source for the Box upload URL, filename guidance and instructions for macOS, Windows and ChromeOS.
- Weekly chapters and Python pages link to that guide rather than repeating the Box URL. This keeps the destination and instructions consistent if they change.
- Students submit one continuous recording with audible narration. Camera video and editing are not required. They must check the saved file's audio before uploading and must never display the shared OpenRouter key.

## Course-book reading space and Colab ownership (2026-09-08)

- Use short labels in the book sidebar and collapse course parts by default. Preserve the complete sociological question as the visible page title.
- Enable reader mode so students can hide both navigation columns when reading or tracing code.
- Python pages use a wider body, a shallower right-hand contents list and more vertical space between code steps. Code scrolls horizontally rather than wrapping into difficult-to-read lines.
- Every developed Python page begins with a compact routine summary naming the trace, the Python introduced and the single required change.
- The canonical public repository owner is `cjbarrie`. Colab links using `christopherbarrie` are invalid and are rejected by `scripts/check_coursebook.py`.

## Setup and Week 1 Python pivot expanded (2026-08-28)

- Introduce Python, notebook, SDK, API, server and model as six distinct pieces before asking students to run a call.
- Explain OpenRouter as a remote routing service and Ollama as a local server at `localhost:11434`. Show the complete outward and return path for each request, including authentication, provider routing, local model loading and the different response shapes.
- Show a simplified request body so students can see that model name, messages and settings are ordinary Python values serialized as JSON. Keep the key in the authorization layer rather than in the prompt or request-body teaching record.
- In Week 1, make both real calls before expanding the Python lesson. Use the resulting request and response objects—not an unrelated toy exercise—to introduce strings, lists, dictionaries, list indexing, dictionary keys, SDK attributes, string methods, integers, Booleans, `print`, `type` and `len`.
- Explicitly contrast `messages[0]`, `first_message["content"]` and `hosted_message.content`. The type of the object on the left determines whether a position, dictionary key or SDK attribute is being accessed.
- Preserve the no-student-defined-functions rule until Week 9. Week 1 calls supplied functions but does not ask students to define one.
## 2026-09-08 — Colab and local-kernel repair for Weeks 1–2

- Every introductory Colab notebook must install its required Python SDKs before the first package import; cloning the repository alone does not install packages into the Colab runtime.
- Local notebooks do not install packages silently. A missing `openrouter` or `ollama` import now produces an actionable instruction to restart from `uv sync` and `uv run jupyter lab`, with the VS Code interpreter alternative documented separately.
- Colab may import the Ollama Python client, but it cannot reach the Ollama service running on a student's laptop. Week 1 and Week 2 therefore skip the local call explicitly in Colab, store `None`, and explain that `None` means “not run,” not a model return or model disagreement.
- Release tests must check setup-before-import ordering, package installation commands, the public repository URL, actionable local instructions and the guarded Ollama branch. Both notebooks must execute completely under controlled local and Colab-style model returns before publication.
## 2026-09-08 — Colab audit extended through Weeks 3–13

- Every student notebook now uses the same setup contract: detect Colab directly, install missing notebook packages before imports, shallow-clone the public repository, enter the correct weekly folder, and add the repository root to `sys.path` for course utilities.
- Weeks 3–7 and 9–12 select OpenRouter automatically in Colab and retain Ollama as the local default. This prevents an apparently valid Colab notebook from failing later when it reaches a local-server call.
- Week 8 preserves the required two-route comparison without pretending Ollama ran in Colab: hosted results are produced there, local summaries are `None`, and the local half is completed outside Colab. Week 13 similarly limits its Colab grid to hosted rows.
- Week 13's setup checks and, if necessary, installs `pandas` before its final table cell.
- Future release checks cover all Weeks 1–13, including setup-before-import order, package declarations, public repository URLs, repository import paths, Colab route selection and the special dual-route behavior in Weeks 8 and 13.

## 2026-09-08 — Cold-start Colab setup regression fixed

- `invalidate_caches()` belongs to the top-level `importlib` module, not `importlib.util`. Notebook setup cells therefore import `importlib` and use `importlib.util.find_spec(...)` for package discovery.
- Warm-kernel tests are insufficient because they skip the installation branch once dependencies are present. Release tests must simulate a fresh Colab runtime with missing packages, intercept the install step, execute cache invalidation and then execute the following package-import cell.
- The cold-start regression test now runs against every Week 1–13 notebook, so the exact Week 2 failure cannot silently return through either notebook generator.
