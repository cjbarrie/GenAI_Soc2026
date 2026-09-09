# Session 7 synthesis — synthetic respondents and population claims

**Status:** Stage 3 methodological synthesis completed on 25 August 2026. Ready for Review Gate 2 before final slide production.

## Communication job

By the end of the session, graduate sociology students should be able to explain why a set of LLM-generated answers is not a sample of a social group, identify several different targets against which synthetic data might be validated, and use a transparent Python comparison to decide what one synthetic distribution does and does not reproduce.

The session should not ask whether synthetic respondents are generally “accurate.” It should make that question look incomplete until the target population, generation procedure, comparison evidence and intended use have been specified.

## Central argument

Survey researchers ordinarily support population claims by documenting a chain:

`target population → sampling frame → selected people → responses to an instrument → estimator → population claim`

Every part of that chain can introduce error. Probability sampling does not depend on each respondent being a typical member of a demographic category. It depends on the documented relationship among the population, the selection procedure and the estimator.

A synthetic-population study uses a different chain:

`human benchmark or profile information → prompt → trained model → decoding or elicitation procedure → generated record → summary → claim about people`

The records may be useful predictions, simulations or stress tests. They are not observations of sampled group members merely because the prompt contains demographic information.

The central claim is:

> A synthetic respondent is a generated model output conditioned on a description or record. It is not a sampled member of the described social group.

The complementary validation claim is:

> Matching a mean, a majority answer or one published result does not establish that the synthetic data preserve human disagreement, subgroup relationships, individual differences or the social processes that produced the original responses.

## Why this session follows Session 6

Session 6 examined interviews in which a model helped produce the questions while a person still produced the account. Session 7 changes the source of the answer.

- **Session 6:** a person answers; the model may alter the interaction and the path through the interview.
- **Session 7:** a model answers as if it were a person or predicts how a population would answer.
- **Session 8:** the course asks whether model-generated data can recover opinions or outcomes that were not observed.

The transition should be explicit. Interview transcripts can be used as inputs to a later “digital twin,” but the transcript remains evidence from a person while the twin's later answer is a model prediction. Gordon et al. make this distinction particularly visible because the same 996 people supply both the human survey answers and the interviews used to construct richer synthetic personas.

## Four things sociology and survey research did before LLMs

The historical section should not become a procession of famous authors. Each source establishes one burden that the contemporary studies must address.

### Computational prehistory: Simulmatics and explicit social simulation

Clinton et al. (2026) make Simulmatics a useful bridge between survey inference and contemporary silicon sampling. In 1960, the company combined accumulated poll records, 480 voter types and issue groupings to predict how electoral segments might respond to campaign moves. The episode establishes that turning past survey traces into a computational public predates LLMs. It also makes two current limitations unusually concrete: excluded people do not reappear because a simulation is more detailed, and a successful real-world outcome does not establish that the model or its advice caused that outcome.

One compact comparison with Orcutt's microsimulation and Schelling's segregation model should clarify that not all artificial populations make the same representational claim. Classical social simulations ordinarily expose simplified rules in order to study policy consequences or emergent patterns. LLM personas instead hide a much richer behavioral model in trained weights and can produce language that sounds like testimony. That fluency makes it especially important to distinguish a modeled unit from a human respondent.

### 1. Link observations to a defined population

Kish and probability-sampling theory establish that representation is a property of a design, not a resemblance between a respondent and a stereotype of a group. Students need to see the target population, sampling frame, selected sample, respondents and estimator as distinct objects.

### 2. Treat error as a chain rather than a single number

Deming and the total-survey-error tradition show that a large sample or small sampling error does not remove coverage, nonresponse, measurement or processing error. Groves and Lyberg's measurement/representation framework should organize this part visually.

### 3. Ask whether the instrument is eliciting a meaningful opinion

