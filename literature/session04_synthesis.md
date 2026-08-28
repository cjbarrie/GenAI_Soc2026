# Session 4 synthesis — What can we learn from a recorded situation?

**Status:** Revised after the Week 4 slide review on August 26, 2026. The working example is now the Zidane–Materazzi incident rather than a synthetic protest confrontation.

## Revision note

The lecture now begins from official FIFA close and tactical-camera footage. This makes the evidentiary problem concrete: bodily movement is visible, but the crucial speech and participant experience are not. Simmel, Mead and Goffman establish sensory access, response and the interaction order; Goodwin is taught through his Munsell and Rodney King examples; Nassauer's video method precedes Collins; Collins is introduced as a theory to investigate rather than an automatic codebook. Nassauer's *Situational Breakdowns* remains further reading only. The LLM and Python sections operate on the same FIFA frames and store model descriptions beside source details and researcher corrections.

## Central argument

Social scientists do not begin with interchangeable text, image, and audio files. They begin with people acting in material and social situations. Researchers then produce selective records of those situations: observations, fieldnotes, photographs, video, recordings, transcripts, interviews, sensor measurements, and administrative data. Each record makes some features inspectable while changing, excluding, or leaving other features unobserved.

Multimodal models extend what can be processed computationally. They can describe images, transcribe speech, classify sound, align modalities in a shared representation, and learn regularities useful for predicting future states. These are significant technical capabilities. They do not remove the need to specify what social phenomenon the record can evidence, how the record was produced, what the representation loses, and what comparison or validation would warrant the eventual sociological claim.

The session should be organized around this chain:

`lived social situation → sensory trace → research record → model representation → measurement claim`

The central teaching claim should be:

> More modalities can give a researcher more traces of a social situation. They do not give direct access to the whole experience or make the resulting sociological interpretation self-validating.

This formulation avoids two bad positions. It does not treat a transcript, image, or model embedding as a transparent copy of reality. It also does not claim that only unrecorded first-person experience is legitimate evidence. The methodological task is to understand what access each record provides, what it omits, and what additional evidence the intended claim requires.

## Four things students must keep separate

| Level | What it is | Protest-confrontation example | What it cannot establish by itself |
|---|---|---|---|
| Lived situation | Temporally unfolding activity involving bodies, objects, other people, institutions, memory, and interpretation | Protesters and police confront one another; distance, rhythm, attention, fear, and relative advantage change over several seconds | It is not available to the researcher in its totality, including participants' perception and bodily experience. |
| Sensory trace or research record | A selected and technically produced inscription of part of the situation | Video angles, audio, transcripts, still frames, fieldnotes, and participant accounts | No single record reproduces the situation, and each camera or microphone has a position and temporal boundary. |
| Model representation or output | A learned numerical representation or generated description based on selected input | Frame descriptions, tracked movement, ASR transcript, action label, embedding, or predicted next state | Successful recognition or prediction does not explain the interactional mechanism or establish actors' intentions. |
| Sociological claim | A researcher-authored inference tied to a question, comparison, and evidentiary standard | “A shift in distance, communication, and situational advantage enabled this confrontation to become violent.” | One plausible reconstruction does not establish causality, generality, responsibility, or the dispositions of a group. |

These levels should recur throughout the class. “Multimodal” describes inputs or representations; it does not by itself describe the scope or validity of the inference.

## What researchers did before multimodal foundation models

The pre-LLM benchmark is not a single manual procedure. Several established practices address different parts of the chain.

### Researchers studied how the senses organize social relations

Simmel treated sensory contact as constitutive of relations among people rather than as neutral information transmission. Later sensory sociology examined how bodies, identities, places, times, rituals, media, and inequalities organize what people learn to notice, tolerate, value, or avoid. Sight and hearing are therefore not merely two input formats. Looking, listening, being looked at, being overheard, bodily proximity, and sensory exposure can themselves be social relations.

### Researchers studied meaning within social action and the lifeworld

Mead located meaning in organized social acts rather than in isolated signs. Schutz began from an intersubjective everyday world already interpreted by participants. These traditions make a useful demand of computational claims: a representation of observable regularities should not automatically be described as the participant's meaning, practical knowledge, or experienced world.

### Researchers treated face-to-face interaction as a social order

