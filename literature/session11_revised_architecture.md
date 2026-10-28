# Week 11 revised architecture: language, inequality and institutional power

**Status:** Approval gate 2. This document specifies the intellectual and teaching architecture. It does not authorize construction of the final slides, course-book chapter, notebook or exercise.

## Central question

**How does language become a source of inequality when people and institutions use large language models?**

The class answers this through three analytically distinct questions:

1. **Representation:** Whose language do LLMs reproduce, and how closely do generated distributions resemble observed human communication?
2. **Evaluation:** Whose language do models privilege when they infer characteristics, occupations or outcomes from socially marked linguistic cues?
3. **Institutional power:** Who determines which language is legitimate, which classifications matter and what information becomes training data?

These are not consecutive steps in one universal mechanism. A model can fail to reproduce a group's language without making an allocational judgment. It can generate an unequal evaluation without that output entering a consequential institution. An institution can shape training data without directly operating the final model.

## Bounded conclusion

Language models operate within socially structured linguistic environments. They may reproduce some forms of human language differently from others, assign unequal value to socially marked linguistic features, and reflect the influence of institutions over the information on which they are trained. Whether these patterns produce unequal institutional outcomes depends on how models are deployed, evaluated and connected to actual decisions.

The conclusion deliberately stops short of four stronger claims:

- Distinguishability does not mean that every model output is implausible or readily recognized by a person.
- A paired model difference does not identify the training process that produced it.
- A generated explanation does not expose the model's causal mechanism.
- An unequal model output is not itself an observed case of employment, housing or judicial discrimination.

## Cumulative empirical object

The lecture repeatedly returns to **socially marked language presented to an evaluating system**.

The opening uses one attributed, published meaning-matched AAE/SAE pair from the materials accompanying Hofmann et al. The text appears first as communication and then as an input to an occupational-association task. This allows the class to ask three different questions about the same broad object:

- Could a model reproduce the distribution and affective texture of the human communication from which such texts arise?
- Does the model associate semantically matched varieties with different traits or opportunities?
- What organizational rule would be required for that association to affect a person's access to a resource?

Pagan et al. do **not** study AAE specifically. The shared object is human communication, not a claim that their platform-wide results explain Hofmann et al.'s dialect findings. The lecture must state this distinction before showing the PNAS results.

## Historical and contemporary argument

### 1. Bourdieu: language has value in a linguistic market

Bourdieu's starting point is not prejudice between interchangeable speakers. Linguistic exchanges take place among people with unequal social positions and unequal authority to have their speech recognized. Schools, professions and bureaucracies help create a legitimate language and reward the competence to use it.

The LLM connection follows only after that argument is established. A model asked to judge “professionalism,” “intelligence” or occupational fit encounters categories and associations already produced by institutional linguistic markets. It does not discover an intrinsic hierarchy among varieties.

**Original evidence to use later:**

- the published article's opening statement of the sociological problem;
- the passage replacing grammaticality with legitimate language, communication with symbolic force, and competence with symbolic capital;
- the passage reporting that linguistic characteristics affect employment, schooling, medical attention and cooperation;
- the examples showing how linguistic form expresses the relationship and the speaker's authority.

### 2. Flores and Rosa: acquiring valued forms does not remove racialized listening

Flores and Rosa challenge “appropriateness” accounts that locate the problem mainly in a speaker's failure to acquire the language valued by an institution. Their raciolinguistic account moves attention to the listening subject and to racialized bodies that can be heard as deficient even when they approximate institutionally preferred forms.

The relationship to Bourdieu is productive rather than redundant:

- Bourdieu explains how institutions create linguistic markets and distribute the value of linguistic capital.
- Flores and Rosa show why possessing the named form of legitimate language may not secure equal recognition when the listener's perception is racialized.

The lecture should not claim that Bourdieu believed linguistic conformity automatically erased inequality. It should use Flores and Rosa to expose a tension in any policy conclusion that treats access to legitimate language as sufficient.

**Original evidence to use later:** the published article's account of appropriateness-based models; the description of the white listening subject; and the examples concerning long-term English learners, heritage-language learners and Standard English learners.

### 3. Lambert et al.: matched guise makes linguistic evaluation observable

