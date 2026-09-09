# Session 7 architecture — synthetic respondents and population representation

**Status:** Stage 4 session architecture and slide-arc plan completed on 25 August 2026. This document must be approved before the final deck, workbook and task are rebuilt.

## Intended endpoint

Students should leave able to answer four questions in plain language:

1. What makes a human survey response part of a population estimate?
2. What process produces a synthetic respondent record?
3. Which feature of the human data is a given validation statistic checking?
4. What claim remains unwarranted after that check passes?

The narrow computational endpoint is that students can trace a function which selects cached responses, counts every point on a seven-point scale, converts counts to proportions and compares the returned distribution across human, forced-choice and probability-sampled records.

## Connection to the semester arc

`interpret a human corpus (Session 3) → observe situated action (Session 4) → generate a treatment (Session 5) → let a model help produce interview questions (Session 6) → let a model produce the respondent's answer (Session 7) → predict unobserved outcomes (Session 8)`

The opening should state this connection rather than expecting students to infer it.

## Cumulative example and provenance

### Substantive question

> How are U.S. adults divided over whether government should reduce income differences?

### Human benchmark

Use the 2024 General Social Survey `EQWLTH` item. NORC's 2024 Release 3a codebook reports the following unweighted frequencies among 2,161 valid responses:

| Scale point | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Count | 699 | 180 | 294 | 326 | 207 | 120 | 335 |
| Valid % | 32.3 | 8.3 | 13.6 | 15.1 | 9.6 | 5.6 | 15.5 |

Source: *2024 GSS Cross-section Documentation and Public Use File Codebook*, Release 3a (NORC, July 2026), `EQWLTH`, codebook pages 187–188 (PDF pages 265–266): <https://gss.norc.org/content/dam/gss/get-documentation/pdf/codebook/GSS%202024%20Codebook%20R3a.pdf>.

The variable label in that codebook ends mid-sentence. Use an official GSS questionnaire for the complete question wording and the Release 3a codebook for the 2024 frequency table. The slide should not present the truncated codebook label as the administered question.

Before final implementation, record:

- exact wording and response labels;
- survey year and field dates;
- target population;
- sample and relevant weight;
- source URL and citation;
- whether the class file contains row-level public data or instructor-authored teaching records reconstructed from a published distribution.

The codebook distribution is a distributable benchmark for the responding cases, but it is explicitly unweighted. The deck must not call it an estimate of all U.S. adults without applying the documented GSS weight to the public-use data. This difference is part of the substantive lesson. The deck must not call reconstructed records “GSS respondents,” and it must never invent a plausible distribution.

### Synthetic conditions

Use the same profile fields and question in three cached conditions:

- one forced scale choice per profile;
- one reported probability distribution per profile;
- one sampled scale choice per profile drawn from the probabilities with a recorded random seed.

The raw model output, parsed answer, parser status and provenance fields remain in the class data. The required exercise never depends on a live model call.

## 165-minute sequence

| Time | Section | Main question | Student activity | Evidence of understanding |
|---|---|---|---|---|
| 9:30–9:40 | Opening puzzle and course connection | Can a distribution tell us whether it represents people? | Compare two distributions and justify an initial answer | Students identify missing provenance rather than choosing by visual resemblance |
| 9:40–10:16 | What survey representation and social simulation involved before LLMs | How do responses become population claims, and what did earlier computational publics claim? | Read a survey item, sampling diagram, Simulmatics history and source passages | Students distinguish survey inference, categorical prediction and explicit rule-based simulation |
| 10:16–10:34 | What a synthetic respondent is | What is actually sampled or generated? | Trace one profile through an exact prompt and saved record | Students name the source and type of every object |
| 10:34–10:48 | The positive proposition | Why did researchers think silicon samples and interview-grounded agents might work? | Reconstruct Argyle and Park designs | Students state the proposed target and its human comparison |
| 10:48–10:58 | Break |  |  |  |
| 10:58–11:35 | What current validation studies find | Which parts of human variation are reproduced or distorted? | Read figures from Taubenfeld, Boelaert, Bisbee, Wang, Gordon, Chen and Abeliuk | Students separate majority direction, full distribution, within-group variation and between-group differences |
| 11:35–11:53 | Apply the framework to one survey item | What does our cached comparison permit us to claim? | Whole-room interrogation of one human/synthetic comparison | Students produce a bounded claim and name one missing validation target |
| 11:53–12:10 | Local model and Python walkthrough | How was each record generated and how does the code calculate the comparison? | Trace request, response, first loop iterations and returned dictionary | Students explain exact inputs, types, updates and outputs aloud |
| 12:10–12:15 | Close | What should be recorded and said when the respondent is generated? | Return to opening; individual exit sentence | Students distinguish measurement from model-based prediction |

