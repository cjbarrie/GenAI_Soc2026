# Instructor notes — Session 4: What part of social experience becomes evidence?

## Intended endpoint

Students should leave able to say:

> Collins asks us to explain violence through the unfolding situation rather than a stable violent type. Image, audio, transcript, fieldnote, participant, and model records preserve different parts of that situation. The code records ordered changes and missing alignment. It prepares a sequence for interpretation; it does not identify intention, responsibility, or a causal mechanism.

They should also explain the focal Python block without live AI assistance:

`exact input and type → operation → exact output and type → sociological meaning → limit`

## Provenance and classroom care

The confrontation is an **instructor-authored synthetic reconstruction**. State this before the first frame and repeat it when participant recollections appear. It contains no real people, institution, testimony, injury, or empirical outcome. It is non-graphic and stops immediately after brief contact.

Students can complete every activity from the text descriptions. Never require anyone to listen to or inspect a confrontation scene. Do not ask the class to decide which group is morally or legally responsible.

## 165-minute plan

### 9:30–9:40 — Go back from text to action

- Revisit the Week 2 label and Week 3 interview excerpt.
- Ask: what had to happen before either became text in Python?
- Collect concrete omissions: body position, sequence, sound, gaze, setting, audience, experience.
- Introduce today's substantive question without mentioning a model.

**Evidence of understanding:** students name a feature of an unfolding situation rather than saying only “context.”

### 9:40–9:58 — How sociologists have studied situations

Keep this section general. The purpose is to establish a sequence of methodological questions before introducing the protest example.

- **Simmel:** sight, hearing, distance, reciprocal perception.
- **Mead:** a movement becomes a gesture within a social act through others' responses.
- **Goffman:** co-presence has an interaction order of mutual monitoring, displays, boundaries, and obligations.
- **Conversation analysis:** timing, overlap, response, and repair are part of the action.
- **Emerson, Fretz, and Shaw:** fieldnotes select and write the event; they are not the event.
- **Goodwin:** coding, highlighting, and representation organize what a trained community sees.

Do not teach six miniature theories. Each author contributes one question that can later be applied to the same scene.

**Evidence of understanding:** students explain that human observation is theoretically and professionally organized before a model enters.

### 9:58–10:05 — Introduce the constructed case

- State clearly that the storyboard is a synthetic teaching example and does not depict real people or an empirical event.
- Introduce the question: what happens within a confrontation that allows violence to begin—or enables it to remain nonviolent?
- Show only the starting position. Establish that no contact has yet occurred and that the camera provides one view.
- Remind students that the six questions from the preceding section now guide the observation.

### 10:05–10:18 — Collins shifts the explanation to the situation

Show the public Princeton chapter page and make it clear that it is a book chapter.

Explain:

- grievances, identities, or individual traits do not make violence automatic;
- confrontational tension/fear is usually a barrier;
- most confrontations do not become competent violence;
- close sequence comparison is needed to identify a proposed pathway through the barrier.

Avoid presenting confrontational tension/fear as directly visible in a frame. It is a theoretical claim that needs multiple forms of evidence.

**Student prompt:** What would a dispositional explanation ask us to observe? What would a situational explanation ask us to reconstruct?

### 10:18–10:30 — Observe the common sequence before seeing its endings

Reveal t=0, 2, 4, and 6. Students write only what is visible or audible. Ban “aggressive,” “threatening,” “fearless,” and “chaotic” for the first pass.

Then reveal the de-escalation and escalation endings. Ask for the earliest defensible divergence and an alternative account. Introduce Nassauer's comparison of violent and nonviolent outcomes.

**Evidence of understanding:** students distinguish conduct, interpretation, and unobserved experience.

### 10:30–10:40 — A video becomes evidence through a method

Introduce Nassauer and Legewie explicitly as a methods paper. Apply its questions to the same sequence:

- event boundary;
- unit of analysis;
- camera position and start time;
- audio/transcript synchronization;
- segmentation and coding;
- comparison;
- validity and ethics.

Reveal Camera B, which begins at five seconds behind one group. Ask how it changes the apparent first movement.

**Evidence of understanding:** students call a video positioned evidence rather than a transparent replay.

### 10:40–10:50 — Break

Leave the paired endings beside the cached whole-event summary:

> Aggressive protesters approached police and caused the confrontation to become violent.

Below it leave: **description, prediction, or explanation?**

### 10:50–11:04 — Different records preserve different parts of the action

Compare the storyboard, audio transcript, automatic transcript, detailed transcript, observation note, and two synthetic participant recollections.

For each record ask:

1. What does it contribute?
2. What did its production remove?
3. What claim can it not support?

Bring Simmel and Goodwin back. Add Davidson for transcription and Mestre and Ryan for audio.

**Important:** state that the recollections are instructor-authored and not testimony.

### 11:04–11:17 — What multimodal and world models actually do

Explain the technical operations in plain language:

- **shared representation:** ImageBind places information from several modalities in a common representational space;
- **recognition/description:** a model names an action or produces text about it;
- **next-state prediction:** V-JEPA 2 learns to predict a future representation from prior video;
- **planning:** a system uses such prediction to select an action.