Bourdieu's critique of public opinion polling identifies assumptions that become more consequential when a model always produces a fluent answer: that everyone can produce an opinion, that all opinions are equivalent units, and that respondents accept the problem as the pollster has posed it. A generated answer can eliminate “don't know,” ambivalence, refusal and reinterpretation without improving measurement.

### 4. Treat social categories as internally heterogeneous and relational

McCall's discussion of intersectional complexity prevents “woman,” “working class,” “Black,” or “rural” from becoming self-explanatory persona variables. Social positions do not operate as independent labels with one typical opinion attached to each. This provides the sociological basis for later findings on identity flattening and demographic over-determination.

## Definitions students need before the contemporary papers

### Human respondent

A person who was recruited or selected under a documented design and answered a stated instrument. This does not guarantee valid evidence; it identifies the source and inferential chain.

### Aggregate prediction

The model is asked to predict the response distribution for a population or sample as a whole. It does not create one record per simulated individual.

### Demographic persona or silicon sample

The model receives a profile such as age, education, region and political identity, then returns an answer “as this person.” Repeating the procedure creates individual-shaped records, but those records remain draws from a model conditional on the prompt.

### Interview-grounded agent or digital twin

The model receives idiographic material from a real person, such as a long interview transcript, and predicts how that person would respond elsewhere. This supplies more individual information but does not make the prediction an additional observation from that person.

### Assistant persona in model training

Minder et al. use “persona” differently: a desired assistant identity is introduced during pretraining and associated with the assistant role during post-training. This is a short clarification about terminology and model provenance, not evidence about survey simulation.

### Directional and distributional alignment

- **Directional alignment:** Does the model lean toward the option preferred by the human majority?
- **Distributional alignment:** Does the model reproduce how human responses are divided across the options?

Taubenfeld et al. show why these cannot be collapsed. A model can choose the human-majority action while remaining much more confident and homogeneous than the human responses.

## The papers have distinct teaching jobs

### Argyle et al. state the initial positive proposition

Demographic backstories can condition an LLM so that aggregate response patterns resemble those found in human samples. The paper introduces algorithmic fidelity and makes the construction of a silicon sample concrete.

**Teaching job:** Establish the proposition later papers test. Do not begin with the critiques before students understand the actual claim and procedure.

### Kozlowski and Evans define the methodological program

Their six concerns—bias, uniformity, atemporality, disembodiment, linguistic cultures and alien intelligence—show that “realistic text” is not a sufficient target. They argue for validation against the human evidence relevant to the proposed inference.

**Teaching job:** Supply the sociological framework for asking what a simulated subject would have to preserve. This is the constructive required reading.

### Park et al. provide the strongest interview-grounded positive case

Agents built from long interviews with 1,052 people reproduce GSS responses at 85 percent of the participants' own two-week test–retest agreement and reduce some demographic accuracy gaps relative to demographic-only agents.

**Teaching job:** Show why richer individual grounding is attractive and create the question that Gordon et al. directly investigate. State clearly that “85 percent” is relative to human self-replication, not 85 percent raw accuracy.

### Taubenfeld et al. separate majority direction from human disagreement

The Google Research team converts psychometric self-report statements into human-validated situational judgment tests. Across 25 LLMs, models remain highly confident even when human raters are divided. Model self-descriptions also fail to predict their recommendations reliably.

**Teaching job:** Establish the validation distinction before the polling papers. The paper does not use demographic personas, so it should not be described as a test of synthetic populations.

### Boelaert et al. show topic-specific machine bias and compressed variance

Models answer opinion-poll questions with strong bias and low variance, but the direction of the bias changes by topic.

**Teaching job:** Demonstrate that there is no single ideological correction or global fidelity score. This is the required empirical sociology paper.

### Bisbee et al. show how aggregate similarity can conceal other failures

Synthetic feeling-thermometer means can resemble ANES averages while dispersion, regression relationships, prompt stability and time stability fail.

**Teaching job:** Give the first direct empirical demonstration that a matching average is not a sufficient replacement criterion.

