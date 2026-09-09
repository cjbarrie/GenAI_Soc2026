# Session 6 synthesis — interviewing when the next question can change

**Status:** Stage 3 methodological synthesis completed on 2026-08-24. Ready for Review Gate 2 before slide implementation.

## Communication job

By the end of the session, graduate sociology students should be able to evaluate an AI-assisted or AI-led interview by first specifying what the interview is meant to establish, then examining how the interviewer produced the account, and finally reconstructing the questions and probes that each participant actually received.

The session should not ask whether AI is generally a “good interviewer.” It should make that question look underspecified.

## Central argument

Sociologists have used interviews for different purposes: reconstructing lives, understanding responses to shared situations, measuring comparable attributes, eliciting cultural accounts, and examining how people understand institutions. These purposes give the interviewer different jobs and make different kinds of evidence relevant.

LLMs do not replace one settled interview method. They automate or redistribute decisions that sociologists have long argued about: when to probe, whether to clarify, how much to standardize, what counts as a satisfactory answer, how to respond to disclosure, and when to move on.

The central claim is:

> Before judging an AI interview, specify the research job, the interaction that produced the account, and the interview path the participant actually received.

The complementary computational claim is:

> Assignment to the same interview system does not guarantee exposure to the same interview.

## Three questions that hold the lecture together

The historical material should not appear as seven separate traditions. Each part answers one of three questions that recur when the contemporary papers appear.

### 1. What kind of evidence is the interview meant to produce?

- a life history;
- a response to a defined situation;
- a comparable measurement;
- an account of meaning, classification, or institutional experience;
- a report of behaviour;
- evidence of behaviour itself.

### 2. What is the interviewer allowed or expected to do?

- read fixed wording;
- use approved neutral probes;
- clarify a concept;
- request a concrete episode;
- notice a contradiction;
- introduce an interpretation;
- reciprocate or disclose;
- decide that the topic is complete;
- stop or escalate when risk appears.

### 3. What social relationship produces the answer?

- who or what appears to be listening;
- what the participant believes will happen to the disclosure;
- how identity, institutional position, judgment, privacy, and rapport affect the exchange;
- whether the interviewer can recognize obligations created during the interaction.

These three questions become the evaluation framework for Geiecke and Jaravel, Jack et al., Wuttke et al., Cuevas et al., Liu et al., and the cumulative example.

## The overall narrative

The lecture should follow a question–analysis–answer structure rather than a chronological literature review.

### Opening question

Two interview extracts can both be fluent, complete, and twelve turns long. That does not tell us which is better. Better for what?

### Historical analysis

Sociologists developed different interview forms because they wanted different kinds of evidence. Attempts to increase comparability restricted interviewer discretion; attempts to understand meaning and experience required probing, repair, and attention to the relationship. Automation later changed privacy and disclosure before it could generate novel probes.

### Contemporary problem

LLMs can now make consequential interviewing decisions during data collection. The instrument is no longer fully represented by the interview guide or system prompt. The realized sequence also matters.

### Practical answer

Evaluate an AI-mediated interview at four levels:

1. **research claim:** what is the interview supposed to establish?
2. **interviewer design:** which decisions are fixed, selected, generated, or left to a human?
3. **realized interaction:** what did this participant actually experience?
4. **validation:** what evidence addresses protocol adherence, specificity, depth, rapport, participant experience, and downstream inference?

The Python audit addresses the third level. It does not substitute for the other three.

## Section structure and pacing

The meeting runs from 9:30 to 12:15. The exact clock should stay in the instructor notes rather than appear on student-facing slides.

