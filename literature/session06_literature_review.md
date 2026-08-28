# Session 6 literature review — when the model becomes an interviewer

**Status:** Stages 1–2 complete; awaiting Review Gate 1  
**Last updated:** 2026-08-24

## What this session needs to do

By the end of the session, students should be able to explain why an interview is not simply a neutral way of collecting answers, identify what changes when a model asks the questions and chooses the probes, and use a small Python audit to reconstruct the interview that a participant actually experienced.

The central methodological distinction is:

> Assignment to an interview condition is not the same as exposure to a particular interview.

In an adaptive conversation, later questions depend on earlier answers. Two people assigned to the same system may therefore receive different probes, disclose different information, and encounter different interviewer behaviour. Those differences are part of the data-generating process.

## Audit of the current Session 6 materials

### What is worth retaining

- The existing title question — “What changes when the model becomes an interactant?” — is broad enough to support the rebuilt session.
- The distinction among assignment, exposure, response, and output is methodologically useful.
- The current code uses an ordered list of turns and a state dictionary. This is the right Python progression after the earlier sessions.
- Conversational persuasion is a useful second application because it makes the causal stakes of a changing interaction especially clear.
- The session falls immediately before the midterm release, so a bounded exercise in reading and explaining code is appropriate.

### What is not yet working

- The deck is only a short scaffold. It lacks a history of interviewing, a sociological account of interaction, paper-specific evidence, and a cumulative empirical example.
- The current readings make the week look mainly like a persuasion session. They do not adequately explain interviewing as a method.
- “Interactant” remains abstract. Students are not shown what a human interviewer does, what an AI interviewer does differently, or why this affects inference.
- The code counts turns and unique topics, but does not preserve the exact probes, their source, their order, or the answers to which they responded.
- The current Python output therefore cannot reconstruct treatment exposure. It also gives students no basis for discussing rapport, repair, interviewer effects, or stopping decisions.
- The workbook explains syntax line by line, but the research object remains underspecified. Students can follow the loop without understanding why a sociologist would need the resulting record.

## Continuity with the course

Session 3 asked how a researcher interprets an existing qualitative corpus. Session 6 asks how the corpus is produced through interaction. Session 7 will ask whether models can stand in for people or populations.

The transition should be explicit:

1. In qualitative coding, the researcher revisits and interprets a corpus.
2. In an interview, the interviewer helps produce that corpus by asking, probing, clarifying, and moving on.
3. In an AI-moderated interview, some of those decisions are made by a model during the interaction.
4. The resulting transcript is therefore both substantive evidence and a record of an adaptive intervention.

Session 5 provides a second bridge. A conventional vignette experiment assigns a fixed treatment. Velez's adaptive survey work lets the shared item bank change as evidence accumulates across respondents. Session 6 moves to participant-specific adaptation: the next question can change because of what this participant just said.

These are different forms of adaptation and should not be collapsed:

- **Fixed treatment:** everyone assigned to a condition receives the same wording.
- **Evolving shared item bank:** later respondents may encounter questions selected using earlier respondents' results.
- **Participant-specific tailoring:** background information determines which branch a respondent receives.
- **Turn-by-turn interviewing:** the next probe is generated from the current conversation.

## What came before AI interviewing

The earlier version of this review treated “what came before” too narrowly as a debate about standardized questions and conversational repair. The rebuilt session needs a longer sociological lineage. Interviewing has been used to recover lives, study responses to shared situations, measure comparable attributes, interpret meaning, and analyse social boundaries. Those purposes imply different standards for a good interview.

The history should therefore be taught as a sequence of changing research objects and interviewer jobs, not as a list of canonical names.

### 1. Personal documents and life histories: connecting a life to social change

An early sociological problem was how to connect large processes—migration, urbanization, disorganization, occupational change—to the lives through which they were experienced.

Thomas and Znaniecki's *The Polish Peasant in Europe and America* assembled letters, autobiographical writing, institutional records, and the life history of an immigrant. The point was not simply to solicit an opinion. Personal documents were evidence about how social values and individual attitudes developed across a life and within changing institutions.