The evidence section is deliberately longer than the live-technology section. The session is about inference and representation, not an Ollama product demonstration.

## Complete slide arc

The working plan contains approximately 70–75 slides. This is a planning maximum rather than a target to inflate. During implementation, combine slides only when the combined composition remains readable and the two jobs genuinely belong together. Do not preserve a slide merely because it appears in this numbered plan.

### Part 1 — Begin with the missing inferential chain (Slides 1–4)

#### Slide 1 — “Whose attitudes do synthetic respondents represent?”

Minimal title slide. Subtitle: “Survey samples, model predictions and population claims.” Do not begin with the course movement label or an LLM capability claim.

#### Slide 2 — “Which distribution could support a claim about U.S. adults?”

Show two clearly labeled distributions for the same seven-point question, but initially disclose only that one comes through a survey design and one through a model-generation procedure. Include the complete question wording above the plots. Ask the room what else it needs to know.

**Purpose:** Establish that visual resemblance is not enough.

#### Slide 3 — “The distribution alone cannot tell us where the responses came from”

Answer the opening immediately. Beneath each distribution, reveal a short provenance chain. State that either distribution could be numerically closer on one metric; the issue is what observation or prediction each bar represents.

**Purpose:** Prevent the unresolved-opening problem from Session 6.

#### Slide 4 — “Today we need to understand the survey design, the generation process and the comparison”

Use three ordinary questions, directly connected to Slide 3:

- How did the human responses become evidence about a population?
- What did the model receive and return?
- What would the synthetic data have to reproduce for the intended use?

Add one sentence connecting Sessions 6–8: last week the model influenced questions; this week it supplies answers; next week the course considers unobserved outcomes.

### Part 2 — What population representation involved before LLMs (Slides 5–15)

#### Slide 5 — “Start with the question people were actually asked”

Show the complete published survey item, response card and field information for the cumulative example. Define the endpoints of the scale. If “don't know” or refusal was available, show it.

**Purpose:** Establish the construct and instrument before discussing samples or models.

#### Slide 6 — “A survey estimate depends on more than the people who answered”

Build the conventional chain with one sourced survey example:

`target population → frame → selected sample → respondents → answers → weighted estimate`

Define each object underneath in one short sentence. The final estimate should be visually separated from the individual response.

#### Slide 7 — “A probability sample does not require every respondent to be typical”

Use Kish to explain selection probabilities and estimators. Contrast two claims:

- warranted: the design links selected units to the target population;
- unwarranted: each selected person represents a demographic “type.”

Use an actual Kish page or a clean cited sampling illustration, not an invented authoritative diagram without a source.

#### Slide 8 — “Groves and Lyberg separate errors of measurement from errors of representation”

Introduce the paper fully and show its measurement/representation framework at a readable scale. Define construct, measurement, target population and frame before pointing to the model.

#### Slide 9 — “Deming was already warning against treating sampling error as the whole problem”

Show the 1944 *American Sociological Review* article and a readable crop of the relevant error discussion. Connect directly to Slide 8: an enormous synthetic sample can make computational sampling variation tiny while leaving other errors untouched.

#### Slide 10 — “Bourdieu asks whether a poll has produced an opinion that can be counted”

Introduce “Public Opinion Does Not Exist” as an argument about polling practice, with publication history and a readable source passage.

#### Slide 11 — “His critique depends on three assumptions built into opinion polling”