| Section | Approximate time | Main question | Classroom mode |
|---|---:|---|---|
| Opening and course connection | 10 minutes | What would make one interview better than another? | Read two short extracts; whole-room initial judgment |
| What sociologists wanted interviews to do | 30 minutes | What kind of evidence can an interview produce? | Historical materials, published pages, one focused-interview exercise |
| Interviewing as interaction and social relation | 25 minutes | What does the interviewer contribute to the answer? | Transcript repair exercise, Oakley/Bourdieu, interview-evidence debate |
| Pre-LLM automation | 10 minutes | What had computers already changed? | CASI comparison and disclosure result |
| Break | 10 minutes |  |  |
| Current AI-led and AI-assisted interviewing | 40 minutes | What is genuinely new, how do text and voice systems work, and what evidence do current studies provide? | Paper figures, architecture, privacy routes, comparison across studies |
| Return to the opening and cumulative synthetic study | 15 minutes | How do two participants receive different interviews from the same system? | Answer the opening judgment; whole-room interrogation of two probe paths |
| Python audit and voice pipeline | 30 minutes | How can we reconstruct the interview path and record STT/TTS steps without hiding the evidence? | Slow code walk-through, voice demonstration and output interpretation |
| Close | 5 minutes | What belongs in the source record before a transcript becomes evidence? | Source-record checklist and four closing questions |

The timing deliberately gives more space to methodological history and interaction than to system novelty. The Python audit remains narrow; the voice material explains the interfaces and provenance without requiring students to build a live audio system for the completion task.

## Detailed slide arc

The following is a content plan, not a mandate for one-sentence slides. Most slides should carry a published image, transcript, instrument, figure, worked example, or code/output object. The working plan contains approximately 61 slides. A source figure may require an extra slide if it cannot remain readable, but implementation should remove repetition rather than routinely expanding the deck.

### Part 1 — Begin with a judgment students cannot yet make (about 5 slides)

#### Slide job 1: state the session question plainly

**Provisional title:** “What changes when a model starts asking the questions?”

Keep the title slide simple. The subtitle can name AI-assisted and AI-led interviewing without using “interactant” as the first explanation.

#### Slide job 2: show the two interview extracts

**Provisional title:** “Both interviews are fluent. Which one gives us better evidence?”

Show two short, synthetic exchanges about seminar participation. Keep the opening question identical. In one exchange the interviewer asks for a concrete episode; in the other it paraphrases the answer and moves on. Do not reveal interviewer type yet.

#### Slide job 3: ask the room to justify its answer

**Provisional title:** “What did you use to judge the interviews?”

Record several plausible criteria on the slide: length, specificity, comfort, comparability, relevance, lack of leading, and whether the participant answered the research question. The purpose is to show that “quality” already contains several different standards.

#### Slide job 4: expose the missing information

**Provisional title:** “We cannot judge the interview until we know what the study is trying to learn”

The same exchange may be useful for reconstructing a concrete experience but poor for estimating a standardized measure. This becomes the problem the historical section resolves.

#### Slide job 5: connect to the previous weeks

**Provisional title:** “Last week we fixed the treatment. This week the next question can depend on the last answer”

Use one compact comparison:

- Session 5: fixed candidate pool and fixed exposure;
- Velez: an item bank can evolve across respondents;
- Session 6: the interview path can change within one participant's conversation.

The transition should state why this matters: the interview guide no longer completely describes what happened.

### Part 2 — What sociologists wanted interviews to do (about 9 slides)

This section should not become a roll call of theorists. Each historical case adds one criterion to the developing evaluation framework.

#### Slides 6–7: life histories and personal documents

**Provisional titles:**

- “Early Chicago sociology used personal documents to connect lives to social change”
- “A transcript was one record of a life, not the life itself”

Use the University of Chicago archive and a readable page from the Władek life record. Show letters, case material, autobiography, and researcher interpretation as related evidence. Explain what the researchers were trying to understand: migration and institutional change as lived over time.

The takeaway is not that contemporary researchers should reproduce *The Polish Peasant*. It is that a short interview is limited when the claim concerns a process unfolding across a life.

**Criterion added:** temporal and contextual adequacy.