The Chicago tradition subsequently used life and case histories in studies of migration, delinquency, work, neighbourhoods, and marginal social worlds. Interviews often sat alongside observation, documents, and official records. This matters because it prevents the class from treating a transcript as a self-sufficient representation of a person.

**Historical example for the slides.** Use the University of Chicago archive's life-history materials and a page from the Władek life record. Students should see the material form of the evidence: letters, case records, autobiographical narrative, and researcher interpretation.

**Question for an AI interviewer.** Can a short model-led conversation recover a life process, or does it mainly produce decontextualized answers? What other records would be needed to interpret the account?

**Useful sources.**

- Thomas and Znaniecki, *The Polish Peasant in Europe and America*, especially the methodological introduction to the life record.
- University of Chicago Library, “Life History Method,” with examples from the Chicago sociology archives: https://www.lib.uchicago.edu/collex/exhibits/mapping-young-metropolis/life-history-method/

### 2. The focused interview: probing responses to a situation already studied

Merton and Kendall's 1946 focused interview is an especially important predecessor for this course because it joins experimental design to open-ended interviewing. The researcher first analyses a shared situation—such as a film, radio programme, or other communication—and then interviews people exposed to it.

The interview was meant to discover:

- which aspects of the situation mattered to participants;
- where actual responses differed from the researcher's prior expectations;
- how responses varied across groups; and
- what process connected exposure to response.

Merton and Kendall also gave the interviewer substantive criteria: range, specificity, depth, and attention to personal context. Probing was not generic encouragement. It was a way of connecting a participant's account back to a known situation without forcing the expected answer.

**Historical example for the slides.** Show a page of the original *American Journal of Sociology* article alongside one short exchange in which a vague evaluation is followed by a request for a specific moment or feature. This provides a direct predecessor to model-generated follow-up questions.

**Question for an AI interviewer.** Does the model recognize what requires a probe? Can it ask for specificity without leading? Does it know enough about the shared stimulus to notice a discrepancy?

**Source.** Merton and Kendall (1946), “The Focused Interview,” *American Journal of Sociology*: https://doi.org/10.1086/219886

### 3. Standardized survey interviewing: treating interviewer discretion as a source of error

Large-scale survey research gave the interview a different job. The aim was to administer comparable questions to many respondents and turn their answers into variables. Standardized wording, neutral probes, interviewer training, response categories, and skip patterns were designed to reduce interviewer-related variation.

This tradition should not be presented as simply naïve. Standardization addresses a genuine causal and measurement problem: if interviewers phrase questions differently, explain terms differently, or selectively encourage elaboration, observed differences may reflect administration rather than respondents.

The consequence is a familiar trade-off. Fixing the wording can improve procedural comparability while failing to ensure that respondents interpret the wording in the same way.

**Historical example for the slides.** Use an interviewer instruction page from a survey instrument: exact question wording, an instruction to read as written, allowable neutral probes, and a skip pattern. This shows the interviewer as a trained administrator rather than an unconstrained conversational partner.

**Question for an AI interviewer.** Is the model reproducing a fixed instrument, choosing among approved probes, or composing unrestricted follow-ups? Each design makes a different reproducibility claim.

### 4. Interactional and cognitive critiques: an answer is produced turn by turn

Cicourel, Mishler, Briggs, and later conversation-analytic work challenged the idea that questions carry identical meanings independently of the interview encounter. Respondents interpret unfamiliar categories using everyday knowledge. Interviewers decide whether an utterance counts as an answer, repair misunderstanding, repeat or rephrase a question, and steer the exchange back toward the instrument.

Suchman and Jordan made this visible in standardized survey interviews. Ordinary conversation permits people to identify trouble and establish shared meaning; strict interviewing rules can block those resources. Schober and Conrad later tested the trade-off experimentally. Conversational clarification could improve the accuracy with which respondents mapped unusual circumstances onto official survey concepts, although it required more time and introduced variation in interviewer behaviour.

This strand supplies the most direct conceptual bridge to the Week 6 code. An interview is an ordered sequence in which each turn changes the context for the next. The research record must therefore retain the exact question, the exact answer, the repair or probe, and their order.

