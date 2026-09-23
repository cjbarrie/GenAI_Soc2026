# Instructor notes — Session 4: What can we learn from a recorded situation?

## Intended endpoint

Students should leave able to explain four linked points:

1. A recording preserves selected features of a situation from a particular position.
2. Actions become interpretable through their place in an unfolding sequence and the responses of others.
3. Codes, visual highlights, theory and interfaces organize what an observer notices.
4. A multimodal model can propose a structured description, but the researcher must check each claim against the source record and state what the record cannot establish.

For the Python routine, students should be able to narrate:

`two image paths + prompt string + schema dictionary → route-specific model call → raw JSON string → parsed dictionary → source check`

## The exact Goodwin argument

Do not reduce Goodwin to “people can interpret the same image differently” or to a generic warning about bias. His argument is more sociological and more useful:

> Professional vision consists of socially organized practices through which members of a community make selected features of a complex perceptual field relevant, intelligible and available as evidence for the work they are doing.

Goodwin follows three connected practices:

- **Coding schemes** transform continuous, ambiguous material into professionally recognized objects. The Munsell chart does not merely report a private perception of soil colour; it helps an archaeologist produce an observation in categories colleagues can compare and act upon.
- **Highlighting** makes some features conspicuous while pushing others into the background. Highlighting is material: bodies, charts, overlays, pointing and talk all direct attention.
- **The production and articulation of material representations** rearranges an event into a form that can be inspected and argued over. In the Rodney King trial, individual frames were enlarged, cropped and pasted into a long spatial sequence. Counsel's language and the display mutually reinforced a proposed reading.

Professional vision is therefore perspectival and socially situated, but it is not simply arbitrary individual opinion. Communities provide practices, categories, artefacts and standards through which members learn to see. Those practices can also be contested, as the opposing courtroom accounts demonstrate.

### The white-line correction

The white line in Goodwin is **not a line beneath King's foot or a feature already present in the scene**. The defence placed transparent overlays on enlarged still frames, with white lines tracing King's body. This altered the figure–ground relation: King became the conspicuous moving figure while the officers receded. Counsel described the displayed movement as going “from the ground to a charge.” The important point is that the visual overlay and the verbal coding worked together to construct the event as evidence for a particular legal account.

Do not ask the slide to settle what “really happened.” Ask how a courtroom practice turned a complex recorded encounter into an intelligible object for the jury.

## How to teach the Goodwin section

### 1. Begin with archaeology

Ask students what happens between seeing a patch of soil and entering a comparable observation in a field record. Use the Munsell chart to show that professional categories do not arrive after perception; they help organize the act of seeing and reporting.

Suggested question:

> What does the chart allow archaeologists to see and communicate that an unaided description such as “brownish” would not?

### 2. Move to the courtroom

Explain that the Rodney King video did not enter court as a self-interpreting record. Lawyers selected frames, slowed and reorganized time, named movements and connected those movements to competing legal accounts.

Suggested questions:

- What has happened to time when a video becomes a row of still images?
- Which actor becomes figure and which becomes background?
- What does a label such as “aggressive” ask the jury to treat as relevant?

### 3. Reveal the overlays

First let students inspect the published figure. Then identify the transparent overlays and white bodily outlines. Stress that this is a demonstration of highlighting as an embodied and material practice, not merely a metaphor.

Suggested question:

> If the outlines had instead traced the officers' bodies and batons, how might the perceptual field have been reorganized?

### 4. State the argument explicitly

Use the synthesis slide only after both empirical examples. Give the three practices—coding, highlighting and representation—and then state that professional vision is socially organized seeing.

### 5. Carry Goodwin into the rest of the lecture

- **Heinlein:** green bounding boxes are live algorithmic highlights. They can direct attention, be overridden or interrupt the procedure. The sociological issue is how attention, judgement, authority and training change—not only whether detection accuracy rises.
- **Nassauer:** camera position, segmentation and sequence reconstruction organize the evidentiary field. They are methodological choices, not neutral retrieval.
- **Collins:** a theory supplies another coding scheme by making timing, distance, confrontation and emotional dominance analytically relevant. It must still be tested against appropriate evidence.
- **The LLM routine:** the prompt and JSON schema tell the model what to notice and how to represent it. The model's output is another professionally organized description, not an unmediated account of the pixels.

## 165-minute plan

### 9:30–9:43 — Establish the empirical problem

- Open on the FIFA thumbnail and note that “moments of madness” supplies an interpretation before the clip plays.
- Compare the close broadcast and tactical views.
- Separate what is visible, what is audible and what must be inferred.
- State the day's question: how does a recorded situation become sociological evidence?

**Check:** students should name a feature omitted by a recording, not say only “context.”

### 9:43–10:03 — A short sociological prehistory

