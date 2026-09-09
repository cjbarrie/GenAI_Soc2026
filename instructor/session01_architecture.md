# Session 1 rebuild architecture — from a model call to a research claim

## Communication job

By the end of the session, beginning graduate sociology students should be able to describe one LLM-assisted research operation from input to saved output, distinguish the model output from the research claim, and explain why reporting, reproducibility and validity require different evidence.

## Central argument

An LLM call is easy to run. A social-scientific result requires the researcher to specify what the model was asked to do, preserve what went in and came out, check how the result changes, and justify the claim made from it.

The lecture should not begin with an abstract framework and then add examples. It should begin with one inspectable classification task, follow the objects through a model call, and let the literature explain why the resulting output is not yet a finding.

## Problems in the current deck

1. The deck alternates between course orientation, the sociology of science, reproducibility, reporting and Python without making one question generate the next.
2. The current code-progression slide promises inputs, outputs and types but does not show them. The concrete objects arrive much later.
3. Hao et al. and Messeri and Crockett appear as isolated warnings rather than answers to a question about scientific production and knowledge.
4. The six application domains are useful as a course map, but six consecutive near-identical slides interrupt the opening argument.
5. The “five decisions” and “seven questions” are presented as free-standing methodological claims. Their relationship to the cited literature is not visible.
6. The move into replication is not announced through a research problem. Accuracy, repetition terminology and the Barrie–Palmer–Spirling typology therefore feel like a second lecture.
7. GUIDE-LLM is described but not used. Students do not see what a completed reporting record would look like for the example already on screen.
8. The model-access section is definition-heavy and visually abstract. It does not show what ChatGPT, a terminal program, OpenRouter and a local Ollama service actually look like.
9. The current model-call overview implies that only four components matter and then introduces many additional objects without revising the overview.
10. The code sequence teaches Python types and SDK syntax as separate topics. `build_research_record` then appears without its definition, with variables whose provenance is unclear.
11. Several paper images are technically present but too small because their source pages contain large margins and the layouts give evidence less space than commentary.
12. The final title restates a slogan rather than resolving the opening example in concrete terms.

## Revised narrative arc

### Part 1 — Begin with one small research operation

1. Course question: when can an LLM output contribute to a sociological claim?
2. Opening discussion about current AI use and what students may stop learning when the operation becomes invisible.
3. Course AI policy: permitted with responsibility, disclosure and oral explanation.
4. Show the source text used throughout the morning: “You can never be too careful when dealing with people.”
5. Show a beginner Python trace immediately:
   - input value: the quotation;
   - input type: `str`;
   - operation: store it under `source_text` and inspect it;
   - output: the printed string and `<class 'str'>`;
   - research meaning: this is the material to be classified, not yet a trust score.
6. Show the model task and returned object: classify the text on a stated 0–2 trust scale and return a structured object such as `{"trust_score": 0}`.
7. Put four possible claims beside the same output:
   - “The model returned 0 for this text.”
   - “The text expresses low generalized trust.”
   - “The model measures generalized trust accurately.”
   - “People represented by these texts differ in social trust.”
   Ask what additional evidence each claim requires.

This resolves the current discontinuity between the coding promise and the model-output/research-claim slide. Students meet the exact object before any methodological framework.

### Part 2 — Explain why this distinction matters for science

8. Introduce Alvero et al. as a survey of 433 sociology authors: GenAI use is already common enough to matter, but trust in its outputs is low and most use is still concentrated in writing assistance.
9. Introduce Davidson and Karell as the sociology-first map: measurement, prompting and simulation place LLMs in different parts of the research process and therefore create different validation problems.
10. Condense the six course domains into two visually varied slides rather than six repeated domain slides. Each domain should contain one concrete example and the week in which it returns.
11. Ask what happens when easier production becomes a norm of scientific work.
12. Introduce Hao et al. properly: material, design, comparison and the associational character of the result. Use one actual published figure or result crop, not only three numbers.
13. Introduce Messeri and Crockett as the conceptual interpretation of that broader problem, not as an unrelated caution. Explain their taxonomy of AI visions and their claim about illusions of understanding and scientific monocultures with an actual figure or focused passage.
14. Return to the opening output: producing the score was fast; deciding what it measures and what claim it supports remains the research work.