Goffman argued that co-present interaction has its own organization and obligations. Bodily presence, mutual monitoring, glances, gestures, talk, accessibility to others, and the management of encounters are not incidental details beneath “larger” social processes. They are organized phenomena through which institutions, identities, deference, conflict, and inequality are accomplished.

### Researchers examined action sequentially

Ethnomethodology and conversation analysis ask how participants themselves make an unfolding situation intelligible and produce its order moment by moment. Sacks, Schegloff, and Jefferson show that turn-taking is locally managed, interactionally controlled, and sensitive to recipients. The broader methodological lesson is that the meaning of an action depends partly on what precedes it, what follows it, and how others respond. Reordering or compressing a sequence can change the phenomenon under study.

### Researchers documented situated, embodied, and professionally organized vision

Goodwin shows that talk, gaze, gesture, bodies, objects, graphic fields, and historically shaped environments make interdependent contributions to action as it unfolds. His account of professional vision also shows that coding, highlighting, and graphic representation teach members of a community what to notice and how to transform a perceptual field into an object of knowledge. Video and transcript analysis can preserve and reconstruct different parts of action, but no modality or coding scheme contains the situation intact.

### Researchers turned participation and observation into written records

Participant observation joins involvement in a social setting with the regular production of fieldnotes. Emerson, Fretz, and Shaw make clear that writing does not simply download remembered experience: researchers select scenes, dialogue, movement, moods, and relevant details and transform them into an accumulating record. Observation is therefore already a representational practice before a camera or model enters.

### Researchers reconstructed the dynamics of violent situations

Collins builds on this concern with co-presence, bodies, emotion, and interactional sequence. His micro-sociology of violence shifts attention away from supposedly violent kinds of people and toward the conditions under which violence becomes possible. His evidence includes photographs, video, ethnography, interviews, and forensic reconstruction. The theory proposes that face-to-face confrontation commonly produces tension and fear that inhibit effective violence; particular pathways around that barrier, including sudden situational dominance and forward panic, help explain why some confrontations become violent while many do not.

Nassauer develops the situational approach through comparisons of protests that remain peaceful and protests that break down. Nassauer and Legewie's video data analysis framework then makes the research procedure explicit: define the event and unit, sample recordings, reconstruct temporal order, compare perspectives, code visible and audible conduct, preserve context, and link situational observations to larger explanatory claims.

### Researchers produced visual, audio, and textual evidence deliberately

Visual methods attend to who made an image, from where, for what purpose, and how it circulated. Audio and interaction research make choices about microphone placement, temporal units, speakers, noise, prosody, overlap, and synchronization. Qualitative researchers decide what enters fieldnotes and how observation relates to participant accounts. Documentary and archival methods preserve provenance and chains of transformation.

### Researchers treated transcription and coding as analytic transformations

A transcript selects which sounds become words, which pauses or overlaps are represented, how speakers are identified, and what nonverbal events are included. A code similarly turns a record into a variable using a construct and decision rules. Automated transcription, description, and labeling change the scale and speed of these operations without making them lossless.

This history gives the benchmark for the LLM-assisted workflow. The new question is not whether the computer can accept the file. It is whether the computational transformation supports the researcher's intended inference.

## What current multimodal and world-model systems change

### One interface can process several kinds of record

A contemporary model or representation system may accept text, images, audio, video, or sensor data. This removes some practical barriers between media and enables new tasks such as image description, cross-modal search, and audiovisual question answering. It also makes it easier to conceal the different production and error processes behind a common prompt or API call.

### A shared embedding can connect modalities

ImageBind demonstrates that images, text, audio, depth, thermal data, and inertial measurements can be aligned in a common learned space. That enables retrieval and association across media. The methodological point is precise: common coordinates express learned similarity. They do not show that the media are evidentially equivalent or that the model has undergone the unified sensory experience of a person in the scene.

### A world model can learn compressed predictive structure

Ha and Schmidhuber's “World Models” and V-JEPA 2 represent environments in ways that support prediction and action. V-JEPA 2's learned visual dynamics can help a robot plan reaching and object manipulation in unfamiliar physical settings. This gives the course a concrete, non-mystical definition: a world model is useful insofar as its representation supports the predictions and actions for which it is evaluated. In the confrontation example, predicting that a body will advance, retreat, or fall is not yet an explanation of how the interaction produced violence.