- **Simmel:** sensory access and distance are part of social relations.
- **Mead:** gesture and response form an unfolding social act.
- **Goffman:** actors, officials, audiences and rules organize the situation.
- **Sequence analysis:** a movement becomes intelligible through what precedes and follows it.

Keep applying each point to the same football sequence. The authors are not a chronology quiz; each contributes one question for the case.

### 10:03–10:25 — Goodwin and professional vision

Teach the Goodwin sequence above: Munsell chart → courtroom coding → white body outlines → three-part synthesis.

Return to the FIFA thumbnail and ask how cropping, captioning and repetition have already organized the viewer's attention.

**Check:** students should be able to explain why professional vision is neither neutral sight nor arbitrary opinion.

### 10:25–10:40 — Heinlein and live algorithmic highlighting

- Introduce the study design: observations and interviews in AI-assisted colonoscopy.
- Explain the intermittent green boxes marking suspected polyps.
- Compare following a mark, overriding it and switching the system off.
- Explain the circular gaze and the concern that novices may wait for the interface to tell them where to look.

Bridge explicitly:

> Goodwin shows how a professional community organizes seeing. Heinlein asks what changes when an algorithm begins to participate in that organization during the work itself.

### 10:40–10:50 — Break

Leave the four questions—access, sequence, situation and representation—on screen.

### 10:50–11:08 — Turn the problem into a video method

Use Nassauer to introduce recording quality, multiple angles, ordered reconstruction and source documentation. Build the FIFA source record and then show the selection funnel.

Bridge explicitly:

> The recording does not interpret itself, so we first need a defensible reconstruction method. Only then should we apply a theory of violence.

### 11:08–11:28 — Collins as a theory to investigate

- State the comparative puzzle: most confrontations do not become competent violence.
- Explain confrontational tension and fear as a proposed barrier, not something automatically visible in a still.
- Present Collins's routes around the barrier and his narrower idea of the tunnel of violence.
- Ask what changed immediately before contact in this case.

Do not treat an instructor-created list of stages as Collins's theory. Keep the observed sequence descriptive and use Collins to formulate comparative questions.

### 11:28–11:42 — Compare claims and evidence

- Separate observable, causal and theoretical statements in the table.
- Put Collins beside Morrissey's habitus account and the experimental anger account.
- Use the Morrissey quotation to provoke discussion about how much additional biographical and historical evidence a strong interpretation requires.

**Check:** students should identify the evidence needed for a claim rather than choosing their preferred explanation.

### 11:42–11:52 — Apply Goodwin to the model

Explain that the model is not a neutral second pair of eyes. The prompt defines what should count; the schema highlights fields; the model and interface produce a representation. Ask what this setup pushes into the foreground and background.

### 11:52–12:12 — Walk through the Python routine

Move slowly through the exact routine used in the Week 4 coursebook and notebook:

1. inspect `frame_1` and `frame_2`;
2. read the prompt string aloud;
3. identify the three schema fields;
4. compare OpenRouter data URLs with Ollama local image paths;
5. inspect the route-specific call;
6. print the raw JSON string before parsing;
7. use `json.loads(...)` to create a dictionary;
8. check each named field against the source images; and
9. replace only `frame_2` with `zidane_fine2_170.png` and rerun.

There are no student-defined functions or loops this week. Those Python ideas are introduced later in the course.

### 12:12–12:15 — Close

Return to the opening thumbnail and ask students to name four layers now visible in it: source selection, sequence, social situation and representation. Preview Week 5 as a move from interpreting model-mediated evidence to constructing experimental material.

## Beginner-code narration

For every block ask, in this order:

1. What is the exact input value?
2. What Python type or object stores it?
3. What operation is performed?
4. What exact output is produced?
5. What does that output let us check?
6. What does it not establish?

Likely sticking points:

- A `Path` stores a file location; it is not the image pixels or a description.
- The prompt is a string.
- The schema is a nested dictionary containing strings, dictionaries and a list.
- OpenRouter and Ollama use different transport syntax even though the research instruction is held fixed.
- `raw_output` is still text, even when the text follows JSON syntax.
- `json.loads(raw_output)` turns that text into a Python dictionary.
- Retrieving `description["visible_evidence"]` does not validate the contents of the list.
- A structured output can be perfectly well formed and empirically wrong.

## Completion standard

Students replace only the second frame, rerun through one selected route and submit a narrated screen recording. The recording should:

- identify both image-path inputs;
- explain whether OpenRouter or Ollama performs the inference;
- explain the prompt string and schema dictionary;
- show the raw JSON before parsing;
- identify the parsed dictionary and its three fields;
- check every visible-evidence claim against the displayed frames;
- identify any imported identity, motive or event knowledge; and
- connect the methodological limit to Goodwin, Heinlein or Nassauer.

Syntax elegance is irrelevant. The student is demonstrating that they understand the input, operation, output and evidentiary check.