The order matters. Alvero establishes actual disciplinary uptake; Davidson and Karell map research uses; Hao shows a production/focus pattern; Messeri and Crockett name the epistemic risk. No paper appears merely to provide a warning.

### Part 3 — Shift explicitly from one plausible output to repetition

15. Run the same trust-classification task again or change one innocuous-looking prompt phrase. Show the two actual returned objects.
16. Ask a new question plainly: if the answer changes, what exactly would it mean to repeat this result?
17. Introduce Barrie, Palmer and Spirling as a paper about this question. Give the full citation, rolling iterated replication design, tasks, repeated runs, time span, model/crowd comparison and principal result before presenting the typology.
18. Use the published typology at readable size and explain only the cells needed for language-model research.
19. Show a real empirical stability result from the paper. Replace the invented `.90 / ?` slide with a figure or table that reports both accuracy and variation.
20. Show the downstream-consequences result at large size and explain what outcome changes when the labels change.
21. Present the recommendation for locally versioned open models as one response to version instability, while stating the remaining hardware, environment and maintenance requirements.

The replication section should be a worked paper sequence: question → design → result → downstream consequence → practical response. “Accuracy and replicability are different” becomes a conclusion from evidence rather than an isolated comparison band.

### Part 4 — Turn reporting into a completed research record

22. Ask what another researcher would need in order to inspect or repeat the opening trust-classification example.
23. Introduce GUIDE-LLM as a consensus-based reporting checklist for behavioural science, with its complete citation and a readable crop of the actual checklist.
24. Map the focal example onto the checklist:
   - A.1 role: text classification for a teaching example;
   - A.2 oversight: human review of the scale and output;
   - B.1–B.3 model, provider, access date and generation settings;
   - C.1–C.2 exact user and system prompts;
   - E.1–E.2 human validation and post-processing;
   - F.1 shared call code.
25. Show a mocked-up completed checklist for the exact call rather than another generic list of things to save. Mark it visibly as a course example based on GUIDE-LLM.
26. Compare three questions, each attached to its source and an example:
   - **Reporting:** can another researcher see what was done? — GUIDE-LLM.
   - **Reproducibility:** what survives a justified repetition? — Barrie, Palmer and Spirling.
   - **Validity:** does the operation support the intended measurement or substantive claim? — Davidson and Karell, with Messeri and Crockett as the wider epistemic caution.

The current “five decisions,” “what should we save,” “three separate questions,” “none can stand in for the others,” and “seven questions” slides should be consolidated into this source-anchored sequence.

## Literature-derived workflow to replace the unsourced five decisions

The deck may use five stages as a course organization, but it must label them as a synthesis and show the source behind each stage.

| Course stage | Visible question | Literature anchor |
|---|---|---|
| Research role and claim | What is the model doing in this study, and what claim will use its output? | Davidson and Karell (2025); GUIDE-LLM A.1–A.2 |
| Input and instruction | What material, system instruction and user prompt enter the call? | GUIDE-LLM C.1–C.2 |
| Model and access | Which model/version, provider, route, date, state and settings produced the response? | GUIDE-LLM B.1–B.5 |
| Output and checking | What raw output was returned, how was it parsed, and who checked it against what? | GUIDE-LLM E.1–E.2; Davidson and Karell (2025) |
| Preservation and repetition | What code and records are retained, and what changes under reruns, prompt variation or model updates? | GUIDE-LLM F.1; Barrie, Palmer and Spirling (2025) |

This is preferable to claiming that the literature contains one canonical five-stage procedure. Each stage is traceable, and students can see where the synthesis came from.

## Part 5 — Explain model access through things students can see

