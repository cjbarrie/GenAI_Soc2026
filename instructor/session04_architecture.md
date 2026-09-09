# Session 4 architecture — What can we learn from a recorded situation?

**Status:** Rebuilt after instructor review, 2026-08-26.

## Communication job

Students should leave able to explain:

1. why a recording is a positioned and selected record rather than the situation itself;
2. why an action must be studied in sequence and in relation to responses;
3. how Simmel, Mead, Goffman, Goodwin, Nassauer and Collins contribute different parts of that argument;
4. which claims the Zidane–Materazzi footage supports and which require other evidence; and
5. how a multimodal model call is constructed, what it returns, and how a researcher records corrections.

## Running case

The lecture uses the Zidane–Materazzi incident in the 2006 World Cup final. The case was selected because:

- official FIFA close and tactical-camera footage is available;
- the sequence contains movement, gesture, response, contact, officials and a mass audience;
- the crucial words are not clearly recorded, making the limits of video immediately visible;
- the official thumbnail itself frames the event as a “moment of madness,” providing a concrete Goodwin-style example of coding and highlighting; and
- published sociological work interprets the case through Elias and Bourdieu (Morrissey 2009), while Collins provides a distinct situational account of violence.

The footage must not be treated as a complete explanation. It records visible action from particular camera positions. It does not provide direct access to speech, intention, emotion, bodily experience or habitus.

## Narrative arc

### 1. Begin with the empirical problem

Open on the FIFA thumbnail and ask what the cameras recorded. Compare close and tactical views. Establish visible, audible and inferred material before introducing theory.

### 2. Establish the sociological lineage

- **Simmel:** sensory access is part of the relation.
- **Mead:** gesture and response form a social act.
- **Goffman:** actors, officials, audiences and rules organize the encounter.
- **Sequence analysis:** actions acquire meaning through temporal position.
- **Goodwin:** coding, highlighting and representation teach observers what to see.

Use real examples: Goodwin's Munsell chart and Rodney King courtroom analysis, not abstract summaries. Show Goodwin's later influence in protest/policing, medical vision and AI-assisted clinical seeing.

### 3. Introduce video sequence analysis before Collins

Use Nassauer (2022) to explain optimal capture, multiple angles, reconstruction and ordered coding. Build a source record for the FIFA material and show how selection narrows from the match to the frames sent to a model.

Nassauer's *Situational Breakdowns* is further reading only. It should not occupy a separate lecture sequence.

### 4. Introduce Collins as a theory to investigate

Use screenshots from Collins (2008) for the barrier of confrontational tension/fear and his comparative logic. Do not present an instructor-created sequence as Collins's stages.

Explain the “tunnel of violence” from Collins (2013) as an extended altered state involving changed perception of time, vision, sound and self. A brief head-butt clip does not establish that such a state occurred.

The descriptive sequence for the case is simply:

`close bodily positioning → movement and apparent talk → separation → turn → approach → contact → aftermath`

This is a source description, not a theoretical codebook.

### 5. Compare claims with their evidentiary requirements

Separate visible statements from causal and theoretical interpretations. Contrast Collins's interactional question with Morrissey's account of masculinity and habitus and experimental work on provocation and performance. The point is that different claims require different evidence.

### 6. Use an LLM as a second observer

The first prompt asks for visible actions only and explicit uncertainty. A second call adds an adjacent frame. The researcher then records a correction and source detail next to the model response.

### 7. Teach Python through that same operation

The code sequence is cumulative:

1. `Path` object for the image;
2. prompt string;
3. image bytes and base64 encoding;
4. message list containing text and image;
5. OpenRouter client and model call;
6. response object and answer string;
7. JSON parsing into a dictionary;
8. human check added to the dictionary;
9. ordered list of frame observations; and
10. loop that repeats the same routine.

Every slide must state the input, object type, operation and output. The sociological interpretation remains a human judgment.

## Visual and language rules carried forward

- No Observe/Intervene/Simulate course-map slides.
- No black section backgrounds.
- No slides that announce what “the next six slides” will do.
- Avoid slogans, false contrasts and compressed phrases that sound machine-written.
- Put the purpose of the slide in the title and enough explanation on the slide to recover the argument without presenter rescue.
- Use readable crops of the relevant page or figure, not small first pages surrounded by dead space.
- State whether a sequence, checklist or synthesis is taken from a source; do not allow instructor synthesis to masquerade as a published typology.
- Show real inputs and outputs throughout the code walkthrough.
- Close the lecture itself; mention world-model literature only as an optional technical extension.

## Main sources

- Simmel, Georg. 1997 [1907]. “Sociology of the Senses.”
- Mead, George Herbert. 1934. *Mind, Self, and Society*.
- Goffman, Erving. 1983. “The Interaction Order.” *American Sociological Review* 48(1):1–17.
- Goodwin, Charles. 1994. “Professional Vision.” *American Anthropologist* 96(3):606–633.
- Collins, Randall. 2008. *Violence: A Micro-sociological Theory*.
- Collins, Randall. 2013. “Entering and Leaving the Tunnel of Violence.” *Current Sociology* 61(2):132–151.
- Nassauer, Anne. 2022. “Video Data Analysis as a Tool for Studying Escalation Processes.” *Sociological Methods & Research*.
- Morrissey, Sean. 2009. “‘Un homme avant tout’: Zinedine Zidane and the Sociology of a Head-butt.” *Soccer & Society* 10(2):210–225.
