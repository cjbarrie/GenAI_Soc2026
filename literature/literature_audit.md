# Literature Audit — Generative AI in Sociology, Fall 2026

**Audit date:** 2026-08-18  
**Status:** Phase 2 working recommendation for instructor review; no reading is final until approved.  
**Scope:** The co-authored chapter, the 2025 syllabus and bibliography, the 2025 *Sociological Methods & Research* special issue, and literature published or circulated through August 18, 2026.

## Selection rules

1. The chapter is the weekly methodological anchor, not an additional paper competing for space.
2. A normal week has two or three required papers; a third is included only when it creates a deliberate empirical or epistemological contrast. Page ranges or excerpts will keep the total reading burden close to the 2025 course.
3. Prefer sociology when it supplies the same lesson. Retain adjacent disciplines when a paper originates a method, provides the strongest design, or anchors an important controversy.
4. A paper is required only when its claim can be made operational in lecture, discussion, or code.
5. Preprints are labeled. A recent preprint may be required when it supplies a genuinely new question unavailable in published work, but students must evaluate its provisional status.
6. The list privileges inferential clarity, inspectable methods, available materials, and pedagogical contrast over comprehensiveness.

## Headline findings

- The August 2025 *Sociological Methods & Research* special issue is the strongest sociology-first methods core. Its most useful articles divide naturally across measurement, qualitative coding, multimodal analysis, and synthetic subjects rather than belonging in one overloaded block.
- The old Weeks 2–3 technical sequence should disappear. Embeddings and transformers become optional background or short lecture explanations.
- The old course had no proper treatment-generation week and no research-agent week. The chapter and 2025–26 literature now support both.
- Junsol Kim's work belongs in the course without reconstructing the Blumer session: Kim and Lee anchor opinion prediction, while Kim et al.'s “societies of thought” paper supports a sociological discussion of collective intelligence and internal social organization.
- The 2026 literature materially strengthens replication and audits: GUIDE-LLM supplies an actionable reporting standard; Waight et al. provide a strong causal and cross-national audit of state-media influence; Buyl et al. connect model behavior to creator geography and values.
- Published 2026 work supersedes several old preprints, most notably Ashokkumar et al. on forecasting social-science experiments and Chae and Davidson on text classification.

## Proposed required sequence

The computational link states what students should be able to inspect or reproduce after reading. “Anchor” refers to sections of Barrie, Argyle, Bisbee et al., **AI and Research Methods**.

### Session 1 — What kind of research technology is an LLM?

**Anchor:** Introduction and §10.7 (PDF pp. 1–2 and 34–35).

**Required**