#### Slides 8–10: Merton and Kendall's focused interview

**Provisional titles:**

- “Merton and Kendall interviewed people about a situation the researchers had already studied”
- “The interviewer looked for specificity, range and depth”
- “A probe can deepen an answer without supplying the answer”

Use a large screenshot of the original *AJS* article and a legible crop defining the focused interview. Introduce its wartime and mass-communication setting briefly: researchers wanted to understand responses to films, broadcasts, or other analysed situations.

Then use a concrete comparison:

- response: “I found it uncomfortable”;
- useful probe: “Was there a particular moment when you began to feel uncomfortable?”;
- leading probe: “Was it the speaker's dismissive tone that made you uncomfortable?”

Ask the room what the useful probe adds and what the leading probe introduces.

**Criterion added:** specificity without direction.

#### Slides 11–13: standardized survey interviewing

**Provisional titles:**

- “Survey interviewing gave the interviewer a different job”
- “The wording, order and allowable probes were fixed to improve comparability”
- “Identical wording does not guarantee identical interpretation”

Show an actual interviewer instruction page at readable size: “read exactly as written,” response categories, a neutral probe, and skip logic. Explain each element before discussing its limitation.

The presentation should be fair to standardization. It solves a real problem. If interviewer A explains a category and interviewer B does not, a comparison across respondents becomes harder to interpret.

End with a simple unusual case in which the respondent does not know whether an object fits an official category. This creates the need for interactional repair.

**Criterion added:** procedural comparability.

#### Slide 14: pause and synthesize the first disagreement

**Provisional title:** “Depth and comparability are not the same research objective”

Use one flat comparison rather than a three-card typology:

| Interview job | What the interviewer does | Main risk |
|---|---|---|
| Reconstruct a life or process | follows chronology and context | short accounts detach events from a life |
| Understand response to a situation | requests specificity and depth | the probe can direct the answer |
| Produce comparable measurements | restricts discretion | shared wording may conceal different meanings |

This slide earns the transition to interviewing as interaction.

### Part 3 — The interviewer is part of the data-generating process (about 9 slides)

#### Slides 15–17: trouble and repair

**Provisional titles:**

- “Respondents do not always interpret a survey category as its designers intended”
- “A standardized response and a conversational clarification produce different exchanges”
- “Changing the words can sometimes make the meaning more comparable”

Use a real published Suchman–Jordan or Schober–Conrad transcript, not a newly invented generic example. First show the question and respondent difficulty. Then reveal the interviewer response. Finally show the design and result of the conversational-interviewing comparison.

The purpose is to make the causal trade-off explicit:

- strict wording standardizes the stimulus;
- flexible clarification may standardize the intended meaning;
- flexible clarification also creates interviewer discretion that must be recorded.

**Criterion added:** successful repair and semantic fidelity.

#### Slides 18–20: Oakley and Bourdieu

**Provisional titles:**

- “Methods sections often describe the interview but omit the relationship”
- “Oakley asked what disappears when the interviewer is written out of the account”
- “Bourdieu treated the interview as a social relation, not a neutral exchange”

Use screenshots of the original texts with a readable highlighted passage, alongside a concrete methods-report comparison. One version says “74 interviews, average 42 minutes”; the fuller version records who interviewed whom, what the participant understood about the study, reciprocity, setting, and what followed a disclosure.

Avoid turning this into a generic “ethics slide.” The substantive point is that the relationship affects the evidence produced.

**Criterion added:** reflexivity about power, rapport, and participant understanding.

#### Slides 21–23: what interview accounts can establish

**Provisional titles:**

- “A detailed account is still an account”
- “Jerolmack and Khan warn against treating talk as direct evidence of action”
- “Lamont and Swidler ask what interviews are actually well suited to showing”

Begin from one synthetic passage about seminar participation and offer three claims:

1. the participant described worrying that their point was insufficiently original;
2. the participant understands seminar participation partly through judgments of intellectual worth;
3. the participant always remains silent when senior students are present.

