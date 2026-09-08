# Literature-led weekly build process

**Status:** Canonical process for Sessions 4–14, consolidated from the collaborative revisions of Sessions 1–3.

## Why this process exists

The first three sessions improved most when literature, methodological history, and the teaching argument were settled before slides and code were built. Early builds were weakest when they began with an LLM capability, treated readings as a sequence of summaries, used several unrelated examples, or expected a screenshot or code block to explain itself.

The required order is:

`audit → literature review → methodological synthesis → session architecture → aligned build → rendered editorial review → testing → stored lessons`

Slides are not the starting point. Each stage leaves a durable record so that later revisions do not restore decisions that have already been rejected.

## Stage 1 — Audit and orientation

Inspect the existing syllabus entry, reading guide, instructor notes, workbook, task, solution, tests, slides, data, and relevant material from the previous course. Record:

- what the existing session is trying to teach;
- what is worth retaining;
- what is thin, disconnected, outdated, or pitched incorrectly;
- how the session follows from previous weeks;
- the established sociological or methodological practice that preceded the LLM application.

Write the audit to `literature/sessionXX_literature_review.md`. Do not build slides.

## Stage 2 — Literature review

Search current primary sources as well as the relevant methodological foundations. Do not produce an undifferentiated bibliography. For every candidate reading, record:

1. material or data;
2. research question;
3. method or comparison;
4. principal finding;
5. specific teaching job in this session.

Separate required readings, in-class evidence, and optional asides. Keep the assigned load comparable with other weeks. Verify bibliographic details and preserve direct source links.

Use an explicit source hierarchy. Prefer the published peer-reviewed article when it exists. A dissertation, preprint, or working paper should enter only when its recency, evidence, or unique design warrants the status tradeoff, and its status must be visible to students. A convenient figure or easily downloaded PDF is not by itself a reason to make a source central.

**Review gate 1:** The instructor reviews the audit, fresh literature review, and proposed core readings before methodological synthesis begins.

## Stage 3 — Methodological synthesis

Explain what researchers did before LLMs, what an LLM changes, and what inferential burden remains. Give each focal paper a distinct role. Select one cumulative sociological research problem that can support the readings, conceptual explanation, code, discussion, and assessment.

The synthesis must distinguish technical capability from warranted inference and identify the relevant validation evidence, failure modes, and researcher judgments. Clearly label all example material as empirical, adapted, cached, synthetic, or instructor-authored and state what it cannot establish.

Write the result to `literature/sessionXX_synthesis.md`.

**Review gate 2:** The instructor approves the central argument, reading-to-teaching map, and cumulative example before session architecture begins.

## Stage 4 — Session architecture

Create `instructor/sessionXX_architecture.md` before writing final slides. It must specify:

- the substantive research question and intended endpoint;
- the connection to the semester arc;
- the cumulative example and its provenance;
- the complete 165-minute sequence, including the break;
- the purpose of each section and the student activity;
- evidence of student understanding;
- the job of each reading;
- the reading-to-code and human-method-to-code mappings;
- the Python progression from the previous week;
- the completion task and oral-assessment rehearsal;
- material that should remain outside the session.

Begin with the established social-scientific practice, construct, source material, and stakes of error. Introduce the LLM only after students understand the activity it extends or changes.

Before Review Gate 3, read the proposed slide titles in order without the body content. For every transition, be able to answer: Why does this slide come next? What question from the previous slide does it answer? What question does it create for the following slide? Add a visible roadmap when a session spans several literatures, kinds of evidence, or technical operations.

Decide deliberately when the cumulative example enters. An example can open a class when it establishes the stakes or a puzzle. If its meaning depends on a conceptual or methodological lens, establish that lens first and then introduce the example as an application.

**Review gate 3:** The instructor approves the architecture and proposed slide sequence before final artifacts are built.

## Stage 5 — Build aligned artifacts

Update the session syllabus, reading guide, instructor notes, workbook, completion task, solution, tests, deck, data, bibliography, `COURSE_PLAN.md`, and `DECISIONS.md` as one system.

Use one cumulative research problem rather than disconnected demonstrations. Every focal reading must motivate a research decision, diagnostic, failure mode, or validation check that appears in the example and code. Every code object must have a clear role in the methodological argument.

## Stage 6 — Beginner Python progression

Assume that students remain beginners even when an object has appeared before. Reintroduce familiar objects before adding a small new step. Every code segment must state:

1. research task;
2. exact input value;
3. Python type;
4. operation performed;
5. exact output and its type;
6. meaning for the sociological question;
7. what the result does not establish.

Map the computational procedure onto the human research procedure and say where the representation is thinner. Split complete programs across several slides, trace actual values through the first iteration or branch, insert prediction pauses, print intermediate outputs, explain assertions in ordinary language, and include oral rehearsal.