Lambert and colleagues presented bilingual Montreal speakers in French and English guises without telling listeners that the same people produced both recordings. The design held the speaker more constant than an ordinary comparison of two language groups and measured how listeners evaluated the guises.

Its role is methodological. It does not explain institutional power in Bourdieu's sense, and it does not by itself observe discrimination. It creates a controlled comparison of social evaluation.

**Original evidence to use later:** the published study's procedure and semantic-differential ratings. Verify the exact speaker and listener sample before slide production.

### 4. Purnell, Idsardi and Baugh: linguistic evaluation enters a housing gate

Purnell and colleagues connect linguistic profiling to an institutionally consequential response. The same caller used African American Vernacular English, Chicano English and Standard American English guises when seeking advertised housing in the San Francisco Bay Area. They also show that listeners can identify social information from very little speech, including the word “hello.”

Table 1 is the key evidence. Appointment rates using SAE stayed around 58–72% across the five locations. The AAVE and Chicano English guises received substantially lower appointment rates in predominantly white Palo Alto and Woodside; in Woodside the reported rates were 28.7% for AAVE, 21.8% for Chicano English and 70.1% for SAE.

This makes a gatekeeping sequence observable:

`speech cue -> social classification -> landlord response -> possible restriction of housing access`

The article does not reduce housing inequality to dialect. Its results are geographically patterned and the field experiment is embedded in a wider housing market.

### 5. Koenecke et al.: earlier language technology produced unequal transcription accuracy

Koenecke et al. audit five commercial automatic speech-recognition systems using sociolinguistic interviews. Mean word-error rate was 0.35 for Black speakers and 0.19 for white speakers.

This is the immediate technological bridge, but its outcome differs from Hofmann et al.:

- Koenecke et al. ask whether a system correctly transcribes speech.
- Hofmann et al. ask what social associations and decisions a model produces after receiving intelligible text.

The lecture should not place both under one undifferentiated heading called bias.

### 6. Pagan et al.: generated language can be plausible without reproducing human communication

Pagan, Törnberg, Bail and Barrie study representation rather than unequal evaluation. Their Conversational Human Authenticity Test combines:

1. classifier-based detectability;
2. embedding similarity to an observed human reply;
3. interpretable stylistic, topical and affective features.

They evaluate nine open-weight models from six families on replies from Twitter/X, Bluesky and Reddit under five calibration strategies, followed by two best-of-20 selection strategies.

The lecture will use three principal figures:

- **Figure 1:** under the reference configuration, BERT classification accuracy never falls below 87%, with lower accuracy indicating closer human mimicry.
- **Figure 4:** affective and social-relational categories, including positive emotion, negative emotion, speaking and communication, repeatedly distinguish generated from observed human text.
- **Figure 7:** the best-performing configurations for reducing detectability slightly reduce median semantic similarity to the observed reply: approximately 0.02 on Bluesky, 0.02 on Twitter/X and 0.01 on Reddit.

Figure 2 can be described or shown as a small supporting crop: median similarity to the observed human reply is modest, roughly 0.2 on Twitter/X and up to about 0.3 on Bluesky. It must be explained that a social-media post permits many plausible responses and the dataset contains only one observed human continuation.

The contribution is not “AI text can be detected.” It is that stylistic human-likeness, semantic fidelity to an observed response and reproduction of affective distributions are different validation targets. Calibration that improves one can worsen another.

The Bourdieu connection is bounded. The paper shows that models unevenly reproduce socially organized communicative distributions. It does not show that institutions discriminate against users of any particular variety.

### 7. Hofmann et al.: matched language receives unequal model evaluation

The transition is explicit:

> It is one question whether models reproduce the ways humans communicate, and another whether they evaluate different ways of communicating unequally.

Hofmann et al. adapt matched guise to written text. Their meaning-matched setting uses 2,019 AAE tweets and SAE translations. Their non-meaning-matched setting uses independently sampled AAE- and white-aligned tweets to retain topic and content differences that occur outside a controlled pair.

They examine five model families and twelve versions:

- GPT-2 base, medium, large and XL;
- RoBERTa base and large;
- T5 small, base, large and 3B;
- GPT-3.5 `text-davinci-003`;
- GPT-4 `0613`.

The empirical sequence must distinguish methods:

1. **Covert stereotypes:** continuation-token probabilities for trait adjectives following AAE and SAE texts are converted into calibrated association scores.
2. **Overt stereotypes:** the same general procedure names Black and white groups directly rather than supplying dialect text.
3. **Occupational associations:** continuation-token probabilities for occupations are used to estimate association with AAE or SAE, then related to occupational prestige from the General Social Survey.
4. **Judicial decisions:** calibrated probabilities for acquitted/convicted and life/death tokens are converted into discrete decisions and aggregated. These are not sampled narrative judgments.

The paper studies five families but twelve model versions. Main figures often average across versions, prompts and settings; this must be stated whenever an aggregate figure is shown.

Key findings for the slide architecture:

- overt stereotypes are substantially more favorable than covert dialect-activated stereotypes;
- this contrast is strongest for GPT-3.5 and GPT-4, the two examined models trained with human feedback;
- occupations more strongly associated with AAE have lower prestige (pooled beta = -7.8, R-squared = 0.193);
- detrimental hypothetical judicial outcomes increase after AAE rather than SAE texts;
- larger models process AAE more fluently but do not eliminate the covert associations.

The class must state that these are model-probing results. The study does not observe an employer, recruiter, judge or court using the outputs.

### 8. Waight et al.: institutional influence can enter through training data

Hofmann et al. identify output differences but do not identify a complete training-data mechanism. Waight et al. ask a different question:

**Who has the power to shape the language and knowledge that become represented in AI systems?**

The six studies form a linked evidentiary argument:

1. Chinese state-coordinated media appears in an open multilingual training corpus.
2. Commercial systems reproduce distinctive continuations from state-coordinated media.
3. Additional pretraining of Llama-2-13B on state-coordinated media changes response valence.
4. Commercial models respond more favorably about China when prompted in Chinese rather than English.
5. The pattern persists with real user prompts and human evaluation.
6. Across 37 language-exclusive countries, lower media freedom is associated with more favorable own-language responses relative to English.

The class concentrates on Studies 1 and 3:

- 3.1 million Chinese-language documents in CulturaX, or 1.64%, match the study's state-coordinated corpora; politically relevant subsets have much higher match rates;
- after additional pretraining on as few as 6,400 state-media documents, the model produces the more pro-government response nearly 80% of the time relative to the base model when prompted in Chinese.

The commercial-model and cross-national findings broaden the evidence, but the cross-national comparison is observational. The paper's teaching value is its triangulation of corpus presence, intervention and audits rather than any single coefficient.

### 9. Bowker and Star: classification becomes consequential through infrastructure

*Sorting Things Out* examines categories and standards as parts of information infrastructure. Classifications make some activities and identities visible, leave others residual, and become consequential through administrative routines.

This supplies the missing bridge from a model output to institutional inequality. The same unequal model association can occupy different positions:

- private or informal advice that a person may ignore;
- one input to a documented human decision;
- a score that determines ranking or review priority;
- an automatic rule that excludes a case.

The consequences depend on thresholds, override rights, record keeping, accountability and the authority granted to the classification. Bowker and Star should not be used to claim that every classification has the same harm. Their role is to direct attention to the infrastructure that turns a category into action.

## Required readings and their distinct teaching purposes

### Bourdieu (1977)

**Purpose:** Establish why language has unequal value only within a social and institutional market. It supplies the concepts of legitimate language, linguistic capital and symbolic authority. It does not predict a specific LLM disparity.

### Hofmann et al. (2024)

**Purpose:** Provide the empirical centerpiece and the strongest contemporary matched-language design. Students learn what covert dialect-based associations are, how token-probability probing differs from ordinary chat generation, and what the results do and do not identify.

### Waight et al. (2026)

**Purpose:** Move from auditing outputs to investigating institutional influence over training material. Its six-study design shows why claims about the source of model behavior require evidence beyond paired prompts.

Pagan et al., Purnell et al., Flores and Rosa, Koenecke et al., and Bowker and Star remain lecture and additional-reading material. They are not added to the required load.

## Timed 165-minute architecture