The transcript directly supports the first, may contribute to the second with further analysis, and does not by itself establish the third as behaviour.

The published debate then has a clear job rather than appearing as an aside.

**Criterion added:** claim–evidence fit.

### Part 4 — Computers had already changed interviews (about 3 slides)

#### Slides 24–26: CAPI, CASI and audio-CASI

**Provisional titles:**

- “Computers were administering parts of interviews before LLMs”
- “Changing the mode changed the social situation and sometimes changed disclosure”
- “What these systems could not usually do was compose a new substantive probe”

Show the same sensitive item across interviewer-administered, screen self-administered, and audio self-administered modes. Explicitly separate:

- who asks or voices the question;
- who is present;
- who can observe the answer;
- whether branching was authored in advance;
- whether the system can interpret an open response.

Tourangeau and Smith provide the empirical result. The conclusion should be restrained: mode affects disclosure, and greater disclosure is not automatically greater validity.

This is the bridge to the break. Students should now be able to say what is and is not new about LLM interviewing.

### Part 5 — What LLM interviewing adds (about 13 slides)

#### Slides 27–29: define the systems before evaluating them

**Provisional titles:**

- “An ‘AI interview’ can describe several different systems”
- “Some systems follow a fixed script; others choose or write the next probe”
- “The important question is where each interviewing decision is made”

Use one explicit continuum grounded in system operation:

1. fixed automated script;
2. researcher-authored branching;
3. selection from an approved probe bank;
4. model-generated probe with human approval;
5. model-generated probe delivered automatically.

Do not depict this as a ladder of sophistication. Each design trades flexibility, control, labour, and auditability differently.

Then explain a beginner-level system in sequence:

1. the researcher supplies an interview protocol and instructions;
2. the participant gives an answer;
3. the answer and earlier turns are sent to a model;
4. the model returns a proposed next question;
5. the system, or a human interviewer, decides whether to deliver it;
6. the transcript and decision record are stored.

This is where OpenRouter or a local model may be mentioned as an access route, but the slide should not repeat the general API explanation from earlier weeks. The method is the same whether the model is accessed directly, through OpenRouter, or locally; privacy and logging implications differ.

#### Slides 30–32: Geiecke and Jaravel

**Provisional titles:**

- “Geiecke and Jaravel make the positive case for AI-led interviews at scale”
- “Their system combines a protocol with adaptive follow-up”
- “Scale is useful, but it does not settle what counts as interview quality”

Establish the paper before showing results: question, system, applications, comparison, outcomes. Use the actual system diagram and one central evaluation figure at readable size. Explain each axis and comparison inside the slide.

The teaching job is to make the attraction concrete and technically inspectable—not to present it as the final verdict.

#### Slides 33–34: Wuttke et al.

**Provisional titles:**

- “Wuttke and colleagues compare AI and human interviewers using the same questionnaire”
- “Random assignment helps isolate interviewer type, but the study remains a particular kind of interview”

Connect explicitly to Session 5: identify assignment, interviewer condition, realized interview, outcomes, and what remains uncontrolled. Show the paper's design and one result rather than listing all metrics.

#### Slides 35–37: Jack, Cuevas and participant-facing limits

**Provisional titles:**

- “Jack and colleagues asked social scientists to experience the chatbot interview themselves”
- “Participants completed the interview but still described problems of repetition, nuance and interaction”
- “A model can look successful on one metric and weak on another”

Use actual article pages and figures. Put positive and critical evidence into conversation:

- completion and scale;
- specificity and concrete examples;
- repetition and missed opportunities;
- participant experience;
- disagreement between human and automated evaluations.

The point is not a balanced-scorecard slide. It is that different validation measures answer different questions.

#### Slides 38–39: Liu and Panfilova

**Provisional titles:**

