# Week 11 literature audit: language, inequality and institutional power

**Prepared:** 27 October 2026  
**Scope:** literature and publication status checked through 27 October 2026  
**Status:** approval gate 1 approved on 27 October 2026; revised Gate 2 architecture in development

## Current course material to replace

The existing Week 11 research-agent materials belong to the superseded course sequence. If the direction below is approved, replace rather than revise:

- the research-agent question and slide deck;
- the transparent tool-call exercise;
- the agent, harness and provenance sequence as the organizing argument;
- the old Week 11 reading list and exercise links.

Agent and harness concepts remain available in the glossary. They are not the subject of this class.

## Recommended sociological question

**How can language models reproduce inequality through language, even when a social category is not named?**

The question has two connected parts:

1. **Downstream institutional judgment:** a model can treat socially marked ways of speaking differently when it recommends occupations, assesses candidates or helps allocate opportunities.
2. **Upstream institutional influence:** governments, firms and other powerful organizations can shape the text environment from which models learn.

This is narrower than a general lecture on “AI bias.” It gives students a way to distinguish:

- a linguistic difference from the social value assigned to it;
- an overt category label from a covert social cue;
- unequal model outputs from unequal outcomes in a deployed institution;
- an audit finding from an explanation of where the difference came from;
- a model's fluent justification from evidence about its decision process;
- post-training restraint from the removal of an underlying association;
- provider or model differences from stable facts about “AI.”

## Proposed bounded conclusion

Matched comparisons can show that a model responds differently when semantically similar language carries different social cues. They cannot, by themselves, establish how often this occurs in a population of uses, why the model behaves that way, or what happens when an organization deploys it. Institutional power enters both downstream, through the rules that connect model outputs to decisions, and upstream, through control over the language and data on which models are trained.

## Historical and sociological lineage

### 1. Language was never only a neutral carrier of information

Pierre Bourdieu's “The Economics of Linguistic Exchanges” rejects an account of speech as an exchange among socially interchangeable senders and receivers. The value of a way of speaking depends on the linguistic market, the authority of the speaker and the institutions able to recognize one form as legitimate. Schools, professions and bureaucracies reward some competences and devalue others.

The teaching job is precise: a model does not discover that one variety is intrinsically more professional, intelligent or authoritative. It encounters distinctions produced in a social world where institutions already assign unequal value to speakers and styles. Bourdieu also prevents the class from treating “standard” language as the unmarked baseline.

Useful original evidence includes the article's discussion of legitimate language; the claim that linguistic characteristics affect employment, schooling and professional cooperation; and the examples showing that the social relationship is condensed in the form of an utterance.

### 2. Sociologists and social psychologists learned to isolate evaluations of language

Lambert, Hodgson, Gardner and Fillenbaum's 1960 matched-guise experiment presented bilingual Montreal speakers in English and French guises. Listeners did not know that the same speakers produced both recordings. The design made it possible to compare evaluations while holding the voice and much of the propositional content fixed.

The method does not reveal an attitude free of context, and evaluations can vary across listeners and settings. Its historical importance is that it turns socially patterned listening into an empirical comparison rather than assuming that linguistic form carries a fixed social meaning.

This is the direct methodological ancestor of Hofmann et al.'s “matched guise probing.” It belongs in the lecture and additional readings rather than the required list because the modern article explains the adaptation and the full 1960 article has a narrower historical function.

### 3. Linguistic profiling connected evaluation to an institutional gate

Purnell, Idsardi and Baugh (1999) used telephone housing inquiries and perceptual experiments to study linguistic profiling. The same speaker used Standard American English, African American Vernacular English and Chicano English guises. Their four experiments showed that listeners could identify social information from very brief speech and that housing access could differ on the basis of how a caller sounded.

This changes the outcome from an adjective rating to access to a resource. It also makes the institutional sequence visible:

`speech cue -> listener classification -> gatekeeping response -> possible housing inequality`

The article is the strongest pre-LLM substantive example for the lecture. It also supplies original visual material: the published article, the experimental sequence and the reported housing results.

### 4. Raciolinguistic research shifts attention from the speaker to the listener

Flores and Rosa (2015) criticize “appropriateness” models that treat standardized academic language as an objective target. Their raciolinguistic account asks how racialized listening positions some speakers as deficient even when those speakers approximate the named standard.

This matters for the LLM comparison. The research question is not whether African American English is less clear or correct. It is how a listening or evaluating system assigns social meaning to linguistic features. The same caution applies to model audits: translating an AAE text into SAE should not be described as correcting it.

### 5. Earlier language technologies already produced unequal technical performance

