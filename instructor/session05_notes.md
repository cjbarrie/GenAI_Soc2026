# Instructor notes — Session 5: Constructing experimental treatments

## Intended endpoint

Students should leave able to say:

> A condition is a theoretical category, while a stimulus is one message or image used to represent it. We defined rights, economics, and family frames, produced several cached candidates, preserved their provenance, applied stated candidate-level checks, and compared the retained pools. The code records those decisions. It does not prove construct validity, and random assignment would not repair an ambiguous treatment.

They should also explain the focal Python block without live AI assistance:

`exact input and type → operation → exact output and type → sociological meaning → limit`

## Revision record — 27 August 2026

The final slide arc should be checked against these decisions before reuse:

- Open with recognisable experimental materials rather than the course-wide Observe/Intervene/Simulate sequence.
- State the subject plainly: LLMs can help produce candidate treatments and can also contribute to adaptive survey instruments.
- Introduce the sociology of vignettes, matched applications, confederates, and constructed interfaces before distinguishing fixed and adaptive designs.
- Put a standard citation directly under every paper screenshot; use the full citation on first appearance and author-year plus page or figure on later crops.
- When a screenshot supplies evidence, enlarge the relevant passage and highlight it. Never place explanatory text over the image.
- State the precise statistical comparison in results slides. For Bai et al., treatment-versus-control effects were significant, while direct LLM-versus-human differences were not.
- Introduce Velez as a substantive method in its own right. Then explicitly say that the hands-on example returns to a fixed message pool; do not imply that the exercise implements Velez.
- Before showing JSON fields or rules, state the exercise in one sentence: screen 12 candidates, preserve rejection reasons, and compare the retained pools.
- Introduce each annotation by meaning and purpose. Warmth appears because a systematic tone difference could confound a framing comparison.
- Start the Python section with the whole route in pseudocode. Then show exact inputs, the value and source of each field, the loop, checks, output lists, and pool summary.
- Place the answer immediately after an output-prediction slide.
- End by showing what the review produced and what decision follows. Do not list unrelated things the session was never intended to estimate.

## Provenance

The twelve candidate texts are cached course outputs created with an LLM and lightly edited by the instructor. The exercise file supplies review scores and flags so that students can concentrate on the screening procedure. Python calculates word counts from the displayed text. The rules are researcher choices. State the source and meaning of each field before screening the first message.

## 165-minute plan

### 9:30–9:42 — What can an experimental treatment look like?

- Open with four visible examples: a neighbourhood vignette, a matched application, a confederate performance, and the Music Lab interface.
- State that LLMs can write candidates, vary specified features, or help build an adaptive survey instrument.
- Introduce the three questions for the morning: what is the treatment, what else changes, and what must be saved and checked?

**Evidence of understanding:** students distinguish an existing research record from a researcher-produced treatment.

### 9:42–10:06 — What sociologists constructed before generated media

- Use the opening map to distinguish standardized partners, confederates, vignettes, audit testers, and artificial social systems.
- **Music Lab:** same forty-eight songs; separate markets; social-information display is part of the treatment.
- **Ridgeway and Erickson:** choices and arguments held constant; deferential or nondeferential performance varied; recorded behavior checked.
- Mention Piliavin's subway team briefly as a field comparison and ethical boundary.
- **Emerson et al.:** begin with the original article and its substantive segregation question, then explain the neighbourhood dimensions and judgment task. Wallander is the methods reading, not the source of the example.
- **Correll et al.:** show how matched application materials represent parenthood within a status-theory argument.

Do not teach a miniature history of each source. Each supplies one material construction problem.

**Evidence of understanding:** students can say what carried the treatment in each example.

### 10:06–10:31 — A condition is not one stimulus

- Define condition, candidate stimulus, retained pool, assignment, outcome, and claim.
- Introduce Bloemraad, Silva, and Voss's published framing experiment and show the exact rights, economics, and family contests printed in the article.
- Explain that each contest contains an argument and counterargument within one domain. The synthetic course candidates preserve those three domains but are not excerpts from the study.
- Compare one candidate from each frame.
- First mark the intended difference; then mark warmth, facts, implied beneficiaries, and other differences.
- Introduce Dafoe et al. through the unintended inferences students have already identified.
- Separate construction, validation, assignment, and estimation.

