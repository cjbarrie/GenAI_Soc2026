# Extended literature review — LLMs across the qualitative research process

**Status:** Supplementary review requested after the first Session 3 synthesis. Literature checked through 19 August 2026. This document deliberately looks beyond post-hoc coding and thematic analysis, especially at AI-moderated interviews and AI-assisted data collection.

## Why the first review was too narrow

The first Session 3 review concentrated on what happens after a qualitative corpus exists: coding, theme development, interpretation, source traceability, and reflexivity. The newer literature makes that boundary untenable. LLMs are now being used to:

- draft and pilot interview guides;
- recommend follow-up questions to a human interviewer;
- administer fixed questions while generating adaptive probes;
- conduct complete text or voice interviews;
- analyze the transcripts they helped produce;
- simulate focus groups or “synthetic participants”; and
- screen, summarize, or release large collections of interview data.

This matters methodologically because interview data are not raw accounts waiting to be collected. They are produced through an interaction. If an LLM selects the follow-up, changes the pace, avoids a silence, repeats a formulation, or signals a particular institutional relationship, it helps produce the material that will later be coded and interpreted.

## A more useful spectrum of LLM involvement

| Arrangement | What the model does | Human role | Main methodological issue |
|---|---|---|---|
| Interview preparation | Drafts or stress-tests a guide | Researcher approves and pilots it | Simulated answers may conceal problems real participants would reveal. |
| Interview assistant | Privately suggests probes or reminders | Human decides whether and how to ask | Divided attention, deskilling, responsibility, and disruption of rapport. |
| Controlled adaptive interviewer | Administers researcher-authored questions and generates bounded probes | Researcher defines protocol and monitors | Tension between standardization and contextual responsiveness. |
| AI-moderated interview | Conducts the conversation directly by text or voice | Researcher designs and later reviews | The model becomes an interviewer effect and a representative of the institution. |
| End-to-end pipeline | Plans, interviews, codes, synthesizes, and quotes | Human validates selected stages | One system can recursively confirm patterns it helped create. |
| Synthetic interview | Model answers as a persona or simulated participant | Researcher prompts and interprets | Generated text is not evidence about the represented population. |

The literature is often described with the single phrase “AI interviewing,” but these arrangements distribute agency and responsibility very differently.

## 1. AI-led interviews: the positive empirical case

### Geiecke and Jaravel — conversations at scale