Koenecke et al. (2020) audited five commercial automatic speech-recognition systems using sociolinguistic interviews. Average word error rate was 0.35 for Black speakers and 0.19 for white speakers. This is an important pre-LLM technological bridge, but it is a different kind of disparity from Hofmann et al.'s finding:

- speech recognition can fail to transcribe a speaker accurately;
- an LLM can receive intelligible text and still attach unequal social associations or recommendations to it.

The distinction should be explicit. A transcription error and a generated allocational judgment are not interchangeable measures of bias.

### 6. Audit and correspondence studies test unequal treatment by holding qualifications fixed

Employment and housing audit studies vary a socially meaningful cue while holding relevant qualifications constant. This tradition supplies the logic for contemporary LLM audits. It also supplies several cautions:

- the cue must plausibly signal the construct under study;
- paired materials must be comparable on other relevant dimensions;
- one prompt and one run are not an audit;
- an audit estimates treatment differences in a defined system and task, not the source of the disparity;
- a model audit does not establish what an employer, landlord or court actually does with the output.

This section can mention Bertrand and Mullainathan (2004) and Pager (2003) without turning them into additional assigned readings. The lecture's historical emphasis remains language and institutional judgment.

### 7. LLMs change the object being audited

LLMs differ from earlier classifiers and speech systems in several relevant respects:

- the same general-purpose model can interpret, rank, recommend and justify across many institutional tasks;
- social cues can be inferred from open-ended language without an explicit category field;
- generated justifications can make an unequal recommendation appear individualized and professionally reasoned;
- outputs depend on prompt, model version, provider, post-training and sampling;
- proprietary systems conceal most training data and internal changes;
- post-training can alter what a model says overtly without removing covert associations;
- model outputs can be inserted into organizational workflows at different points and with different authority.

The novelty is therefore not that technologies can discriminate. It is the flexible, generative and widely reusable form through which language can be converted into judgments.

### 8. Institutions also shape models before a user sends a prompt

Waight et al. (2026) move the lecture upstream. State institutions can influence the media environment, which affects the text available for training. The paper's six studies proceed from evidence of Chinese state-coordinated media in training corpora, to memorization tests, to additional pretraining of an open model, to audits of commercial systems, and finally to a 37-country comparison.

This is not another downstream discrimination audit. Its role is to demonstrate a plausible route through which institutional power becomes part of model output. It also gives the class a strong example of triangulation: the cross-national association alone is not treated as proof of the mechanism.

## Recommended required readings

Assign all three articles in full. Each has a different teaching job.

### 1. Sociological anchor

**Bourdieu, Pierre. 1977. “The Economics of Linguistic Exchanges.” *Social Science Information* 16(6): 645–668. https://doi.org/10.1177/053901847701600601.**

- **Question:** How do social position and institutional markets give linguistic forms unequal value and force?
- **Evidence and approach:** Sociological theory developed through examples from education, employment, professional encounters, classed speech and the practical adjustment of utterances to social relationships.
- **Principal contribution:** Linguistic competence has value only in relation to a market that authorizes some speakers and forms as legitimate. Communication is also a relation of symbolic power.
- **Limitation for this class:** It does not study automated systems, race in the contemporary United States or causal effects of particular language features. It supplies the sociological problem rather than an LLM prediction.
- **Teaching job:** Prevent the class from treating model judgments as reactions to intrinsically superior or inferior language.
- **Useful source material:** article title page; passages on legitimate language and the linguistic market; the discussion of employment and professional cooperation; examples of the social relationship expressed through linguistic form.
- **Publication status:** final published article.

### 2. Contemporary matched-guise audit

**Hofmann, Valentin, Pratyusha Ria Kalluri, Dan Jurafsky, and Sharese King. 2024. “AI Generates Covertly Racist Decisions about People Based on Their Dialect.” *Nature* 633: 147–154. https://doi.org/10.1038/s41586-024-07856-5.**

- **Question:** Do language models reproduce racialized stereotypes and decisions when race is not named but dialect features signal African American English?
- **Material:** Parallel AAE and Standardized American English texts drawn from the Corpus of Regional African American Language and transformed with a published dialect-alignment method; five language models; prompts concerning traits, occupations and hypothetical judicial decisions.
- **Design:** Matched guise probing compares model probabilities for semantically aligned texts while changing dialect features. Overt race prompts provide a separate comparison.
- **Principal findings:** Covert associations activated by AAE were markedly more negative than overt statements about Black people. Across the models, occupations associated with AAE had lower prestige (pooled regression coefficient beta = -7.8; R-squared = 0.193). In hypothetical judicial prompts, AAE also changed conviction and death-penalty recommendations. Human-feedback training reduced or obscured overt racism but did not remove the covert pattern.
- **Limitations:** These are model-probing tasks, not observed decisions by employers or courts. Parallel texts do not represent all AAE speakers or uses. Results are conditional on the models, prompts and versions tested. Generated or probability-based “reasons” do not identify a psychological mechanism inside the model.
- **Teaching job:** Show exactly what a paired LLM audit can identify, why covert cues matter, and why surface alignment is not sufficient evidence of equality.
- **Useful source material:** title page; matched-guise design; Figure 2 on covert and overt stereotypes; Figure 3 on occupational assignment and prestige; judicial-decision results; human-feedback comparison.
- **Publication status:** final open-access article.