### Text-trained models can recover some real-world structure

Gurnee and Tegmark complicate a simple form-versus-world opposition by showing that language-model representations can encode spatial and temporal structure. Patterned language contains information about the world. The appropriate conclusion is not that text models know nothing, nor that recovered coordinates equal lived understanding. Students should ask which structure is represented, how it is tested, and what claim follows.

### The comparison opens a sociological question

Current technical evaluations commonly emphasize recognition, retrieval, prediction, planning, and task performance. Social scientists may additionally care about intended meaning, practical familiarity, reciprocal awareness, moral evaluation, institutional position, cultural classification, historical formation, memory, pain, fatigue, and felt belonging. Some of these may leave observable traces; some require participant testimony or sustained observation; some remain only partially accessible.

The question for class is therefore:

> A model can learn enough regularity to predict what happens next. Is that the same as having a world? What else would a social scientist want to know about the situation?

The class should investigate this question rather than settle it by assertion.

## Six cumulative lessons

### 1. Begin with one social situation, not three file types

Students first need to know what happened, who was involved, how the material was produced, and what question the researcher is asking. Only then should they inspect which records exist. This reverses the existing week, which begins with generic modality labels and nonexistent paths.

The session should initially describe a confrontation that has not yet become violent. Students identify what they would need to observe to explain its next several seconds before seeing the images, audio, transcript, or model output. This establishes that data collection is guided by a theory and research question rather than by model capability.

### 2. Every record provides access and introduces absence

Successive images may preserve relative position, bodily orientation, advance, retreat, and clustering but not what happened before the camera started or how participants perceived the threat. Audio may preserve chant rhythm, commands, volume, hesitation, and overlap while obscuring who moved. A transcript makes words searchable while removing tempo, collective noise, tone, and simultaneous action. A fieldnote records context and off-camera conduct while reflecting the observer's position. Participant accounts provide fear, attention, intention, and retrospective interpretation rather than neutral copies of the event.

The relevant exercise is not a competition to identify the “richest” modality. Students should state what claim each record can contribute to and what remains unavailable.

### 3. Converting one representation into another is a measurement decision

Speech-to-text, image-to-text, audio classification, temporal segmentation, and embedding all select information. Davidson provides the human-method analogue: different research purposes produce different transcripts of the same recording. Arminio et al. show a deliberate computational version: converting images into connotative descriptions improves one kind of clustering while changing the meaning of similarity.

The model output should therefore remain linked to the source record. Students must be able to move back from a label or description to the image, audio interval, or passage on which it rests.

### 4. Prediction, recognition, description, and interpretation are different achievements

A world model may predict motion; a vision model may identify an advance or retreat; ASR may recover spoken words; an audio model may recognize chanting; an LLM may describe a participant as “aggressive.” These outputs carry different evidentiary burdens. “Aggressive” is especially instructive because it converts visible conduct into a disposition and may import a culturally patterned judgment that the sequence does not establish.

Students should learn to name the operation before evaluating it. Model performance on one operation cannot be carried into a stronger one without additional evidence.

### 5. Validation evidence must match the proposed claim

Different claims require different checks:

| Proposed claim | Relevant check | Important remaining limit |
|---|---|---|
| One party advanced before the other retreated | Synchronized perspectives, explicit movement rules, and interval-level human coding | The camera may begin late, omit off-frame action, or make depth difficult to judge. |
| An instruction was audible before the advance | Human listening and time-aligned audio/transcript comparison | Audibility on the recording does not establish that every participant heard or understood it. |
| Chanting or crowd response became more synchronized | Defined rhythmic or turn-taking indicators compared across intervals | Visible or audible coordination does not by itself reveal shared emotion or intention. |
| Participants experienced confrontational tension or fear | Contemporaneous bodily evidence plus participant accounts and careful retrospective interpretation | Fear cannot be read reliably from facial appearance or posture alone. |
| A situational pathway contributed to violence | Comparison with nonviolent confrontations, alternative mechanisms, temporal evidence, and a defensible sampling design | Temporal precedence and patterned comparison still require causal argument and do not assign moral responsibility. |

This carries the validation logic of Weeks 2 and 3 into a richer source situation.

### 6. Provenance, privacy, consent, and accessibility shape the evidence