### Wang, Morgenstern and Dickerson make the social stakes explicit

Across four LLMs, 3,200 human participants and sixteen identities, models can misportray groups, flatten within-group variation and encourage essentialist prompting.

**Teaching job:** Move from statistical mismatch to epistemic and representational harm. This is the required reading that explains why the error matters sociologically.

### Gordon et al. test whether richer personas solve the problem

The Prolific study compares the same 996 people's survey responses with aggregate model predictions, demographic personas and personas grounded in AI-moderated interview transcripts. Interview material helps relative to demographic-only personas, but does not beat the no-persona aggregate baseline under forced-choice elicitation. Asking for per-persona probabilities and then sampling changes the result more than adding persona detail.

**Teaching job:** Connect Sessions 6 and 7 and show that model elicitation is part of the research design. Post-stratification does not remove the remaining error, which the authors interpret as model error rather than ordinary sample-composition error.

### Chen, Zhu and Zheng show demographic over-determination

Across the GSS and World Values Survey, demographic personas do not outperform strong non-LLM baselines at individual prediction and make demographic groups look more different than the human data do. Their decision exercise shows that these distortions can change which group a user would target.

**Teaching job:** Pair with Wang. Synthetic outputs can flatten people within categories while exaggerating differences between categories.

### Abeliuk, Gaete and Bro extend the question across societies

Models reproduce U.S. public opinion more closely than Chilean opinion, and the largest group disparities follow different social cleavages in the two countries.

**Teaching job:** Prevent the session from treating U.S. demographic categories as the universal test of representation.

## The validation framework

The session should build this framework cumulatively from the sources rather than presenting it as an invented checklist at the beginning.

1. **Population and benchmark:** Which people, place and time define the target? What human evidence supplies the comparison?
2. **Marginal distribution:** Does the full response distribution match, rather than only the mean or modal answer?
3. **Within-group heterogeneity:** Does each synthetic group preserve the spread found among people assigned the same category?
4. **Between-group relationships:** Are group differences represented in the right direction and magnitude, including intersections?
5. **Associations:** Are relationships among opinions, identities and outcomes reproduced?
6. **Stability:** Does the result survive changes in prompt, model, provider, date and decoding procedure?
7. **Baseline:** Does the LLM outperform a simple prediction built from observed human data?
8. **Decision consequence:** Would the synthetic evidence lead to the same substantive decision as the human evidence?
9. **Social grounding:** Is the task one for which textual regularities plausibly contain the relevant information, or does it depend on situated experience the model has not had?

No study needs to answer every question for every use. It must answer the questions required by the claim it wants to make.

## Cumulative sociological example

### Research question

> How are U.S. adults divided over whether government should reduce income differences?

Use the 2024 General Social Survey `EQWLTH` item, a seven-point response scale about whether the federal government should reduce income differences. The exact wording, field year, target population, sample design, weight and public source must be visible before any chart or record appears.

The exact question wording should come from the official GSS questionnaire rather than the shortened variable label in the 2024 codebook, which visibly ends mid-sentence. The question contrasts reducing income differences with the government not concerning itself with those differences, explains the meanings of endpoints 1 and 7, and asks which score comes closest to the respondent's view. Preserve that wording in the prompt; do not silently paraphrase it.

NORC's 2024 Release 3a codebook reports the following **unweighted** frequencies among 2,161 valid responses: 699, 180, 294, 326, 207, 120 and 335 for scale points 1 through 7. The corresponding valid-response percentages are 32.3, 8.3, 13.6, 15.1, 9.6, 5.6 and 15.5 percent. The build should reproduce this codebook table before introducing synthetic answers.

This published distribution is a benchmark for the responding cases. It should not be described as a population estimate of U.S. adults unless the class analysis uses the appropriate public-use data and documented GSS weight. That distinction should become part of the lesson rather than a footnote.

### Why this example works

