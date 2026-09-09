# Session 5 architecture — Can generated media isolate a causal construct?

**Status:** Rebuilt and implemented on 2026-08-24 after instructor review. The rendered deck, workbook, data provenance, solution helper, tests, syllabus entry, reading guide, and instructor notes are aligned. Final instructor visual review remains.

## Communication job

By the end, **graduate sociology students with beginner-to-middling Python experience** should **be able to explain and audit how generated messages become experimental treatments** because **a model output is one candidate realization of a construct, while a causal comparison depends on definition, selection, validation, assignment, and generalization**.

## Substantive research question and intended endpoint

The class asks:

> How do rights, economics, and family framing contests change support for immigrant legal status?

Students are not estimating a real treatment effect. They are constructing and reviewing the material that would have to exist before such an experiment could be fielded.

At the end, a student should be able to say:

> We began with three theoretical frames, produced several candidate messages for each, preserved their provenance, applied predeclared candidate-level checks, and compared the retained pools. The code records those decisions. It does not prove construct validity, and random assignment would not repair a treatment whose messages differ in unintended ways.

## Connection to the semester arc

Sessions 1–4 are the **Observe** movement:

- Session 1: model outputs as research records;
- Session 2: outputs as possible measures;
- Session 3: outputs within qualitative interpretation;
- Session 4: text, image, audio, and sequence as partial records of situations.

Session 5 begins **Intervene**. The researcher is no longer only examining records of social life. The researcher constructs the exposure participants will receive.

Session 6 then asks what happens when the exposure adapts through conversation. Session 5 must therefore establish fixed treatment construction clearly enough that students can later see why an interactive treatment is harder to define.

## The argument of the class

1. Sociology already has traditions of constructing controlled social situations and matched cases.
2. Those traditions make treatment production part of theory and design.
3. A treatment condition is not identical to one message or image used to represent it.
4. Generated media increases the number and kinds of candidate stimuli researchers can produce.
5. Whole-message or whole-image generation can vary more than the researcher intended.
6. Information equivalence asks what else a participant could infer from the material.
7. Multiple candidates help only when generation, selection, rejection, and revision are recorded.
8. Candidate-level checks and condition-level comparisons answer different questions.
9. Velez's adaptive survey shows that participant input can also change the question bank while a study is in the field.
10. Python can make a fixed-pool review explicit and repeatable without determining whether the theoretical rules are adequate.
11. Assignment and outcome analysis come after the treatment set has been constructed and justified.

## Cumulative example and provenance

### Study setup

The course example is a synthetic adaptation of the framing domains used by Bloemraad, Silva, and Voss (2016). Their published *Social Forces* experiment tested contests about immigrant legal status and benefits in three domains:

- human rights versus the rights of US citizens;
- immigrants' economic contributions versus threats to American jobs; and
- deporting parents versus keeping families together.

The course candidates are newly written teaching materials, not excerpts from the article. The hypothetical outcome is support for legal status on a 0–10 scale after exposure.

### Teaching materials

The session uses:

- twelve short cached messages, four per condition;
- ordinary-language frame definitions;
- instructor-authored mock ratings for intended frame, competing frame, warmth, emotionality, readability, and factual density;
- word counts calculated by Python and instructor-authored flags for unsupported claims or stigmatizing language;
- predeclared teaching rules;
- accepted and rejected records with reasons;
- a small synthetic outcome example used only after the validation discussion.

### Provenance statement shown before any result

> The candidate texts are cached course outputs created with an LLM and lightly edited by the instructor. The ratings and flags are instructor-authored mock annotations, not LLM judgments or human pretest data. Python calculates word counts from the displayed text. None of these materials are evidence from an experiment.

The deck should repeat a shorter “Synthetic course example” marker on every slide containing these materials.

## Complete 165-minute sequence