Use Bisk et al. to ask what embodied and socially situated experience adds. Then state the central limit: accurate prediction of a future frame is not a sociological explanation of the mechanism that produced it.

Do not suggest that models literally share human sensory experience.

### 11:17–11:27 — The visible videos are also a sample

Use Legewie, Nassauer, and Kühne (2026) as an in-class extension.

Ask students to define the target population for “protests become violent when distance narrows.” Then name selection processes: dramatic clips circulate, lead-up is missing, peaceful non-events are not uploaded, cameras are unevenly present, and platform ranking changes availability.

**Evidence of understanding:** students distinguish reconstruction of this episode from generalization across situations.

### 11:27–11:39 — Represent one moment in Python

Build the t=4 dictionary from values students already understand.

Pause on every token that carries meaning:

- `4` is an integer time value;
- quoted text is a string;
- `audible_events` is a list of strings;
- the braces create a dictionary;
- the keys are an instructor-authored coding scheme;
- `moment[\"distance\"]` retrieves one value.

Have students predict the exact output and its type before execution.

### 11:39–11:51 — Put the moments in order

Place dictionaries in a list. Trace:

```python
previous_moment = None

for current_moment in moments:
    print(previous_moment)
    print(current_moment)
    previous_moment = current_moment
```

Act out the first two iterations. Explain `None` as a deliberate absence: on the first iteration there is no previous observed moment to compare.

**Evidence of understanding:** students can state the current values of both names at each pause.

### 11:51–12:03 — Record a change without calling it a cause

Add the two conditions and `.append()` one at a time. The output is a list of structured change records with `time`, `from`, `to`, and `source`. Then add the alignment warning and return the result dictionary.

Run the same `trace_sequence` function on the two endings. Ask what differs in the returned lists and what remains interpretive.

**Required wording:** a software check confirms that the coded expectation was met. It does not validate the sociological explanation.

### 12:03–12:11 — Completion task and oral rehearsal

Students work in pairs and switch roles:

- programmer completes one branch;
- explainer predicts the exact output and describes each line;
- both compare the two endings;
- switch before the alignment-warning branch.

No uninterrupted instructor coding segment should exceed twelve minutes.

### 12:11–12:15 — Revise the initial summary

Return to the initial model summary. Invite revisions that preserve sequence and limits.

Target response:

> In the constructed escalation sequence, narrowing distance, overlapping signals, and a sudden shift in relative position occurred before the shove. The de-escalating ending restored distance at the corresponding moment. The comparison shows how a Collins-inspired situational explanation could be investigated, but it does not establish intention, responsibility, or a general pattern.

Connect forward: Session 5 moves from observing model-mediated evidence to using generated material in an intervention.

## Beginner-code narration

For every code slide ask in this order:

1. What is the exact input value?
2. What Python type is it?
3. What operation happens?
4. What is the exact output value and type?
5. What does it mean for the research question?
6. What does it not establish?

Likely sticking points:

- `=` gives a name to a value; `==` compares values.
- `[]` can create a list or retrieve a list position; `record[\"distance\"]` retrieves a dictionary value by key.
- `.get()` retrieves a value without stopping if the key is absent.
- `is not None` prevents a comparison on the first iteration.
- `.append()` changes the list by adding one item.
- `return` sends a value back to the caller.
- A passing `assert` is a software result, not a validity result.

## Completion standard

Completion requires:

- an output prediction made before execution;
- both missing branches completed;
- supplied checks passing;
- one loop iteration explained in ordinary language;
- a comparison of the two endings;
- 100–150 words linked to Collins or Nassauer, with one explicit limit; and
- AI-use disclosure if applicable.

Syntax elegance is irrelevant. If the environment fails, use the rendered notebook and trace the provided output by hand.
# Rebuild record — 2026-08-26

The original version failed because it opened with a generic course sequence, used a synthetic protest as an ungrounded example, introduced Collins before teaching students how video evidence is constructed, and presented disconnected code objects without a single visible model call. Several slides relied on compressed slogans, black section backgrounds, first-page screenshots and instructor-created syntheses whose provenance was unclear.

Repairs now required in this and future weeks:

- start from a legible empirical problem rather than a course map;
- use one real, sociologically defensible case across theory, methods and code;
- introduce authors through the concrete studies and evidence on which their claims rest;
- show the relevant page, figure, quotation or example at readable size;
- distinguish published concepts from instructor synthesis explicitly;
- establish the method used to construct evidence before applying a substantive theory to it;
- keep observation, participant account, causal interpretation and theoretical interpretation distinct;
- make each code slide continue the same workflow and show input, type, operation and output;
- avoid black backgrounds, empty slide announcements, unexplained callouts and compressed “AI English”; and
- verify that closing slides summarize the lecture rather than an arbitrary block of course weeks.

The rebuilt case is the Zidane–Materazzi incident. Official FIFA close and tactical-camera footage provides a real sequence; missing usable speech makes the limits of video obvious; and the “moments of madness” thumbnail offers a direct example of framing. Goodwin is taught through the Munsell chart and Rodney King trial, Nassauer through published camera-angle and sequence figures, and Collins through the passages that state his comparative claim. *Situational Breakdowns* has moved to further reading.
