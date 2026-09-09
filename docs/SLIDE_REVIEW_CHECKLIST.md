# Slide self-review checklist

**Status:** Required before instructor review of every newly rebuilt week and whenever an earlier week is reopened.

This checklist records the kinds of problems found during the collaborative repair of Session 6. Passing a render or overflow test is not enough. The reviewer must read the deck as a beginner, inspect the evidence as a researcher, and read the visible wording aloud as the instructor.

## 1. Read the lecture as a sequence

- Read only the slide titles in order. Can you explain why every slide follows the previous one?
- For every section break, state the question just answered and the question that now needs answering.
- Does the opening example receive an explicit answer before the deck moves on?
- Do the session's main questions follow from the opening rather than appearing as a second, disconnected opening?
- Does the “what came before” section establish the relevant sociological craft before introducing LLMs?
- Does each foundational author have a distinct teaching job, with enough space to support any large claim?
- When the deck returns to an earlier example, is the return close enough for students to remember what is being resolved?
- Remove asides that interrupt the main method. Move them to notes or another week.
- Introduce the focal LLM procedure near the beginning with one exact input and output. Do not make students infer what “silicon sampling,” an agent, an adaptive interviewer or another new procedure means from later paper examples.
- Check historical order as well as thematic order. If chronology is broken, the slide must have a clear substantive reason for doing so.
- Keep a paper in the main arc only if it changes the question, comparison, standard or procedure. Move repeated findings to additional reading.

## 2. State the purpose of every slide

For each slide, answer in one sentence:

1. What is this slide showing?
2. Why is it here?
3. What should a student understand before moving on?

If these answers are not visible from the slide itself, revise it. Do not rely on the instructor to supply missing study background, definitions, findings, or stakes orally.

## 3. Anchor every methodological claim in literature

- Do not invent criteria, typologies, trade-off tables, or evaluative dimensions and then present them as established knowledge.
- Cite the foundational source for each criterion and show the relevant passage, table, instrument, or figure when it materially helps.
- Distinguish clearly between an author's claim, an instructor synthesis, and a course heuristic. Do not add defensive captions announcing synthesis when the slide can simply cite its component sources.
- Check claims against the complete source passage, including notes and qualifications. Do not shorten a quotation in a way that changes its meaning.
- If a slide says one approach “solves” a methodological problem, verify that the source really makes that claim. Prefer an exact description of how it changes or reduces the problem.

## 4. Introduce each paper properly

At a paper's first appearance, students should be able to identify:

- that the object on screen is a paper;
- the full author, year, title, venue and DOI or stable URL;
- the material or participants;
- the research question;
- the comparison or method;
- the principal finding;
- the reason the paper appears in this lecture.

Do not move directly from a title-page image to a large conclusion. Give major foundational papers more than one slide when their argument carries substantial weight.

Before building the paper sequence, identify the exact published figure, table, quotation, instrument or result that will support the teaching claim. A paper's general methods diagram is not a substitute for the reported result under discussion.

## 5. Use the correct source image

- Use the published article PDF when one exists. Do not use a preprint page, dissertation, login screen, library-access prompt, metadata preview or publisher error as a substitute.
- If the published PDF is unavailable, ask the instructor to place it in `literature/source_pdfs/sessionXX/`.
- When the text says “Figure 2 shows…,” display Figure 2, not the paragraph that refers to Figure 2.
- When discussing a finding, crop the actual result, quotation, treatment wording, table cell or figure panel that supports it.
- Highlight the relevant lines or cells. A full page with unreadable text is not evidence on a slide.
- Crop at semantic boundaries: never end halfway through a paragraph, quotation, figure, arrow, questionnaire item or experimental stage.
- Check every crop at full-slide size. Confirm that the intended text, labels and numbers can be read from the back of a seminar room.
- Prefer original historical documents and objects when the lecture discusses them. Use later scholarship to interpret and cite the history, not automatically as the on-screen proxy for the original material.
- Acquire and organize the focal published PDFs before drafting evidence slides. Temporary web previews should not enter the deck as placeholders.

## 6. Define terms before using them

- Expand acronyms such as CAPI, CASI, STT and TTS at first use and show what the participant or researcher actually experiences.
- Explain paper-specific labels such as “Dynamic Prober,” “Member Checker,” “copilot,” “richness,” or “palpability” before reporting results that use them.
- State what each experimental condition actually received. Do not assume the condition name explains the treatment.
- Define scales, distributions, pools, candidates, annotations and pretests before code or findings depend on them.
- Say who produced every judgment or annotation: participant, human coder, researcher, LLM, or programmatic rule.
- Separate computational designs that are easy for beginners to conflate. For example, asking a model for an aggregate distribution, asking it to answer for individual profiles, and asking it to return probabilities are three different tasks.
- Define “structured output” through the concrete response contract: field name, allowed value, Python type and one returned object.