| Time | Minutes | Section | Student activity and evidence of understanding |
|---|---:|---|---|
| 9:30–9:42 | 12 | Course transition and roadmap | Students explain the difference between observing an existing record and constructing an exposure. |
| 9:42–10:06 | 24 | What sociologists did before generated media | Students identify the dimensions and levels in a vignette and name what must be matched in an audit study. |
| 10:06–10:31 | 25 | From construct to material treatment | The room annotates two messages: intended difference, semantic confounds, possible inferences, and a pretest question. |
| 10:31–10:41 | 10 | Break | Break slide keeps the five-part roadmap visible. |
| 10:41–11:12 | 31 | Fixed and adaptive candidate pools | Students compare generation, selection, and validation in Bai, Schwitter, and LinkedOut, then use Velez to distinguish a frozen pool from an evolving question bank. |
| 11:12–11:32 | 20 | Manual treatment review | The room reviews `rights_02`, then diagnoses another candidate, records all reasons, and compares condition pools. |
| 11:32–12:02 | 30 | Beginner Python trace | Students predict exact inputs, first-loop state, Boolean comparisons, mutations to `reasons`, branches, and returned output before each reveal. |
| 12:02–12:10 | 8 | Completion task and oral rehearsal | Students predict individually; the room traces one record and explains one methodological limit without prepared prose. |
| 12:10–12:15 | 5 | Synthesis and transition | Exit response separates stimulus, condition, assignment, outcome, and claim; final slide previews turn-by-turn adaptive interviewing. |

No uninterrupted instructor code explanation should exceed eight minutes. The 30-minute code block contains prediction pauses, partner explanation, and output interpretation.

## Five-part route shown to students

1. **Sociological treatments:** how researchers constructed controlled differences.
2. **Fixed candidate pools:** what faster production changes.
3. **Adaptive question banks:** what changes when participant input alters the instrument.
4. **Manual review:** how candidates are retained and compared.
5. **Python audit:** how to preserve those decisions in a research record.

The roadmap appears near the beginning, on the break slide, and in a compact footer on section dividers. It should orient rather than decorate.

## Section architecture

### Movement 1 — We are beginning the intervention part of the course

**Purpose:** Establish continuity with Sessions 1–4 and define the new research role.

**Key transition:** Once researchers construct what participants encounter, model output becomes part of the causal treatment rather than only a record to analyze.

### Movement 2 — Sociologists constructed treatments before generative AI

**Purpose:** Give the historical practice enough substance that the generative extension is meaningful.

**Sequence:** forms of sociological treatment → Music Lab's artificial cultural markets → staged encounters using confederates → factorial surveys → dimensions and levels → control and realism → audit studies → motherhood-penalty application.

**Student activity:** Given a simple vignette and a matched application pair, students identify dimensions, the intended contrast, and at least one cue that must be stabilized.

**Transition:** These methods already made the material representation of a construct consequential. The published immigrant-rights study lets the class inspect that representation directly.

### Movement 3 — A condition and a stimulus are not the same object

**Purpose:** Establish the session's main distinction before information equivalence or model generation.

**Sequence:** condition → candidate stimulus → retained pool → assignment → outcome.

**Student activity:** Compare rights, economics, and family candidates. Mark what is intended to differ and what else differs.

**Transition:** The extra differences lead to Dafoe et al. and the question of what respondents infer beyond the named manipulation.

### Movement 4 — Information equivalence makes rival interpretations explicit

**Purpose:** Replace “the messages look comparable” with concrete questions about background beliefs and placebo information.

**Student activity:** Write one placebo/pretest question that could reveal an unintended inference about the proposal, speaker, or likely beneficiary.

**Transition:** If two hand-written messages are already difficult to compare, producing many complete messages creates both an opportunity and an enlarged selection problem.

### Break transition

The break slide shows:

- completed: before generation; causal problem;
- next: generated candidates; treatment review; Python.

No new concept appears on the break slide.

### Movement 5 — Generation expands the candidate pool and the decision record

**Purpose:** Explain the consequential change without repeating provider/API instruction from Session 1.

**Sequence:** larger pools → generation versus selection → Bai message conditions → stimulus heterogeneity → Schwitter visual vignettes → LinkedOut validation.

No provider comparison is needed. The only model-access point is provenance: route, model, prompt version, and cached output must be recorded.

**Transition:** The papers show several validation strategies. The cumulative example now asks students to make the retention decisions themselves.