Show the full passage or three complete highlighted statements: everyone can produce an opinion; all opinions have equivalent weight; the questions express a shared problem. Explain each using the cumulative survey item.

#### Slide 12 — “A model that always chooses a scale point can hide uncertainty rather than measure opinion”

Compare three human responses—substantive answer, “don't know,” and question reinterpretation—with one fluent synthetic choice. Make clear these are instructor-authored examples illustrating Bourdieu's concern, not empirical quotations.

#### Slide 13 — “McCall treats categories as relationships and sources of internal variation”

Introduce the *Signs* paper and the problem it addresses. Do not reduce the paper to “intersectionality matters.” Show the relevant conceptual passage or table.

#### Slide 14 — “The same demographic labels do not define one social position or one likely answer”

Use two profiles sharing a headline category but differing in other positions and contexts. Do not predict their opinions. The slide's point is that the category underdetermines the answer.

#### Slide 15 — “These earlier debates give us four things to check”

Synthesize with citations attached to each line:

- link selected observations to a population;
- show how the instrument produced the response;
- preserve uncertainty, refusal and reinterpretation where they matter;
- examine variation within and across social positions.

Use a flat composition with a closing bottom rule if rendered as a table. This is a sourced synthesis, not a new universal typology.

### Part 3 — What changes when the model answers (Slides 16–24)

#### Slide 16 — “Now replace the respondent's answer with generated text”

Return to the conventional chain and show exactly which link changes. Do not suggest all earlier links disappear; profile fields and benchmark data may still come from people.

#### Slide 17 — “This is the exact information supplied to one synthetic respondent”

Show a small profile dictionary, the complete survey question, response options and instruction. Label every field's provenance. Avoid chat-bubble decoration.

#### Slide 18 — “The model returns text. The research file stores a parsed answer”

Show the raw response beside the parsed integer and saved metadata. Define parsing and show a failed or ambiguous parse as well as a clean one.

#### Slide 19 — “Sampling a person and sampling model output are different operations”

Place the two chains side by side. Use direct prose:

- the survey selects a person under a sampling design;
- the synthetic procedure generates a response conditional on a prompt and model.

Avoid the slogan form “prediction, not measurement” until the evidence has earned it.

#### Slide 20 — “Current studies generate respondents in three different ways”

Define designs through the focal literature rather than inventing a free-standing typology:

- aggregate distribution prediction (Gordon L1/L2);
- one answer per demographic persona (Argyle; Gordon L3);
- one answer per interview-grounded agent (Park; Gordon L4).

#### Slide 21 — “An aggregate prediction asks the model about the population as a whole”

Show the exact input and output shape. There is no individual-level synthetic file unless the researcher creates one later.

#### Slide 22 — “A demographic persona creates one individual-shaped record per profile”

Show the loop concept without code: profile 1 → answer; profile 2 → answer; profile 3 → answer. State that the profile might come from a human record, a census-based reconstruction or an LLM-generated biography; those sources are not equivalent.

#### Slide 23 — “An interview-grounded agent receives information the person actually supplied”

Show a complete but brief input chain: human interview → transcript → model context → held-out question → predicted answer. State why this may reduce stereotyped inference and why the output remains a prediction.

#### Slide 24 — “The source record must include the generation procedure”

Show one saved record containing profile source, model, prompt, elicitation, query date, raw response, parsed answer and parser status. This record becomes the object used later in Python.

### Part 4 — Why researchers thought this might work (Slides 25–32)

#### Slide 25 — “Argyle and colleagues asked whether demographic conditioning could recover human response patterns”

Introduce the *Political Analysis* paper with full citation, material, question and model. Show the published article or final typeset PDF.

#### Slide 26 — “Their comparison established the positive proposition later studies test”

Show the backstory → GPT-3 responses → human comparison design and define algorithmic fidelity using the authors' language. Report a central result and its target precisely.

#### Slide 27 — “Kozlowski and Evans ask what a simulated social subject would have to preserve”

Introduce the *Sociological Methods & Research* paper as a methodological synthesis. Explain why it is required: it supplies the sociological standard, not another accuracy score.