**Whole-room activity:** mark the intended wording in one pair, identify semantic differences that could act as causal confounds, and write one pretest question that could expose a competing inference.

### 10:31–10:41 — Break

Leave the three questions for the morning visible and briefly state which two have already been answered.

### 10:41–11:05 — What generation changes

- A generative model expands the candidate pool and the number of selection decisions.
- Generation and selection must appear separately in the record.
- **Bai et al.:** distinguish human, LLM, and human-selected LLM message conditions; explain pools and message differences.
- **Slater et al.:** ask which population of messages supports the intended generalization.
- **Schwitter:** show generation, selective editing, repair, and human pretesting of visual vignettes.
- **LinkedOut:** show the progression from a large image pool to validated profile images and the comparison of intended and nuisance perceptions.
- **Velez:** distinguish a fixed candidate pool from an adaptive question bank. Participant text is converted into structured items, filtered, and then prioritized by an adaptive algorithm while the survey is in the field. Be explicit that this is not yet a free-form conversational interview.

No provider or SDK comparison is needed. Mention model route and prompt version only as provenance fields.

### 11:05–11:28 — Review candidates by hand

Work through `rights_02` with the room, then ask students to diagnose one additional candidate. They must:

1. inspect the message and ratings;
2. list every failed rule;
3. decide whether it enters the retained pool;
4. preserve the rejected record and reasons; and
5. state what the decision does not establish.

Then compare the retained pools. Reveal that the family pool remains warmer and the economics pool remains more factually dense than the others.

**Required wording:** passing candidate-level rules does not make two condition-level pools comparable.

### 11:28–11:58 — Python repeats the hand review

#### One dictionary

Display candidate `rights_02`. Ask students to identify every value, type, and source. Explain that the text and mock annotations come from the JSON file; Python calculates the word count; the dictionary is one candidate, not the condition or the stimulus pool.

#### List and rules

- A list contains candidate dictionaries.
- A second dictionary contains researcher-chosen rules.
- Ask who selected each threshold and what evidence would justify it.

#### Function trace

1. Read `review_candidates(candidates, rules)` as two exact inputs.
2. Predict the two output types before the body.
3. Initialize `accepted` and `rejected` as empty lists.
4. Select the first candidate in the loop.
5. Start a new `reasons` list for that candidate.
6. Trace each independent `if` statement.
7. Show `rights_02` failing both word-count and unsupported-claim checks.
8. Explain why an `if/elif` chain would hide the second reason.
9. Append either the rejected record or the original candidate.
10. Return two lists.
11. Run `summarize_pools` and interpret the warning.

Pause for prediction and whole-room explanation after steps 2, 5, 7, and 10. No uninterrupted instructor explanation should exceed eight minutes.

### 11:58–12:08 — Completion task and oral rehearsal

Students first predict the output individually. Ask the room to trace `econ_B`, explain the two `.append()` lines, and state one methodological limit. The submitted task remains individual and completion-marked.

### 12:08–12:15 — Close and transition

Return to the opening question. Ask students to separate:

- theoretical condition;
- material stimulus;
- retained pool;
- participant assignment;
- outcome; and
- warranted claim.

Preview Session 6: when the model responds to a participant, the exposure is no longer one fixed message and may diverge across conversations.

## Beginner-code narration

For every code slide ask:

1. What is the exact input value?
2. What Python type is it?
3. What operation happens?
4. What is the exact output value and type?
5. What does it mean for the research question?
6. What does it not establish?

Likely sticking points:

- `[]` creates a list; `candidates[0]` retrieves by position; `candidate["text"]` retrieves by key.
- `reasons = []` creates a new list for each candidate.
- Separate `if` statements allow one candidate to fail several rules.
- `.append()` changes an existing list by adding one item.
- `if reasons:` asks whether the list contains anything.
- `return accepted, rejected` returns a tuple containing two lists.
- A passing `assert` confirms a coded expectation, not construct validity.

## Completion standard

Completion requires:

- an output prediction made before execution;
- both missing lines completed;
- supplied checks passing;
- one candidate traced in ordinary language;
- 100–150 words linked to Emerson et al., Wallander, Dafoe et al., Bloemraad et al., or Bai et al.;
- one explicit inferential limit; and
- AI-use disclosure if applicable.

Syntax elegance is irrelevant. If the environment fails, use the rendered notebook and trace the supplied output by hand.
