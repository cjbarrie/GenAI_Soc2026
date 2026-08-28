# Session 7 literature review — synthetic populations and representation

**Status:** Stage 1 audit and Stage 2 literature review for instructor review.  
**Session:** Wednesday, October 21, 2026, 9:30 a.m.–12:15 p.m.  
**Course position:** Human interview evidence (Session 6) → synthetic respondents and population representation (Session 7) → prediction of unobserved opinions and outcomes (Session 8).  
**Review date:** 25 August 2026.

## 1. Audit of the existing Session 7

### What the existing materials are trying to teach

The current week has one defensible central point: a synthetic sample can match a human group mean while eliminating within-group variation. The code makes that point with four records, then calculates a count, mean and population variance for each source-by-group combination.

The required-reading set also has a useful structure:

- Kozlowski and Evans articulate the promise and methodological limits of simulated subjects;
- Boelaert and colleagues test opinion-poll substitution and identify strong, low-variance, topic-specific “machine bias”;
- Wang, Morgenstern and Dickerson make misportrayal, identity flattening and essentialization central concerns.

### What is worth retaining

- The session question: whose attitudes and experiences do synthetic populations represent?
- The transition from Session 6: the respondent, not only the interviewer, is now generated.
- The insistence that aggregate fit and within-group variation are different validation targets.
- The three required papers, which keep the reading load appropriate and give sociology a central place.
- Cached outputs for required work and a small, orally explainable Python procedure.
- A comparison between human and synthetic distributions rather than a demonstration of fluent model personas.

### What is currently too thin or disconnected

#### The sociological method appears too late—or not at all

The slides begin with “we are learning to simulate” and immediately present the three recent papers. They do not explain how survey researchers ordinarily make a sample represent a defined population, or why a generated response is not another sampled respondent. There is no sampling frame, selection process, nonresponse process, measurement process or estimator. Students therefore cannot yet see what “replacement” would have to replace.

#### “Representation” is reduced to a mean and variance

Mean and variance are useful teaching objects, but representation also concerns:

- the target population and sampling frame;
- coverage and nonresponse;
- the distribution of responses, not only two moments;
- associations among variables;
- subgroup and intersectional error;
- topic, model, prompt and time stability;
- whether the question elicits a meaningful human opinion at all.

The current deck announces a “bounded claim” without first establishing this larger methodological landscape.

#### The readings are labels rather than studies

The existing paper slide says “methodological opportunity” and “validation or counterclaim.” It does not identify the data, model, prompt design, human comparison, findings or limits of any paper. “Wang” is not even given a full author list in visible copy. None of the papers is shown as a paper or supported by a readable figure or source passage.

#### The code example is too abstract

Groups “A” and responses `1, 5, 3, 3` make the arithmetic visible but have no recognizable sociological question or provenance. Students cannot tell whether these are observed survey responses, LLM outputs or invented teaching values. The function also introduces tuple keys, `setdefault`, `.items()`, a generator expression and the variance formula in one step. That is too much hidden Python for a class that still needs a full value-by-value trace.

#### The promised local-model progression is missing

The approved workbook progression designates Session 7 as the full local-LLM lab. The current workbook makes no model call and gives no operational account of Ollama, model selection, memory constraints, server start/stop, request/response logging or cached fallback. This gap should be repaired without making live local inference required for completion.

#### The current deck fails the standing slide-review checklist

- The title sequence does not establish a “what came before” section.
- Several slides are slogans or questions rather than explanations.
- Named concepts are not defined.
- Paper designs, findings and citations are incomplete.
- There is no actual source evidence on screen.
- The code's inputs have no sociological provenance.
- The deck has no visible break despite a 165-minute session.
- It moves from literature to code without a cumulative research design.

## 2. The “what came before” literature

### W. Edwards Deming (1944), “On Errors in Surveys”