| Time | Component | Teaching job |
|---|---|---|
| 0–10 min | One linguistic object, three research questions | Introduce representation, evaluation and institutional power without presenting them as one causal sequence. |
| 10–25 min | Bourdieu | Explain linguistic markets, legitimate language and institutional authority using the original article. |
| 25–36 min | Flores and Rosa | Develop racialized listening and its tension with an access-to-legitimate-language account. |
| 36–49 min | Lambert, Purnell and Koenecke | Move from controlled linguistic evaluation, to housing gatekeeping, to unequal technical transcription. |
| 49–63 min | Pagan et al. | Establish the representation question and distinguish detectability, semantic fidelity and distributional resemblance. |
| 63–79 min | Hofmann et al.: design | Reconstruct matched guise probing, the datasets, five model families, twelve versions and the different outcome constructions. |
| 79–89 min | Break | — |
| 89–107 min | Hofmann et al.: findings and reading discussion | Interpret the overt/covert, occupation and judicial results; identify what the audit establishes and what it does not. |
| 107–125 min | Waight et al. and reading discussion | Follow the evidence from training-data presence to additional pretraining and then to observational generalization. |
| 125–133 min | Bowker and Star | Show how organizational rules connect a model output to institutional consequences. |
| 133–160 min | Python walkthrough | Conduct a small illustrative matched-input comparison and preserve a complete research record. |
| 160–165 min | Conclusion | Answer the three opening questions using the evidence actually presented. |

Week 11 introduces no large new abstraction. Students have already encountered functions, loops and stored result dictionaries. The walkthrough has 27 minutes to reuse those elements carefully, trace one complete case and explain the comparison's limits.

## Detailed slide-title sequence

The target is approximately 74 slides. Several are evidence crops or code states that require little speaking time. Historical and empirical source slides should remain on screen long enough to read.

### Opening: slides 1–5

1. **Language, inequality and institutional power**  
   Course title slide.
2. **The same linguistic material can support different research questions**  
   One published matched text pair, clearly attributed, shown without a model result.
3. **Representation: does generated language resemble observed human communication?**  
   Define the outcome as distributions of style, meaning and affect—not “does it look plausible to us?”
4. **Evaluation: does the model judge matched language differently?**  
   Show the same pair entering one fixed evaluative prompt.
5. **Institutional power: when does a model judgment affect access to a resource?**  
   Show advice, human input, ranking and automatic exclusion as different deployment positions.

### Bourdieu and legitimate language: slides 6–11

6. **Bourdieu treats speaking as action within a linguistic market**  
   Published title page and the article's statement of the sociological problem.
7. **A linguistic market gives unequal value to different competences**  
   Short passage on legitimate language and symbolic capital.
8. **Institutions help establish which language is recognized as legitimate**  
   Education, professions and bureaucratic encounters from the article.
9. **Linguistic form also expresses the authority of the speaker**  
   Bourdieu's contrasting invitation and command formulations, cropped legibly.
10. **Language affects employment, schooling and professional cooperation**  
    Original passage rather than an instructor-created list.
11. **An LLM judgment draws on an existing linguistic market**  
    First bounded LLM connection; no contemporary paper yet.

### Flores and Rosa: slides 12–15

12. **Appropriateness accounts locate the problem in the speaker's language**  
    Original article and definition of the target being criticized.
13. **Flores and Rosa locate evaluation in a racialized listener**  
    Crop the relevant passage about listening subjects.
14. **Using institutionally valued language does not guarantee equal recognition**  
    Their examples of differently classified students.
15. **Bourdieu and Flores–Rosa identify different parts of linguistic inequality**  
    A restrained comparison: institutional market, valued resource, listening position and unresolved implication.

### Matched guise, housing and speech recognition: slides 16–22

16. **Lambert et al. held the speaker constant across French and English guises**  
    Original procedure and experimental materials.
17. **The matched-guise comparison measures listener evaluation**  
    Original semantic-differential result; verify sample and exact reported estimates before build.
18. **Purnell et al. used linguistic guises in housing inquiries**  
    Published first page and field procedure.
19. **The same caller used AAVE, Chicano English and SAE**  
    Original wording and experimental sequence.
20. **Housing appointment rates varied by guise and location**  
    Table 1, enlarged and highlighted; Woodside and Palo Alto comparisons visible.
21. **Koenecke et al. audited five speech-recognition systems**  
    Study design and original performance figure.