**Historical example for the slides.** Use one published transcript in which a respondent struggles with a survey category, followed by the standardized and conversational versions of the interview. Students should be able to point to the moment at which shared meaning succeeds or fails.

**Question for an AI interviewer.** Is a generated rephrasing legitimate clarification, a semantic change to the measure, or both? The answer cannot be inferred from the fact that the conversation continued smoothly.

**Useful sources.**

- Cicourel, *Method and Measurement in Sociology* (1964).
- Mishler, *Research Interviewing: Context and Narrative* (1986).
- Briggs, *Learning How to Ask* (1986).
- Suchman and Jordan (1990), “Interactional Troubles in Face-to-Face Survey Interviews.”
- Schober and Conrad (1997), “Does Conversational Interviewing Reduce Survey Measurement Error?”
- Conrad and Schober (2000), “Clarifying Question Meaning in a Household Telephone Survey”: https://doi.org/10.1086/316757

### 5. Feminist and reflexive interviewing: power, reciprocity, and rapport belong in the method

Feminist methodologists objected to accounts of interviewing that made the interviewer socially invisible. Oakley's critique drew attention to the relationship between interviewer and interviewee: who discloses, who can ask questions, whether the interviewer reciprocates, what emotional labour the exchange requires, and which features of the encounter disappear from the published methods section.

Bourdieu likewise treated the interview as a social relation structured by differences in position and capital. The interviewer cannot remove these relations by following a neutral script. The task is to understand and manage the effects of the research relationship rather than deny that it exists. His account also makes small interactional behaviours—attention, acknowledgment, gaze, encouragement—part of what enables an interview to proceed.

This tradition is essential for evaluating claims that a bot is “non-judgmental” or that respondents “feel heard.” Reduced embarrassment, apparent neutrality, and willingness to disclose may be advantages. They may also alter expectations of reciprocity, care, confidentiality, and institutional responsibility.

**Historical example for the slides.** Contrast the sparse methodological description Oakley criticized—number and length of interviews—with the interactional information it omits: the interviewer's identity, reciprocity, feelings, hospitality, rapport, and continuation of the relationship beyond the recorded encounter.

**Question for an AI interviewer.** What does the participant believe the system is, who do they think receives the disclosure, and what duties attach to the apparent listener? Disclosure is not automatically evidence of an ethically or substantively better interview.

**Useful sources.**

- Oakley (1981), “Interviewing Women: A Contradiction in Terms?”
- Bourdieu (1996), “Understanding,” *Theory, Culture & Society*: https://doi.org/10.1177/026327696013002002
- Oakley (2016), “Interviewing Women Again: Power, Time and the Gift”: https://doi.org/10.1177/0038038515580253

### 6. The active interview and the debate over what talk can establish

Holstein and Gubrium described the interview as an active site of meaning production. The respondent is not a repository from which stable facts are extracted; interviewer and respondent assemble an account using available interpretive resources.

Later sociological debate sharpened the question of what interview evidence is good for. Jerolmack and Khan warn against using verbal accounts as straightforward evidence of situated behaviour. Pugh, Lamont, and Swidler defend interviewing when the inferential target is appropriately specified: meaning, moral understanding, classification, institutional experience, cultural repertoires, or symbolic boundaries rather than unobserved action itself.

This gives the class a necessary limit claim. Improving an interviewer's probes does not turn an account into direct observation. An LLM may elicit a more detailed explanation while leaving the relation between explanation and action unresolved.

**Historical example for the slides.** Give students three claims drawn from the same interview passage: a claim about what the respondent said, a claim about how the respondent makes sense of the situation, and a claim about what the respondent actually does. Ask which claims the transcript supports.

**Question for an AI interviewer.** Is the system collecting reports of behaviour, eliciting cultural accounts, or observing action? More fluent probing cannot erase the distinction.

**Useful sources.**

- Holstein and Gubrium, *The Active Interview* (1995).
- Pugh (2013), “What Good Are Interviews for Thinking about Culture?”
- Jerolmack and Khan (2014), “Talk Is Cheap”: https://doi.org/10.1177/0049124114523396
- Lamont and Swidler (2014), “Methodological Pluralism and the Possibilities and Limits of Interviewing”: https://doi.org/10.1007/s11133-014-9274-z