#### Slide 28 — “Kozlowski and Evans identify six recurring problems”

Give each of bias, uniformity, atemporality, disembodiment, linguistic cultures and alien intelligence an ordinary-language explanation tied to one example. Prefer a readable source figure or highlighted passage; do not render six decorative cards.

#### Slide 29 — “Park and colleagues test whether long interviews improve individual grounding”

Introduce the 1,052-person study and its cross-institutional team. State that the source is a preprint if it remains unpublished at build time.

#### Slide 30 — “Each agent was tested on questions the person had answered separately”

Show the actual study pipeline, including the two-week human retest and the demographic-only comparison. Define every outcome family before results.

#### Slide 31 — “The agents reached 85% of human test–retest agreement on GSS answers”

Show the exact figure or result passage. Explain the denominator in large visible text: this is performance relative to how consistently participants answered themselves two weeks later, not 85% raw accuracy across all questions.

#### Slide 32 — “Does more information about a person remove the main errors?”

Place the question beside the Park design and state what remains unresolved: population distribution, individual agreement, subgroup error, different outcome domains and elicitation. This question creates the need for the post-break evidence.

### Slide 33 — Break

Use a plain break slide. One sentence can preview the return: “After the break: what the newer validation studies actually compare.”

### Part 5 — Validation studies answer different questions (Slides 34–54)

#### Slide 34 — “Different claims require different validation evidence”

Introduce the validation targets accumulated from the literature: majority direction, full distribution, within-group variation, group differences, associations, stability, baseline performance and decision consequence. Attach sources to the relevant rows. Do not present this before the sources that motivate its first elements.

#### Slide 35 — “Taubenfeld and colleagues compare models with divided human judgments”

Introduce the Google Research preprint: 25 models, four dispositions, human-validated situational judgment tests and 550-person rater pool. State the methods discrepancy accurately: 2,576 generated, 2,357 retained; the paper rounds the final set to 2,500 elsewhere.

#### Slide 36 — “Their pipeline turns questionnaire statements into behaviorally specific choices”

Use Figure 1 in full or a semantically complete two-stage crop. Explain human validation, ten human judgments per scenario, twenty sampled model responses and the LLM judge.

#### Slide 37 — “A model can choose the majority answer and still miss the disagreement”

Define directional and distributional alignment with one 60:40 human example and two possible model distributions. State who generated every number.

#### Slide 38 — “Models remain confident even when the human raters are divided”

Use Figure 3 at large size with its axes explained. State the main empirical result and the US/UK, binary-choice and single-turn limits.

#### Slide 39 — “Boelaert and colleagues ask whether models can reproduce opinion-poll distributions”

Introduce the published *SMR* article fully. State the polls, models and comparison before the result.

#### Slide 40 — “Bias and compressed variation change from one topic to another”

Use the paper's central result figure or table. Highlight two topics with different directions of bias and show the low-variance result. Explain why one global correction is not available.

#### Slide 41 — “Bisbee and colleagues compare synthetic feeling thermometers with the ANES”

Introduce the published *Political Analysis* design: eleven groups, 2016–2020 ANES benchmark, personas, prompts and repeated query dates.

#### Slide 42 — “Similar averages coexist with lower variation and different relationships among variables”

Show the relevant figure panels without cutting axes or captions. Separate four findings: mean correspondence, reduced variance, regression mismatch and prompt/time instability.

#### Slide 43 — “Wang, Morgenstern and Dickerson test representation across sixteen identities”

Introduce the *Nature Machine Intelligence* paper: four LLMs, 3,200 participants, sixteen identities and the human/model comparisons.

#### Slide 44 — “The models can misportray groups and make people within a group look too similar”

Use the published paper's most legible result and one author-defined example. Connect flattening to McCall without claiming McCall predicted this technology.

#### Slide 45 — “Gordon and colleagues compare synthetic answers with the same 996 people”

Introduce the 2026 Prolific working paper with full citation, employment/funding disclosure, field date, survey topics and AI-moderated voice interview.