- “Full automation is not the only design”
- “A copilot leaves decisions with the interviewer; model choice still matters”

Liu et al. provides the human-interviewer support design and its risks: divided attention, deskilling, and rapport. Panfilova et al. makes model variation visible. A paper screenshot or comparison figure should anchor each point.

End with one synthesis table:

| Evidence | What it can tell us | What it cannot settle |
|---|---|---|
| protocol adherence | whether required questions were asked | whether the questions produced useful evidence |
| probe classification | what kinds of follow-up occurred | whether the probe was well timed or appropriate |
| response length and completion | how much text was produced | specificity, truth, or depth |
| participant report | how the interview felt | independent evidentiary quality |
| expert transcript review | judged quality of the exchange | participant experience or population validity |

### Part 6 — Apply the framework to one synthetic sociological study (about 6 slides)

#### Research question

> How do graduate students decide whether to speak in a seminar?

All participants and transcripts are synthetic. Students are not asked to disclose their own experiences.

The inferential target is how participants describe and interpret decisions about speaking: confidence, intellectual status, turn-taking, instructor behaviour, and judgments about what counts as a worthwhile contribution. The study does not directly observe how often they speak.

#### Slides 40–45: follow the two interview paths

**Provisional titles:**

- “Our study asks how students understand a decision, not how often they actually speak”
- “Both interviews begin with the same request for a recent episode”
- “The two answers give the model different opportunities to follow up”
- “These probes do different things to the evidence”
- “The participants were assigned to the same system but did not receive the same interview”
- “The interview guide alone no longer reconstructs the instrument”

Use no more than two or three turns on a slide. Label every turn number. Keep the interviewer and participant visually distinct without turning the transcript into chat-app decoration.

Compare four probes directly:

- **specificity:** “Can you describe the point you were considering making?”
- **clarification:** “When you say some people seemed entitled to speak, what did they do that gave you that impression?”
- **leading:** “Did the instructor's behaviour make you feel that your point was not welcome?”
- **double question:** “How did the instructor respond, and did the senior students make it harder to speak?”

The whole room should interrogate one probe: what does it help establish, what does it introduce, and what should be recorded?

The final slide in this section should display two ordered paths side by side. The difference is now concrete enough to motivate the code.

### Part 7 — Reconstruct the interview in Python (about 10 slides, 46–55)

The code section begins with the research job and visible input/output before any syntax.

#### Slide job: state exactly what the program does

**Provisional title:** “The program reconstructs which questions and probes each participant received”

It does not score rapport, truth, depth, or interview quality.

#### Slide job: show the input before the function

**Provisional title:** “The input is one ordered list of interview turns”

Show a small literal list containing three turn dictionaries. Explain:

- square brackets contain the ordered list;
- each pair of braces is one turn;
- each key names a field;
- each value stores the information for that field.

#### Slide job: establish where every field comes from

**Provisional title:** “Some fields come from the system log; one is added later by the researcher”

| Field | Source |
|---|---|
| `role` | system log |
| `text` | exact stored transcript |
| turn order | system log |
| `source` | system decision record: protocol or adaptive probe |
| `responds_to` | system decision record |
| `topic` | later researcher annotation |

This prevents the ambiguity that weakened the Week 5 code explanation.

#### Slide jobs: walk through the function slowly

The function should be shown in small, cumulative excerpts:

1. define the function and empty audit dictionary;
2. use `enumerate(turns)` to obtain a turn number and a turn dictionary;
3. inspect `role` and `source`, then update the relevant counts;
4. append a new topic only when it is first encountered;
5. preserve each generated probe and the earlier turn it responds to, then return the completed audit.

Every code slide should contain:

- the input currently being read;
- the highlighted line being executed;
- the state of the output dictionary before and after;
- one plain-language sentence explaining the operation.

Do not introduce an API call in the required function. The transcript should be cached and inspectable. A later workbook extension can show how an OpenRouter or local-model call might produce a proposed probe, but generating the interview and auditing it are separate operations.