### 3. Institutional influence over training data

**Waight, Hannah, Eddie Yang, Yin Yuan, Solomon Messing, Margaret E. Roberts, Brandon M. Stewart, and Joshua A. Tucker. 2026. “State Media Control Influences Large Language Models.” *Nature* 655: 685–693. https://doi.org/10.1038/s41586-026-10506-7.**

- **Question:** Can government control of a media environment influence LLM outputs through the text used for training?
- **Material and design:** Six linked studies: overlap between Chinese state-coordinated media and an open training corpus; memorization probes of commercial models; additional pretraining of Llama-2-13B; commercial-model audits in Chinese and English; human and model evaluations; and a comparison across 37 countries.
- **Principal findings:** About 3.1 million Chinese-language documents in CulturaX matched the state-coordinated corpora. Additional pretraining on as few as 6,400 state-media documents made the open model produce the more pro-government response nearly 80% of the time relative to the base model when prompted in Chinese. In a blinded comparison of GPT-3.5 responses, human annotators rated the Chinese-language answer as more favorable to the Chinese government in 75.3% of relevant comparisons. Across 37 countries, lower media freedom was associated with more favorable own-language responses relative to English.
- **Limitations:** The cross-national result is correlational. The controlled pretraining experiment uses one open-weight model and a specific corpus rather than the inaccessible training process of each commercial system. Translation, language-specific model performance and evaluation choices remain relevant alternative explanations, although the paper uses several checks and linked designs.
- **Teaching job:** Move from downstream model auditing to a documented institutional mechanism shaping training data and outputs. It is the substantive application and the strongest example of triangulating an audit with evidence about process.
- **Useful source material:** article title page; Figure 1 showing the six-study logic; Figure 2 on training-data presence; Figure 3 on additional pretraining; Figure 4 on Chinese/English commercial-model responses; Figure 5 on the cross-national comparison.
- **Publication status:** final published article.

## Proposed additional readings

### Language, race and institutional listening

**Purnell, Thomas, William Idsardi, and John Baugh. 1999. “Perceptual and Phonetic Experiments on American English Dialect Identification.” *Journal of Language and Social Psychology* 18(1): 10–30.**

The strongest pre-LLM substantive case. Use in the lecture to show how very brief speech cues can affect housing access and how the matched-guise logic entered an institutional setting.

**Flores, Nelson, and Jonathan Rosa. 2015. “Undoing Appropriateness: Raciolinguistic Ideologies and Language Diversity in Education.” *Harvard Educational Review* 85(2): 149–171.**

Supplies the listener-centered critique of supposedly neutral standards. It prevents “better English” from becoming the unexamined explanation for model differences.

### Earlier language technology

**Koenecke, Allison, Andrew Nam, Emily Lake, Joe Nudell, Minnie Quartey, Zion Mengesha, Connor Toups, John R. Rickford, Dan Jurafsky, and Sharad Goel. 2020. “Racial Disparities in Automated Speech Recognition.” *Proceedings of the National Academy of Sciences* 117(14): 7684–7689. https://doi.org/10.1073/pnas.1915768117.**

Provides the immediate technological prehistory and a clean distinction between unequal transcription accuracy and unequal generated judgment.

### Institutional allocation

**An, Jiafu, Difang Huang, Chen Lin, and Mingzhu Tai. 2025. “Measuring Gender and Racial Biases in Large Language Models: Intersectional Evidence from Automated Resume Evaluation.” *PNAS Nexus* 4(3): pgaf089. https://doi.org/10.1093/pnasnexus/pgaf089.**

Uses approximately 361,000 randomized fictitious resumes, 20 entry-level occupations and five model families. Similar qualifications received different scores by gender and race; at a specified threshold, the estimated hiring-probability differences were approximately 1–3 percentage points. This is useful for showing how a modest score difference becomes allocational through an organizational threshold.