- Davidson, Thomas, and Daniel Karell. 2025. “Integrating Generative Artificial Intelligence into Social Science Research: Measurement, Prompting, and Simulation.” *Sociological Methods & Research* 54(3):775–793. [DOI](https://doi.org/10.1177/00491241251339184). **Role:** supplies the sociology-first map of research uses and makes validation central.
- Alvero, AJ, Dustin S. Stoltz, Oscar Stuhler, and Marshall A. Taylor. 2026. “Generative AI in Sociological Research: State of the Discipline.” *Sociological Science* 13:45–62. [Article](https://sociologicalscience.com/articles-v13-3-45/); DOI `10.15195/v13.a3`. **Role:** shows how sociologists actually use and understand GenAI, connecting the tool to the discipline rather than to speculative capability claims.

**Optional:** Bail (2024) for a concise opportunity/risk essay; Bender et al. (2021) for training-data, scale, and political-economy critique; Davidson (2024) for a practical sociology overview.

**Computational link:** inspect one complete research record—Python input types, messages, model/version/settings, raw output, parsed output, and validation field—before making a first OpenRouter call.

### Session 2 — What can an LLM output validly measure?

**Anchor:** §10.1, especially §§10.1.3–10.1.5.

**Required**

- Stuhler, Oscar, Cat Dang Ton, and Étienne Ollion. 2025. “From Codebooks to Promptbooks: Extracting Information from Text with Generative Large Language Models.” *Sociological Methods & Research* 54(3):794–848. [DOI](https://doi.org/10.1177/00491241251336794). **Role:** turns a sociological codebook into an inspectable extraction workflow and demonstrates non-random error.
- Chae, Youngjin, and Thomas Davidson. 2026. “Large Language Models for Text Classification: From Zero-Shot Learning to Instruction-Tuning.” *Sociological Methods & Research* 55(2):501–567. [DOI](https://doi.org/10.1177/00491241251325243). **Role:** compares zero-shot, few-shot, fine-tuned, and instruction-tuned classification and clarifies accuracy/cost tradeoffs.

**Optional:** Egami et al. (2023/2024) on downstream inference with predicted variables; Chausson et al. (2025) on the insight–inference loop; Alizadeh et al. (2025) for local/open-model implementation.

**Computational link:** classify a small sociological corpus, inspect every input and output, construct a confusion matrix, and show why good label accuracy does not automatically validate a downstream coefficient.

### Session 3 — What does interpretation mean when an LLM assists qualitative research?

**Anchor:** §§10.1.4–10.1.5.

**Required**

- Than, Nga, Leanne Fan, Tina Law, Laura K. Nelson, and Leslie McCall. 2025. “Updating ‘The Future of Coding’: Qualitative Coding with Generative Large Language Models.” *Sociological Methods & Research* 54(3):849–888. [DOI](https://doi.org/10.1177/00491241251339188). **Role:** provides a concrete sociological workflow spanning code development, prompting, reliability, and validation.
- Ibrahim, Elida Izani, and Andrea Voyer. 2026. “Qualitative Research with LLM Chatbots: Technological Reflexivity for Interpretative Technology.” *Qualitative Research*. [DOI](https://doi.org/10.1177/14687941251390794). **Role:** treats ambiguity and improvisation as objects of reflexive qualitative practice, not merely errors to eliminate.
- Nguyen, Duc Cuong, and Catherine Welch. 2026. “Generative Artificial Intelligence in Qualitative Data Analysis: Analyzing—or Just Chatting?” *Organizational Research Methods*. [DOI](https://doi.org/10.1177/10944281251377154). **Role:** provides the strongest counterposition, focusing on fabricated evidence and the epistemic limits of pattern completion as interpretation.

**Optional:** Wise, Gresalfi, and Spencer-Smith (2026); Matta, Nordmark, and Masiello (2026); De Paoli (2024).

**Computational link:** compare human, deductive-LLM, and inductive-LLM memoing on the same interview excerpts; preserve quotations and require every proposed theme to point back to source text.

### Session 4 — What counts as evidence across text, image, and audio?

**Anchor:** §§10.1.1 and 10.1.5.

**Required**

- Law, Tina, and Elizabeth Roberto. 2025. “Generative Multimodal Models for Social Science: An Application with Satellite and Streetscape Imagery.” *Sociological Methods & Research* 54(3):889–932. [DOI](https://doi.org/10.1177/00491241251339673). **Role:** gives a substantive sociology application and a tractable visual-measurement workflow.
- Maranca, Alessandra Rister Portinari, Jihoon Chung, Musashi Hinck, Adam D. Wolsky, Naoki Egami, and Brandon M. Stewart. 2025. “Correcting the Measurement Errors of AI-Assisted Labeling in Image Analysis Using Design-Based Supervised Learning.” *Sociological Methods & Research* 54(3):984–1016. [DOI](https://doi.org/10.1177/00491241251333372). **Role:** connects multimodal annotation errors to valid downstream estimation.
- Arminio, Luigi, Matteo Magnani, Matías Piqueras, Luca Rossi, and Alexandra Segerberg. 2026. “Leveraging VLLMs for Visual Clustering: Image-to-Text Mapping Shows Increased Semantic Capabilities and Interpretability.” *Social Science Computer Review*. [DOI](https://doi.org/10.1177/08944393251376703). **Role:** supplies a newer social-media application and raises the difference between denotation and connotation.

**Optional:** Reece et al. (2023), *CANDOR*, as an audio/conversation dataset; the session should include audio in the lab even though current sociological validation work is strongest for images.

**Computational link:** send matched text/image/audio inputs, compare the schemas returned, and hand-audit a stratified subset rather than treating all modalities as interchangeable.

### Session 5 — Can generated media isolate a causal construct?

**Anchor:** §10.2, especially §§10.2.3–10.2.5.

**Required**

- Dafoe, Allan, Baobao Zhang, and Devin Caughey. 2018. “Information Equivalence in Survey Experiments.” *Political Analysis* 26(4):399–416. [DOI](https://doi.org/10.1017/pan.2018.9). **Role:** supplies the indispensable design language for unintended information and bundled treatments; retained from political methodology because no sociological substitute is as precise.
- Evsyukova, Yulia, Felix Rusche, and Wladislaw Mill. 2025. “LinkedOut? A Field Experiment on Discrimination in Job Network Formation.” *Quarterly Journal of Economics* 140(1):283–334. [DOI](https://doi.org/10.1093/qje/qjae035). **Role:** provides a stratification/network application using AI-generated profile images and makes construct fidelity concrete.
- Bai, Hui, Jan G. Voelkel, Shane Muldowney, Johannes C. Eichstaedt, and Robb Willer. 2025. “LLM-Generated Messages Can Persuade Humans on Policy Issues.” *Nature Communications* 16:6037. [DOI](https://doi.org/10.1038/s41467-025-61345-5). **Role:** compares human, LLM, and human-selected LLM treatments and permits analysis of mechanisms and stimulus variation.

**Optional:** Goldstein et al. (2024) on propaganda; Velez and Liu (2025) on tailored experiments; Evsyukova replication materials.

**Computational link:** generate multiple treatment variants, measure intended and nuisance dimensions, and reject a stimulus set that fails a predeclared construct-fidelity check.

### Session 6 — What changes when the model becomes an interactant?

**Anchor:** Selected §§10.2 and 10.5.

**Required**

- Hackenburg, Kobi, Ben M. Tappin, Luke Hewitt, Ed Saunders, Sid Black, Hause Lin, Catherine Fist, Helen Margetts, David G. Rand, and Christopher Summerfield. 2025. “The Levers of Political Persuasion with Conversational Artificial Intelligence.” *Science* 390(6777):eaea3884. [DOI](https://doi.org/10.1126/science.aea3884). **Role:** separates model scale, prompting, post-training, personalization, factuality, and conversation as causal levers.
- Lin, Hause, Gabriela Czarnek, Benjamin Lewis, Joshua P. White, Adam J. Berinsky, Thomas H. Costello, Gordon Pennycook, and David G. Rand. 2025. “Persuading Voters Using Human–Artificial Intelligence Dialogues.” *Nature* 648:394–401. [DOI](https://doi.org/10.1038/s41586-025-09771-9). **Role:** supplies live-election field contexts, dialogue-level treatment, accuracy concerns, and a productive dual-use transparency problem.
- Yin, Yidan, Nan Jia, and Cheryl J. Wakslak. 2024. “AI Can Help People Feel Heard, but an AI Label Diminishes This Impact.” *Proceedings of the National Academy of Sciences* 121:e2319112121. [DOI](https://doi.org/10.1073/pnas.2319112121). **Role:** moves beyond persuasion to relational reception and identifies disclosure as part of the treatment.

**Optional:** Salvi et al. (2025); Costello, Pennycook, and Rand (2024); Argyle et al. (2025).

**Computational link:** build a bounded turn-taking state machine, log every turn, and distinguish fixed treatment assignment from endogenous conversational exposure.

### Session 7 — Whose attitudes and experiences do synthetic populations represent?

**Anchor:** §10.3.

**Required**

- Kozlowski, Austin C., and James A. Evans. 2025. “Simulating Subjects: The Promise and Peril of Artificial Intelligence Stand-Ins for Social Agents and Interactions.” *Sociological Methods & Research* 54(3):1017–1073. [DOI](https://doi.org/10.1177/00491241251337316). **Role:** provides the most explicitly sociological theory of simulated subjectivity and collective representation.
- Boelaert, Julien, Samuel Coavoux, Étienne Ollion, Ivaylo Petev, and Patrick Präg. 2025. “Machine Bias: How Do Generative Language Models Answer Opinion Polls?” *Sociological Methods & Research* 54(3):1156–1196. [DOI](https://doi.org/10.1177/00491241251330582). **Role:** demonstrates low variance and topic-varying bias, undermining naive respondent substitution.
- Wang, Angelina, Jamie Morgenstern, and John P. Dickerson. 2025. “Large Language Models That Replace Human Participants Can Harmfully Misportray and Flatten Identity Groups.” *Nature Machine Intelligence* 7. [DOI](https://doi.org/10.1038/s42256-025-00986-z). **Role:** makes within-group heterogeneity and identity flattening central validation targets.

**Optional:** Argyle et al. (2023); Bisbee et al. (2024); Santurkar et al. (2023); Lyman et al. (2025).

**Computational link:** compare overall fit with subgroup distributions and within-group variance; show how a good population mean can conceal representational failure.

### Session 8 — Can LLMs recover missing or unobserved social worlds?

**Anchor:** §§10.3.4–10.3.6 and §10.7.

**Required**

- Kim, Junsol, and Byungkyu Lee. 2026. “AI-Augmented Surveys: Leveraging Large Language Models and Surveys for Opinion Prediction.” *Sociological Methodology*, accepted/forthcoming; current manuscript at [arXiv:2305.09620](https://arxiv.org/abs/2305.09620). **Role:** distinguishes retrodiction from unasked-opinion prediction using the GSS and foregrounds privacy and autonomy. Publication metadata must be rechecked before syllabus freeze.
- Xie, Yueqi, Lemeng Liang, Shuzhen Li, Yifu Lu, Zhiwen Xiao, Mengdi Shi, Junming Huang, Mengdi Wang, and Yu Xie. 2026. “Evaluating the Statistical Realism of LLM-Generated Social Science Data.” *Proceedings of the National Academy of Sciences* 123(19):e2538145123. [DOI](https://doi.org/10.1073/pnas.2538145123). **Role:** replaces vague “fidelity” with five population-level statistical targets.
- Ashokkumar, Ashwini, Luke Hewitt, Isaias Ghezae, and Robb Willer. 2026. “Large Language Models Can Predict the Results of Social Science Experiments.” *Nature*. [DOI](https://doi.org/10.1038/s41586-026-10742-x). **Role:** supersedes the old working paper, demonstrates strong correlations alongside effect-size inflation, and supports a discussion of pilot selection rather than participant replacement.

**Optional:** Broska, Howes, and van Loon (2025) on mixed-subject designs; Park et al. (2024) on interview-grounded digital agents.

**Computational link:** calculate individual accuracy, aggregate trends, associations, and treatment-effect error separately; require students to name the inferential target before choosing a metric.

### Session 9 — How can micro-level interactions generate macro-level order?

**Anchor:** §§10.4.1–10.4.3.

**Required**

- Macy, Michael W., and Robert Willer. 2002. “From Factors to Actors: Computational Sociology and Agent-Based Modeling.” *Annual Review of Sociology* 28:143–166. [DOI](https://doi.org/10.1146/annurev.soc.28.110601.141117). **Role:** establishes the sociological reason for agent-based explanation before introducing LLM agents.
- Park, Joon Sung, et al. 2023. “Generative Agents: Interactive Simulacra of Human Behavior.” In *UIST '23*. [DOI](https://doi.org/10.1145/3586183.3606763). **Role:** gives the canonical memory–reflection–planning architecture.
- Chuang, Yun-Shiuan, et al. 2024. “Simulating Opinion Dynamics with Networks of LLM-Based Agents.” *Findings of NAACL 2024*:3326–3346. [DOI](https://doi.org/10.18653/v1/2024.findings-naacl.211). **Role:** shows that an apparent pro-consensus tendency is itself a model artifact and that prompt-imposed confirmation bias changes macro outcomes.

**Optional:** Törnberg et al. (2023); Park et al. (2024) on 1,052 interview-grounded agents; the 2025 systematic review “Validation Is the Central Challenge for Generative Social Simulation.”

**Computational link:** implement the same toy diffusion process once with explicit rules and once with LLM policies; expose population, network, observation, policy, state-update, and stopping-rule inputs.

### Session 10 — When can agent diversity and debate produce collective intelligence?

**Anchor:** §§10.4.4–10.4.5.

**Required**

- Ashery, Ariel Flint, Luca Maria Aiello, and Andrea Baronchelli. 2025. “Emergent Social Conventions and Collective Bias in LLM Populations.” *Science Advances* 11(20):eadu9368. [DOI](https://doi.org/10.1126/sciadv.adu9368). **Role:** supplies a clean claim about conventions, collective bias, and committed minorities.
- Barrie, Christopher, and Petter Törnberg. 2025. “Emergent LLM Behaviors Are Observationally Equivalent to Data Leakage.” Preprint. [arXiv:2505.23796](https://arxiv.org/abs/2505.23796), read with Ashery, Aiello, and Baronchelli's [reply](https://arxiv.org/abs/2506.18600). **Role:** turns contamination and observational equivalence into an explicit sociological-inference controversy rather than a footnote.
- Kim, Junsol, Shiyang Lai, Nino Scherrer, Blaise Agüera y Arcas, and James Evans. 2026. “Reasoning Models Generate Societies of Thought.” Preprint. [arXiv:2601.10825](https://arxiv.org/abs/2601.10825). **Role:** provides the new, non-Blumer route to social organization, diversity, conflict, and collective intelligence inside reasoning models.

**Optional:** the Ashery et al. reply can be assigned as a short required appendix if the total load permits.

**Computational link:** vary agent heterogeneity and interaction structure, then run a contamination probe before interpreting convergence as emergence.

### Session 11 — Who—or what—produces research data in an agentic workflow?

**Anchor:** §10.5.

**Required**

- Lu, Chris, Cong Lu, Robert Tjarko Lange, et al. 2026. “Towards End-to-End Automation of AI Research.” *Nature* 651:914–919. [DOI](https://doi.org/10.1038/s41586-026-10265-5). **Role:** provides an inspectable full research loop and concrete failure points in search, code execution, analysis, writing, and review.
- “Multi-Agent AI Systems Need Transparency.” 2026. *Nature Machine Intelligence* 8:1. [Article](https://www.nature.com/articles/s42256-026-01183-2). **Role:** a short counterweight that forces students to justify agent multiplicity, division of labor, cost, and traceability.

**Optional:** Wang et al. (2026), “LLM Agents as Social Scientists” [arXiv:2604.01520](https://arxiv.org/abs/2604.01520); REPRO-Bench [arXiv:2507.18901](https://arxiv.org/abs/2507.18901); PROV-AGENT [arXiv:2508.02866](https://arxiv.org/abs/2508.02866).

**Computational link:** let an agent search and extract evidence from a small bounded source set, but require a human-verifiable provenance table recording query, source, excerpt, transformation, and claim.

### Session 12 — What can we reproduce, and what remains opaque?

**Anchor:** §10.7. This is a lower-stakes, attendance-flexible studio.

**Required resource rather than a normal reading load**

- Feuerriegel, Stefan, Christopher Barrie, M. J. Crockett, et al. 2026. “A Reporting Checklist for Large Language Models in Behavioural Science.” *Nature Human Behaviour* 10:1182–1186. [DOI](https://doi.org/10.1038/s41562-026-02492-7); use the [GUIDE-LLM checklist](https://llm-checklist.com/). **Role:** converts transparency into a concrete audit instrument.
- Barrie, Christopher, Alexis Palmer, and Arthur Spirling. 2025. “Replication for Language Models: Problems, Principles, and Best Practices for Political Science.” Working paper, November 4. [Manuscript](https://arthurspirling.org/documents/BarriePalmerSpirling_TrustMeBro.pdf). **Role:** demonstrates longitudinal instability and explains why temperature zero does not solve reproducibility.

**Computational link:** reproduce one earlier course result using cached output and then a live/local model; submit a one-page GUIDE-LLM discrepancy report. Students away from New York can complete it asynchronously.

### Session 13 — What culture, ideology, and hierarchy are encoded in models?

**Anchor:** §10.6, especially §§10.6.1–10.6.4.

**Required**

- Waight, Hannah, Eddie Yang, Yin Yuan, Solomon Messing, Margaret E. Roberts, Brandon M. Stewart, et al. 2026. “State Media Control Influences Large Language Models.” *Nature* 655:685–693. [DOI](https://doi.org/10.1038/s41586-026-10506-7). **Role:** exemplary cross-national audit plus causal triangulation using additional pretraining.
- Buyl, Maarten, Alexander Rogiers, Sander Noels, et al. 2026. “Large Language Models Reflect the Ideology of Their Creators.” *npj Artificial Intelligence* 2(1):7. [DOI](https://doi.org/10.1038/s44387-025-00048-0). **Role:** compares creators, geopolitical regions, models, and prompting languages and raises the limits of “neutrality.”
- Kim, Junsol, Winnie Street, Roberta Rocca, Diane M. Korngiebel, Adam Waytz, James Evans, and Geoff Keeling. 2026. “Inducing Language Models to Assert Their Own Consciousness Restores Human Beliefs and Values.” Preprint. [arXiv:2607.28607](https://arxiv.org/abs/2607.28607). **Role:** a deliberately provisional, genuinely new study of how safety alignment changes mind attribution, religiosity, moral values, hope, and well-being responses.

**Optional:** Lu, Song, and Zhang (2025), “Cultural Tendencies in Generative AI”; Bai et al. (2025), “Explicitly Unbiased Large Language Models Still Form Biased Associations”; Kozlowski, Taddy, and Evans (2019) as the embedding-era prehistory of cultural audits.

**Computational link:** preregister a small factorial audit across model, language, user frame, and prompt paraphrase; separate an output difference from a claim about its social cause.

### Session 14 — Project presentations

No new reading or computational material is assigned. The meeting is reserved for student presentations and questions.

## Audit of 2025 required and recommended readings

The action refers to the 2026 syllabus, not to the intrinsic quality of the work.

| 2025 item | Action | Reason / new location |
|---|---|---|
| Bail 2024, “Can Generative AI Improve Social Science?” | MOVE TO OPTIONAL | Strong concise overview, but Davidson–Karell and Alvero et al. create a more sociological and current opening. |
| Ziems et al. 2024, “Can Large Language Models Transform Computational Social Science?” | MOVE TO OPTIONAL | Valuable benchmark and review; too broad for required reading once each domain has a stronger sociology paper. |
| Abdurahman et al. 2025 primer | MOVE TO OPTIONAL | Useful evaluation framework from psychology; assigned tasks will teach evaluation more directly. |
| Davidson and Karell 2025 | KEEP | Required in Session 1 as the course map. |
| *NYT* “GPT from Scratch” | DROP | Technical-history format no longer matches the architecture. |
| Karpathy 2023/2025 videos | MOVE TO OPTIONAL | Use short selected segments only; do not require multi-hour architecture viewing. |
| Kozlowski, Taddy, and Evans 2019 | MOVE TO OPTIONAL | Important cultural-computational precursor; no longer merits a full embeddings week. |
| Stoltz and Taylor 2021 | MOVE TO OPTIONAL | Same rationale; useful background for cultural measurement. |
| Rodríguez and Spirling 2022 | DROP | Excellent embeddings methods paper, but displaced by LLM-centered measurement and limited weekly load. |
| Caliskan, Bryson, and Narayanan 2017 | MOVE TO OPTIONAL | Useful prehistory for Session 13 audits. |
| Hassani embeddings primer | DROP | No separate embeddings lab. |
| Hugging Face transformer chapter | MOVE TO OPTIONAL | Reference for interested students; concepts will be taught compactly in Session 1. |
| Bonikowski, Luo, and Stuhler 2022 | MOVE TO OPTIONAL | Strong sociological application but belongs as background to measurement, not a transformer week. |
| Wankmüller 2024 | MOVE TO OPTIONAL | Useful technical bridge; exceeds the required technical depth. |
| Le Mens et al. 2023 | MOVE TO OPTIONAL | Useful validation example but not specific enough to the central LLM workflow. |
| Vaswani et al. 2017 | DROP | Architecture paper is not pedagogically necessary for this seminar. |
| Törnberg 2024 annotation paper | MOVE TO OPTIONAL | Retain as an accessible comparative benchmark; sociology-specific measurement papers now lead. |
| Wang 2023 political-text classification | DROP | Replaced by Chae and Davidson's broader sociological comparison. |
| Brown et al. 2020 | DROP | Historically important but not a sensible required methods reading in 2026. |
| Egami et al. downstream-inference framework | MOVE TO OPTIONAL | Essential advanced extension for Session 2; chapter and lab introduce the core issue. |
| Baumann et al. 2025 annotation-hacking preprint | MOVE TO OPTIONAL | Important adversarial extension once publication status and version are rechecked. |
| Than et al. 2025 | KEEP | Required in Session 3. |
| De Paoli 2024 | MOVE TO OPTIONAL | Retains a useful provocation, but the 2026 qualitative debate is richer and more current. |
| Stuhler, Dang Ton, and Ollion 2025 | KEEP / MOVE | Required in Session 2, not qualitative Session 3. |
| Chen 2025 unpublished fiscalization manuscript | DROP | Do not require an unpublished local application when general methods and published examples are available. |
| Ibrahim and Voyer 2024 preprint | REPLACE | Replace with the published 2026 *Qualitative Research* version. |
| Meng et al. 2024 | MOVE TO OPTIONAL | Human–LLM synergy case remains useful but is not core. |
| Heseltine and Clemm von Hohenberg 2024 | MOVE TO OPTIONAL | Useful expert-annotation comparison; superseded as a required reading by sociology-first measurement work. |
| Le Mens and Gallego 2025 | MOVE TO OPTIONAL | Useful scaling technique, but political-text-specific. |
| Alizadeh et al. 2025 | MOVE TO OPTIONAL | Especially useful for local/open-model guidance rather than the core theory discussion. |
| Barrie, Palmer, and Spirling 2024/2025 | KEEP | Updated November 2025 manuscript required for Session 12. |
| AIPathways prompt video | DROP | Replace generic “prompt engineering” with task specification, validation, and documented model calls. |
| Argyle et al. 2023, “Out of One, Many” | MOVE TO OPTIONAL | Historically central, but Boelaert, Kozlowski–Evans, Wang et al., and Xie et al. now provide a stronger critical sequence. |
| Boelaert et al. 2025 | KEEP | Required in Session 7. |
| Bisbee et al. 2024 | MOVE TO OPTIONAL | Strong controversy paper; the required load already contains a sociology-centered critique and identity analysis. |
| Wang, Morgenstern, and Dickerson 2025 | KEEP | Required in Session 7. |
| Kozlowski and Evans 2025 | KEEP | Required in Session 7. |
| Santurkar et al. 2023 | MOVE TO OPTIONAL | Important precursor for whose opinions models reflect. |
| Velez and Liu 2025 | MOVE TO OPTIONAL | Useful treatment-personalization application, but not the best anchor for conversational treatment in 2026. |
| Argyle et al. 2025 persuasion | MOVE TO OPTIONAL | Keep as theory-testing example; Session 6 uses newer large-scale conversational evidence. |
| Hackenburg and Margetts 2024 | REPLACE | Replace as required reading with Hackenburg et al. 2025 in *Science*, which directly compares the levers of conversational persuasion. |
| Costello, Pennycook, and Rand 2024 | MOVE TO OPTIONAL | Strong substantive application; required readings need to isolate design features across cases. |
| Törnberg et al. 2023 social-media simulation | MOVE TO OPTIONAL | Useful applied GABM extension after the basic comparison lab. |
| Park et al. 2024, 1,000 people | MOVE TO OPTIONAL | Valuable bridge between digital twins and agents, but not a clean introduction to generative ABM architecture. |
| Gao et al. 2025 caution on surrogates | MOVE TO OPTIONAL | Covered by the Session 7 critical sequence. |
| Cheung et al. 2025 cognitive biases | MOVE TO OPTIONAL | Better placed with audits than simulation; audit week has stronger sociological/cultural studies. |
| Kozlowski, Kwon, and Evans 2024 preprint | MOVE TO OPTIONAL | Promising in-silico sociology application; current required sequence emphasizes validated published work. |
| Hewitt et al. 2024 working paper | REPLACE | Superseded by Ashokkumar et al. 2026 in *Nature*. |
| Binz et al. 2025, Centaur | MOVE TO OPTIONAL | Important cognition model, but less central to sociological inference and too technically divergent for the core lab. |
| Horton 2023, *Homo Silicus* | MOVE TO OPTIONAL | Foundational economics framing, retained for comparison rather than required sociology reading. |
| Manning, Zhu, and Horton 2024 | REPLACE | The research-agent topic is now better served by the 2026 end-to-end automation literature and chapter §10.6. |
| Agrawal et al. 2025, Seamless Interaction | DROP | Technically interesting dataset, but it anchored the unsuccessful interaction week and does not support the approved inference sequence. |
| Reece et al. 2023, CANDOR | MOVE TO OPTIONAL | Useful audio and interaction dataset for Session 4, not a theory anchor. |
| Goffman 1959 | MOVE TO OPTIONAL | Valuable sociological lens but no longer required in a methods-heavy multimodal week. |
| Blumer 1969 | DROP | Instructor decision; no sufficiently direct, current LLM use justifies retaining it. |

## Items requiring a final metadata check before syllabus freeze

- Kim and Lee: confirm the final *Sociological Methodology* year, volume, pages, DOI, and whether the July 2026 accepted version differs from arXiv.
- Arminio et al.: confirm final volume, issue, pages, and publication year once the issue record stabilizes.
- Ibrahim and Voyer; Nguyen and Welch: confirm issue, volume, and page ranges.
- Kim et al. “Societies of Thought” and the consciousness/alignment paper: check for conference or journal versions superseding the cited arXiv versions.
- Barrie and Törnberg and the Ashery et al. reply: check whether the debate has moved beyond the current preprints.
- Barrie, Palmer, and Spirling: check for a journal version superseding the November 4, 2025 manuscript.

## Cross-check against current course and workshop designs

This audit also checked publicly available 2025–26 teaching materials. These are design comparators, not sources to copy.

- Daniel Karell's Fall 2025 Yale sociology activity, [“Testing AI Subjects”](https://poorvucenter.yale.edu/resource/testing-ai-subjects), pairs text labeling with synthetic survey respondents. It supports separating measurement from synthetic-subject validation while reusing the same prompting skills across both.
- Northwestern's Fall 2025 [Introduction to Computational Methods in the Social Sciences](https://sociology.northwestern.edu/documents/faculty-docs/syllabi/shiffer-sebba-476.pdf) culminates in a student-designed data-to-paper pipeline. It supports the cumulative workflow idea, but the present course will expose and validate each component before students assemble a full pipeline.
- The University of Michigan's July 2026 [Practical LLMs for Social Science Research](https://nimlas.isr.umich.edu/workshops/past/) explicitly targets researchers with little or no programming experience and moves across text, surveys, interviews, evaluation, and open models. This reinforces the decision to slow the code and compare traditional and LLM-assisted methods rather than front-load architecture.
- NYU Shanghai's July 2026 [Agentic AI for Social Science Research](https://caser.shanghai.nyu.edu/training/2026-summer-school-methods/course-and-instructor-introduction/agentic-ai-for-social-science-research/) moves from collection and cleaning through qualitative analysis and evidence synthesis. It confirms that agents merit a dedicated late-course session; the proposed syllabus adds bounded-source provenance and human verification rather than treating natural-language orchestration as sufficient rigor.

The cross-check therefore changes no required reading. It strengthens four design commitments for Phase 3: one visible input–transformation–output trace in every lab; repeated comparison with a non-LLM baseline; cumulative research records; and a late, bounded agent workflow only after students understand the component tasks.

## Recommendation

Approve the sequence at the level of **reading functions**, then trim page ranges rather than dropping the contrasts that make the course coherent. Sessions 3, 6, 10, and 13 deliberately assign competing or differently situated claims; students should not read those papers as a pile of findings, but as arguments about what counts as evidence.