Images and voices can identify people and places. Cloud transcription can transfer audio to third parties. Copyright can prevent redistribution of apparently ordinary streetscape images. A modality may also create access barriers unless transcripts, captions, descriptions, and non-audio alternatives are provided.

These are not generic final-slide concerns. They determine what researchers can collect, send to a model, share with students, validate, and reproduce. The required exercise must therefore use local, cached, instructor-authored, or appropriately licensed material with an explicit provenance record.

## Productive relationships among the focal readings

The readings should alter the status of the same explanation of a confrontation rather than appear as separate paper summaries.

1. **Simmel, Mead, and Goffman:** sensory reciprocity, social acts, and the interaction order establish the situation as an organized sociological object before it becomes a recording.
2. **Conversation analysis, Emerson, Fretz, and Shaw, and Goodwin:** sequence matters, fieldnotes are produced representations, and professional coding and highlighting organize what observers learn to see.
3. **Collins:** violence is difficult and situational. The analyst must reconstruct how bodily and emotional dynamics either sustain the barrier of confrontational tension and fear or create a pathway around it.
4. **Nassauer:** protests with grievances, threatening actors, and police presence can end differently because interactional combinations and breakdowns unfold differently. The situation is an explanatory object, not contextual decoration.
5. **Nassauer and Legewie:** video evidence requires an explicit research process involving event definition, sampling, segmentation, synchronization, coding, comparison, interpretation, validity, and ethics.
6. **Bisk et al., taught through selected pages:** adding perception and action moves beyond text but does not automatically supply shared social experience or participant meaning.
7. **Law and Roberto plus Mestre and Ryan, taught through figures:** visual descriptions, transcripts, acoustic features, and embeddings are constructed measurements with modality-specific validation requirements.
8. **ImageBind and V-JEPA 2, taught in class:** shared representations and predictive models demonstrate real technical advances while giving students something precise to compare with temporal reconstruction and sociological explanation.

The readings do not yield a binary answer to whether a model “understands.” They help students specify the representation, task, validation, and social phenomenon before making that claim.

## Recommended reading configuration

### Required

1. **Collins (2013), “Entering and Leaving the Tunnel of Violence,”** with a short excerpt from the 2008 book introduction if needed. This provides the substantive theory in an assignable form.
2. **Nassauer and Legewie (2021), selected sections from “Video Data Analysis.”** This provides the human research procedure for constructing and validating evidence from recorded situations.
3. **Short sociological-observation packet:** Simmel's “Sociology of the Senses” plus a selected concrete episode from Goodwin on professional vision or embodied interaction. This establishes sensory reciprocity, socially organized seeing, and multimodal action without adding another full book.

### Taught through selected sequences, pages, or figures

- Nassauer (2019), paired peaceful and violent protest outcomes.
- Legewie, Nassauer, and Kühne (2026), video sampling and generalization.
- Mead, Goffman, conversation analysis, and Emerson, Fretz, and Shaw as the broader observational lineage.
- Bisk et al. (2020), the progression from text and pixels toward embodiment, action, and social interaction.
- Law and Roberto (2025), curation and validation of model-generated image measures.
- Mestre and Ryan (2026), non-equivalent audio representations.
- Davidson (2009), transcription as a selective representation.
- ImageBind and V-JEPA 2, shared representation versus prediction and planning.

Moving Law and Roberto and Mestre and Ryan into concentrated in-class evidence keeps the assigned load broadly stable while allowing the session to begin from a substantive sociological theory and an established observational method.

## Recommended cumulative example

### Study setting

The teaching study concerns a short confrontation between protesters and police that begins as a tense standoff. Its research question is:

> What happens within the situation that allows violence to begin—or enables the confrontation to remain nonviolent?

The example begins before any violent act. Relevant features include distance between groups, bodily orientation, clustering, eye contact, commands, chanting, rhythm, audience responses, failed communication, advance and retreat, sudden imbalance, fear, and attention. These features unfold in sequence. A final frame labeled “violent” cannot show how the situation reached that point, and prior grievances or group identities cannot establish that violence was inevitable.

To make comparison possible without creating unrelated examples, the evidence package should contain two short endings to the same constructed setup: one in which distance is restored and the encounter de-escalates, and one in which a sudden shift in situational advantage precedes a brief shove. The unit remains one cumulative study of a confrontation sequence; the paired ending tests what changes within it.

