# Session 2 architecture — Annotation, measurement, and LLMs

**Status:** implemented revision after instructor review, August 26, 2026.

## Communication job

Beginning graduate sociology students should leave able to explain how a passage of text becomes a labelled variable, what changes when an LLM applies the coding rules, and why classification performance alone does not justify the later sociological claim.

The class stays with one synthetic task: label twelve public comments for explicit support for a rezoning proposal. Every historical reference, paper, figure, and Python object returns to that task.

## Narrative arc

1. **Begin with the sociological decision.** One conditional comment can be `SUPPORT`, `OPPOSE`, or `UNCLEAR` depending on the research question and boundary rule.
2. **Show what came before.** Franzosi anchors rule-based text coding in sociology; codebooks and teams of human coders precede distributed crowd work on MTurk and Prolific; supervised classifiers then learn from those human labels.
3. **Introduce the LLM use case precisely.** The model receives a codebook plus one comment and returns a small structured record. The model changes who applies the rule, not the need to define the construct, unit, categories, and boundary cases.
4. **Use the toy data to establish the stakes.** Two conditional false positives move the estimated support rate from 33% to 50%.
5. **Use the literature to diagnose the problem.** Stuhler et al. clarify the move from codebook to promptbook and show task differences; Barrie et al. motivate prompt-variation checks; Egami et al. show why prediction error must be followed into the downstream estimate.
6. **Rebuild the workflow in Python.** Students see the entire process in plain language before examining each object: source record, codebook, prompt, messages, model response, parsed dictionary, annotation record, dataset, comparison, counts, and rates.
7. **Return to the opening claim.** The class replaces “half support the proposal” with a bounded statement about the synthetic model labels and names the additional evidence needed for a population claim.

## What has been removed

- The recurring `Observe → Intervene → Simulate` course map.
- Arrow-sequence layouts used as generic exposition.
- A disconnected series of prompt, parsing, caching, and dictionary examples.
- The claim that parsing or a dictionary validates a label.
- Model-influence papers as a detour in the main argument; they now appear only as further reading.

This is also a course-wide decision: when earlier weeks are reopened, replace recurring stage maps with a direct statement of that session's question and its connection to the preceding class.

## Evidence and visual rules

- Every paper introduction identifies the paper, question, evidence, and reason it is being shown.
- Published Stuhler pages and figures are used, tightly cropped to readable content.
- Franzosi supplies the sociology-specific prehistory rather than a generic history of NLP.
- MTurk and Prolific are shown as actual work interfaces, with platform and image credits.
- Paper figures are enlarged or selectively cropped when a full-page screenshot would be unreadable.
- Citation lines use a consistent author–year–title–venue form on paper-introduction slides and author–year–figure/table form on figure slides.
- Tables are visually closed with a bottom rule.

## Python teaching contract

The code is one continuous workflow, not a collection of snippets. Before each operation, students identify:

1. the exact input value;
2. its Python type;
3. the operation;
4. the exact output value;
5. the output type; and
6. what the output means for the research.

The overview comes first. Each later slide advances the same record by one operation. The live OpenRouter call is optional; a cached response with the same structure preserves the walkthrough without a key or network connection. Students are expected to explain the code orally, but not to implement the SDK, JSON parser, or stability statistic from scratch.

## Self-checks for this and future weeks

- Can a student state the substantive question before seeing a paper or code block?
- Does each historical step explain a real change in research practice?
- Is every construct, rule, label, comment, and output visible in a concrete example?
- Does each paper earn its place by resolving a question already raised?
- Does the next slide follow from a question or result on the current slide?
- Can every screenshot be read at projected size, without dead space or clipped text?
- Can a beginner explain how the Python objects connect from start to finish?
- Is every methodological claim anchored in cited literature rather than an instructor-created list presented as fact?
- Has decorative, compressed, or recognizably AI-like language been replaced by direct explanation?
