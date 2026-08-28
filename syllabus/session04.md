# Session 4 — What part of social experience becomes evidence?

**Date:** Wednesday, September 23, 2026 · 9:30 a.m.–12:15 p.m.  
**Course movement:** Observe  
**Methodological domain:** situated, sensory, and multimodal evidence

## Substantive question

What happens within a confrontation that allows violence to begin—or enables the confrontation to remain nonviolent?

We will use a clearly labeled, non-graphic, instructor-authored reconstruction. It is not evidence about a real protest, police unit, participant, injury, or population.

## Why this follows Sessions 1–3

- Session 1 recorded an LLM request and output.
- Session 2 treated a label as a proposed measure.
- Session 3 treated a theme as a proposed interpretation.
- Session 4 goes back one step: how does an unfolding situation become a visual, audio, transcript, fieldnote, participant, or model record?

## Learning objectives

By the end, students should be able to:

1. explain why Simmel, Mead, Goffman, conversation analysis, fieldnotes, and Goodwin make observation a sociological problem before any model is introduced;
2. explain Collins's shift from violent kinds of people to the interactional organization of violent situations;
3. separate visible or audible conduct from an interpretation of conduct and from unobserved intention;
4. explain why a video is positioned evidence with a start time, viewpoint, unit, and sampling process;
5. distinguish recognition, transcription, description, prediction, and sociological explanation;
6. compare an escalation and de-escalation sequence without treating a recorded change as a cause; and
7. explain the multimodal message and structured return as exact input and type → operation → exact output and type → sociological meaning → limit.

## Required readings

1. **Short observation packet:** selected passages from Georg Simmel on the sociology of the senses and Charles Goodwin on professional vision.
   - [Simmel, “Sociology of the Senses”](https://cuny.manifoldapp.org/read/georg-simmel-some-collected-works/section/8895b310-16c0-4ef8-8b27-de3e4988526d)
   - [Goodwin (1994), “Professional Vision”](https://doi.org/10.1525/aa.1994.96.3.02a00100)
2. [Collins (2013), “Entering and Leaving the Tunnel of Violence”](https://doi.org/10.1177/0011392112456500), with the short public [Chapter 1 extract from *Violence*](https://assets.press.princeton.edu/chapters/s8547.pdf).
3. Selected sections from [Nassauer and Legewie (2021), “Video Data Analysis”](https://doi.org/10.1177/0049124118769093).

The reading guide identifies the sections and a small set of optional background sources. The assigned load remains comparable with earlier weeks.

## Lecture argument

Close observation does not give us a transparent copy of social life. It gives us positioned, selected, and transformed records. Collins makes sequence central to explaining violence; Nassauer and Legewie show what has to happen before video can support that analysis. Multimodal models may help describe, align, or predict parts of a sequence, but those operations do not by themselves recover experience, intention, responsibility, or a sociological mechanism.

## Computational trace

Students place two ordered observations in a list and ask a hosted or local model for JSON separating an observable change from an interpretation to withhold. They trace prompt construction, the call, JSON parsing and field retrieval.

The code prepares a sequence for human interpretation. It does not discover the cause of violence.

## Weekly completion task

Run the supplied call, change one visible action and run it again. Submit a narrated screen recording explaining every input and output, comparing both descriptions and identifying any identity, motive or remembered context absent from the input. Link the limit to Collins or Nassauer and upload to the Box folder supplied by the instructor.

The task receives a completion mark. Syntax elegance is not assessed. AI use is permitted with responsibility and disclosure, but each student must be able to explain every submitted line and output without AI assistance.

## Preparation for the oral component

Be ready to answer:

- What exact value enters this line, and what Python type is it?
- What changes after this line?
- What exact JSON text is returned and what Python object does `json.loads` create?
- What does that output contribute to the sociological question?
- What would be invalid to conclude from it?