### 7. Computer-assisted interviewing before LLMs: changing privacy, branching, and social presence

LLMs were not the first attempt to automate parts of an interview. Computer-assisted personal and telephone interviewing automated question display, skip logic, and data entry while leaving a human interviewer in place. Computer-assisted self-interviewing and audio-CASI moved sensitive questions from a human interviewer to a screen or recorded voice.

This earlier literature established that mode is substantive. In Tourangeau and Smith's comparison of interviewer-administered and computer-assisted modes, the presence and form of the interviewer affected reporting of sensitive behaviour. Later work showed that even nominally self-administered systems could retain interviewer effects through the human who introduced the system or remained nearby.

This is a crucial missing bridge. Before LLMs, automation could follow a researcher-authored branch but could not ordinarily interpret an open answer and compose a new substantive probe. LLMs change that particular allocation of discretion. They do not create mode effects, branching, or automated interviewing from nothing.

**Historical example for the slides.** Show the same sensitive item administered by a human interviewer, CASI, and audio-CASI. Then separate three changes: who voices the question, who can observe the answer, and whether the next question is fixed in advance.

**Question for an AI interviewer.** Does apparent privacy increase disclosure? If it does, are consent, data storage, model-provider access, and escalation procedures equally clear to the participant?

**Useful sources.**

- Tourangeau and Smith (1996), “Asking Sensitive Questions: The Impact of Data Collection Mode, Question Format, and Question Context”: https://doi.org/10.1086/297751
- Rogers et al. (1999), review of audio-CASI and sensitive-behaviour measurement: https://doi.org/10.2307/1534900

### The historical synthesis students need before the new papers

By the time the model appears, students should already understand that an interviewer may be expected to do at least six different things:

1. recover a situated life or experience;
2. connect a response to a shared stimulus or situation;
3. administer comparable questions;
4. recognize misunderstanding and repair it;
5. build a relationship in which disclosure becomes possible; and
6. help produce an account whose evidentiary status must still be specified.

An LLM can be assigned some or all of these jobs, but success on one does not imply success on the others. A system can adhere closely to a protocol while probing badly. It can elicit long answers while mishandling power or consent. It can feel easier to talk to while producing evidence poorly suited to the research claim.

The transition to the contemporary literature should therefore be:

> We already disagreed about what interviewers should do and what interview accounts can establish. LLMs make interviewer discretion scalable, partly automated, and harder to reconstruct unless the interaction is logged properly.

## Focal sources and the teaching job of each

### 1. Suchman and Jordan (1990), “Interactional Troubles in Face-to-Face Survey Interviews”

**Status:** Peer-reviewed, *Journal of the American Statistical Association*.  
**Link:** https://doi.org/10.1080/01621459.1990.10475331

**Question.** What does strict standardization miss about the interaction required to ask and answer survey questions?

**Design and evidence.** Conversation-analytic examination of problems and repair in face-to-face survey interviews.

**Finding.** Standardized interviewing can inhibit the clarification and repair that ordinary conversation uses to establish shared understanding.

**Teaching job.** Establish that adaptive conversational interviewing did not begin with LLMs. It enters an older conflict between comparability and responsiveness.

**Limitation.** The article predates LLMs and does not tell us whether model-generated probes solve or reproduce these interactional problems.

### 2. Geiecke and Jaravel (2026), “Conversations at Scale: Robust AI-led Interviews”

**Status:** Accepted at the *Review of Economic Studies*; author manuscript and open-source implementation available.  
**Author page:** https://www.xavierjaravel.com/research  
**Project repository:** https://github.com/AI-Researcher/ai-led-interviews

**Question.** Can AI-led text and voice interviews collect open-ended evidence at scale while retaining useful interview quality?

**Design and evidence.** The paper develops an AI-led interview system and evaluates it across multiple applications, including comparisons with human-led interviewing and respondent-reported measures.

**Finding.** The authors present a strong positive case for scalable adaptive interviewing and provide a concrete, inspectable system rather than a purely hypothetical proposal.