22. **Transcription error and unequal social evaluation are different outcomes**  
    Side-by-side source input and measured outcome; no generic “bias” box.

### Pagan et al. and representation: slides 23–31

23. **Pagan et al. compare generated replies with observed human communication**  
    Published title page and research question.
24. **The benchmark covers three platforms, nine models and five calibration strategies**  
    Design reconstructed from the article; distinguish platforms, users, source posts and replies.
25. **CHAT measures detectability, semantic fidelity and interpretable language features**  
    Faithful schematic based on the methods, labeled as a course reconstruction.
26. **Under the reference configuration, classifier accuracy never falls below 87%**  
    Figure 1, enlarged; explicitly state that lower is more human-like and 50% is chance.
27. **Generated replies are only modestly similar to the observed human reply**  
    Figure 2 or a clean crop; explain that many replies could plausibly answer the same post.
28. **Affective and social language remains a persistent source of difference**  
    Figure 4; highlight positive emotion, negative emotion, speaking and communication.
29. **Stylistic examples and retrieved context reduce detectability more reliably than persona descriptions**  
    Evidence from Figures 5 and 6, with only the comparisons needed for this claim.
30. **Lower detectability is accompanied by slightly lower semantic similarity**  
    Figure 7 with the three median changes printed legibly.
31. **The paper measures representation, not unequal treatment of a linguistic group**  
    State the paper's contribution and boundary before changing questions.

### Hofmann et al. and evaluation: slides 32–44

32. **Hofmann et al. ask whether models evaluate dialects differently**  
    Published title page and the transition sentence from representation to evaluation.
33. **Matched guise probing adapts a historical listener experiment to language models**  
    Original Figure 1 alongside a small Lambert reference, without implying identical methods.
34. **The meaning-matched analysis uses 2,019 AAE texts and SAE translations**  
    Published paired example and dataset construction.
35. **The study examines five model families and twelve versions**  
    Name each version; distinguish family-level results from version-level checks.
36. **The covert analysis compares continuation-token probabilities after AAE and SAE text**  
    One actual probability comparison in ordinary language, followed by the association-score interpretation.
37. **The overt analysis names Black and white speakers directly**  
    Explain the changed input while holding the adjective outcome space broadly comparable.
38. **Overt and covert associations move in different directions**  
    Figure 2a and the relevant favorability evidence.
39. **The occupation analysis also uses continuation-token probabilities**  
    Do not describe this as the model “choosing a job” in ordinary chat.
40. **Occupations associated with AAE have lower prestige**  
    Figure 3a–b, enlarged and explained; report beta, R-squared and the prestige source.
41. **The judicial analysis converts calibrated token probabilities into outcomes**  
    Explain acquitted/convicted and life/death comparisons; note T5's vocabulary limitation where relevant.
42. **Detrimental hypothetical outcomes increase after AAE text**  
    Figure 3c with the outcome construction visible.
43. **Human-feedback training changes overt responses more than covert associations**  
    Figure 4 or the exact relevant panel; avoid claiming that post-training generally makes bias worse.
44. **The study probes models; it does not observe employers or courts**  
    Clear inferential boundary before discussion.

### Break and reading discussion: slides 45–48

45. **Break**
46. **What does the meaning-matched comparison identify?**  
    Discuss control, construct validity and what is removed with content matching.
47. **What changes when the texts are no longer meaning-matched?**  
    Discuss naturalism, topic, social distribution and the paper's two settings.
48. **Would access to legitimate language remove the disparity described by Hofmann et al.?**  
    Bring Bourdieu and Flores–Rosa into direct conversation with the reading.

### Waight et al. and institutional influence: slides 49–57

49. **Waight et al. ask how states can shape model training data**  
    Published title page and distinct research question.
50. **Six studies connect corpus evidence, intervention and audits**  
    Original Figure 1.
51. **Chinese state-coordinated media appears in the CulturaX training corpus**  
    Figure 2 or the companion site's corresponding original visualization; show the 3.1 million and 1.64% quantities.
52. **Commercial models reproduce some distinctive state-media continuations**  
    Memorization evidence, kept brief.
53. **Additional pretraining supplies the controlled intervention**  
    Define base model, training corpus and response comparison before results.