27. Show ChatGPT first because students recognize it. Identify what the interface hides or manages for them: conversation state, model access, credentials, request formatting, output display and sometimes tools.
28. Show a real terminal prompt running a small Python file. Contrast clicking “send” in a chat window with executing a program that constructs and saves a request.
29. Show a real OpenRouter model page or terminal/API response and explain the router in one sentence: the notebook contacts one service, which forwards the request to the selected hosted model provider.
30. Show a real Ollama terminal example: model list, local server and one request. Explain that the same client/request idea can point to a service on the student's computer.
31. Expand the call overview into the complete beginner pipeline:

`Python values → messages and settings → SDK client → API request → router/provider or local service → model → response object → extraction/parsing → saved research record`

32. Visually distinguish the pieces students choose from those handled by software. State that tools, retrieval, structured-output schemas, safety systems, provider routing, conversation state and post-processing may also be involved. Do not imply that every call contains only four relevant decisions.

The CLI should be a genuine HTML/CSS terminal composition using the actual commands and outputs from the course example. A restrained blinking cursor or Reveal fragment sequence can make the request and response appear in order. It should not be a decorative stock animation.

## Part 6 — Rebuild the Python walkthrough around one object moving through the call

### What Week 1 teaches

Week 1 teaches enough Python to inspect a model call:

- variables as names attached to values;
- `str`, `int`, `float`, `bool` and `None`;
- one dictionary with named fields;
- one ordered list of message dictionaries;
- importing a package;
- creating a client object;
- calling a method with named arguments;
- retrieving a value from a returned object;
- inspecting `type()` and printing values;
- saving a transparent record.

Week 1 does not need loops, a user-defined function, exception handling, asynchronous calls, token-generation theory or a survey of every model parameter. Model name, temperature, output limit and structured-output schema are introduced because they alter or document the research operation, not as a general parameter lecture.

### Concrete walkthrough

33. Begin with `source_text`, print its value and type, and show the exact output.
34. Define `task_instruction` and a small `scale` dictionary. Explain which part comes from the researcher and which part comes from the source material.
35. Build `user_message`; show the dictionary before and after creation.
36. Build `messages`; retrieve `messages[0]`; show why order matters.
37. Import the SDK and read the key from the environment. Show the terminal setup separately and never display a real key.
38. Create the client. State that no request has yet left the computer.
39. Show the full request with only the settings used in the example. Use color or highlighting to connect each Python value to the pipeline overview.
40. Animate or reveal the terminal command, waiting state and returned response.
41. Inspect the full response object before extracting the generated content.
42. Use a structured-output schema for `trust_score` and, if included, a short `reason`. Define every field and allowed type before showing the call syntax.
43. Print the parsed value and its type. Contrast the integer `0` with the string `"0"` returned by an unconstrained text call.
44. Build the research-record dictionary explicitly on screen:

```python
record = {
    "source_text": source_text,
    "task_instruction": task_instruction,
    "model": MODEL_NAME,
    "access_route": "OpenRouter",
    "settings": settings,
    "raw_response": raw_response,
    "trust_score": trust_score,
    "validation": None,
}
```

45. Print one field and then the complete record. Explain that `validation = None` means no validation has yet been recorded.
46. Only after students understand the explicit dictionary should a later workbook extension wrap this construction in `build_research_record(...)`. The function should not be the main Week 1 slide example.
47. Run the call a second time or change one prompt element and add the second record to a list. Use this to reconnect code with the earlier reproducibility question.
48. End with a completed GUIDE-LLM row set and one bounded statement: what the saved record establishes and what it still does not establish about generalized trust.

Every code slide must show: exact input value and type → current operation → exact output value and type → research meaning → what remains unchecked.

## Recommendations keyed to the instructor's current-slide notes