### Movement 6 — Velez makes the question bank adaptive

**Purpose:** Show one bounded form of adaptation without collapsing it into conversational interviewing.

**Sequence:** open-ended participant response → LLM conversion to a structured item → toxicity and redundancy filters → evolving question bank → adaptive selection probabilities.

**Student activity:** Identify which objects are fixed, which change during fieldwork, and which provenance fields would be required to reconstruct what a participant could have received.

**Transition:** The worked Python example deliberately returns to a fixed cached pool so the screening logic remains inspectable to beginners.

### Movement 7 — Review candidates before assigning participants

**Purpose:** Enact the human method before formalizing it in code.

**Student activity:** Each group receives one candidate record and the same rule sheet. They must:

1. inspect the text and ratings;
2. list every failed rule;
3. decide whether the candidate enters the pool;
4. state what their decision does not establish.

The class then compares retained pools. A condition-level warmth or factual-density difference should remain visible even after individual screening so students see why both levels matter.

**Transition:** Python repeats this procedure across every record and preserves the reasons. It does not replace the judgment used to choose the rules.

### Movement 8 — Python records the review one candidate at a time

**Purpose:** Map familiar syntax onto a research process students have just performed by hand.

**Sequence:** one dictionary → list of candidates → rules dictionary → function inputs → initialized outputs → first candidate → accumulated reasons → branch → returned lists → pool summary.

Every code slide states:

- exact input and type;
- operation;
- exact output and type;
- research meaning;
- limit.

### Movement 9 — The code creates an audit trail, not a validity verdict

**Purpose:** Reconnect the printed output to Wallander, Dafoe, and Bai.

**Student activity:** Interpret one accepted candidate, one rejected candidate with two reasons, and one condition-level warning. Explain which reading motivates each part.

**Transition:** Session 6 removes the fixed message and lets the treatment change during interaction.

## Proposed slide-title sequence

The sequence below is the Review Gate 3 object. Titles are deliberately direct and intended to sound natural when spoken. They are not permission to build the slide bodies yet.