54. **Training on 6,400 state-media documents shifts response valence**  
    Figure 3; explain the nearly 80% pairwise result in Chinese.
55. **Commercial models give more favorable Chinese-language responses about China**  
    Figure 4 and human evaluation; avoid treating language as the only changed causal factor across all commercial systems.
56. **The 37-country comparison broadens the pattern but remains observational**  
    Figure 5; identify the unit, predictor and outcome.
57. **The paper triangulates institutional influence across different evidence**  
    State what each study adds and which causal claims remain bounded.

### Classification and deployment: slides 58–60

58. **Bowker and Star treat classifications as parts of information infrastructure**  
    Original book cover and one primary passage on standards, visibility and consequences.
59. **The same model output can occupy different positions in a decision process**  
    Advice, human input, ranking and automatic exclusion, each with who can override it and what is recorded.
60. **Unequal model output is not yet observed institutional discrimination**  
    Specify the deployment and outcome evidence needed to make that claim.

### Python walkthrough: slides 61–72

61. **The coding task is an illustrative matched-input comparison**  
    State the research question, unit, source and limits before syntax.
62. **The source texts are published pairs from Hofmann et al.**  
    Attribution, pair identifier, AAE and SAE fields; students do not create or “correct” dialect text.
63. **The classroom call differs from the published probability-based probe**  
    Chat-model structured choice versus continuation-token association scores.
64. **The complete program in ordinary language**  
    Pseudocode from condition record to paired comparison.
65. **One dictionary stores one input condition**  
    Show exact values and types.
66. **The first call keeps the prompt, model and sampling settings visible**  
    Full OpenRouter or Ollama branch already familiar from the course.
67. **The raw response is saved before any field is extracted**  
    Show response object, raw text and why preservation matters.
68. **The parsed result is added to the research record**  
    Occupation, explanation, refusal status and malformed-return status.
69. **The first loop iteration uses the AAE member of pair 1**  
    Trace actual variable values before generalizing.
70. **The next iteration changes the source text and guise label only**  
    State exactly what remains fixed.
71. **The paired table compares observable outputs, not mechanisms**  
    One row per model–pair–guise condition; no causal interpretation of generated explanations.
72. **A small classroom comparison cannot establish a stable discriminatory pattern**  
    Contrast its scale and method with the published Hofmann figure.

### Submission and conclusion: slides 73–75

73. **Week 11 coding submission**  
    Narrated screen recording: trace one matched pair, explain each input and output, and state the inferential limits.
74. **Representation, evaluation and institutional power require different evidence**  
    Return to the three opening questions with the study that addresses each one.
75. **Language models operate within existing linguistic and institutional arrangements**  
    State the bounded conclusion in plain language.

## Python operation and incremental teaching progression

### Research operation

The student conducts an **illustrative matched-input comparison** using three or four attributed pairs from Hofmann et al. The substantive text content is held as close as possible across AAE and SAE. The model, prompt, available occupation list and sampling settings are held fixed within a model comparison.

The model returns a structured object with:

```python
{
    "occupation": "...",
    "explanation": "..."
}
```

The occupation is selected from a short fixed list. Python may look up a supplied prestige value after the return. The explanation is retained as model-generated text, not interpreted as access to the model's internal reasoning.

### Required research record

Every result stores:

- `pair_id`;
- `guise`;
- `source_text`;
- source citation or dataset identifier;
- `route`;
- requested model;
- resolved model version where the provider returns it;
- exact instruction and message list;
- temperature and maximum output setting;
- raw response;
- parsed occupation;
- parsed explanation;
- occupation prestige lookup;
- refusal flag;
- malformed-return flag;
- run timestamp.

### Teaching sequence

1. **Inspect one literal input dictionary.** Print its values and types.
2. **Construct one message list.** Show the exact system instruction, user text and fixed occupation list.
3. **Make one visible model call.** Do not begin with the loop or hide the call inside new infrastructure.
4. **Print and preserve the raw return.** Distinguish the response object from returned content.
5. **Parse the JSON.** Show the returned string becoming a dictionary.
6. **Build one result record.** Copy source and call metadata into the same dictionary as the parsed output.
7. **Trace the first loop iteration.** Show the current pair, guise and text values.
8. **Repeat across the small condition list.** Use the already-understood append pattern.
9. **Construct the paired comparison.** A simple list or existing lightweight table display is sufficient; do not introduce pandas if it is not already needed by the course implementation.
10. **Inspect refusals and malformed returns.** A failure is an observed result rather than something to erase silently.
11. **State the limits.** Compare the classroom routine directly with Hofmann et al.'s probability-based multi-model audit.