- **Current “We will learn the code…”:** replace the abstract six-step strip with the concrete `source_text` trace.
- **Current readings/model-output transition:** replace the paper triptych with a question-led reading map and move the concrete model output before the papers.
- **Hao and Messeri–Crockett:** introduce them after disciplinary uptake and the research-use map. Give each paper its material, question, evidence and job.
- **Current juxtaposition slide:** remove the “Producing text is easier…” slogan and use the four escalating claims from the same trust score.
- **Six domains:** retain as the broader course arc but condense to two slides with examples and week numbers.
- **Five decisions:** replace with the literature-derived workflow above.
- **Replication transition:** generate a second output first, ask what repetition means, then introduce Barrie, Palmer and Spirling.
- **Sparse repetition slides:** replace invented numbers and repeated maxims with the paper's actual design, empirical stability result and downstream result.
- **Hosted/local slide:** move it to the practical response after model/version instability and later revisit it in the access-route demonstration.
- **What should we save:** replace with a completed GUIDE-LLM example using the exact trust-classification call.
- **Seven questions:** remove as a separate unsourced list. Use the three sourced standards and the five-stage workflow.
- **Python transition:** explicitly say that the class is about to reconstruct the opening call as Python objects.
- **Model-call components:** replace the four-item definition stack with the complete pipeline and then define each component as it appears.
- **Access routes:** use real interface and terminal views, showing how ChatGPT differs from a script, how OpenRouter routes, and how Ollama runs locally.
- **Code section:** remove the hidden `build_research_record` abstraction from the main lecture; construct and print the record dictionary visibly.
- **Final slide:** replace the abstract title with a direct answer to the opening example, such as “We can report what the model returned; we cannot yet claim that it measures social trust.”

## Visual and source-image repair

1. Render a contact sheet and classify every paper image as title page, argument passage, method, result or checklist. Images with no clear evidentiary job should be replaced or removed.
2. Re-crop every retained page at the content boundary rather than displaying page margins.
3. Use approximately 55–70% of the slide for evidence students must read. Commentary should identify the evidence rather than compete with it.
4. Use a full-width or two-slide sequence for the Barrie–Palmer–Spirling typology and downstream figure if labels are not legible in a split layout.
5. Use one actual empirical figure from Hao et al. and one actual taxonomy/argument figure or highlighted passage from Messeri and Crockett.
6. Show the actual GUIDE-LLM checklist, then a separate filled course example. Do not shrink the full checklist to fit beside prose.
7. Use consistent thin borders and neutral backgrounds for paper crops. Preserve aspect ratios and avoid fixed-height rules that leave the meaningful content small.
8. Inspect every figure and quotation at full-slide size after rendering, not only through the HTML source or a contact sheet.

## Source files needed before implementation

Already obtainable without instructor action:

- Barrie, Palmer and Spirling (2025), current manuscript PDF.
- Alvero et al. (2026), open-access published PDF.
- GUIDE-LLM web checklist and downloadable checklist materials.

Please supply the following version-of-record PDFs if they are not already under an unrecognized filename in `Downloads`:

1. Hao et al. (2026), “Artificial intelligence tools expand scientists’ impact but contract science’s focus,” *Nature*, DOI `10.1038/s41586-025-09922-y`.
2. Messeri and Crockett (2024), “Artificial intelligence and illusions of understanding in scientific research,” *Nature*, DOI `10.1038/s41586-024-07146-0`.
3. Feuerriegel et al. (2026), “A reporting checklist for large language models in behavioural science,” *Nature Human Behaviour*, DOI `10.1038/s41562-026-02492-7`, if the published PDF contains a figure or layout preferable to the downloadable checklist.
4. Davidson and Karell (2025), “Integrating Generative Artificial Intelligence into Social Science Research: Measurement, Prompting, and Simulation,” *Sociological Methods & Research*, DOI `10.1177/00491241251339184`, if we want a readable source passage or figure rather than a title citation only.

Store supplied files in `literature/source_pdfs/session01/`. Do not use publisher previews or login screens as substitutes.

## Pre-build checks

- Read the revised title sequence aloud and explain why each slide follows the previous one.
- Confirm that every framework row has a visible literature source.
- Confirm the exact OpenRouter SDK syntax and structured-output support against current official documentation before writing code.
- Run the complete example and save the actual terminal output used in the deck.
- Mark any course-created checklist or output visibly as a teaching example.
- Render and inspect all paper crops, terminal compositions, code/output slides and citations at full size.
- Remove visible production language, abstract bridge announcements and repeated “not X but Y” constructions.
- Check the revised deck against `docs/SLIDE_REVIEW_CHECKLIST.md` before instructor review.
