# Instructor Notes — Session 2: Annotation and Measurement

## Session purpose

Students should leave able to explain why fast, structured output is not yet a valid measurement. The conceptual hinge is the shift from “How accurate is the model?” to “Which errors matter for the inference I want to make?” The computational hinge is seeing every object before and after transformation.

## 165-minute run of class

| Time | Activity | Instructor move | Evidence of understanding |
|---|---|---|---|
| 9:30–9:42 | Retrieval and opening case | Ask students whether 10 correct labels out of 12 sounds adequate before revealing the support-rate bias | Students state an initial criterion and can revise it later |
| 9:42–10:05 | Classification, extraction, measurement, inference | Keep the four nouns distinct; use one student’s annotation problem to test each | Student can name the unit, construct, and downstream use |
| 10:05–10:28 | Stuhler et al. | Rebuild the codebook → promptbook move; compare age, military service, and education | Student explains why task properties change which method is attractive |
| 10:28–10:38 | Chae and Davidson | Contrast model size with training regime and cost | Student can give one case favoring a smaller fine-tuned model |
| 10:38–10:48 | Break | Keep the conditional-comment slide visible | — |
| 10:48–11:00 | Code orientation | Show file paths, cached/live distinction, and research record | Student identifies which objects are strings, lists, and dictionaries |
| 11:00–11:28 | Worked notebook | Pause after load, prompt construction, raw output, merge, counts, and metrics; ask for predictions before running | Students predict types and important values |
| 11:28–11:50 | Paired completion task | Students write the four-way conditional and metric function without copying the solution | Each pair explains one branch aloud |
| 11:50–12:05 | Error audit | Locate the two false positives and ask why they are sociologically similar | Students identify conditionality as patterned error and connect it to inflated support |
| 12:05–12:15 | Exit record | Claim → target → evidence → failure mode → revised claim | One bounded inference statement per student |

## Reading discussion prompts

1. Does a promptbook merely document a measure, or does writing it also change the construct?
2. Stuhler et al. report that a simple age-extraction rule approaches generative-model accuracy. When is an LLM methodological overkill?
3. Chae and Davidson find that large prompted models often perform best, while smaller fine-tuned models can be competitive and cheaper. What counts as the relevant cost for a graduate researcher?
4. If the expert reconciler and the model disagree, what evidence could establish which is better?
5. If false positives cluster among conditional or marginalized speakers, which downstream estimands become unreliable?

## Code walkthrough script

For every focal cell, ask these questions in order:

1. What is the input value?
2. What is its Python type?
3. What operation is applied?
4. What object comes out?
5. What would count as evidence that the result is wrong?

Do not run more than two new cells without a prediction or explanation from a student. When a student uses “the data” or “the model” vaguely, ask them to point to the exact variable.

## Likely sticking points

- **Sentiment versus stance:** liking affordable housing is not the same as supporting this proposal.
- **Positive class:** precision and recall require declaring which label counts as positive.
- **`and` branches:** students may not see why the four branches are mutually exclusive and exhaustive.
- **False positive:** use the human label as the reference for this exercise; do not imply it is metaphysically true.
- **Accuracy:** 10/12 correct is 83%, but the model estimates 6/12 support instead of 4/12.
- **Cached output:** emphasize that it is instructor-authored for stable teaching, not evidence about a named model.
- **Temperature zero:** it reduces a source of variation but does not guarantee longitudinal or provider-level reproducibility.

## Oral-assessment bridge

Tell students that the later oral walkthrough will look like today’s paired explanation. A student should be able to say, for example: “This comparison produces a Boolean; the `elif` runs only when the human reference is not support but the model output is support; then the false-positive counter increases by one.” Technical jargon beyond that is unnecessary.

## Contingencies

- **No network:** use the cached JSON; all required work remains available.
- **OpenRouter rate limit or key failure:** demonstrate the request object without sending it.
- **Mixed Python experience:** pair students by self-reported comfort, but require the less experienced student to explain the branch logic.
- **Task runs long:** calculate precision together; leave recall/F1 as the completion submission.
- **Task runs short:** compare errors by `speaker_role` or run the optional local-model schema mapping.

## Completion decision

Mark complete only when the submission includes:

1. a prediction made before the task code is run;
2. working outcome and metric functions;
3. passing checks plus an interpretation of the two false positives;
4. a 100–150 word note connecting the observed error to Stuhler et al., Chae and Davidson, or chapter §10.2.

Return incomplete work with the missing element named; students have one week to supply it.

## Source and version notes

- Chapter: Barrie, Argyle, Bisbee et al., “AI and Research Methods,” chapter proof dated August 3, 2026, §§10.2.1–10.2.5.
- Stuhler, Dang Ton, and Ollion: published 2025 version, DOI 10.1177/00491241251336794. The accessible March 2025 manuscript reports the selected task comparisons used in the deck.
- Chae and Davidson: volume 55, issue 2 (2026), pp. 501–567, DOI 10.1177/00491241251325243; first published online April 24, 2025.
- OpenRouter SDK syntax checked against the official Python SDK documentation on August 18, 2026.
- The rezoning comments, reference labels, and cached model output are synthetic course materials, not research findings.