**Source:** W. Edwards Deming. 1944. “On Errors in Surveys.” *American Sociological Review* 9(4): 359–369. [DOI](https://doi.org/10.2307/2085979).

**Material and question:** Deming catalogued multiple sources of survey error rather than treating sampling error as the only threat to useful inference.

**Teaching job:** Establish that survey quality has long been a sociological methods problem. A response can be generated perfectly according to a procedure and still enter a weak inferential chain.

**Use in class:** A short historical slide, ideally with the published article and the original error list. This makes “representation” part of sociology's own methodological history rather than a new AI fairness vocabulary.

### Leslie Kish and probability sampling

**Sources:** Leslie Kish. 1965. *Survey Sampling*. New York: Wiley; Leslie Kish. 1985. “Sample Surveys versus Experiments, Controlled Observations, Censuses, Registers, and Local Studies.” *Australian Journal of Statistics* 27(2): 111–122. [DOI](https://doi.org/10.1111/j.1467-842X.1985.tb00553.x).

**Material and question:** How can observations from selected units support estimates about a defined population?

**Teaching job:** Define the conventional inferential claim. A probability sample does not work because each respondent is “typical”; it works because the population, frame, selection probabilities and estimator are linked by a documented design.

**Use in class:** Compare “sample a person from a frame” with “sample text from a model conditioned on a persona.” A demographic description in a prompt is not a sampling frame or selection probability.

### Groves and Lyberg (2010), total survey error

**Source:** Robert M. Groves and Lars Lyberg. 2010. “Total Survey Error: Past, Present, and Future.” *Public Opinion Quarterly* 74(5): 849–879. [DOI](https://doi.org/10.1093/poq/nfq065).

**Material and question:** The article reviews the total survey error framework, including the linked measurement and representational inference processes.

**Teaching job:** Give students a sourced map of the chain a survey statistic depends on: construct → measurement → response and target population → frame → sample → respondents. Synthetic respondents do not merely create a new sample; they change or bypass several links at once.

**Use in class:** Reproduce the source's measurement/representation diagram, then mark where an LLM enters. This should become the organizing visual for the first part of the lecture.

### Pierre Bourdieu (1973/1984), “Public Opinion Does Not Exist”

**Source:** Pierre Bourdieu. 1973. “L’opinion publique n’existe pas.” *Les Temps modernes* 318: 1292–1309; reprinted in *Questions de sociologie* (1984). [English teaching copy](https://is.muni.cz/el/fss/podzim2019/POLn4102/um/blok1/Bourdieu_PO_Does_Not_Exist.pdf).

**Material and question:** Bourdieu examines the social assumptions built into opinion polling: that everyone can produce an opinion, that opinions can be treated as equivalent units, and that respondents share the pollster's definition of the problem.

**Teaching job:** Show why an LLM that always returns a fluent answer can make an old polling problem more severe. The absence of “don't know,” ambivalence, reinterpretation or refusal is not necessarily improved data quality.

**Use in class:** Use the source passage listing the three postulates. Apply each one to a persona-prompted synthetic respondent.

### Leslie McCall (2005), “The Complexity of Intersectionality”

**Source:** Leslie McCall. 2005. “The Complexity of Intersectionality.” *Signs* 30(3): 1771–1800. [DOI](https://doi.org/10.1086/426800).

**Material and question:** McCall distinguishes approaches to studying intersectional complexity and shows that categories must be examined relationally and at multiple levels of detail.

**Teaching job:** Prevent “identity group” from becoming a self-explanatory prompt label. A group mean can conceal relationships among gender, race, class and other positions, as well as variation within the named category.

**Use in class:** A bounded bridge into Wang and colleagues. McCall should not be made to “predict” LLM flattening; her role is to establish why internally heterogeneous, relational categories cannot be represented adequately by a single demographic script.

## 3. How silicon sampling entered the literature

### Argyle et al. (2023), “Out of One, Many”

**Source:** Lisa P. Argyle, Ethan C. Busby, Nancy Fulda, Joshua R. Gubler, Christopher Rytting and David Wingate. 2023. “Out of One, Many: Using Language Models to Simulate Human Samples.” *Political Analysis* 31(3): 337–351. [DOI](https://doi.org/10.1017/pan.2023.2).

**Material:** GPT-3 was conditioned on thousands of sociodemographic backstories derived from U.S. surveys and asked to produce responses comparable with human survey samples.

**Claim:** The authors introduce “algorithmic fidelity” and argue that demographic conditioning can recover meaningful patterns across subpopulations.

**Teaching job:** Establish the original positive proposition that later papers test. Students need to see the actual construction: human profile → prompt → repeated model output → comparison with human answers.

**Status in Session 7:** In-class historical evidence, not required reading. It should introduce the claim that the three required papers qualify.

### Bisbee et al. (2024), “Synthetic Replacements for Human Survey Data?”

**Source:** James Bisbee, Joshua D. Clinton, Cassy Dorff, Brenton Kenkel and Jennifer M. Larson. 2024. “Synthetic Replacements for Human Survey Data? The Perils of Large Language Models.” *Political Analysis* 32(4): 401–416. [DOI](https://doi.org/10.1017/pan.2024.5).

**Material:** ChatGPT personas generated feeling-thermometer scores for eleven sociopolitical groups, compared with the 2016–2020 ANES.

**Finding:** Synthetic averages often corresponded closely with ANES averages, while synthetic responses showed less variation, regression coefficients differed and outputs changed with small prompt changes and over a three-month period.

**Teaching job:** Provide the clean empirical bridge to the workbook: a matching average does not warrant replacement when dispersion, associations and stability fail.

**Status in Session 7:** In-class evidence or optional reading. Boelaert supplies the required sociology-centered version of the critique.

## 4. Recommended required readings

### Kozlowski and Evans (2025), “Simulating Subjects”

**Full citation:** Austin C. Kozlowski and James A. Evans. 2025. “Simulating Subjects: The Promise and Peril of Artificial Intelligence Stand-Ins for Social Agents and Interactions.” *Sociological Methods & Research* 54(3): 1017–1073. [DOI](https://doi.org/10.1177/00491241251337316).

**Material and question:** A methodological synthesis of work using LLMs to simulate culturally situated subjects and interactions.

**Principal contribution:** The paper identifies six model characteristics that threaten realistic simulation: bias, uniformity, atemporality, disembodiment, linguistic cultures and alien intelligence. It argues for an ongoing methodological program with validation against human-subject data.

**Teaching job:** Supply the strongest sociological account of what a simulated subject would need to represent and why validation must remain task-specific. It is the constructive paper, not a general endorsement of replacement.

**Keep required:** Yes.

### Boelaert et al. (2025), “Machine Bias”

**Full citation:** Julien Boelaert, Samuel Coavoux, Étienne Ollion, Ivaylo D. Petev and Patrick Präg. 2025. “Machine Bias: How Do Generative Language Models Answer Opinion Polls?” *Sociological Methods & Research* 54(3): 1156–1196. [DOI](https://doi.org/10.1177/00491241251330582).

**Material and question:** LLM responses to opinion-poll questions are compared with human public-opinion distributions.

**Principal finding:** The models show strong bias and low variance on individual topics, but the direction of bias changes across topics. The problem is not one stable ideological skew that could be corrected with a single weight.

**Teaching job:** Make topic-specific bias and compressed variance visible. It directly supports the claim that synthetic respondents cannot currently replace people in opinion or attitudinal research.

**Keep required:** Yes.

### Wang, Morgenstern and Dickerson (2025), identity flattening

**Full citation:** Angelina Wang, Jamie Morgenstern and John P. Dickerson. 2025. “Large Language Models That Replace Human Participants Can Harmfully Misportray and Flatten Identity Groups.” *Nature Machine Intelligence* 7: 400–411. [DOI](https://doi.org/10.1038/s42256-025-00986-z).

**Material and question:** Four LLMs are compared with human studies involving 3,200 participants across sixteen demographic identities.

**Principal finding:** Models can misportray groups, flatten within-group differences and encourage essentialist identity prompting. The authors connect replacement to positionality, lived experience and epistemic injustice. Inference-time techniques reduce but do not remove the harms.

**Teaching job:** Move beyond statistical fit to the social and epistemic stakes of replacing participants whose identities matter to the task.

**Keep required:** Yes.

## 5. Additions from the 25 August literature update

### Gordon et al. (2026), the Prolific "fidelity paradox" study

**Full citation:** Andrew Gordon, Nora Petrova, John Burden, Oriol J. Bosch and Ning Ding. 2026. "Do Richer Personas Improve LLM Survey Simulation? A Fidelity Paradox." Prolific Academic Ltd working paper, posted 20 August 2026. [SSRN](https://ssrn.com/abstract=7306183); [DOI](https://doi.org/10.2139/ssrn.7306183).

**Material:** The authors fielded a 21-item political-opinion and consumer survey to a politically representative U.S. Prolific sample (`N = 996`) in April 2026. In the same session, participants completed an AI-moderated voice interview about values, moral reasoning, lifestyle and institutional trust. The authors then attempted to reproduce the same people's survey answers with Claude Sonnet 4.6 and GPT-5.4 at four levels:

1. the survey questions alone, asking for the aggregate distribution;
2. the questions plus the sample's aggregate demographic composition;
3. one demographic persona for each respondent;
4. the demographic persona plus that respondent's verbatim interview transcript, with a separate condition using an LLM-distilled values profile.

Within the interview-grounded condition, they also compare a forced single answer, a reasoning prompt, an instruction intended to discourage safe modal answers, and a probability distribution over answer options for each persona.

**Principal findings:** More personal information does not produce a simple improvement in accuracy. Forced-choice demographic personas roughly triple distributional error relative to asking the model for an aggregate distribution. Verbatim interview transcripts help relative to demographic personas, but they remain worse than the no-persona aggregate baseline; compressing the interviews into structured profiles discards useful differentiation. The largest gain comes from changing the output format: asking each persona for probabilities over all answer choices and then sampling from those probabilities reduces distributional error by 35–48 percent. Even the best condition remains more than five times above the sampling-variation floor the authors estimate for two real surveys of this size. Post-stratification does not remove the remaining error.

The paper also shows why a single "accuracy" number is inadequate. A condition can identify the modal answer while badly misrepresenting the full distribution. In their results, the demographic-persona condition can look good on plurality-winner accuracy precisely because it pushes respondents toward the same modal response.

**Teaching job:** This should become a focal empirical study in the second half of the lecture. It connects Session 6's AI-moderated interviewing directly to Session 7: even a real interview transcript does not turn a model into the interviewed person. It also gives the Python exercise a better purpose. Students can compare an observed distribution with four synthetic conditions, then see how a forced answer and a probability distribution lead to different synthetic samples.

**Status:** Prominent in-class study and recommended optional reading. The paper is 54 pages and appeared only two months before the class meeting, so it should not automatically displace a required sociology reading. Reconsider that decision at the synthesis stage.

**Local source:** `literature/source_pdfs/session07/gordon_et_al_2026_fidelity_paradox.pdf`.

### Taubenfeld et al. (2026), behavioral dispositions in LLMs

**Full citation:** Amir Taubenfeld, Zorik Gekhman, Lior Nezry, Omri Feldman, Natalie Harris, Shashir Reddy, Romina Stella, Ariel Goldstein, Marian Croak, Yossi Matias and Amir Feder. 2026. "Evaluating Alignment of Behavioral Dispositions in LLMs." arXiv:2602.11328. Google Research. [Paper](https://arxiv.org/abs/2602.11328); [Google Research account](https://research.google/blog/evaluating-alignment-of-behavioral-dispositions-in-llms/).

**Material:** The authors begin with established psychological self-report measures covering empathy, emotion regulation, assertiveness and impulsiveness. They convert statements from those instruments into realistic Situational Judgment Tests (SJTs), each offering two opposing courses of action. Three independent annotators must agree that the generated scenario and actions represent the intended disposition. The methods section reports 2,576 generated SJTs and 2,357 retained after validation; the abstract and introduction describe this more loosely as a final dataset of 2,500. Ten raters per SJT, drawn from a pool of 550 participants, establish a distribution of human preferences. The authors then sample twenty free-form responses per scenario from each of 25 open- and closed-weight LLMs and map them to the two actions using an LLM judge.

**Principal findings:** The study separates two targets that are easy to conflate:

- **Directional alignment:** When humans strongly agree on an action, does the model lean in the same direction? Larger and frontier models perform well under unanimous human agreement, but some still choose against the human majority in 15–20 percent of cases when agreement falls below 90 percent. Smaller models often perform much worse.
- **Distributional alignment:** When humans disagree, does the model reproduce that disagreement? All 25 models are markedly overconfident. Even when human preferences are close to 50:50, repeated model responses remain concentrated above roughly 90 percent on one action.

The direction of that overconfidence varies across models, suggesting that post-training and other model-specific procedures produce different behavioral tendencies. The paper also finds substantial discrepancies between models' questionnaire-style self-descriptions and their recommendations in the corresponding scenarios.

**Teaching job:** This is worth a short but substantive sequence immediately before the synthetic-population evidence. It supplies three ideas that recur throughout the week:

1. a fluent answer is not evidence of a stable human-like disposition;
2. matching the majority direction is different from matching the distribution of disagreement;
3. what a model says about "itself" is not a validated measure of how it will respond in an applied situation.

The most useful visual pairing is Figure 1, which makes the human/model comparison pipeline explicit, followed by Figure 3, where model confidence remains high as human consensus falls. Figure 4 is useful only if the lecture needs the model-size comparison; the heatmap is too dense to introduce the paper on its own.

**Relationship to Week 7:** This paper does not simulate demographic groups or claim that models can replace survey respondents. Its human preference distributions nevertheless provide a controlled demonstration of the same error that matters for synthetic populations: models can recover an apparent majority position while removing genuine human disagreement. It therefore strengthens the conceptual bridge into Boelaert, Wang and Gordon without duplicating them.

**Limits to state explicitly:** The SJTs reduce each situation to two reference actions, the analysis concerns single-turn advice, and the human rater pool is drawn primarily from the United States and United Kingdom. "Human alignment" here therefore means correspondence with this study's rater distributions, not a universal account of appropriate social behavior.

**Status:** High-priority in-class evidence; optional rather than required reading.

**Local source:** `literature/source_pdfs/session07/taubenfeld_et_al_2026_behavioral_dispositions.pdf`.

### Minder et al. (2026), "Synthetic Persona Pretraining"

**Full citation:** Julian Minder, Viktor Moskvoretskii, Raghav Singhal et al. 2026. "Synthetic Persona Pretraining: Alignment from Token Zero." arXiv:2608.13482, version 1, 13 August 2026. [Paper](https://arxiv.org/abs/2608.13482).

**Material:** The authors append constitution-guided, first-person normative reflections to about ten percent of pretraining documents, then compare when the intervention is introduced. Their data-matched experiments train models up to 3B parameters on 500B tokens and evaluate constitution following, choices in moral dilemmas and jailbreak robustness. A later supervised-fine-tuning stage is used to associate the pretrained persona with the assistant role, which the authors call "persona binding."

**Principal finding:** Introducing the persona-related material from the start of pretraining improves constitution following and some out-of-distribution value measures relative to introducing the same material late. All intervention variants improve jailbreak robustness, but that effect can be brittle under template changes and later training. The paper therefore provides evidence that the apparent identity and values expressed by an assistant depend on the model's training history, not only the persona text in the current prompt.

**Teaching job:** Use this as a short conceptual aside called **"Persona means two different things here."** In survey simulation, a persona is a description placed in the prompt so that a model will role-play a respondent. In this paper, a persona is a comparatively persistent assistant identity the authors attempt to install during model training. The distinction matters: a prompted synthetic respondent is generated through a model whose own behavioral tendencies have already been shaped by pretraining and post-training. Adding a demographic biography does not erase those tendencies.

**Scope warning:** This is an alignment paper, not evidence that LLMs represent human populations more accurately. It has no human survey sample and should not be used to support a claim about synthetic respondents. The author-affiliation page in the supplied PDF does not list Google; the paper is led by researchers affiliated with EPFL and several partner institutions.

**Status:** Brief in-class aside or workbook extension, not required reading.

**Local source:** `literature/source_pdfs/session07/minder_et_al_2026_synthetic_persona_pretraining.pdf`.

### Park et al. (2024/2025), the strongest positive digital-twin proposition

**Full citation:** Joon Sung Park, Carolyn Q. Zou, Aaron Shaw, Benjamin Mako Hill, Carrie Cai, Meredith Ringel Morris, Robb Willer, Percy Liang and Michael S. Bernstein. 2024. "Generative Agent Simulations of 1,000 People." arXiv:2411.10109. [Paper](https://arxiv.org/abs/2411.10109).

**Material:** The team recruited 1,052 people, conducted roughly two-hour qualitative interviews about their lives, constructed interview-grounded agents and tested them on General Social Survey questions, Big Five measures, economic games and experimental replications.

**Finding and limit:** The headline result is that agents reproduced participants' GSS answers at 85 percent of the participants' own two-week test–retest agreement, and interview-grounded agents reduced some racial and ideological accuracy gaps relative to demographic-only agents. This is not the same as 85 percent raw accuracy, and performance varies by outcome.

**Teaching job:** Present this before Gordon et al. The Prolific paper is intelligible as a direct test of the claim that detailed interviews provide the missing individual grounding. The contrast is more productive than treating one paper as simply right and the other wrong: they use different outcomes, metrics, prompts and validation targets.

**Status:** In-class positive countercase. It also clarifies the continuity between Sessions 6 and 7.

## 6. Other recent, consequential evidence

### Chen, Zhu and Zheng (2026), demographic over-determination

**Full citation:** Zihan Chen, Di Zhu and Lei Nico Zheng. 2026. "When Synthetic Users Fail: A Cross-Domain Benchmark of LLM-Simulated Human Survey Responses." arXiv:2607.26348, 28 July 2026. [Paper](https://arxiv.org/abs/2607.26348).

**Material:** Four models from two model families are evaluated against held-out human responses from the U.S. General Social Survey and the World Values Survey. Crucially, the LLMs are compared with simple non-LLM prediction baselines rather than being judged only by whether their answers look plausible.

**Principal finding:** No LLM beats the strongest baseline at individual-level prediction; on the World Values Survey, all fall well below it. The models also make demographics appear much more predictive of attitudes than they are among people. In a segment-targeting exercise, this inflates between-group differences two- to fourfold and often identifies the wrong group to target.

**Teaching job:** This is a particularly strong extension of Wang and colleagues. "Flattening" within a group and "over-determining" differences between groups can happen together: model outputs can make members of each category too similar while making categories look too different from one another. Use one result figure in class, but retain preprint status in the citation.

**Status:** High-priority in-class evidence or optional reading.

### Kuric, Demcak and Krajcovic (2026), systematic review of 182 studies

**Full citation:** Eduard Kuric, Peter Demcak and Matus Krajcovic. 2026. "Synthetic Participants Generated by Large Language Models: A Systematic Literature Review." Research Square preprint, posted 10 March 2026. [DOI](https://doi.org/10.21203/rs.3.rs-9057643/v1).

**Material:** A systematic review of 182 studies using LLM-generated synthetic participant data across several research traditions.

**Principal contribution:** The review organizes recurring problems into cognitive misalignment, distortions and bias, misleading believability, and overfitting or contamination. Across prompting, participant modeling and model-selection strategies, reported fidelity improvements are generally modest. The authors recommend treating synthetic participants as heuristic supplements rather than human substitutes.

**Teaching job:** Use the review to show that the failures in the focal studies are recurring patterns rather than isolated demonstrations. It should not replace close reading of well-designed validation studies, and its preprint status needs to remain visible.

**Status:** One synthesis slide or optional reading.

### Stojanov (2026), participant-matched psychological profiles

**Full citation:** Ana Stojanov. 2026. "Do Participant-Matched LLM Personas Approximate Human Survey Data?" *Personality and Individual Differences* 261: 113915. [DOI](https://doi.org/10.1016/j.paid.2026.113915).

**Material:** `N = 177` participants answered measures covering 91 psychological constructs. GPT-4o personas received either demographics alone or demographics plus the participant's Big Five scores.

**Finding:** Big Five conditioning yields small improvements in means and individual similarity and reduces under-dispersion, but the synthetic answers still reproduce individual differences only modestly.

**Teaching job:** A compact published corroboration of the Prolific paper's conclusion: added personal information can help on some targets without producing a convincing substitute for the person.

**Status:** Optional reading or citation on the interview-grounding comparison slide.

### Gao et al. (2025), a controlled behavioral failure

**Full citation:** Yuan Gao, Dokyun Lee, Gordon Burtch and Sina Fazelpour. 2025. "Take Caution in Using LLMs as Human Surrogates." *Proceedings of the National Academy of Sciences* 122(24): e2501660122. [DOI](https://doi.org/10.1073/pnas.2501660122).

**Material and finding:** Across multiple models and prompting approaches, the authors test whether LLMs reproduce the distribution of human play in the 11–20 money-request game. Nearly all approaches fail, with results changing unpredictably with language, assigned role and safety behavior.

**Teaching job:** This is a clean published reminder that verbal plausibility is not behavioral validation. It also returns to the embodiment question from Session 4: models do not share the incentives and stakes through which human strategies are formed.

**Status:** One in-class example; do not add to the required load.

### Meshi et al. (2026), the Google Research user-simulation study

**Full citation:** Ofer Meshi, Krisztian Balog, Sally Goldman, Avi Caciularu, Guy Tennenholtz, Jihwan Jeong, Amir Globerson and Craig Boutilier. 2026. "ConvApparel: A Benchmark Dataset and Validation Framework for User Simulators in Conversational Recommenders." *Proceedings of EACL 2026*: 5270–5304. [Paper](https://aclanthology.org/2026.eacl-long.244/); [Google Research account](https://research.google/blog/convapparel-measuring-and-bridging-the-realism-gap-in-user-simulators/).

**Material and finding:** The authors collect human conversations with both effective and deliberately poor apparel-recommendation agents, then compare prompted, retrieval-based and fine-tuned Gemini user simulators. Data-driven simulators improve on the prompted baseline, especially when reacting to previously unseen agent behavior, but a classifier still identifies nearly all simulated conversations as synthetic.

**Teaching job:** This is an optional boundary case: simulating users to test an AI system is a different goal from estimating a population's opinions, but both require validation against human behavior. It should not be presented as the Google behavioral-dispositions paper.

**Status:** Optional aside or later workbook note.

### Kuric, Demcak and Krajcovic (2026), real design preferences

**Full citation:** Eduard Kuric, Peter Demcak and Matus Krajcovic. 2026. "Distorted Perspectives of LLM-Simulated Preferences: Can AI Mislead Design?" arXiv:2605.18311. [Paper](https://arxiv.org/abs/2605.18311).

**Material and finding:** The authors aggregate 29 real-world visual preference studies involving 2,073 participants and 78 tasks. Across changes in model, reasoning, sampling and persona design, simulated choices and justifications differ systematically from human preferences; synthetic explanations are more generic and more inclined to praise the designs.

**Teaching job:** This is the best recent multimodal example of a failure that cannot be reduced to survey wording. It connects the week to the broader course question of sensory and situated experience, but belongs in optional material unless the lecture needs a concrete visual case.

## 7. Newer evidence already identified for use in class or as optional reading

### Abeliuk, Gaete and Bro (2026), cross-societal fairness

**Full citation:** Andrés Abeliuk, Vanessa Gaete and Naim Bro. 2026. “Auditing Socio-Demographic and Cross-Societal Fairness in LLM-Simulated Public Opinion.” *EPJ Data Science* 15: 75. [DOI](https://doi.org/10.1140/epjds/s13688-026-00673-y).

**Material:** Nationally representative survey data from Chile and the United States, evaluated across sociodemographic groups.

**Finding:** LLMs reproduce U.S. responses more faithfully than Chilean responses. The largest disparities also follow different social cleavages in the two countries.

**Teaching job:** Demonstrate that “which groups are represented?” is also “which societies and cleavages are represented?” This is the best current geographic extension of the core week.

**Status:** In-class evidence or optional reading. Do not add to the required load.

### Wang et al. (2025), SocioBench

**Full citation:** Jia Wang, Ziyu Zhao, Tingjuntao Ni and Zhongyu Wei. 2025. “SocioBench: Modeling Human Behavior in Sociological Surveys with Large Language Models.” *Proceedings of EMNLP 2025*: 26257–26289. [DOI](https://doi.org/10.18653/v1/2025.emnlp-main.1335).

**Material:** More than 480,000 ISSP records from over thirty countries, ten sociological domains and more than forty demographic attributes.

**Finding:** Individual-level simulation accuracy is about 30–40%, with significant differences across topics and demographic groups.

**Teaching job:** Show that a large, cross-national benchmark does not yield one general fidelity score. Scale exposes domain and subgroup variation.

**Status:** Optional or one in-class figure. It is technically useful but less sociologically developed than the required papers.

### Xie et al. (2026), statistical realism

**Full citation:** Yueqi Xie et al. 2026. “Evaluating the Statistical Realism of LLM-Generated Social Science Data.” *Proceedings of the National Academy of Sciences* 123(19): e2538145123. [DOI](https://doi.org/10.1073/pnas.2538145123).

**Teaching job here:** A closing bridge only: mean, variance and subgroup comparisons are three of several possible targets. The full paper belongs in Session 8, where individual prediction, population distributions, associations, treatment effects and extrapolation can be separated.

## 8. Synthesis of the literature

The most useful organizing distinction is not “human data versus fake data.” It is the inferential chain that produces a population claim.

### Human survey sample

`defined population → sampling frame → selected people → responses to an instrument → estimator → population claim`

Each arrow has known or at least nameable error sources. The respondents are not expected to be individually typical. Representation comes from the design linking selected people to the target population.

### Persona-conditioned synthetic sample

`human benchmark or demographic profile → prompt → model and training distribution → decoding choices → generated responses → summary → claim about people`

This can be useful, but it is a different inferential chain. Prompting a model with “You are a 45-year-old working-class woman…” does not select a person from that social group. It asks a model to generate text associated with a description of that group.

The literature identifies at least nine separate validation questions:

1. **Marginal fit:** Does the overall average or distribution match?
2. **Within-group variation:** Does the synthetic group contain the heterogeneity present among people?
3. **Between-group relationships:** Are social differences and intersections represented in the right direction and magnitude?
4. **Associations:** Do relationships among attitudes and characteristics match human data?
5. **Stability:** Do results persist across prompts, models, providers, time and decoding settings?
6. **Social grounding:** Is the model representing lived positions and contexts, or reproducing textual stereotypes associated with labels?
7. **Baseline performance:** Does the LLM improve on a simple prediction from observed human data, or only on an intentionally weak comparison?
8. **Elicitation dependence:** Does the conclusion change when the model makes a forced choice, reports probabilities or is sampled repeatedly?
9. **Decision consequence:** Would the synthetic result lead to the same substantive decision as the human evidence?

No single score answers all nine. A model can match a population mean or identify the plurality response while failing individual-level, relational or decision-relevant targets.

## 9. Recommended teaching architecture before slide planning

### Central question

What would have to be true for generated answers to stand in for answers from members of a defined population?

### Proposed cumulative example

Use one real, clearly worded public-opinion item with:

- a small cached human benchmark;
- synthetic responses generated from the same profile fields;
- visible provenance for every record;
- at least two social groups;
- the same mean in one comparison but different dispersion;
- a second failure involving subgroup or topic differences.

Avoid anonymous groups “A” and “B.” The response scale, question wording, source, group definition, model, prompt and decoding settings must appear before the result. If a real benchmark cannot be distributed cleanly, use instructor-authored teaching records and label them as such on every relevant artifact.

### Recommended sequence

1. Return to Session 6: a human answered there; what changes when the model answers?
2. Show how a conventional sample supports a population claim.
3. Use Deming/Groves to separate measurement from representation.
4. Use Bourdieu to ask whether a generated answer is evidence that an opinion exists.
5. Use McCall to ask what a demographic category can and cannot encode.
6. Define persona prompting and silicon sampling with an exact input/output example.
7. Introduce Argyle's positive proposition.
8. Introduce Park et al.'s interview-grounded digital twins as the strongest positive proposition.
9. Test the proposition with Bisbee, the three required papers and Gordon et al.'s matched Prolific study.
10. Use Chen et al. to distinguish within-group flattening from between-group over-determination.
11. Compare validation targets: overall distribution, within-group variation, associations, subgroup error, stability, baselines and decision consequences.
12. Use Taubenfeld et al. to separate majority-direction accuracy from the distribution of human disagreement.
13. Briefly distinguish a prompted respondent persona from Minder et al.'s pretrained assistant persona.
14. Run a small cached human-versus-synthetic comparison that contrasts forced choices with sampled per-persona probabilities.
15. Explain and optionally demonstrate the local Ollama pipeline.
16. Trace the Python summary one value at a time.
17. End with a bounded use claim and a bridge to Session 8.

## 10. Provisional reading-load decision

Keep the three existing required readings for the moment: Kozlowski and Evans for the sociological methodological argument, Boelaert et al. for direct opinion-poll validation, and Wang, Morgenstern and Dickerson for identity flattening and epistemic harm. Make Gordon et al. a substantial instructor-led case rather than a fourth required paper. At the synthesis stage, consider replacing Boelaert with Gordon only if the latter's matched human/interview/synthetic design is needed for the workbook strongly enough to justify assigning a new 54-page working paper. Do not make the alignment-focused Minder et al. paper required for this week.

## 11. Python and local-model implications

The code should be rewritten around a recognizable research record. Each row should include at least:

- `source`: human or synthetic;
- `question_id`;
- `group` or explicitly named profile fields;
- `response`;
- `model`, `prompt_id` and `run_id` for synthetic rows;
- provenance indicating whether the record is empirical, cached model output or instructor-authored.

The required function should first make one comparison fully transparent. Avoid introducing tuple keys, `setdefault`, `.items()`, a generator expression and a variance formula simultaneously. A clearer progression is:

1. select the values for one source and group;
2. print the selected list;
3. calculate `n` and mean;
4. calculate or call a clearly explained measure of spread;
5. return a small dictionary;
6. repeat through a separately explained loop only after the one-group case is understood.

The local-model component should show:

`profile dictionary + survey question + instructions → Ollama request → one generated answer → parsed response record → saved provenance`

Required student work must use cached outputs. The live local call is an instructor demonstration and optional student extension, with explicit hardware and model-size routes. Starting the server, choosing a model that fits, inspecting logs and stopping the server should be documented in the workbook.

## 12. Recommendation at Review Gate 1

Keep the three required readings provisionally. Add Deming/Groves, Bourdieu, McCall, Argyle and Bisbee as in-class foundations. Use Taubenfeld et al. to establish the difference between identifying a majority position and representing human disagreement. Use Park et al. to state the strongest interview-grounded digital-twin proposition, Gordon et al. to test it with matched Prolific respondents, and Chen et al. to show the practical consequences of demographic over-determination. Use Minder et al. only to distinguish a prompted respondent persona from a model persona shaped during training. Do not add all of these to the assigned reading load.

The synthesis should be organized around a simple claim:

> A synthetic respondent is a draw from a model's conditional text distribution, not a sampled member of a social group. Any claim about people therefore depends on validation against the particular population structure and outcome the study needs.

This moves beyond the current “means versus variance” slogan while retaining it as the first computational diagnostic.
