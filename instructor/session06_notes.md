# Instructor notes — Session 6: AI-assisted and AI-led interviewing

## Intended endpoint

Students should reject “Is AI a good interviewer?” as underspecified. They should identify the interview purpose, allowable discretion, social relationship, realized path and relevant validation evidence, then explain `audit_interview` line by line.

## 165-minute plan

- **9:30–9:40:** opening interviews and criteria.
- **9:40–10:10:** life histories, focused interviews and standardization.
- **10:10–10:35:** repair, Oakley/Bourdieu and claim–evidence fit.
- **10:35–10:45:** claim–evidence fit versus mode effects; CAPI/CASI/audio-CASI and what predates LLMs.
- **10:45–10:55:** break.
- **10:55–11:15:** system types, access routes, privacy and local/remote trade-offs.
- **11:15–11:40:** current evaluations of text, voice and model variation.
- **11:40–11:50:** return to the opening and compare the two seminar interviews.
- **11:50–12:10:** generate and record one adaptive probe; voice pipeline; slow Python trace and completion branch.
- **12:10–12:15:** source record and close.

## Arc checks

- Each historical source adds a criterion reused after the break.
- Name the research purpose before judging a probe.
- Separate pre-LLM automation from generated follow-up.
- For every paper state the question, comparison and remaining uncertainty.
- Return to the opening interviews before the final checklist.
- When returning to an example after many slides, reproduce the relevant exchange instead of relying on memory.
- When showing voice, distinguish speech-to-text, the text interviewer and text-to-speech. Hold the question and delivery instruction fixed when comparing voice types.
- A paper slide must state the study design before presenting what it suggests. Use the published article and show the relevant finding at a readable scale.
- Prefer direct methodological language. Delete captions that merely restate a diagram or use paired abstractions such as “the transcript shows / the record shows.”

## Python language

Use **input and type → current line → state before and after → research meaning**. The worked example must first generate one adaptive probe, then append it to the interview record. A list preserves order; one dictionary is one turn; `enumerate(..., start=1)` yields a turn number and dictionary; `source` comes from the decision log; `topic` is researcher annotation; `.append()` preserves the probe and link; `return` produces a path record, not a quality score.

## Oral assessment

Ask students to explain a turn dictionary, `enumerate`, `source` versus `topic`, what changes on an adaptive probe, and why a passing assertion cannot validate an interview.

The required exercise sends a cached synthetic exchange through OpenRouter, then records and audits the generated probe. Keep the cached completed paths as a fallback if the API is unavailable. The optional instructor-led voice comparison needs a separate compatible speech service or local TTS; students do not need a second key. It uses no research data: play the same question and delivery instruction using several voices, then record the class's judgments about authority, intimacy, pressure and intelligibility.

## Repairs to carry forward

- The bridge from Jerolmack and Khan to CAPI/CASI must explicitly distinguish two questions: what an interview account can support, and how administration mode shapes the account.
- For Liu et al., use the published PACM HCI article, identify the 16-person interview study, and show the reported interest in follow-up support. Do not compress study design, findings, cautions and interpretation into one crowded slide.
- Quote participant reactions exactly when they matter. Do not add explanations about quotation length or mix paraphrase and quotation in a way the audience cannot follow.
- If the lecture returns to its opening comparison, show the two exchanges again.
- State the research aim, fixed opener and probing rule before the worked example.
- A coding task about adaptive interviewing should actually generate an adaptive probe, show its exact output, append it to the record and explain each input and output.
- Keep voice comparison inside the Python walkthrough. A standalone demo-app slide is unnecessary unless an app has actually been built.