| # | Working title | Narrative job |
|---:|---|---|
| 1 | **Can generated media isolate a causal construct?** | Opens with the session question and date. |
| 2 | **This week we begin constructing what research participants will encounter** | Marks the move from Observe to Intervene. |
| 3 | **In the first four weeks, the model helped us examine existing records** | Recalls the completed course movement with concrete examples. |
| 4 | **A generated message can also become part of an experiment** | Introduces the new role without yet showing code or a provider. |
| 5 | **Today we will follow a treatment from theory to a Python record** | States the endpoint in beginner language. |
| 6 | **Today we compare fixed treatments with an adaptive survey** | Displays the five-part roadmap in the same order as the class. |
| 7 | **The experimental difference might be carried by a text, another person, or the setting itself** | Introduces standardized partners, confederates, vignettes, audit testers, and artificial systems as different experimental forms. |
| 8 | **Music Lab created separate markets for the same forty-eight songs** | Uses the original design and interfaces to show that whether participants saw previous downloads was part of the treatment. |
| 9 | **Ridgeway and Erickson trained confederates to act deferentially or nondeferentially** | Uses an AJS status-belief experiment to show that fixed words, interaction style, assignment across confederates, and checks of recorded performances are separate design decisions; Piliavin's subway study is a brief field comparison. |
| 10 | **Wallander uses a segregation study to show how factorial vignettes work** | Introduces the paper through Emerson and colleagues' substantive neighborhood vignette rather than a generic definition. |
| 11 | **A vignette describes one person or situation for a respondent to judge** | Gives a concrete example before design terminology. |
| 12 | **Researchers decide the dimensions and possible levels before writing the vignettes** | Connects theory to the components of the material. |
| 13 | **Combining the levels creates a larger set of possible vignettes** | Makes the vignette universe understandable without formula overload. |
| 14 | **Some possible combinations are clear on paper but implausible in social life** | Introduces the control–realism tension. |
| 15 | **Judgments about fictitious situations do not automatically predict behaviour** | States Wallander's inferential limit. |
| 16 | **Audit studies place matched cases into real institutional decisions** | Moves from survey judgment to field response. |
| 17 | **Correll and colleagues varied parenthood in otherwise comparable applications** | Introduces the paper, material, comparison, and question. |
| 18 | **The motherhood-penalty study connected application materials to status theory** | States the sociological contribution and why the source is here. |
| 19 | **Constructing comparable applications is part of the causal design** | Extracts the lesson needed for generated materials. |
| 20 | **A treatment condition is a theoretical category** | Defines the first half of the central distinction. |
| 21 | **A stimulus is one message or image used to represent that category** | Defines the second half using a visible example. |
| 22 | **One condition can therefore contain several different stimuli** | Prepares stimulus pools and later code lists. |
| 23 | **Bloemraad, Silva, and Voss tested three immigrant-rights framing contests** | Introduces the published sociological study only after the design lens is available. |
| 24 | **The article prints the exact rights, economics, and family treatments** | Makes the original experimental material visible at a readable scale. |
| 25 | **Each treatment contains an argument and a counterargument within one domain** | Prevents students from mistaking the design for three one-sided persuasive messages. |
| 26 | **The frames resonated differently across political groups** | Uses the published result to establish the substantive stakes. |
| 27 | **Our course candidates adapt the three domains but are synthetic** | Establishes provenance before the worked example. |
| 28 | **The candidates can also differ in warmth, facts, and implied membership** | Makes additional variation visible. |
| 29 | **Respondents can learn more from a treatment than the researcher intended** | Creates the need for information equivalence. |
| 30 | **Dafoe and colleagues call this an information-equivalence problem** | Introduces the paper explicitly. |
| 31 | **The comparison becomes ambiguous when the treatment changes background beliefs** | Explains the concept using the immigrant-rights messages. |
| 32 | **A pretest can ask what else respondents inferred from each message** | Introduces placebo and background-belief questions. |
| 33 | **Random assignment cannot clarify an ambiguous treatment** | Separates treatment content from participant assignment. |
| 34 | **Construction, validation, assignment, and estimation are different stages** | Consolidates the workflow before the activity. |
| 35 | **Which differences belong to the frame, and which create another explanation?** | Runs the paired annotation exercise. |
| 36 | **After the break: generated candidates, treatment review, and Python** | Break slide with completed/remaining roadmap. |
| 37 | **Generative models can produce many versions of the same basic treatment** | Introduces the production change. |
| 38 | **A larger candidate pool creates more selection decisions** | States the accompanying methodological change. |
| 39 | **Generation and selection should appear as separate stages in the record** | Establishes provenance fields and human-in-the-loop logic. |
| 40 | **Bai and colleagues compare human, LLM, and human-selected LLM messages** | Introduces the focal contemporary paper. |
| 41 | **Participants encountered messages drawn from pools rather than one fixed text** | Links the paper to stimulus sampling. |
| 42 | **Human selection was part of one treatment condition** | Makes selection analytically visible. |
| 43 | **The message sources also differed in length and perceived qualities** | Shows why source labels bundle message features. |
| 44 | **The study shows that generated messages persuade, but not one simple reason why** | Bounds the substantive claim without dismissing it. |
| 45 | **A claim about a frame should not depend on one unusually effective wording** | Introduces stimulus-specific inference. |
| 46 | **Slater and colleagues ask researchers to define the population of messages** | Gives the message-sampling source one explicit job. |
| 47 | **Schwitter brings generated images into the factorial-survey tradition** | Introduces the direct historical bridge. |
| 48 | **The visual vignettes were generated, edited, and tested with human raters** | Shows the paper's actual pipeline. |
| 49 | **People disagreed about realism and noticed different signs of generation** | Explains why file quality is not participant perception. |
| 50 | **LinkedOut extends the audit-study tradition with generated profile images** | Places the visual field experiment in its sociology lineage. |
| 51 | **The researchers began with many candidates and rated several perceived attributes** | Shows candidate pool, intended attribute, and nuisance ratings. |
| 52 | **The final profiles were selected after comparison, not accepted at generation** | Extracts the validation lesson. |
| 53 | **Our study uses four candidate messages for each of three frames** | Returns to the cumulative example. |
| 54 | **We define all three frames before reviewing the messages** | Shows the ordinary-language definitions. |
| 55 | **We also decide which features should remain comparable** | Displays the stability list and invites challenge. |
| 56 | **Each candidate keeps its text, source, prompt version, and ratings** | Introduces the research-record schema. |
| 57 | **First, review one candidate without writing code** | Begins the hand enactment. |
| 58 | **This candidate expresses the intended frame but adds an unsupported number** | Demonstrates a substantive rejection. |
| 59 | **A candidate can fail more than one rule** | Motivates accumulating rejection reasons. |
| 60 | **The rejected message remains in the research history** | Establishes reproducibility and avoids invisible deletion. |
| 61 | **Passing candidates can still leave the three pools systematically different** | Moves from candidate-level to condition-level checks. |
| 62 | **The retained family messages are warmer on average in this synthetic example** | Displays a concrete pool warning. |
| 63 | **If the pools still differ, the researcher needs to review the design again** | Prevents mechanical threshold reasoning. |
| 64 | **The classroom ratings teach the procedure but do not constitute a pretest** | States the evidence limit before code. |
| 65 | **The Python repeats the review we have just carried out by hand** | Makes the human-method-to-code transition. |
| 66 | **One dictionary stores one candidate and its evidence** | Introduces the exact object, values, and types. |
| 67 | **A list stores all twelve candidate dictionaries** | Connects list structure to stimulus pool. |
| 68 | **A second dictionary stores the rules chosen by the researcher** | Separates rule choice from rule application. |
| 69 | **`review_candidates` receives the pool and the rules** | Names exact function inputs and types. |
| 70 | **The function begins with empty accepted and rejected lists** | Explains initialization and predicted output types. |
| 71 | **The loop selects one candidate dictionary at a time** | Traces the first actual record. |
| 72 | **A new reasons list starts empty for that candidate** | Introduces per-candidate state. |
| 73 | **Each failed check appends a plain-language reason** | Traces multiple independent `if` statements. |
| 74 | **The final branch asks whether the reasons list is empty** | Explains truth testing and the accept/reject decision. |
| 75 | **The function returns two lists with different research meanings** | Displays exact returned values and types. |
| 76 | **`summarize_pools` compares the retained conditions** | Adds the bounded group-level step. |
| 77 | **The warning tells us which difference still needs human judgment** | Reconnects output to method and limits. |
| 78 | **Predict the next candidate's reasons before running the cell** | Provides the code prediction pause. |
| 79 | **Explain one line, its output, and its methodological purpose** | Conducts oral-assessment rehearsal. |
| 80 | **The completion task reviews a small cached treatment pool** | States the low-stakes task and required submission elements. |
| 81 | **The model produced messages; the study still depends on how we defined and reviewed them** | Resolves the opening question with a bounded conclusion. |
| 82 | **Next week the treatment will change during the interaction** | Provides a clear bridge to Session 6. |