#### Slide 46 — “The four conditions differ in exactly what the model knows”

Define L1–L4 in ordinary language before using the labels:

- questions only;
- aggregate sample demographics;
- respondent demographics;
- respondent demographics plus interview transcript or distilled profile.

#### Slide 47 — “Demographic personas produce the largest distributional error in this comparison”

Use Figure 1 or a focused crop of Table 5. Explain JSD only to the level needed: lower values mean closer distributions. Point out that winner accuracy and distributional error move differently.

#### Slide 48 — “Changing the requested output improves the distribution more than adding persona detail”

Show forced choice versus per-persona probabilities and the sampled-answer construction. Report the 35–48% improvement and retain the sampling-noise-floor comparison.

#### Slide 49 — “Post-stratification does not remove the remaining error”

Define post-stratification before showing Table 6 or Figure 2. Explain the paper's conclusion: the remaining difference is not the kind of sample-composition error this correction addresses.

#### Slide 50 — “Chen, Zhu and Zheng compare LLMs with simple non-LLM baselines”

Introduce the GSS/WVS preprint, four models and held-out human benchmark. Explain the baseline in concrete terms before reporting that the LLM does not beat it.

#### Slide 51 — “The models make demographics look more predictive of attitudes than they are”

Use the over-determination figure and the segment-targeting result. State the magnitude: group differences inflated two- to fourfold and the wrong target selected in many cases.

#### Slide 52 — “Models can flatten people within groups and exaggerate gaps between groups”

Bring Wang and Chen into one explicit comparison. Use one human distribution with overlap and one synthetic representation with narrow, separated groups. Label any reconstruction as a course illustration rather than empirical data.

#### Slide 53 — “Abeliuk and colleagues find a larger gap for Chile than for the United States”

Introduce the published *EPJ Data Science* comparison and display the cross-country result. Explain that the relevant social cleavages differ across societies.

#### Slide 54 — “The evidence supports some uses more strongly than population measurement”

Use a source-anchored continuum of claims:

- instrument debugging and code testing;
- exploratory sensitivity analysis;
- explicitly model-based aggregate prediction;
- individual prediction;
- replacement of human population measurement.

For each, state what validation would still be required. Avoid green/red traffic-light verdicts that flatten use-specific evidence.

### Part 6 — Apply the framework to one survey item (Slides 55–61)

#### Slide 55 — “Our example asks how adults divide over government action on income differences”

Return to the exact question from Slide 5. State the target population and comparison groups. Do not introduce a second substantive example.

#### Slide 56 — “The codebook reports unweighted responses; a population estimate needs the survey weight”

Show the official codebook excerpt next to the seven counts and valid-response percentages. State plainly that these are unweighted frequencies for 2,161 valid responses. Then show the population claim that would require the public-use cases and the documented GSS weight. If teaching records reproduce the aggregate table, say so visibly and explain what they cannot represent.

#### Slide 57 — “Every synthetic condition uses the same profiles and question”

Show the shared inputs once and then the three elicitation instructions: forced choice, probabilities, and probability-based sampling. The random seed and cached generation date must be visible.

#### Slide 58 — “The forced answers are more concentrated than the human benchmark”

Show all response categories, including categories with zero synthetic responses. Explain the bars and sample sizes. Do not show only a mean.

#### Slide 59 — “Probability-based sampling restores some of the missing spread”

Compare the second synthetic condition with the human benchmark. State which metrics improve and which validation questions remain unanswered.

#### Slide 60 — “The subgroup comparison asks whether the model exaggerates a social difference”

Use one documented grouping, such as degree status, and show overlapping human distributions before the synthetic distributions. Avoid language suggesting the profile causes the response.

#### Slide 61 — “What can we say after these comparisons?”

Whole-room task. Give a claim template:

> In this cached comparison, [condition] reproduced [specific feature] but differed on [specific feature]. This supports using it for [bounded purpose], not for [stronger purpose].

Ask the room to identify one additional comparison needed.

### Part 7 — Show how the records were generated locally (Slides 62–67)

#### Slide 62 — “A local call still involves a client, a server, a model and a response”