#### Slide job: interpret the output

**Provisional title:** “The audit shows where the interview paths diverged”

Show the output as a readable table before showing the printed dictionary. Students should identify:

- fixed questions both participants received;
- number and wording of adaptive probes;
- the prior response linked to each probe;
- topics encountered in order.

#### Slide job: state the limit

**Provisional title:** “This audit preserves the interview path. It does not tell us whether the interview was good”

Return to the evaluation framework. Transcript review, participant reports, protocol checks, disclosure and consent records, and substantive validation remain necessary.

#### Completion and oral-assessment task

Students complete one missing branch that records adaptive probes and explain orally:

1. what a turn dictionary represents;
2. why turn order matters;
3. what `enumerate()` returns;
4. where `source` and `topic` come from;
5. what changes in the audit when a new probe is encountered;
6. why the function does not measure depth.

### Part 8 — Transfer the method to conversational persuasion (about 3 slides, 56–58)

#### Three slides: Hackenburg and Yin

**Provisional titles:**

- “In a persuasive conversation, the dialogue is also the treatment”
- “The treatment record includes the sequence, not only the initial assignment”
- “Feeling heard and being persuaded are different outcomes”

Hackenburg et al. is the main transfer. Establish the study and show one central figure. The purpose is to let students reuse the concepts they have just learned:

- fixed condition;
- participant-specific disclosure;
- generated response;
- realized treatment path;
- outcome.

Yin, Jia, and Wakslak appears only as a concise aside on perceived listening, disclosure, and source identity. It should not start a second literature review.

### Part 9 — Close by returning to the opening interviews (about 3 slides, 59–61)

#### Penultimate slide

**Provisional title:** “We can now say what each opening interview was good for”

Return to the original two extracts. Evaluate them against the now-visible research purpose. The conclusion can be specific rather than announcing a universal winner.

#### Final substantive slide

**Provisional title:** “A reproducible AI interview needs more than a transcript”

The source record should include:

- research question and inferential target;
- protocol and approved probes;
- system instructions;
- model, version, access route, and settings;
- disclosure and consent language;
- exact ordered transcript;
- source of every interviewer turn;
- links between a generated probe and the answer that prompted it;
- human approvals, edits, overrides, and escalation;
- stopping rule;
- validation evidence;
- data storage and provider access.

#### Closing question

**Provisional title:** “What would you need to know before treating this transcript as sociological evidence?”

This prepares students for the midterm and Session 7's question about whether models can represent people or populations.

## How the historical material remains active after it is introduced

The history should visibly reappear in the contemporary sections:

| Earlier tradition | Criterion carried forward | Contemporary return |
|---|---|---|
| Chicago life histories | a short account may be inadequate for a process unfolding across time | limits of brief scalable interviews and decontextualized transcripts |
| Merton and Kendall | specificity, range, depth, and non-direction | evaluation of generated probes in Geiecke/Jaravel and the synthetic study |
| standardized survey interviewing | comparability and restricted discretion | fixed protocol versus generated follow-up; Wuttke design |
| Suchman/Jordan and Schober/Conrad | repair and semantic fidelity | whether model rephrasing clarifies or changes the measure |
| Oakley and Bourdieu | power, reciprocity, rapport, and participant understanding | Jack participant reflections; disclosure; bot identity and institutional responsibility |
| interview-evidence debate | distinguish accounts of meaning from observed action | inferential target for the seminar-participation study |
| CASI and audio-CASI | mode, privacy, social presence, and disclosure | claims that participants disclose more to a bot or feel less judged |

This table is primarily a planning device. The deck should not necessarily reproduce it in full. Its job is to prevent the “what came before” section from disappearing once the AI papers begin.

## Reading roles after synthesis

### Required