### Provenance and limits

The classroom scene should be an **instructor-authored, non-graphic synthetic reconstruction**, not real protest footage presented without its history. It can be built from a sequence of drawn or generated frames, staged voices, and explicit written observations. It must not use an identifiable person's image, voice, injury, or attributed testimony. Every artifact should carry a visible provenance label.

The example can teach temporal reconstruction, theory-guided observation, model comparison, and the distinction between prediction and explanation. It cannot establish that Collins's theory is correct, that the depicted mechanism generalizes, that either party is responsible for a real event, or that any social group is violent. The final class claim must retain those limits.

### Connected source records

The eventual build should create a small local evidence package containing:

1. **A six-moment frame sequence:** separation, mutual orientation, narrowing distance, overlapping signals, a shift in relative position, and either restored distance or a brief shove.
2. **One 10–15 second staged audio file for each ending:** chanting, an instruction, hesitation or overlap, audience response, and a change in collective volume or rhythm.
3. **Two transcripts of the same audio:** a plain automated-style transcript and a detailed human-style transcript marking timing, overlap, volume, chant, and non-speech response.
4. **Two camera perspectives or explicit frame-boundary diagrams:** enough to show that the apparent first movement can depend on position and recording onset.
5. **One instructor-authored observation note:** the wider sequence, off-camera movement, uncertainty, and the observer's location.
6. **Two explicitly synthetic participant accounts:** contrasting recollections of fear, instruction, attention, and perceived threat.
7. **One model observation sequence:** cached descriptions of each moment plus a whole-event summary.

These are connected records of one constructed comparison, not independent examples of text, image, and audio.

### Candidate model outputs

Cached model-style outputs should remain plausible rather than obviously incompetent:

- per-moment description: “Police step forward as protesters continue chanting”;
- audio description: “Raised voices, chanting, and an instruction to move back”;
- automated transcript that turns simultaneous speech into orderly consecutive turns;
- next-state prediction: “The front protester is likely to move backward”;
- whole-event summary: “Aggressive protesters approach police, causing the confrontation to become violent.”

The descriptions and prediction can be checked against defined intervals. The whole-event summary changes observed action into disposition and causality. The class should identify where that transformation occurred, which interval or perspective is missing, and which alternative explanation remains possible.

### Candidate sociological claim

The model-assisted workflow may initially produce:

> “Aggressive protesters approached police and caused the confrontation to become violent.”

The class should revise this to something the synthetic case can actually support:

> “In the constructed escalation sequence, narrowing distance, overlapping signals, and a sudden shift in relative position occurred before the shove. The de-escalating ending restored distance at the corresponding moment. These records show how a Collins-inspired situational explanation could be investigated, but they do not establish the participants' intentions, assign responsibility, validate the theory, or support a claim about protesters or police generally.”

This is deliberately less dramatic and more defensible. It models the course's recurring distinction between an interesting output and a warranted claim.

## Human-method-to-code mapping

| Human research practice | Python representation | Where the code is thinner |
|---|---|---|
| Assign a stable identifier to each record | `record_id` string | An ID does not establish correct alignment or provenance. |
| State who or what produced the record | `source`, `creator`, and `production_mode` strings | A filled field may still contain an inadequate description. |
| Segment an unfolding event into inspectable moments | ordered `moments` list with `time` values | Segmentation imposes boundaries on continuous action and can miss rapid changes. |
| Record the medium, perspective, and temporal relation to the scene | `record_type`, `scene_id`, `camera`, and `time_window` fields | Matching IDs do not prove synchronization or a complete view. |
| Describe observable conduct before interpreting it | `observed_actions` and `audible_events` lists | A list freezes researcher judgments and cannot recover unrecorded conduct. |
| State what the representation cannot show | `known_limits` list | Researchers cannot enumerate every unknown or absence. |
| Preserve transformations | `derived_from` and `transformation` fields | The record documents a transformation but not every internal model operation. |
| Compare adjacent moments and paired endings | loop using the current and previous dictionaries | Temporal order does not by itself establish a causal mechanism. |
| Link a proposed mechanism to its sequence | `evidence_ids` and `time_windows` lists | Citation to intervals does not prove that the proposed mechanism is correct. |