- It is recognizably sociological rather than an arbitrary numerical exercise.
- The response is an ordered distribution, so majority direction, mean, spread and polarization can diverge.
- The item supports comparisons by education or another clearly documented social position without implying that the category determines the response.
- It connects Bourdieu's concerns about producing an opinion to contemporary concerns about models that always choose a scale point.
- It is manageable in beginner Python.

### Required provenance

The official benchmark source is the *2024 GSS Cross-section Documentation and Public Use File Codebook*, Release 3a (NORC, July 2026), `EQWLTH`, codebook pages 187–188 (PDF pages 265–266): <https://gss.norc.org/content/dam/gss/get-documentation/pdf/codebook/GSS%202024%20Codebook%20R3a.pdf>. NORC permits free use and distribution of the codebook subject to retaining its copyright and permission notice.

The first build may use the published unweighted frequency table directly. If row-level public data are later added, retain the original values and relevant weight and distinguish the unweighted sample distribution from the weighted estimate. If the workbook instead uses a small instructor-authored record set constructed to reproduce the published table, every relevant artifact must say so. Do not label reconstructed teaching records “GSS respondents.”

Synthetic records must preserve:

- the exact profile fields supplied;
- the exact question and response options;
- model and version;
- local or remote access route;
- prompt identifier;
- decoding or elicitation method;
- query date or cached-generation date;
- raw response;
- parsed scale value;
- parser status and any human intervention.

### Three synthetic conditions

Use the same cached profiles and question in three clearly named conditions:

1. **forced choice:** the model returns one scale point;
2. **reported probabilities:** the model assigns a probability to every scale point;
3. **sampled answer:** one scale point is drawn from the reported probabilities using a recorded random seed.

The required class comparison uses cached records. A live local-model demonstration may generate one new forced-choice answer and one probability distribution, but no student's completion mark depends on the live call.

### What the example can establish

- whether the cached synthetic distribution matches the selected human benchmark on stated summaries;
- whether forced choice is more concentrated than probability-based sampling;
- whether a selected subgroup difference is larger or smaller in the synthetic records;
- how results change when the elicitation method changes.

### What it cannot establish

- that the model represents U.S. public opinion generally;
- that the selected demographic profile causes an attitude;
- that a synthetic answer is an observation of a person's belief;
- that one local model or one survey item generalizes to other models, topics, countries or dates.

## Python progression

The existing `group_summaries` function should be replaced. Anonymous groups A and B and the values `1, 5, 3, 3` have no sociological provenance. The manual variance expression also introduces too much syntax while hiding the distribution students are meant to inspect.

### Narrow research job

> Select the responses produced under one source or elicitation method, count how many times each scale point occurs, and convert those counts into proportions that can be compared with the human benchmark.

### Reused Python ideas

- list of dictionaries as the record collection;
- dictionary fields accessed with `record["field"]`;
- `for` loops;
- `if` conditions;
- `.append()`;
- `len()`;
- a function with an argument and returned dictionary.

### One new idea

Initialize the possible response scale explicitly, then update a count for every observed response. This keeps missing response categories visible rather than allowing them to disappear from the returned object.

### Beginner trace

The workbook should show:

1. one complete input record and the source of every field;
2. the list before filtering;
3. the first `if` decision with an actual source value;
4. the selected list after each of the first two iterations;
5. the counts dictionary initialized with all seven scale points;
6. the count before and after one update;
7. the conversion from one count to one proportion;
8. the complete returned distribution and its type;
9. a plain-language comparison with the human distribution;
10. one assertion and exactly what it checks.

Use `statistics.mean()` or `statistics.pvariance()` only after the distribution is visible, and only as a secondary summary. Do not make students decode a generator expression and the variance formula simultaneously.

## Local-model lab

Session 7 is the right point for the fuller local-model laboratory because a synthetic population requires repeated calls and explicit provenance.

The complete process is:

`profile dictionary + question string + answer-format instruction → Python request to the local Ollama server → response dictionary → extracted model text → parsed answer → saved research record`

Students need a plain explanation of each component:

- **Ollama application:** downloads and manages compatible model files and runs a local inference server.
- **Model file:** weights stored on the machine; model size determines memory requirements and affects speed.
- **Local server:** a program listening on the student's own computer, usually through a `localhost` address.
- **Python client request:** a dictionary containing the model name and messages.
- **Response:** another dictionary containing generated text and metadata.

The lab must state the trade-offs rather than imply that local is always better:

- raw profiles and prompts need not be sent to a remote provider;
- local files, logs and transcripts still need protection;
- smaller local models may be slower or less capable than remote models;
- RAM/VRAM and model quantization constrain what can run;
- downloads are large and setup may fail;
- exact model files and versions are easier to preserve than silent hosted-model updates;
- the researcher assumes responsibility for installation, storage and maintenance.

Required work uses cached responses. The live demonstration is optional and has a printed fallback showing the exact request and response objects.

## Reading-to-code map

| Source | Methodological question | Code or data object |
|---|---|---|
| Groves and Lyberg | What inferential chain connects responses to a population? | provenance fields kept beside every record |
| Bourdieu | What does a forced answer hide about opinion production? | missing/refusal/parse status remains explicit |
| McCall | What does a demographic category fail to capture? | profiles remain separate fields; no “typical group member” label |
| Taubenfeld et al. | Does the model preserve disagreement as well as majority direction? | forced-choice and probability-based distributions |
| Boelaert et al. | Does bias and dispersion vary by topic? | full scale counts and proportions, not one mean |
| Wang et al. | Are people flattened within identity categories? | within-group distribution comparison |
| Gordon et al. | Does persona detail or elicitation method change fidelity? | explicit `elicitation` field and three cached conditions |
| Chen et al. | Are group differences exaggerated? | one bounded subgroup comparison against human data |

## Material to keep outside the main session

- Minder et al. receives no more than one terminology/provenance aside.
- ConvApparel belongs in optional notes or a later user-simulation discussion.
- Xie et al.'s full statistical-realism benchmark belongs in Session 8.
- The PNAS survey-fraud paper belongs with data integrity, verification or research agents rather than the main representation argument.
- The systematic review of 182 studies can support one synthesis statement but should not displace close engagement with the focal empirical designs.
- Do not add a general reprise of APIs, OpenRouter and remote providers. Explain only what is needed to understand the local Ollama request and the provenance differences relevant to repeated persona generation.

## Bounded conclusion

Synthetic respondents can be useful for piloting an instrument, testing analysis code, generating hypotheses, exploring sensitivity to prompts or producing explicitly model-based predictions. They should not be described as measurements of a population without validation against the human evidence and population structure required by the claim.

The closing sentence should be ordinary and explicit:

> If the data were generated by a model, say what the model was asked to predict, compare it with the people and distribution that matter, and describe it as a prediction rather than another survey response.

## Self-reflection applied before architecture

The following decisions directly address failures repaired in earlier weeks:

- The lecture begins with a population-estimation problem, not a list of LLM capabilities.
- The opening question receives an answer on the next slide: the distribution alone cannot reveal the inferential chain.
- “What came before” occupies a coherent section and gives each source one job.
- Every contemporary paper enters because it answers a question created by the preceding evidence.
- The positive proposition is presented before the critique.
- Required papers remain central; recent working papers add evidence without expanding the assigned load.
- Terms such as persona, digital twin, directional alignment, distributional alignment, forced choice and post-stratification are defined before their results appear.
- The cumulative example has a real survey question and an explicit provenance requirement.
- The code starts from the research job, not a function header.
- The local-model demonstration shows exact request and response objects and has a cached fallback.
- The slide architecture will specify source images and semantic crop boundaries before implementation.
- Titles will be read aloud as a sequence before the deck is built.