1. **Merton and Kendall (1946), selected sections:** establishes what a focused interviewer is trying to accomplish and gives students a vocabulary for evaluating probes.
2. **Geiecke and Jaravel (2026), selected sections:** provides the strongest current positive case, a system architecture, and multiple forms of evaluation.
3. **Jack, Cooper, and Flower (2026):** introduces participant experience and the possibility that completion and abundance coexist with weak depth or interaction.

### Worked through in class

- Chicago life-history archive: material form and triangulation.
- Suchman and Jordan plus Schober and Conrad: trouble, repair, and accuracy.
- Oakley and Bourdieu: relationship and reflexivity.
- Jerolmack and Khan plus Lamont and Swidler: inferential target.
- Tourangeau and Smith: pre-LLM automation and disclosure.
- Wuttke et al.: randomized interviewer comparison.
- Cuevas et al.: validation metrics and richness.
- Liu et al.: human interviewer with model support.
- Panfilova et al.: model variation.
- Hackenburg et al.: adaptive conversation as treatment.
- Yin, Jia, and Wakslak: perceived listening and source identity.

No source should receive a standalone slide merely because it is relevant. Each source must introduce a criterion, supply evidence for it, or change the interpretation of the cumulative study.

## Visual and layout plan

### Evidence first

Paper introduction slides should use actual paper pages, system diagrams, transcript extracts, instruments, or figures. Every screenshot must be large enough to read and cropped to semantic boundaries. If an entire figure is needed, give it the width of the slide rather than splitting labels or arrows across slides.

### Historical material should look materially historical

Use archive pages, original journal typography, survey interviewer manuals, and transcript pages. Do not represent the history with generic portraits or a decorative timeline.

### Transcripts should be treated as evidence, not chat decoration

Use line numbers or turn numbers, stable speaker labels, and highlighting of the relevant phrase. Avoid phone mockups, chat bubbles, and excessive interface styling.

### Vary density deliberately

- full-page document or figure with a short explanation;
- split layout with source on one side and interpretation on the other;
- full-width transcript with annotated turn;
- comparison table for closely related systems;
- code plus input/state/output only where syntax is being explained.

Avoid consecutive sequences of sparse slogan slides. Avoid making every section look like a card grid.

### Language check

Titles should say what the slide is showing in language the instructor could plausibly use aloud. Avoid constructions such as “the model proposes; the researcher evaluates,” “interaction becomes exposure,” or “the course begins where the output ends.”

## What should be removed from the current deck

- The current generic readings-disagreement slide.
- Repeated general explanations of model access routes already covered in Session 1.
- Any suggestion that turn counts and topic counts measure interview quality.
- Persuasion as the organizing subject of the entire week.
- Abstract claims about “interactional treatment” before students have seen an interview exchange.
- Code shown before the input, provenance of fields, and intended output are established.

## What the eventual workbook must add

- Two complete synthetic transcripts with stable turn numbers.
- A visible protocol and distinction between protocol question and generated probe.
- A field-by-field account of who creates the data.
- The same input used on the slides.
- A hand-trace exercise before the full function.
- A completed output interpreted in sociological language.
- A limitations section explaining why the audit is not a quality metric.
- An optional extension showing a proposed probe produced through OpenRouter or a local model, clearly separated from the required cached workflow.

## Review Gate 2

Before slide implementation, approve or revise:

1. the three-question framework: evidence, interviewer discretion, and social relationship;
2. the allocation of roughly 75 minutes before the break to the historical and interactional foundations;
3. Merton and Kendall replacing Suchman and Jordan as the required classic reading, with Suchman/Jordan taught through a transcript;
4. the synthetic seminar-participation study and its limited inferential target;
5. the narrow Python job: reconstruct realized interview paths, without scoring quality;
6. persuasion as a short transfer application near the end.

Once approved, the next stage is implementation: acquire the exact paper pages and figures, rewrite the deck, rebuild the code/workbook around the shared input, render every slide, and conduct narrative and visual QA.
