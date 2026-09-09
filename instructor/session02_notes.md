# Instructor notes — Session 2: Annotation, measurement, and LLMs

## Intended endpoint

Students should be able to explain how a sociological construct becomes a codebook, how humans or an LLM apply it to text, and why remaining errors matter for the quantity a study reports. They should also be able to narrate the Python workflow as `input and type → operation → output and type → research meaning`.

## 165-minute run of class

| Time | Section | Main teaching move | Evidence of understanding |
|---|---|---|---|
| 9:30–9:47 | Begin with one comment | Compare explicit support for the proposal with general openness to more housing. | Students explain why the research question changes the label. |
| 9:47–10:08 | What came before | Move from Franzosi and codebooks to human coding teams, MTurk/Prolific, and supervised classifiers. | Students identify what remains constant: construct, unit, categories, rules, and reference decisions. |
| 10:08–10:23 | The LLM annotation task | Show the exact codebook + comment input and the structured label output. Introduce the twelve-comment synthetic corpus. | Students can name the input, requested output, and intended use of the label. |
| 10:23–10:38 | Two errors, one changed estimate | Inspect the two conditional false positives and compare 4/12 with 6/12. | Students explain why the support rate rises. |
| 10:38–10:48 | Break | Leave the unresolved question on screen: what evidence would make the measure credible? | — |
| 10:48–11:10 | Stuhler and promptbooks | Use the published information-extraction figure, Table 2, and model-size comparison. Return each result to the rezoning rule. | Students distinguish substantive coding instructions from model-facing input/output instructions. |
| 11:10–11:30 | Prompt stability | Compare reasonable prompt versions on the two difficult comments; introduce intra- and inter-prompt stability and selected PSS results. | Students explain why stability is useful and why stable output can still be wrong. |
| 11:30–11:43 | Downstream consequences | Use Egami et al. to connect independently sampled expert labels to the final estimate and uncertainty. | Students distinguish record-level agreement from validity of the reported estimate. |
| 11:43–12:07 | One Python workflow | Begin with the whole pseudocode flow, then trace the same record through prompt construction, model response, parsing, storage, looping, comparison, counts, and rates. | Students predict values and types and explain the first loop iteration. |
| 12:07–12:13 | Completion/oral rehearsal | Complete a small missing operation and explain it without saying only “the data” or “the model.” | Each student names exact inputs, outputs, and research meaning. |
| 12:13–12:15 | Bounded conclusion | Revisit the opening comment and the 33%/50% comparison. | One defensible claim plus one necessary next check. |

## Discussion prompts

1. What exactly does `SUPPORT` mean in this study?
2. What changed when coding moved from a research team to a crowd platform?
3. What changes—and what does not—when the written rules are applied by an LLM?
4. Which two comments produce the error, and what do they share?
5. What can prompt stability establish? What can it not establish?
6. Why can 10/12 agreement still be inadequate for the study's main quantity?

## Code walkthrough language

For every focal block ask:

1. What exact value enters?
2. What is its Python type?
3. What operation occurs?
4. What exact value comes out?
5. What is the output's type?
6. What does it mean for the research claim?

The walkthrough must retain the same variable names and records. Do not introduce a fresh example to teach parsing, lists, dictionaries, loops, or Booleans.

## Likely sticking points

- A label is an implementation of a prior construct decision.
- A dictionary stores named fields; it does not validate their contents.
- JSON parsing changes a string into a Python object; it does not change whether the label is correct.
- `=` assigns a value; `==` performs a comparison and returns a Boolean.
- The loop repeats the same operation on each record and appends each result to one list.
- Stability, reference agreement, and downstream validity answer different questions.
- The reference labels are independently produced comparison labels for this exercise, not unquestionable truth.

## Completion decision

Completion requires a prediction before execution, the short code task, a plain-language explanation of one operation, an interpretation of the conditional false positives, a bounded substantive claim, and an AI-use disclosure where applicable. Code elegance is not graded.

## Contingencies

- **No key or network:** use the cached response; its structure matches the live response used in the walkthrough.
- **Mixed Python experience:** ask the less experienced student to explain the first iteration before a partner adds detail.
- **Short on time:** keep the one-record trace and support-rate calculation; treat the supplied prompt-variation helper as read-only.
- **Extra time:** add a new boundary case and ask students to predict which prompt formulation will be least stable.

## Source notes

- Franzosi (1998), “Narrative Analysis—Or Why (and How) Sociologists Should be Interested in Narrative,” *Annual Review of Sociology*.
- Stuhler, Dang Ton, and Ollion (2025), “From Codebooks to Promptbooks,” *Sociological Methods & Research*.
- Barrie, Palaiologou, and Törnberg (2024), “Prompt Stability Scoring for Text Annotation with Large Language Models.”
- Egami, Hinck, Stewart, and Wei (2026), “Using Large Language Model Annotations for the Social Sciences.”
- Wazny (2020), “Applications of Crowdsourcing in Health,” for the broader social-science crowd-work context; MTurk and Prolific platform materials are credited on the slide.
- All rezoning comments, cached outputs, prompt-variant labels, and reference labels are instructor-authored synthetic course material.