Show the complete pipeline before code:

`Python profile and question → Ollama client → local server → model weights → response dictionary → saved record`

Define “local” as where inference runs, not as a guarantee that the whole research environment is secure.

#### Slide 63 — “Ollama manages model files and serves requests on the researcher's computer”

Show what the student actually sees: model list, server status and one terminal command. Define RAM/VRAM, parameter size and quantization only as needed for choosing a model that fits.

#### Slide 64 — “This dictionary is the exact request Python sends”

Show one small request object with model name and messages. Identify every string, list and dictionary. Point to the profile and question values carried over from Slide 57.

#### Slide 65 — “The response is another dictionary containing generated text and metadata”

Show the relevant returned fields at readable size and the line that extracts the text. Include an ambiguous output to motivate parsing rather than assuming every response is clean.

#### Slide 66 — “Parsing creates the scale value; it can also record failure”

Show raw text → parser decision → integer or missing value → parser status. Say whether the parser is a programmatic rule, human decision or second model call. For the required lab, use a transparent programmatic rule.

#### Slide 67 — “Cached outputs keep the exercise independent of hardware and setup”

Compare live and cached routes in ordinary language: same record schema, different origin. Cover privacy, local files/logs, model download, speed, memory and maintenance. State that no required student work needs a key, network connection or successful Ollama setup.

### Part 8 — Reconstruct the distribution in Python (Slides 68–72)

#### Slide 68 — “The program counts the saved answers for one condition”

State what it does and does not do before syntax:

- does select records, count scale points and calculate proportions;
- does not call a model, decide whether an answer is valid, weight a survey or establish population representation.

#### Slide 69 — “One input record contains the answer and its provenance”

Show one complete dictionary and its type. Explain why `source`, `elicitation`, `response`, `model`, `prompt_id` and `parser_status` remain together.

#### Slide 70 — “The first loop selects the records that match the requested condition”

Trace two iterations with state before and after. Reuse lists, dictionaries, `for`, `if` and `.append()` from earlier weeks. Avoid tuple keys and `setdefault`.

#### Slide 71 — “The second loop updates one count at a time”

Initialize all seven response categories to zero, then show one count before and after. Explain why retaining zeros matters for distributional comparison.

#### Slide 72 — “Counts become proportions only after we know the total”

Trace one exact division. Show the complete returned dictionary and its type. Then display human, forced-choice and probability-sampled outputs together.

#### Slide 73 — “The checks verify the calculation, not the population claim”

Use two assertions: proportions sum to one within rounding tolerance; a known response category has the expected count. Explain both sides in plain language. Then ask students to explain four consecutive lines orally and predict one changed input.

### Part 9 — Close by resolving the opening (Slides 74–75)

#### Slide 74 — “Now we can explain what the opening distributions represent”

Return to Slides 2–3 with complete provenance and one bounded comparison. The answer should be explicit: the survey distribution is an estimate linked to people through a survey design; the synthetic distribution is a model-based prediction that must be described and validated as such.

#### Slide 75 — “Next week asks whether models can recover outcomes we did not observe”

Bridge to Session 8. State the new question plainly: once synthetic data are treated as predictions, how should predictions of missing or future social outcomes be validated?

## Reading-to-teaching map

| Reading | Job in the lecture | Later decision it changes |
|---|---|---|
| Kozlowski and Evans | Define what simulated social subjects may fail to preserve | Broadens validation beyond one accuracy statistic |
| Boelaert et al. | Show topic-specific polling bias and compressed variance | Requires a full distribution and topic-specific checks |
| Wang, Morgenstern and Dickerson | Show identity flattening and epistemic stakes | Requires within-group and representational-harm analysis |
| Taubenfeld et al. | Separate majority direction from disagreement | Motivates forced-choice versus probability elicitation |
| Gordon et al. | Test richer personas and output format against matched humans | Adds `elicitation` to the source record and code comparison |
| Chen, Zhu and Zheng | Show demographic over-determination and decision consequences | Adds simple baselines and bounded subgroup comparisons |

## Human-method-to-code map