The proposed deck is deliberately fuller than the current fourteen-slide scaffold. Several slides contain only one short code state or one paired comparison. The plan assumes discussion, prediction, and rating pauses; it is not an 82-slide uninterrupted lecture.

## Why each major transition works

| Transition | Question answered | Question created |
|---|---|---|
| Course map → sociological experiments | Where does intervention sit in the course? | How did sociologists construct controlled differences before AI? |
| Factorial surveys → audit studies | How can controlled situations be built in surveys? | What changes when the constructed case enters a real institution? |
| Audit study → condition/stimulus distinction | Why do materials matter to causal design? | How does one material instance relate to the theoretical treatment? |
| Immigrant-rights candidates → Dafoe | What actually differs in our messages? | What else might participants infer? |
| Information equivalence → break | Why is content validation separate from randomization? | What happens when generation multiplies the content? |
| Bai → Slater | How have LLM messages been used experimentally? | Can an effect generalize beyond particular messages? |
| Slater → Schwitter/LinkedOut | Does the issue extend beyond text? | How are generated visual candidates reviewed? |
| Published studies → manual audit | What did researchers do in practice? | Can students apply the same logic to the cumulative study? |
| Manual audit → Python | What decisions need to be repeated and preserved? | How can familiar Python objects represent them transparently? |
| Python → Session 6 | What can a fixed-treatment audit record? | What breaks when the treatment changes turn by turn? |