The code should reproduce the discipline of an evidence ledger. It should not attempt to compute sensory richness or decide which representation is true.

## Beginner Python progression

The technical ambition should remain below the conceptual ambition. Week 4 can reuse the objects introduced in Weeks 1–3:

- a **string** stores one ID, record type, or source note;
- a **list** stores an ordered sequence of moment dictionaries;
- a **dictionary** stores the observations for one moment;
- a `for` **loop** visits one moment at a time in temporal order;
- an `if` statement applies a clearly stated temporal or evidence check;
- `.append()` adds one warning to a list;
- a small **function** packages the evidence-ledger check and returns a dictionary.

No list comprehension should appear before students have built and traced the equivalent loop. Nested structures should be introduced through one concrete value at a time.

### Proposed code progression

1. Show the exact integer `time = 0` and string `distance = "separated"`; print each value and type.
2. Assemble one `moment` dictionary from those already understood values.
3. Read one dictionary key and predict the exact output.
4. Put two moment dictionaries in a list and explain why their order matters.
5. Use a loop to print each time, distance, and observed action.
6. Add `previous_moment = None` before the loop and trace why the first iteration has no earlier comparison.
7. Add one transparent branch that compares the current distance with the previous distance.
8. Accumulate observed changes with `.append()` and print the list after each iteration.
9. Add provenance and perspective checks for the connected video, audio, and transcript records.
10. Wrap the already understood operations in `trace_sequence(moments)` and return a structured record for human interpretation.

### Proposed evidence record

```python
moment = {
    "time": 4,
    "distance": "narrowing",
    "police_action": "advance one step",
    "protester_action": "front line remains in place",
    "audible_events": ["chant", "move-back instruction", "overlap"],
    "source_record": "ANGLE_A_00_04_00_06"
}
```

Students should be able to say that `moment` is a dictionary, `time` is an integer, `distance` is a string, and `audible_events` is a list of strings. They should also explain that “narrowing” and “advance one step” are human-authored observational codes rather than facts that arrived automatically from the video.

### Proposed audit output

```python
{
    "moments_checked": 6,
    "observed_changes": ["distance narrowed at time 4", "relative position changed at time 6"],
    "alignment_warnings": ["automatic transcript has no time window for the overlap"],
    "ready_for_human_review": False,
    "warning": "A documented sequence does not establish the cause of violence."
}
```

The first output fields are produced by simple temporal comparisons and record checks. `ready_for_human_review` should be `False` when a known alignment requirement is missing. It should never be named `violence_cause` or `valid_explanation`. If all fields are complete, the result may say the sequence is documented enough for human review, not that the mechanism is correct.

### Oral-assessment rehearsal

With the adjacent-moment comparison visible, a student should be able to explain:

1. the exact current and previous dictionaries;
2. why the first iteration treats `previous_moment` differently;
3. what values the condition compares;
4. when a change string is appended;
5. what the changes list contains afterward;
6. what temporal reconstruction practice the comparison represents; and
7. why an observed sequence does not establish causality or intention.

This is an appropriate rehearsal for the later individual oral code walkthrough.

## Reading-to-code alignment

| Reading contribution | Object or operation in the code | Interpretation students should make |
|---|---|---|
| Collins: violence emerges through temporal and interactional pathways | ordered moment dictionaries and adjacent-moment comparison | The explanatory object is an unfolding situation, not a final frame or a type of person. |
| Nassauer: similar protest settings can end differently | paired escalation and de-escalation endings | A situational claim requires comparison, including cases where violence does not occur. |
| Nassauer and Legewie: video analysis requires explicit units, sequence, perspective, and validation | `time`, `camera`, `source_record`, and alignment warnings | Video does not analyze itself; the research design constructs the observable sequence. |
| Simmel: sensory contact helps organize social relations | visible actions, audible events, and known limits | Seeing, hearing, and reciprocal orientation are part of the encounter, not only input formats. |
| Bisk et al.: grounding extends beyond text and pixels toward action and social interaction | compare frames, audio, transcript, observation, and participant accounts | Adding a modality supplies another trace; it does not automatically supply embodied or shared experience. |
| Law and Roberto: curation, discovery, measurement, and validation remain distinct | provenance fields and source-to-derived links | A model description belongs inside an inspectable research workflow. |
| Mestre and Ryan: audio can become several non-equivalent representations | audio record, automated transcript, detailed transcript, and aligned time window | Words, delivery, background sound, timing, and embeddings support different questions. |
| Davidson: transcription is selective | `derived_from` and `transformation` | A transcript is a produced representation of a recording, not the recording in text form. |
| Goodwin: action uses interdependent semiotic resources | shared time windows with modality-specific records | Alignment helps reconstruct action but does not make the resources independent or interchangeable. |
| ImageBind: modalities can share a representation space | instructor diagram or cached similarity output, not student implementation | Computational alignment is useful but does not establish evidentiary equivalence. |
| V-JEPA 2: learned representations can support prediction and planning | conceptual prediction example outside required code | Prediction performance warrants a task-specific capability claim, not a claim of lived social understanding. |