| Human research operation | Python representation | What is thinner in code |
|---|---|---|
| identify the target question and response scale | stored question ID and integer response | code does not establish construct validity |
| document the origin of each observation or prediction | provenance fields in each dictionary | fields can be wrong or incomplete |
| separate sources or experimental conditions | `if` condition selecting records | selection does not make groups comparable |
| tabulate response categories | counts dictionary initialized for 1–7 | counts do not address survey weights or sampling error |
| compare distributions | proportions dictionary and plotted output | similarity does not establish social grounding |
| audit unexpected answers | raw response and parser status | rule-based parser cannot resolve substantive ambiguity |

## Python progression from Session 6

Session 6 used dictionaries, lists, loops, conditionals, `.append()`, functions and `enumerate()` to reconstruct interview paths. Session 7 reuses these objects. The new procedural idea is an explicit frequency table that retains zero-count categories, followed by conversion to proportions.

Do not introduce tuple keys, `setdefault`, a generator expression and a manual variance formula in the same function. If mean or population variance appears, call a named function from `statistics` after students can see the underlying distribution.

## Completion task and oral rehearsal

The completion-marked task should ask students to:

1. predict one updated count before running code;
2. complete or modify the small distribution function;
3. run supplied checks;
4. compare the human benchmark with one synthetic condition in 100–150 words;
5. state one feature the code has not validated;
6. disclose any material AI assistance.

For oral rehearsal, the student receives one input record and four consecutive lines. They must explain every name and bracket, state the object before and after the lines, and predict what changes if the elicitation label or response value changes.

## Material explicitly excluded from the main arc

- A general history of synthetic data.
- A repeat of the Week 1 API/OpenRouter explanation.
- A long tour of commercial synthetic-user products.
- Detailed social-agent interaction, reserved for Sessions 9–10.
- Full treatment of SSDataBench and prediction of unobserved outcomes, reserved for Session 8.
- Survey fraud and autonomous form-filling, reserved for data-integrity or research-agent material.
- ConvApparel, unless needed as a brief optional comparison.
- More than one slide on Synthetic Persona Pretraining.

## Title-only narrative audit

Reading the provisional titles alone produces this sequence:

1. ask which distribution can support a population claim;
2. answer that provenance is missing;
3. establish the three questions for the day;
4. show the actual survey item;
5. reconstruct how survey estimates ordinarily work;
6. show where measurement and representation can fail;
7. add Bourdieu's question about whether an opinion was produced;
8. add McCall's warning about treating categories as homogeneous;
9. replace the human answer with generated text;
10. define aggregate prediction, demographic personas and interview-grounded agents;
11. present the initial positive proposition and its strongest elaboration;
12. ask whether richer information resolves the problem;
13. compare distinct validation targets after the break;
14. move from disagreement, to polls, to identities, to richer personas, to demographic over-determination and cross-societal error;
15. apply those checks to one survey item;
16. show exactly how a local model produced the cached record;
17. trace how Python turns records into a distribution;
18. return to the opening with an explicit answer;
19. bridge from observed synthetic comparisons to prediction in Session 8.

No paper appears merely because it is recent. Each one answers a question created by the previous section.

## Pre-build self-review commitments

Before final artifacts are shown to the instructor:

- verify the human benchmark and label any reconstructed teaching records;
- obtain the published PDF for every published focal paper or ask the instructor for it;
- use working-paper title pages only for papers that remain working papers;
- give every paper a full first citation and a clear sample/design/finding sequence;
- use Figure 1 when discussing a study's Figure 1, not nearby prose;
- crop at complete figures, tables, questionnaire blocks and paragraphs;
- highlight only text checked against the complete source passage;
- preserve all image aspect ratios;
- place a closing rule under every table;
- read all visible prose aloud and remove slogan-like or “Claudish” wording;
- inspect the title sequence, contact sheet and every evidence/code slide at full size;
- show exact inputs, outputs, types and provenance in every Python segment;
- rerender affected slides and their neighbours after every repair;
- realign syllabus, reading guide, notes, workbook, task, solution, tests and decisions after the deck is approved.