## 7. Report designs and findings precisely

- State the sample, assignment, conditions, model, access route and relevant technical stack when these affect interpretation.
- Separate what was randomized from what was merely held constant.
- Say what the comparison identifies; do not add generic claims about random assignment that are not the point of the design.
- Report the direction and size or substantive form of the finding, not merely that “there was a difference.”
- Distinguish completion, fluency, participant experience, response quality, qualitative richness, validity and behavioral evidence.
- State important limits plainly: simulated respondent versus human participant, working paper versus published article, text versus voice, and benchmark versus field validation.

## 8. Write in the instructor's voice

- Read every title and caption aloud. Would the instructor plausibly say this sentence in class?
- Replace compressed abstractions and “Claudish” constructions with direct descriptions of who did what.
- Search for slogan-like contrasts, abstract noun clusters, unnecessary “not X but Y” formulas, and phrases such as “our route,” “the answer becomes input,” “trade external transfer,” “realized path,” or “not clerical tidying.”
- Avoid production notes in visible copy: “instructor synthesis,” “this slide shows,” or defensive explanations of how the deck was made.
- Remove captions that merely repeat the title or add a generic methodological warning without advancing the argument.
- Prefer enough ordinary language to a sparse one-sentence slide. Do not confuse brevity with clarity.
- Remove instructor-facing phrases such as “reason for using it here,” “role today,” “the direct bridge,” “this is the complete input,” and “this slide summarizes.” Make the substantive connection visible without narrating deck construction.

## 9. Check layout as communication

- Confirm no slide is blank.
- Do not use recurring course-stage maps or arrow sequences as default exposition. They flatten different methods into a generic workflow and quickly become visual filler. Use a concrete case, comparison, source object or worked example instead. Apply this repair whenever an earlier week is reopened.
- Give every table a visible closing bottom rule and cite its source or label it as a course synthesis.
- Preserve every image's aspect ratio. Never stretch photographs, paper pages or figures to fill a frame.
- Enlarge figures and quotations that students need to read. Do not surround crucial evidence with unused space.
- Check that citations are fully visible and do not run below the slide. Shorten repeated citations or move them below the full-width composition.
- Break overloaded slides into a sequence. Combine sparse slides when they do not each have a distinct teaching job.
- Vary layouts when it helps exposition, but do not use layout variety to hide a weak argument.
- Inspect the actual reading order of multi-column slides.
- Label every instructor-created plot, reconstruction or teaching distribution. State the source values and do not let a polished illustration resemble published empirical evidence.

## 10. Make technology and Python explicit for beginners

- Explain the complete pipeline before its pieces: for voice, microphone audio → speech-to-text → text model → text-to-speech → audible question.
- Explain what an API, routing service and local model each do, and state the input and output of every call.
- When discussing remote versus local models, cover privacy and retention as well as speed, hardware and maintenance.
- Before code, state the narrow research job and what the program does not do.
- Introduce the study, research question, source unit and relevant context before asking students to code or interpret an excerpt.
- State the exact material sent to the model and distinguish a model's context window from any memory system built around it.
- When the model proposes a theme or relationship, label it as a suggestion to check and show the source-checking and interpretive-review stages that follow.
- For every block, show the exact input value and type, the line being executed, the state before and after, the output and its research meaning.
- Trace one complete example through the code. Identify where annotations and dictionaries came from.
- Map the code onto the human method and identify what is lost, especially memory, iterative review, interpretation and relationship.
- State the exact model task before showing the call: aggregate estimation, one profile-conditioned answer, probability estimation, classification or free-text generation.
- If a live call is the intended classroom route, teach that route first. Keep cached or saved outputs as an operational fallback rather than making them the conceptual center of the example.

## 11. Final rendered checks

Run these in order:

1. title-only narrative review;
2. full-deck contact-sheet review;
3. full-size review of every paper, figure, table, quotation, code slide and citation;
4. aloud voice review of all visible prose;
5. source-to-slide comparison for every screenshot;
6. overflow and clipping check;
7. rerender after every meaningful repair;
8. final check of the affected slides and their immediate neighbours.

The reviewer must be able to answer “yes” to the following before delivery:

- Can a beginner tell what every slide is doing?
- Can a student identify where every important claim and criterion came from?
- Can every necessary screenshot, figure and citation be read?
- Are all named systems and conditions defined before their results appear?
- Does every sentence sound like the instructor rather than a generated summary?
- Does the code show exact inputs, outputs and provenance?

## Retrospective audit rule

When Sessions 1–5 are next opened, apply this complete checklist rather than limiting review to the requested local edit. Pay particular attention to citation format, published-versus-preprint images, unexplained paper-specific terminology, title-to-title transitions, sparse slides, stretched or incomplete screenshots, and code provenance. Sessions 7–14 must pass the checklist before instructor review.