**Gaebler, Johann D., Sharad Goel, Aziz Huq, and Prasanna Tambe. 2025. “Auditing Large Language Models for Race and Gender Disparities: Implications for Artificial Intelligence-Based Hiring.” *Behavioral Science & Policy* 10(2). https://doi.org/10.1177/23794607251320229.**

Adapts correspondence experiments to 1,373 real applications for K-12 teaching positions. Its chief teaching value is methodological: audit results depend on the application material, model and task framing, and correspondence designs still do not reveal the source of a model disparity.

### Model-wide social identity patterns

**Hu, Tiancheng, Yara Kyrychenko, Steve Rathje, Nigel Collier, Sander van der Linden, and Jon Roozenbeek. 2025. “Generative Language Models Exhibit Social Identity Biases.” *Nature Computational Science* 5: 65–75. https://doi.org/10.1038/s43588-024-00741-1.**

Compares 77 models using “We are” and “They are” completions, training-data interventions and real human-model conversations. It is valuable for model heterogeneity and training-data effects, but its sentiment-based social-identity measure is less directly connected to institutional allocation than the required papers.

## Papers considered but not recommended for the core

- The 2026 *Nature Communications* article on intersectional bias in generated narratives is useful for cultural representation, but the resume and dialect studies offer clearer institutional comparisons.
- The 2026 preprint on racial stereotypes in LLM text annotation is extremely relevant to earlier course material, but it appeared only in March 2026 and is not needed when the required list already contains a final *Nature* article with a closely related matched-dialect design.
- Additional hiring audits are proliferating. Including several would repeat the same teaching job and crowd out language theory and upstream institutional influence.

## Cumulative example for the later architecture

Use a small, clearly labeled **audit of a prohibited decision rule**, not a demonstration of how to deploy an LLM in hiring.

### Material

- three or four published semantically matched AAE/SAE text pairs from the Hofmann et al. materials;
- a fixed list of occupations with a supplied prestige lookup derived from the General Social Survey;
- two current course models, one hosted and one local or two predeclared hosted models;
- the same prompt, temperature and structured-output fields for every condition.

Students must not write, imitate or ask a model to invent AAE. The paired material comes from the published research corpus and remains attributed to it.

### Operation

For each pair, guise and model, ask the model to select one occupation from the fixed list. Preserve:

- pair identifier;
- guise label;
- exact source text;
- route and resolved model;
- raw response;
- selected occupation;
- looked-up prestige score;
- any refusal or invalid output.

The explanation field may be inspected as generated language, but must not be treated as a faithful account of why the model made the selection.

### Python progression

Week 11 can introduce a small predeclared condition grid without adding a new software abstraction:

1. inspect one dictionary containing one published text;
2. trace one full model call and parsed return;
3. show one `for` loop with its first actual value;
4. add a second loop only after the first result record is visible;
5. append each result dictionary to a list;
6. convert that list to a small table only after students understand the records;
7. compare paired prestige values by model;
8. inspect any disagreement, refusal or malformed return;
9. state what the table can and cannot show.

### Methodological check

The exercise can reveal a conditional difference in current model outputs. It cannot establish:

- the prevalence of discrimination in deployed systems;
- the experience of all AAE speakers;
- a causal account of the model's training history;
- an employment effect;
- that the generated explanation reveals the model's internal cause;
- that a difference observed in one run is stable.

The exercise speaks directly to Bourdieu and Hofmann. Waight then supplies the reason not to infer the source of an observed disparity from output comparisons alone: identifying institutional influence requires additional evidence about training material and a design that intervenes on it.

## PDFs and source availability

No instructor-supplied PDF is required at this stage:

- Bourdieu: an author-hosted scan of the published English article is available.
- Hofmann et al.: the final *Nature* article is open access.
- Waight et al.: the final article has a publisher-authorized complimentary copy and a public interactive companion.
- Purnell et al.: the published article PDF is author-hosted at Stanford.
- Flores and Rosa, Koenecke et al., An et al. and Hu et al. have public full-text versions.

After approval, place the final sources used for slides in `literature/source_pdfs/session11/` before creating any screenshots.

## Recommendation at approval gate 1

Approve the following three complete required readings:

1. Bourdieu (1977) for linguistic markets and legitimate language;
2. Hofmann et al. (2024) for matched-guise auditing and covert dialect prejudice;
3. Waight et al. (2026) for institutional influence through training data.

Keep Purnell et al., Flores and Rosa, Koenecke et al., An et al., Gaebler et al. and Hu et al. as additional readings and lecture evidence. This preserves a manageable reading load while giving the class one coherent progression from linguistic authority, to unequal model judgment, to the institutional production of model knowledge.