## Likely failure modes and stakes

### Treating visible conduct as disposition or intention

A forward step is observable within a defined view. Calling it “aggressive,” “provocative,” or “fearless” interprets conduct through a category that requires additional situational and participant evidence.

### Treating a transcript as the audio

Chanting, crowd noise, and simultaneous commands may mask speech; ASR may reorder or drop overlap and perform unequally across accents and recording conditions. Later text analysis can then turn a disordered encounter into a falsely orderly exchange.

### Treating co-occurrence as alignment

Two camera angles and an audio recording may begin at different moments or be edited at different boundaries. A shared `scene_id` cannot repair poor synchronization or establish which action occurred first.

### Treating a shared embedding as a shared construct

Records may be close in a learned space because of common objects or labels while differing on the sociological feature of interest. Similarity requires an interpretation and task-specific validation.

### Treating prediction as explanation

A model may predict that a body advances, retreats, or falls without explaining how tension, communication, audience response, institutional roles, or sudden advantage produced the transition.

### Generalizing from an evocative violent episode

One vivid sequence can reveal a candidate mechanism. It cannot establish that protesters, police, or another social group are generally violent. Selection is especially consequential because recordings disproportionately circulate when violence occurs; peaceful standoffs and the lead-up to violence may be missing.

## What should remain outside Session 4

- detailed encoder, transformer, JEPA, or reinforcement-learning mathematics;
- implementation of ImageBind or V-JEPA 2;
- a general verdict on machine consciousness or whether AI “really understands”;
- a comprehensive history of phenomenology or sensory anthropology;
- facial or emotion recognition as a classroom coding exercise;
- live processing of identifiable voices or images through a hosted service;
- the causal design of generated multimodal treatments, which belongs in Session 5;
- sustained analysis of the model as an interactant or AI interviewer, which belongs in Session 6;
- extended audiovisual conversation analysis, which can reappear with CANDOR in Session 6;
- statistical correction for image-label error in full technical detail, already conceptually prepared in Session 2.

World models should occupy a bounded conceptual segment. They sharpen the week’s question but should not displace visual, audio, sensory, and interactional research practice.

## What students should be able to say at the end

A successful student explanation would sound like this:

> We reconstructed a confrontation as an ordered sequence rather than beginning with a label for the people or the final event. The video angles, audio, transcript, observation note, and participant accounts do not contain the same information. A multimodal system can describe and align those records, and a world model may predict what movement comes next. Prediction is not yet a Collins-style explanation of how the situation enabled or inhibited violence. The code records time, perspective, observable changes, and missing alignment. It prepares the sequence for human interpretation; it does not identify the cause, intention, or responsible group.

That explanation should govern the later session architecture, slides, workbook, completion task, and oral-assessment rehearsal.

## Review Gate 2 recommendation

Approve the following before Stage 4 begins:

1. the revised session question: **What part of social experience becomes evidence?**
2. the representational chain from lived situation to measurement claim;
3. the non-graphic synthetic protest confrontation with paired escalation and de-escalation endings as the cumulative example;
4. Collins and Nassauer/Nassauer–Legewie as the principal theory-and-method sequence, with the sensory, grounding, visual, and audio literature placed around it;
5. Simmel, Goodwin, Bisk et al., ImageBind, V-JEPA 2, Law and Roberto, and Mestre and Ryan as supporting bridges rather than competing centers;
6. an ordered-sequence Python exercise rather than generic multimodal normalization; and
7. the endpoint that documented temporal records become ready for human interpretation, never automatically a valid causal explanation.