**Teaching job.** Show why researchers are interested: adaptive follow-up need not be restricted to a small number of human-led interviews. It also provides an architecture students can inspect: protocol, model, turn history, stopping rules, and stored transcript.

**Limitation.** Scale and favourable quality metrics do not by themselves establish equivalence to skilled qualitative interviewing. Selected sections must be assigned because the full manuscript is too long for the weekly reading load.

### 3. Jack, Cooper, and Flower (2026), “Automating the qualitative interview? Using Gen AI chatbots in social science research”

**Status:** Peer-reviewed, published online in 2026.  
**DOI:** https://doi.org/10.1177/20597991261448157

**Question.** What do social scientists themselves experience when interviewed by a generative-AI chatbot?

**Design and evidence.** Seventy-four social scientists completed chatbot-led interviews and twenty-three later reflected by email on the experience.

**Finding.** The system made completion and abundant data collection possible, but participants identified problems of depth, nuance, repetition, and interaction.

**Teaching job.** Supply a sociologically recognizable critique of the idea that a completed transcript is sufficient evidence of a successful interview. The follow-up reflections also make participant experience part of the evaluation.

**Limitation.** The study evaluates one implementation and a particular participant group. It should not be used to claim that all AI-led interviews have the same weaknesses.

### 4. Wuttke et al. (2025), “AI Conversational Interviewing: Transforming Surveys with LLMs as Adaptive Interviewers”

**Status:** Peer-reviewed conference paper, ACL Anthology.  
**Link:** https://aclanthology.org/2025.latechclfl-1.17/

**Question.** How does an AI conversational interviewer compare with a human conversational interviewer when both work from the same political questionnaire?

**Design and evidence.** University students were randomized to AI-led or human-led conversational interviews. The paper evaluates protocol adherence, interview quality, engagement, and efficacy; materials are public.

**Finding.** The controlled comparison makes it possible to separate some effects of interviewer type from differences in the questionnaire itself.

**Teaching job.** Provide the clearest experimental bridge from Session 5. Students can identify treatment assignment, participant exposure, outcomes, and remaining confounds.

**Limitation.** A controlled political questionnaire is not equivalent to an open-ended ethnographic or life-history interview.

### 5. Cuevas et al. (2025), evaluation of LLM-based qualitative interviews

**Status:** Peer-reviewed, *Proceedings of the ACM on Human-Computer Interaction*.

**Question.** Do conventional interaction metrics capture the substantive richness of an AI-led interview?

**Design and evidence.** A large participant study compares evaluations of AI-led interviews using conventional metrics and closer qualitative assessment.

**Finding.** An interview can look successful on completion or interaction measures while remaining weak in motives, examples, and qualitative richness. Human and model-based judgments can also disagree.

**Teaching job.** Motivate the validation section. Counting turns, topics, or completed interviews is an audit of process, not a measure of interview depth.

**Limitation.** Use the precise study measures and figures in the deck; do not reduce the result to a general claim that automated interviews are shallow.

### 6. Liu et al. (2025), “Envisioning AI Support during Semi-Structured Interviews Across the Expertise Spectrum”

**Status:** Peer-reviewed, *Proceedings of the ACM on Human-Computer Interaction*.

**Question.** Should AI conduct the interview, or should it support a human interviewer?

**Design and evidence.** Interviews with sixteen researchers examine proposed AI support across levels of interviewing experience.

**Finding.** Researchers see value in suggested probes and real-time support, but also anticipate divided attention, deskilling, and damage to rapport.

**Teaching job.** Prevent a false choice between wholly human and wholly automated interviewing. Introduce a copilot design in which the human can accept, edit, ignore, or defer a model suggestion.

**Limitation.** This is evidence about anticipated use and design priorities, not a causal estimate of interview quality.

### 7. Panfilova et al. (2026), “AI Interviewer”

**Status:** Peer-reviewed, *Scientific Reports*.

**Question.** How consistently do different models behave when they are asked to act as adaptive interviewers?

**Design and evidence.** Six models are compared under a controlled interviewer evaluation, using standardized conversational inputs.

**Finding.** Model choice changes interviewer behaviour and protocol performance.

**Teaching job.** Show why “the AI interviewer” is too vague a methods description. Model, version, prompt, decoding, and access route belong in the source record.