**Friedrich Geiecke and Xavier Jaravel. 2024–2026. “Conversations at Scale: Robust AI-led Interviews.”** Working paper, accepted version under development. [SSRN record](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4974382) and [open-source platform](https://github.com/friedrichgeiecke/interviews).

- Develops an open-source platform for text and voice AI-led interviews.
- Uses applications involving decision-making, political views, subjective mental states, and mental models of public policies.
- Compares transcripts with interviews conducted by trained sociologists and uses respondent ratings and other quality measures.
- Reports that AI-led interviews can be rated around the level of an average human interviewer under matched constraints.
- Finds substantially longer responses than conventional open-text survey fields and emphasizes hypothesis generation, measurement, and mechanism discovery.
- Makes the operational case for thousands of conversational interviews and mixed qualitative–quantitative analysis.

**Methodological caution:** the strongest comparison is often AI interview versus an open-text box or a constrained human chat/structured interview. That is important evidence, but it does not show equivalence to long, relational, ethnographic, or highly sensitive interviewing. “More words” is also not the same as richer situated understanding.

### Chopra and Haaland — early AI-led qualitative interviewing

**Felix Chopra and Ingar Haaland. 2023–2026. “Conducting Qualitative Interviews with AI.”** [SSRN record](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4572954) and [code](https://github.com/fchop/interviews).

- Introduces an LLM interviewer embedded in survey infrastructure.
- Applies the method to economic-policy views and other questions for which researchers want open-ended explanations at larger scale.
- Argues that adaptive probes reveal explanations and possible mechanisms that fixed open-ended questions miss.
- Uses the resulting material for inductive theme development and hypothesis generation.

**Course role:** an early social-science demonstration. It is useful for asking whether this is best understood as scalable qualitative interviewing, a new kind of conversational survey, or a hybrid method.

### Wuttke et al. — randomized human/AI comparison

**Alexander Wuttke, Matthias Aßenmacher, Christopher Klamm, Max Lang, Quirin Würschinger, and Frauke Kreuter. 2025. “AI Conversational Interviewing: Transforming Surveys with LLMs as Adaptive Interviewers.”** *LaTeCH-CLfL 2025*. [ACL Anthology](https://aclanthology.org/2025.latechclfl-1.17/).

- Randomly assigns university students to AI or human conversational interviews using the same political questionnaire.
- Evaluates protocol adherence, response quality, participant engagement, and interview effectiveness.
- Finds viable data quality broadly comparable to the human condition in this controlled setting.
- Publishes data and materials, making it a useful methodological teaching case.

**Course role:** the cleanest small experimental comparison. It also makes clear that the inferential target is interviewer-mode performance under a defined protocol, not “qualitative research” in general.

### Panfilova et al. — auditing adaptive questioning

**Anastasia Panfilova et al. 2026. “The AI Interviewer: Multi-faceted Evaluation of Adaptive Questioning by Large Language Models.”** *Scientific Reports* 16:20257. [Article](https://doi.org/10.1038/s41598-026-46517-7).

- Compares six models as adaptive interviewers across 54 semi-structured psychological questions.
- Evaluates whether follow-ups are benevolent, necessary, context-aware, open, and appropriately skipped.
- Finds systematic model differences in empathy, speed, coverage, contextualization, and format compliance.
- Provides prompts, orchestration, and an annotation rubric for auditing interview-agent behavior.

**Important limitation:** the controlled comparison uses a single LLM as the interviewee to standardize responses. It is therefore strong evidence about differences among interviewer agents under controlled conditions, not direct evidence about how diverse human participants experience or respond to them.

## 2. The critical empirical case: engagement is not depth

### Cuevas et al. — high-quality surface interaction, weak richness

**Alejandro Cuevas, Jennifer Scurrell, Eva Brown, Jason Entenmann, and Madeleine Daepp. 2025. “Collecting Qualitative Data at Scale with Large Language Models: A Case Study.”** *Proceedings of the ACM on Human-Computer Interaction* 9(2). [Open record](https://doi.org/10.3929/ethz-b-000735095).

- Compares three interviewing chatbots in a study of 399 participants, including two LLM systems and a hard-coded baseline.
- Measures engagement, participant experience, established chatbot-quality criteria, and a new measure of qualitative richness.
- Finds that systems can elicit responses judged good on conventional interaction metrics while rarely obtaining participants' specific motives and personalized examples.
- Finds low agreement between human and LLM evaluations of both quality and richness.

**Course role:** the best counterweight to the scale narrative. It shows that satisfaction, response length, conversational smoothness, and qualitative depth are different outcomes.

### Jack, Cooper, and Flower — what the interaction actually felt like

**Tullia Jack, Alex Cooper, and Lisa Flower. 2026. “Automating the Qualitative Interview? Using Gen AI Chatbots in Social Science Research.”** [DOI](https://doi.org/10.1177/20597991261448157).

- Uses a Gemini-based chatbot to interview 74 social scientists at a Swedish university, followed by email reflections from 23 participants.
- Produces 149 pages of text from mostly 8–12 minute interviews with high completion.
- The bot usually remains on topic, adapts probes, and avoids prohibited sensitive topics.
- Participants sometimes value its directness, knowledge, and nonjudgmental character.
- Others experience excessive friendliness, repetition, premature follow-up, disrupted thought, and reduced engagement.
- The authors conclude that the study generated abundant data but did not achieve the depth and nuance they would want from qualitative interviewing.
- The paper is unusually valuable because it analyzes interviewing and then experiments with model-assisted analysis of the same corpus; plausible ideal types and mostly accurate quotations coexist with hallucinated demographic claims and weakened researcher reflexivity.

**Course role:** the strongest sociological paper for teaching AI-moderated interviews. It treats talk as situated data and asks how interviewer identity, pacing, institutional setting, and sampling shape the accounts produced.

### Beltoft, Schneider-Kamp, and Askegaard — the ethnographic limit

**Stine Lyngsø Beltoft, Peter Schneider-Kamp, and Søren Askegaard. 2025. “Interview Bot: Can Agentic LLMs Perform Ethnographic Interviews?”** *ICAART 2025*. [Paper](https://www.scitepress.org/Papers/2025/133878/133878.pdf).

- Designs an open-weight agentic chatbot to approximate adaptability and empathy in ethnographic interviews.
- Finds that it can engage participants and collect meaningful data but does not fully reproduce human-facilitated interviewing.
- **Course role:** a targeted extension showing that “interview” is not one homogeneous method. Ethnographic interviewing demands field knowledge, situated responsiveness, and attention to more than the propositional content of answers.

### Very recent deployed evidence — probe-light behavior and trust

**“When the Interviewer Is a Bot: Behavior, Breakdowns, and Trust in MLLM-Led Interviews.” 2026.** [arXiv](https://arxiv.org/abs/2608.10412).

- Observes a deployed voice-based multimodal interviewer in a practice study with 15 participants and a subsequent human reflection interview.
- Reports an acknowledgment-heavy but probe-light style; deepening probes comprise only a small proportion of turns.
- Documents information loss, premature termination, latency, and interruption.
- Shows that trust depends partly on what institutional delegation to AI signals, while reduced social pressure can coexist with shallower elaboration.

**Status caution:** this appeared in August 2026 and is a preprint. It is valuable as emerging evidence and a lecture example, not yet a core assigned authority.

## 3. Hybrid interviewing may be more important than full automation

### Liu et al. — what researchers want from an interview assistant

**Zhe Liu, Jiamin Dai, Cristina Conati, and Joanna McGrenere. 2025. “Envisioning AI Support during Semi-Structured Interviews Across the Expertise Spectrum.”** *Proceedings of the ACM on Human-Computer Interaction* 9(2). [DOI](https://doi.org/10.1145/3710909).

- Interviews 16 researchers with varying interviewing experience.
- Researchers envision help with research objectives, real-time reminders, and interpersonal communication.
- They also worry about divided attention, disruption, and long-term erosion of interview skill.
- Frames the interview as a triangular collaboration among interviewer, interviewee, and AI rather than a simple user–tool interaction.

**Course role:** a better entry point for students than immediate autonomous interviewing. It allows a concrete discussion of what judgment remains with the interviewer.

### Zhang et al. — AI-generated follow-up questions in practice

**He Zhang, Yueyan Liu, Xin Guan, Jie Cai, and John M. Carroll. 2025–2026. “Harnessing the Power of AI in Qualitative Research: Role Assignment, Engagement, and User Perceptions of AI-Generated Follow-Up Questions in Semi-Structured Interviews.”** [Preprint](https://arxiv.org/abs/2509.12709).

- Uses a Wizard-of-Oz arrangement in which GPT-4o proposes follow-up questions that a co-interviewer may select or edit.
- Finds that suggestions can catch overlooked details, make broad concepts more concrete, and open useful new paths.
- Also finds that an individually “good” follow-up can interrupt the interview's intended direction or rewrite its purpose.
- Emphasizes role boundaries, interviewer agency, delivery, tone, and timing.

**Course role:** useful current evidence for a model-as-copilot design. It should be labeled as a preprint.

### Ethics of live AI-generated probes

**“Ethics and Social Responsibility in AI-Assisted Interviewing: An LLM-in-the-Loop Study of AI-Generated Follow-Up Questions.” 2026.** [Preprint](https://arxiv.org/abs/2606.30980).

- Studies 17 interviewers using editable real-time GPT-4o follow-up suggestions.
- Identifies five connected concerns: unpredictable harm or discriminatory language; reduced respect through divided attention and missing nonverbal cues; unequal technological access; unclear responsibility; and privacy, disclosure, and compliance risks.
- **Course role:** governance and ethics extension. The important question is not only whether the suggested probe is relevant, but who is responsible for asking it and for any harm it causes.

## 4. System design is a methodological choice

### Gårdhus et al. — standardization, local models, and control

**Tobias Gårdhus, Nikolas Vitsakis, Fie Lejre Frederiksen, Anna Rogers, and Hjalmar Bang Carlsen. 2026. “AInterviewer: A Platform for Designing and Conducting AI-led Qualitative Interviews.”** *ACL 2026 System Demonstrations*. [ACL Anthology](https://aclanthology.org/2026.acl-demo.12/).

- Separates controlled administration of researcher-authored questions from LLM-generated adaptive functions.
- Can use locally hosted models, directly addressing confidentiality, data security, and dependence on proprietary providers.
- Supports guide design, pilot testing, distribution, and monitoring.
- Makes a central design tradeoff visible: fully generative interviewing maximizes adaptability but reduces control over wording and question order.

**Course role:** an excellent technical example for the approved hybrid environment. It connects local models to a substantive research reason rather than presenting Ollama or local hosting as merely an installation option.

### Anthropic Interviewer — scale and the closed-loop problem

**Anthropic. 2025–2026. “Anthropic Interviewer.”** [Method overview](https://www.anthropic.com/about-anthropic-interviewer) and [initial 1,250-participant study](https://www.anthropic.com/research/anthropic-interviewer).

- Uses Claude to help draft the interview plan, conduct adaptive interviews, and synthesize themes and quotations.
- The initial study interviewed 1,250 professionals; later deployments reached much larger multilingual samples.
- Reports very high participant satisfaction and publishes methodological and transcript material.

**Course role and limitation:** this is a consequential real-world case, but it is company research about people's experiences with the company's own technology, using that company's model to interview and help analyze. It should be taught as an institutional and methodological case, not as independent validation of the method.

The design raises a productive question:

> What happens when the same model family helps frame the questions, conduct the interviews, classify the answers, and inform the institution whose technology is being discussed?

## 5. Privacy and consent become harder as interviews become richer

### Re-identification of qualitative transcripts

**Tianshi Li. 2026. “Agentic LLMs as Powerful Deanonymizers: Re-identification of Participants in the Anthropic Interviewer Dataset.”** [arXiv](https://arxiv.org/abs/2601.05918).

- Demonstrates that public interview details can be cross-referenced with web sources using ordinary agentic tools.
- Links several ostensibly anonymized scientist interviews to scientific works and, in some cases, likely individuals.
- Shows that removing names is not sufficient when rich narrative details form a distinctive digital fingerprint.

This risk is especially important for qualitative research because depth and contextual detail—the qualities researchers often want—also increase re-identification risk.

### Consent is not a one-line disclosure

An AI-moderated interview may involve:

- audio capture and speech-to-text;
- transfer to one or more model providers;
- dynamically generated questions not individually reviewed in advance;
- model-created memory or participant profiles;
- automated safety classification;
- transcript analysis by another model;
- data retention and possible model-provider logging; and
- risks that cannot be removed by ordinary pseudonymization.

A useful research record should therefore distinguish consent to participate, consent to AI moderation, consent to third-party processing, consent to transcript release, and consent to future automated analysis.

## 6. LLMs also alter who or what counts as a participant

### Participant use of LLMs in online focus groups

**Lucy Stafford, Catherine Preston, and Alexandra Pike. 2024. “Participant Use of Artificial Intelligence in Online Focus Groups: An Experiential Account.”** *International Journal of Qualitative Methods* 23. [DOI](https://doi.org/10.1177/16094069241286417).

- Identifies nine of 42 participants using chat responses as potentially submitting LLM-generated material.
- Emphasizes that AI-text detection is fallible and that surveillance-oriented responses can exclude participants who need text chat for accessibility, privacy, or anxiety reasons.
- Considers both prevention and the possibility of treating model-assisted participant responses as part of the social phenomenon under study.

### Authenticity, deepfakes, and unequal verification

**Alan Santinele Martino and Kristen Hardy. 2026. “Authenticity in Question: Navigating Qualitative Interviewing in the Era of Artificial Intelligence and Deepfakes.”** *Sociological Research Online*. [DOI](https://doi.org/10.1177/13607804251403342).

- Argues that mandatory video or ID verification can reproduce ableist, racialized, and classed standards of believability.
- Draws on crip, feminist, and decolonial methods to propose relational ethics rather than escalating surveillance.
- **Course role:** essential counterweight to a simple “verify that participants are human” checklist.

### Synthetic respondents are not AI-moderated human interviews

Some papers propose using LLM personas to expand or probe an existing corpus. These can be useful as thought experiments or codebook stress tests, but their outputs are model-generated conjectures, not observations of the represented population.

This material belongs primarily in Session 7 on synthetic populations. Week 3 should establish the categorical distinction:

- **AI interviewer, human respondent:** the model helps produce empirical human data.
- **Human interviewer, AI respondent:** the researcher is studying or eliciting model behavior.
- **AI interviewer, AI respondent:** a simulation or system evaluation, not human qualitative data.

## 7. New analysis literature also sharpens the debate

The second search surfaced several useful 2026 contributions beyond the original three papers.

### Xu — a worked pro-AI account of reflexive thematic analysis

**Wen Xu. 2026. “Doing Thematic Analysis in the Age of Generative AI: Practices, Ethics and Reflexivity.”** *International Journal of Qualitative Methods*. [DOI](https://doi.org/10.1177/16094069261425173).

- Provides an end-to-end worked example organized around Braun and Clarke's phases.
- Explicitly distinguishes “Big Q” reflexive thematic analysis from narrow coding reliability exercises.
- Uses a dataset with which the researcher had already spent roughly eighteen months, allowing model suggestions to be judged against substantial prior immersion.
- Argues that AI can participate in a human-led reflexive process when contextual knowledge, interpretive agency, reflexivity, and ethics remain central.

**Course role:** a valuable constructive counterposition to Nguyen and Welch. It may be more directly about interpretation than Than et al., though adding it as a fourth full reading would overload the week.

### Greenhalgh — move beyond adoption versus refusal

**Trisha Greenhalgh. 2026. “Reflexive Qualitative Research and Generative AI: A Call to Go Beyond the Binary.”** *Qualitative Inquiry*. [DOI](https://doi.org/10.1177/10778004261429383).

- Reframes the issue around where epistemic authority resides and whether AI displaces or constrains reflexive engagement.
- Treats refusal as legitimate in some settings while arguing that categorical camps can obstruct serious governance and methodological judgment.
- **Course role:** a concise framing text or final slide quotation, not another main empirical paper.

### Forster et al. — an auditable multi-stage pipeline

**Eva Forster et al. 2026. “Multi-Stage LLM Pipeline to Support Qualitative Content Analysis: A Proof of Concept Experiment with Expert Validation.”** [DOI](https://doi.org/10.3233/SHTI260065).

- Applies segmentation, coding, concept development, and quotation extraction to 28 semi-structured interview transcripts.
- Uses five researchers from the original study to evaluate results.
- Reports strong overlap and traceability, with most outputs judged usable after minor revision.
- **Course role:** current applied evidence for structured, auditable pipelines. It represents content analysis more readily than fully reflexive interpretation.

## What the AI-interview literature actually establishes

The evidence supports several bounded conclusions:

1. LLM interviewers can administer protocols consistently and generate adaptive probes at a scale unavailable to human interviewers.
2. In controlled or relatively structured settings, resulting data can compare favorably with open-text survey responses and sometimes with human interview conditions.
3. Participants often report high satisfaction, nonjudgment, and willingness to disclose.
4. Model, prompt, orchestration, interface, voice/text modality, and institutional setting all alter the interaction.
5. High satisfaction, response length, or protocol coverage does not establish contextual richness, rapport, theoretical usefulness, or ethical adequacy.
6. AI moderation changes the corpus itself; interviewer behavior cannot be treated as neutral infrastructure.
7. Full automation introduces responsibility, consent, privacy, and closed-loop interpretation problems that are not solved by validating individual questions.

## Seven evaluation questions for an AI-moderated interview study

1. **Comparison:** Is the system being compared with an open-text box, a novice interviewer, a trained qualitative interviewer, or an ethnographic relationship?
2. **Interview target:** Is the aim standardized measurement, hypothesis generation, elicitation of mechanisms, life-history understanding, or relational interpretation?
3. **Interaction:** Which follow-ups were asked, skipped, rephrased, or generated, and how did that vary across participants?
4. **Interviewer effect:** How did disclosure, tone, pacing, trust, and institutional legitimacy differ because the interviewer was an AI?
5. **Coverage and depth:** Did the interaction cover the guide, and did it elicit concrete episodes, motives, contradictions, and situated examples?
6. **Governance:** Who is responsible for harmful, leading, or inappropriate questions, and what human intervention was possible?
7. **Provenance:** Can another researcher reconstruct the model, prompt, interface, modality, turn history, safety rules, provider route, and analysis procedure?

These questions are more defensible than asking whether “AI interviews are as good as human interviews.”

## Recommended placement in this course

### Session 3 — qualitative analysis

Add a short upstream bridge, not a second major topic:

- State explicitly that a qualitative corpus is co-produced rather than merely found.
- Use one AI-moderated transcript turn to show how a generated follow-up changes what evidence becomes available.
- Mention Jack, Cooper, and Flower as the empirical case demonstrating that abundance and completion do not guarantee depth.
- Add an `interview_mode` and `interviewer_provenance` field to the synthetic mutual-aid excerpts.

This strengthens the Week 3 example without sacrificing its central focus on interpretation.

### Session 6 — the model as interactant

Make AI-moderated and AI-assisted interviewing a substantial part of this week. Session 6 already asks what changes when the model becomes an interactant. The topic fits better here because:

- the interaction is the treatment and the data-generation process;
- different participants receive different probes and therefore different exposure;
- rapport, disclosure, perceived judgment, and institutional legitimacy become outcomes;
- the ordered dialogue record already matches the planned Python trace; and
- human, copilot, controlled-adaptive, and fully automated designs can be compared directly.

A strong Session 6 reading set could pair:

- **Geiecke and Jaravel or Wuttke et al.** for the positive scale/quality case;
- **Jack, Cooper, and Flower or Cuevas et al.** for the depth and interactional critique; and
- **Liu et al.** for the hybrid copilot design.

The current persuasion papers can then remain as a second application of model-as-interactant rather than the entire identity of the week.

### Session 7 — synthetic populations

Keep synthetic respondents and persona interviews here. Make clear that generating a plausible interview response is not the same as collecting human testimony. Stafford et al. and Martino and Hardy can bridge participant authenticity, accessibility, and verification without collapsing those questions into silicon sampling.

## Provisional recommendation

AI-moderated interviewing should not be a small aside in the course as a whole. It is now developed enough to receive sustained treatment, but moving it wholesale into Session 3 would again make that week too broad. The cleanest architecture is:

`Session 3: how an LLM participates in interpreting qualitative material`

`Session 6: how an LLM participates in producing qualitative material through interaction`

`Session 7: what changes when the participant is simulated rather than human`

That sequence also gives students a clearer conceptual progression: **interpret a corpus → co-produce a corpus → simulate a population**.