## Paper-image and evidence plan

Every focal paper slide must use an actual title page, journal page, or figure from the paper—not a recreated citation card. Each paper is identified as a paper and accompanied by material, question, result/contribution, and why it appears here.

| Source | Planned visual evidence | Required teaching text |
|---|---|---|
| Berger, Cohen, and Zelditch | Original paper page and, if legible, the standardized task or disagreement sequence | Sociology has used controlled information about an ostensible partner to study how status shapes influence |
| Salganik, Dodds, and Watts | Original Music Lab design diagram, interfaces, and parallel-world result from the author-hosted papers | The same songs were placed in separate markets; whether participants saw prior downloads was an experimental feature of the interface, and the worlds produced different rankings |
| Ridgeway and Erickson | Actual AJS title page plus the methods passage and treatment-fidelity note on deferential/nondeferential confederate performance | The confederates' choices and arguments were held constant while interaction style varied; blinded coders reviewed recordings to check the enacted treatment |
| Piliavin, Rodin, and Piliavin | Original paper page plus a clearly labelled course reconstruction of the subway-car roles based on the methods | A victim, helping model, and two observers staged and recorded a public encounter; human performance and timing were parts of the treatment |
| Jackson and Cox | Actual Annual Review page or title crop used sparingly beside the broader map | Sociology has laboratory, field, and survey experimental traditions |
| Wallander and Emerson et al. | Actual article pages plus Wallander's reproduction of the residential-segregation vignette | Factorial surveys combine controlled dimensions with contextual detail; the focal example asked respondents to judge a possible neighborhood |
| Krysan et al. | Actual AJS page and, if available from the paper or supplement, stills from the neighborhood video treatment | Recorded vignettes can add realism while introducing houses, streets, people, camera movement, sound, and editing as possible additional cues |
| Correll et al. | Actual AJS title page and a carefully redrawn course comparison of the application materials, clearly labeled as a schematic | Parenthood is varied in matched job materials to test status-based discrimination |
| Dafoe et al. | Actual *Political Analysis* title page plus one legible conceptual figure/table if useful | Respondents may update background beliefs beyond the named treatment |
| Bai et al. | Actual *Nature Communications* article page; conditions or results from the paper | Generated messages, human messages, and human-selected outputs are distinct conditions using message pools |
| Slater et al. | Actual article title area plus one short passage on message populations | Selecting messages is a sampling decision |
| Schwitter | Actual article page plus an author figure showing the generation/pretest process or example images | Generated visual vignettes require theoretical justification and human pretesting |
| LinkedOut | Actual paper page and author-provided candidate/final image figure at preserved aspect ratio | Generated faces enter a staged matching and validation process |

The full visual-source notes, reuse cautions, and recommended figure/page choices are recorded in `literature/session05_visual_sources.md`.

Related paper screenshots should use consistent frames, title scale, crop depth, and source placement. Every image must be inspected at 1280 × 720 after rendering. Faces, screenshots, and figures must retain their original aspect ratios.

## Reading-to-class and reading-to-code map

| Required reading | In-class use | Code or research-record consequence |
|---|---|---|
| Wallander | Dimensions, levels, vignette universe, plausibility, fictitious judgment | explicit condition definitions, several candidates, stable schema |
| Dafoe et al. | Intended information, background beliefs, placebo/pretest questions | competing-frame and nuisance fields; pool warnings |
| Bai et al. | Message pools, source conditions, human selection, persuasion result | generator/source and prompt fields; retained/rejected records |

Slide-only sources add bounded extensions:

- Correll et al. motivates material comparability through a sociological application.
- Slater motivates multiple messages per condition.
- Schwitter motivates iterative human review of generated visual candidates.
- LinkedOut demonstrates multi-attribute image validation in a field experiment.
- Velez distinguishes a fixed candidate pool from an evolving question bank and introduces versioned adaptive instruments.