**Limitation.** Controlled or simulated conversational inputs cannot establish how human participants experience the interviewer.

### 8. Hackenburg et al. (2025), conversational persuasion

**Status:** Peer-reviewed, *Science*.

**Teaching job.** Retain as the main second application. If a model adapts its argument to the participant, the conversation is both treatment delivery and treatment record. This lets students transfer the interview audit to a clearer causal setting.

**Boundary.** Persuasion should take one compact section rather than define the entire week.

### 9. Yin, Jia, and Wakslak (2024), feeling heard by an AI interlocutor

**Status:** Peer-reviewed, *Proceedings of the National Academy of Sciences*.

**Teaching job.** Use as an aside on disclosure, perceived listening, and interviewer identity. It helps distinguish the content of a response from how a participant experiences its source.

**Boundary.** Do not let the paper displace the interviewing-methods literature.

## Recommended reading structure

The reading load should remain close to three articles, using selected pages where necessary.

### Required

1. **Merton and Kendall (1946), selected sections.** A specifically sociological predecessor that defines probing, depth, specificity, and the relation between an interview and a previously analysed situation.
2. **Geiecke and Jaravel (2026), selected sections.** The strongest current case for robust AI-led interviewing at scale.
3. **Jack, Cooper, and Flower (2026).** The participant-facing and sociological critique: completion is not the same as depth.

Together these readings produce an intelligible progression and disagreement: what an interviewer is meant to do, why researchers now want to automate it, and what can be lost when they do.

### In class, with figures or short extracts

- Chicago life-history archive material for the earlier relation among interviews, personal documents, and social change.
- Suchman and Jordan for a real trouble-and-repair sequence.
- Short Oakley and Bourdieu extracts for power, reciprocity, and the socially situated interviewer.
- Jerolmack and Khan alongside Lamont and Swidler for the limits and proper inferential uses of interview talk.
- Tourangeau and Smith for evidence that computerized interview mode affected sensitive reporting before LLMs.
- Wuttke et al. for the randomized AI-versus-human comparison.
- Cuevas et al. for the gap between process metrics and qualitative richness.
- Liu et al. for human-interviewer copilot designs.
- Panfilova et al. for model-to-model variation and reporting requirements.
- Hackenburg et al. for conversational persuasion as an adaptive treatment.
- Yin, Jia, and Wakslak for perceived listening and disclosure.

### Optional or later reference

- Local-model interview systems such as AInterviewer, particularly when the course workbook covers Ollama and local inference.
- Very recent 2026 preprints on voice interview breakdowns, ethical live suggestions, and hybrid control interfaces. These can update the instructor notes but should not anchor the required list until their publication status is clearer.

## Proposed cumulative example

Use two short, fully synthetic interviews about the same sociological question:

> How do graduate students decide whether to speak in a seminar?

This example is preferable to an abstract product-preference dialogue because it makes the interactional decisions legible:

- A protocol question asks the participant to describe the last time they considered speaking.
- One participant mentions uncertainty about whether their point is “good enough”; the interviewer asks for a concrete episode.
- Another mentions status differences in the room; the interviewer asks who seemed entitled to speak and how the participant knew.
- A poor probe repeats the participant's wording without deepening it.
- A leading probe supplies a motive the participant did not express.
- A double question makes it unclear which issue the answer addresses.
- A human or model interviewer eventually decides to move on.

All transcripts should be labelled synthetic. The exercise should not collect students' own potentially sensitive experiences.

The same example can carry the session:

1. Read a human-interview extract and identify repair, probing, and interviewer choices.
2. Compare a fixed protocol with an adaptive branch.
3. Inspect two AI-led transcripts assigned to the same system.
4. Reconstruct the probe path in Python.
5. Ask what the audit can and cannot establish about interview quality.
6. Transfer the method to a short persuasive conversation.

## Consequences for the Python progression

### The research job

The code should reconstruct the interview each participant actually received. It should not pretend to measure rapport, validity, richness, or causal effects.

### Input

One ordered Python list. Each item is one turn represented by a dictionary. The fields should remain visible and concrete:

- `role`: `interviewer` or `participant`
- `text`: the exact words stored in the transcript
- `topic`: a simple researcher-supplied label
- `source`: `protocol`, `adaptive_probe`, or `participant_response`
- `responds_to`: the earlier turn number that prompted an adaptive probe, or `None`

The workbook must say who creates each field. `role`, `text`, and turn order come from the interview log. `source` is created by the interview system when it selects a protocol question or generates a probe. `topic` is a later researcher annotation and must not be presented as if the model necessarily supplied it.

### Transformation

A beginner-facing function can loop through the turns and build an audit record containing:

- number of interviewer and participant turns;
- number of fixed protocol questions and adaptive probes;
- topics in the order first encountered;
- a probe log containing the exact probe, its turn number, and the participant turn to which it responded.

`enumerate()` is the one useful new Python element: it gives each turn a position while the loop reads it. The slides should explain both the value returned by `enumerate()` and the structure of the dictionary being updated.

### Output

The output is a transparent interview audit, not a quality score. Students should be able to answer:

- What fixed questions did both participants receive?
- Where did their interview paths diverge?
- Which probes were generated during the interaction?
- What exact prior answer prompted each probe?
- What information would still be needed to evaluate rapport or depth?

### What the current function should no longer do

The existing `summarize_exposure()` function only counts turns and unique topics. Those counts can remain as part of the output, but they are not the main result. A summary that discards the exact probe wording destroys the evidence needed to audit adaptive treatment exposure.

### Oral-assessment connection

Students should be able to explain:

1. what one turn dictionary represents;
2. why the list must preserve order;
3. what the loop reads on each pass;
4. which values come from the system log and which are later annotations;
5. why two interviews assigned to the same system can have different audit records;
6. why the audit does not by itself prove that one interview was better.

## Provisional narrative arc for the later synthesis

This is not yet a slide list. It records the logic the deck must eventually follow.

1. Begin with a recognizable interview exchange and ask what kind of evidence an interview produces.
2. Use Chicago life histories to show interviews and personal documents connecting individual lives to social change.
3. Use Merton and Kendall to show probing as a method for understanding responses to a shared situation.
4. Introduce standardized survey interviewing as a different solution: restrict interviewer discretion to improve comparability.
5. Show the resulting problem through a real trouble-and-repair transcript and the Schober–Conrad comparison.
6. Use Oakley and Bourdieu to put interviewer identity, power, reciprocity, and rapport back into the research record.
7. Use the interview-versus-ethnography debate to specify what an account can and cannot establish.
8. Introduce CASI and audio-CASI to show that automation and mode effects predate LLMs.
9. Only then introduce AI-led interviewing: the new feature is model-generated interpretation and probing during the exchange.
10. Compare the strongest positive evidence with participant-facing and qualitative critiques.
11. Separate fixed scripts, approved probe banks, model-generated probes, human-interviewer copilots, and full automation.
12. Treat the transcript as both substantive evidence and a record of the interviewer's decisions.
13. Use Python to reconstruct those decisions from an ordered turn log.
14. Show the limits of that audit: process counts are not depth, rapport, or validity.
15. Transfer the same logic to conversational persuasion, where adaptive dialogue is treatment delivery.
16. Close by specifying what a reproducible source record for an AI-mediated interaction must contain.

## Review Gate 1

Before slide synthesis begins, the instructor should approve or revise four choices:

1. **Centre of gravity:** AI-assisted and AI-moderated interviewing is the main application; persuasion is secondary.
2. **Required readings:** selected Merton and Kendall; selected Geiecke and Jaravel; Jack, Cooper, and Flower.
3. **In-class comparison:** Wuttke et al. supplies the main randomized AI-versus-human design.
4. **Historical allocation:** roughly the first third of the substantive session establishes life histories, focused interviewing, standardization and repair, power and rapport, the limits of interview accounts, and pre-LLM computer-assisted interviewing. This material is not a brief preface.
5. **Cumulative example:** two fully synthetic interviews about deciding whether to speak in a graduate seminar.

Once these choices are approved, the next stage is a literature synthesis and detailed slide-arc plan. No slide implementation should begin before that synthesis is reviewed.