Weeks 1–2 use both OpenRouter and Ollama with synthetic, public or instructor-authored material. Weeks 3–7 use a visible route selector, Week 8 compares both routes again, and Week 9 introduces the first student-defined function. A recorded return must remain available when access fails. Continue to unpack prompt, messages, route-specific call, raw return and methodological check in every routine.

The Python arc follows the LLM routine: strings and messages; JSON and structured outputs; generation parameters; conversation state; a first loop in Week 8; and the first small student-edited function, with every parameter explained, in Week 9. Later weeks reuse loops and functions for interaction, tool records, reruns and audits.

Every weekly task is submitted as a narrated screen recording by 5:00 p.m. Eastern on the Tuesday before the next class. Students show the original run and one named change and explain each operation's input and output, a methodological limit and the reading connection. Link to `coursebook/recording-and-submission.qmd` for the current Box folder and platform instructions; do not duplicate the URL across weekly pages.

Before the first syntax slide, state the program's narrow research task and list important operations it does not perform. A sequence can be locally well explained while its overall purpose remains vague; both levels are required.

## Stage 7 — Slide writing and visual evidence

Use the instructor's direct, explanatory voice. Titles should say what the slide is doing or what students should understand. Avoid slogans, compressed abstractions, artificial oppositions, and consultant-style phrasing.

Do not assume that a recorded voice rule will enforce itself. Read visible copy aloud and replace phrases that are grammatically tidy but implausible in speech. Be especially suspicious of compressed “X, not Y” formulations, abstract nouns standing in for actions, and titles that sound like editorial taglines.

A slide should identify its source, evidence, intended inference, and relevance without depending entirely on the spoken explanation. Introduce papers explicitly as papers and state their material, question, finding, and role. Use actual paper or publisher images where possible. Never present a bibliographic card or recreation as a paper screenshot.

Treat screenshots as evidence, not decoration. Keep framing and scale consistent and ensure that titles, figures, tables, code, and citations are legible at 1280 × 720.

Use one visible citation format throughout every deck: **Author(s) (Year), “Article title,” Journal volume(issue): pages. DOI or stable URL.** A paper's first appearance must identify it as a paper and give the full citation. Later finding slides may use an abbreviated author–year citation only when the full reference has already appeared. Put complete source links in the speaker-note `[Sources]` block as well. Audit Sessions 1–5 for this format when they are next revised.

Never use a login prompt, bot-protection page, library error, metadata card, or preprint screenshot as a visual stand-in for a published article. If the published PDF cannot be obtained, use a properly sourced quotation or a plain citation and ask the instructor to place the PDF in the relevant `literature/source_pdfs/sessionXX/` directory.

Crop to semantic boundaries as well as visual boundaries. A crop should end after a complete abstract, paragraph, table, figure, caption, questionnaire block, or experimental stage. Do not split arrows, faces, axes, treatment wording, or other relational evidence across slides. When a wide process figure cannot be divided cleanly, show the complete figure and simplify the accompanying prose.

Preserve the aspect ratio of every image unless distortion is itself part of the teaching point. A geometry check can detect overflow but cannot detect stretched people, plots, screenshots, or paper pages. Compare the rendered image with the source and inspect every reused crop at full size.

## Stage 8 — Rendered editorial review and testing

Rendering is part of authorship. First read the title sequence as a lecture outline and check the logic of every transition. Then inspect the complete rendered deck as a contact sheet for narrative structure, followed by every paper image, figure, table, code slide, citation, reused image, and dense slide at full size. Read the wording aloud. Rewrite anything the instructor would not naturally say. Check that the opening supplies the necessary context, no aside displaces the argument, and every slide has one identifiable teaching purpose. For each paper slide, ask whether a student can tell that it is a paper, why it appears here, and what later research or code decision it changes.

After revisions:

- rerender and reinspect affected slides;
- execute the complete notebook;
- run session tests and full integration checks;
- verify citations and student-facing links;
- check that secrets and live credentials are absent;
- report exactly what passed and any remaining limits.

The complete required review is maintained in `docs/SLIDE_REVIEW_CHECKLIST.md`. It must be used for every newly rebuilt week and whenever an earlier week is reopened. A local correction does not exempt the rest of that deck from the retrospective checks in the file.

## Stage 9 — Store what the collaboration taught us

After final instructor review, add a dated section to `DECISIONS.md` titled `What worked in the Session X collaboration`. Record:

- requested changes;
- why the earlier version fell short;
- what passed formal checks but still failed editorially or pedagogically;
- which revisions improved it;
- reusable lessons for later weeks;
- session-specific choices that should not be generalized.

Update this file when the collaboration reveals a better process.

## Release principles inherited from Sessions 1–3

- Establish continuity before novelty.
- Give every example its provenance before showing a result.
- Make each slide intelligible without relying on the talk track.
- Use one cumulative research problem.
- Give readings distinct jobs rather than summarizing them serially.
- Make code implement the methodological argument.
- Keep technical ambition below explanation ambition.
- Preserve iterative human practices that a computational record cannot reproduce.
- Treat rendered review as an editorial stage rather than a final technical check.