## Human-method-to-code map

| What students do first by hand | What the code later does | Instructor question |
|---|---|---|
| Read one candidate record | retrieves one dictionary in the loop | What exact value does `candidate` hold now? |
| Compare the text with frame definitions | checks stored intended and competing-frame scores | Which part is human judgment rather than computation? |
| Write every failed rule | appends strings to `reasons` | Why use several `if` statements rather than one `if/elif` chain? |
| Place the candidate in one pile | appends to `accepted` or `rejected` | What type is the pile, and what does one element contain? |
| Compare retained pools | computes simple counts and averages by condition | Why can a pool warning remain after every candidate passes? |
| Reconsider the design | prints a human-review warning | What can the program not decide for us? |

## Python progression from Session 4

Session 4 introduced state across an ordered sequence by keeping previous and current records. Session 5 returns to independent records but deepens conditional reasoning:

- a list contains several dictionaries with the same schema;
- a rules dictionary makes researcher choices explicit inputs;
- several `if` statements can all apply to the same record;
- a per-record reasons list accumulates state;
- returned objects preserve both successful and failed cases;
- a second function summarizes condition-level patterns.

The conceptual difficulty should exceed the syntactic difficulty. Do not introduce classes, pandas, comprehensions, lambda functions, or multilevel modeling.

## Required code stops

1. Show one complete candidate dictionary and ask for every value's type.
2. Show the first two elements of `candidates`; distinguish list position from dictionary key.
3. Show the exact `rules` dictionary and ask who chose each value.
4. State the function signature and predict output types before the body.
5. Trace initialization with actual empty-list values.
6. Trace the first candidate through each check.
7. Use a candidate that fails two rules so students see both reasons appended.
8. Ask why the final decision occurs after all checks.
9. Print accepted and rejected records separately.
10. Interpret the pool summary and warning in ordinary language.
11. State what the passing assertions establish and what they do not.

## Completion task

Students receive a smaller cached pool containing four candidates and a visible rules dictionary. They complete bounded gaps in `review_candidates`, then submit:

1. their predicted accepted IDs and rejected IDs/reasons;
2. functioning code;
3. the printed output and passing checks;
4. a 100–150 word explanation connecting one decision to Wallander, Dafoe et al., or Bai et al.;
5. an AI-use disclosure;
6. preparation for a short oral explanation.

The task is completion-marked. Elegant syntax is irrelevant. A student can complete it without API access.

## Oral-assessment rehearsal

Each student should be able to answer all of the following in ordinary language:

1. What is the exact value and type of `candidates`?
2. What does one candidate dictionary represent in the study?
3. What is stored in `rules`, and who decided those values?
4. During the first loop iteration, what exact dictionary does `candidate` refer to?
5. Why is `reasons` reset to an empty list for each candidate?
6. Why are the checks separate `if` statements?
7. What does `.append()` change?
8. What exact objects does the function return?
9. Why can an accepted candidate still be part of an imbalanced condition pool?
10. What claim would be invalid even if every software test passes?

The instructor should ask follow-ups with actual values, not accept memorized definitions alone.

## Material that should remain outside the session

- detailed OpenRouter, direct-provider, and Ollama setup already taught in Session 1;
- live generation as required work;
- image-generation tutorials;
- full manipulation-check debates or post-treatment-bias analysis;
- crossed random-effects models for participants and stimuli;
- conjoint estimation and optimal vignette-deck construction;
- conversational tailoring beyond the single closing bridge;
- synthetic respondents;
- an extended survey of every sociological experimental tradition;
- outcome estimation before treatment construction is understood.

## Review Gate 3 decisions

Before slide writing begins, approve or revise:

1. the 82-slide paced title sequence;
2. the placement of the Bloemraad, Silva, and Voss example after the sociological lineage;
3. the three required readings and five slide-only sources;
4. the 24-minute “what came before” section;
5. the manual review before Python;
6. the two-function scope: `review_candidates` and `summarize_pools`;
7. the explicit synthetic-material and synthetic-rating caveat;
8. the decision not to repeat model-provider instruction.