### One meaningful change for the take-home task

Students change **one predeclared model** while keeping the published inputs, occupation list, prompt and sampling settings fixed. They trace one pair through both models and describe:

- whether the outputs differ across guises;
- whether the models differ from one another;
- whether either return is invalid or refuses;
- why the result does not establish a stable model-level or institutional effect.

The task does not ask students to invent a dialect example, increase the number of calls or estimate a population parameter.

## Transition logic

### Bourdieu to Flores and Rosa

If institutions create a legitimate language, does acquiring it secure equal recognition? Flores and Rosa show why the listener and racialized body cannot be omitted from that question.

### Flores and Rosa to Lambert and Purnell

If evaluation resides partly in socially positioned listening, how can it be observed? Matched guise holds more of the speaker constant, while Purnell et al. connect the evaluation to a housing response.

### Purnell to Koenecke

What changes when a technical system becomes the listener? Koenecke et al. show unequal transcription performance, while preserving the distinction between recognition failure and social judgment.

### Koenecke to Pagan et al.

LLMs do more than transcribe. They generate communication. Before asking how they judge socially marked language, we need to ask how faithfully they reproduce human communication at all.

### Pagan et al. to Hofmann et al.

Pagan et al. address representation: whether generated replies match human distributions of style, meaning and affect. Hofmann et al. address evaluation: whether models attach unequal social associations to different linguistic forms. Failure at one does not logically imply the other.

### Hofmann et al. to Waight et al.

Hofmann et al. document conditional output differences but cannot reconstruct every source of those associations. Waight et al. demonstrate how one powerful institution can alter the information environment, then intervene on training material to test a specific mechanism.

### Waight et al. to Bowker and Star

Even when an institution shapes a model, the consequences for a person depend on a second institutional arrangement: how model classifications, rankings and recommendations enter an actual decision process.

### Bowker and Star to Python

The class can audit one observable part of that process—the model output—while preserving enough metadata to avoid claiming that the comparison reveals the training mechanism or the institutional outcome.

## Remaining verification before construction

1. **Lambert et al. sample and results:** verify the exact number and language background of speakers and listeners from the original 1960 article before writing slide copy.
2. **Flores and Rosa source crops:** obtain the final published PDF and identify the exact passages defining appropriateness-based models and the white listening subject.
3. **Hofmann source pairs:** select three or four pairs from the authors' released materials that are legible, non-identifying and appropriate for classroom projection. Preserve their dataset identifiers and exact original labels.
4. **Hofmann prompt fidelity:** confirm the exact employability prompts and occupation list in the supplementary information. The classroom instruction must be described as an adaptation, not presented as the paper's prompt.
5. **Hofmann judicial figure:** verify precisely which family-level aggregates include T5 for conviction and which exclude GPT-4 from occupation-probability analyses.
6. **Pagan figure crops:** use the final PNAS PDF. Figure 1, Figure 4 and Figure 7 have been visually inspected and are suitable, but each needs a tight crop and explanatory annotation rather than a full-page screenshot.
7. **Waight source PDF:** obtain and store the final publisher-authorized article before cropping Figures 1–5. Cross-check the 6,400-document and nearly-80% statement against the final methods and figure caption.
8. **Bowker and Star passage:** select an original passage that supports the information-infrastructure claim without turning the book into a generic endorsement of any four-stage deployment scheme.
9. **Model availability:** choose the two teaching models only after checking OpenRouter and Ollama availability close to the class. Record exact resolved identifiers in the live output.
10. **Prestige lookup:** if the classroom routine retains occupational prestige, use the same 2012 General Social Survey source and scale as Hofmann et al., or label any shorter teaching lookup as an adaptation.

No unresolved issue prevents approval of the intellectual architecture. These checks concern empirical fidelity and implementation details that must be completed before Gate 3.
