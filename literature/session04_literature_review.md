# Session 4 literature review — Stage 1 audit and orientation

**Session question:** What part of social experience becomes evidence across text, image, and audio?  
**Principal domain:** Multimodal measurement  
**Date:** September 23, 2026  
**Status:** Stage 2 literature review and sensory/world-model extension approved at Review Gate 1 on August 21, 2026. Stage 3 synthesis is recorded separately.

## What the existing session is trying to teach

The existing materials make one defensible point: putting text, image, and audio records into a common data structure can make them easier to compare, but it does not make the evidence or validation requirements equivalent. The computational example operationalizes this point by checking that a text record has text, an image record has a path and source, and an audio record has a path and duration.

The three assigned papers suggest a visual-methods emphasis:

- Law and Roberto use generative multimodal models with satellite and streetscape imagery;
- Maranca and colleagues address measurement error in AI-assisted image labeling;
- Arminio and colleagues study image-to-text mapping and visual clustering with vision-language models.

The intended class therefore appears to combine two goals: introduce multimodal models as tools for social measurement and teach students that modality-specific information must survive any common representation.

## Existing artifact inventory

| Artifact | Current state | Audit finding |
|---|---|---|
| `syllabus/session04.md` | Complete but very compressed | States a bounded claim and three readings, but gives no history of multimodal evidence, cumulative study, or distinction between construct validity and metadata completeness. |
| `readings/session04_reading_guide.md` | 21 lines | Uses the same generic questions for all three papers and does not explain their data, designs, findings, disagreements, or distinct teaching roles. |
| `instructor/session04_notes.md` | Generic 165-minute template | Protects beginner pacing, but “reading disagreement” and “study anatomy” have no substantive content or student-facing example. |
| `slides/session04/session04.qmd` | 16 slides | A release skeleton rather than a teachable 165-minute deck. It introduces no established human method, source material, construct, empirical stakes, paper images, actual multimodal evidence, or modality-specific failure cases. |
| Workbook | 17 cells | Provides careful line-by-line prose, but places a complete function and list comprehension before students have seen the operations separately. It never inspects actual image or audio content. |
| Completion task and solution | One normalization function | Appropriately low stakes, cached, and small. The function checks metadata presence rather than multimodal measurement or interpretation. |
| Tests | One smoke test | Confirms only that `run_checks()` does not fail. It does not test modality-specific branches, unknown modalities, input preservation, or substantive failure cases. |
| Data and visual assets | None | The paths `street.jpg` and `meeting.wav` name files that do not exist. Students cannot compare what is visible, audible, transcribed, or described. |

## What is worth retaining

1. **The bounded warning:** a common schema can conceal modality-specific evidence and error.
2. **The insistence on provenance:** image source, transcript availability, and audio information should not disappear during normalization.
3. **Cached and synthetic required work:** no API credit, special hardware, or live service should determine completion.
4. **A small transparent Python task:** lists, dictionaries, missing values, loops, and returned records are appropriate for the course level.
5. **The visual-measurement papers as candidates:** Law and Roberto, Maranca et al., and Arminio et al. may supply distinct parts of a coherent image-analysis sequence, subject to the Stage 2 literature review.

## What is thin, disconnected, outdated, or pitched incorrectly

### The week begins with a data schema rather than a research practice

Students are told to normalize records before they know how sociologists have treated photographs, streetscapes, speech, sound, captions, transcripts, or audiovisual interaction as evidence. The session therefore begins with a programming convenience rather than an inferential problem.

### The three modalities exist only as labels

The example contains one caption string and two nonexistent file paths. It never asks what can be seen in an image, heard in a recording, lost in a transcript, or inferred differently from a written description. As a result, the exercise is about missing metadata, not multimodal evidence.

### The construct and substantive stakes are absent

There is no cumulative sociological study, sampling decision, measurement target, unit of analysis, human codebook, reference evidence, or downstream claim. “Storefront signs in Spanish” hints at a possible study of neighborhood change or linguistic landscape, but the materials do not develop it.

### The readings are not yet doing distinct work

The deck describes Law and Roberto as “methodological opportunity” and the other two papers as “validation or counterclaim.” This does not tell students what each paper analyzed, compared, or found. It also leaves audio almost entirely unsupported by the assigned literature.

### Visual evidence dominates a supposedly multimodal week

All three current readings concern images or vision-language models. Text is treated as a generic baseline and audio is represented only by a duration field. The title promises a comparison across text, image, and audio that the readings and example do not deliver.

### Metadata completeness is being asked to carry too much weight

An image source and audio duration may matter, but their presence does not establish that a construct is visible or audible, that a model used the relevant cues, or that records are comparable across modalities. The current `missing` list risks becoming another software check mistaken for validity.

### The code advances too quickly for the agreed beginner standard

The slides project a full function, nested dictionary, loop, list comprehension, `.get()`, membership test, `or`, and `.append()` before tracing concrete values through each operation. The workbook explains these lines afterward, but explanation should precede assembly. The task asks students to reproduce the whole function even though the conceptual payoff is only a metadata check.

### The 2025 precedent should not simply be transplanted

The 2025 syllabus used CANDOR and Seamless Interaction in a later session on audiovisual social interaction, alongside Blumer and Goffman. CANDOR may remain useful as an example of genuinely multimodal social data, but Week 4 now concerns measurement rather than interaction theory. The old session provides a possible dataset and warning about reducing interaction to isolated features, not a ready-made Week 4 architecture.

## How Week 4 should follow Weeks 1–3

The opening four weeks form an increasingly demanding sequence of observational claims:

1. **Week 1:** an LLM call becomes a research record whose inputs and outputs can be inspected.
2. **Week 2:** a generated label is a proposed measurement that requires a construct, reference evidence, stability checks, and attention to downstream error.
3. **Week 3:** a generated theme is a proposed interpretation that requires context, comparison, counterexamples, memoing, and iterative human judgment.
4. **Week 4:** multiple modalities raise a new question: does adding an image or recording provide new evidence for the same construct, change the construct, or merely create the appearance of richer measurement?

Week 4 should therefore retain the validation habits of Weeks 2–3 while changing the source material. It should not repeat the general explanation of model providers or present multimodal input as self-validating because it is technically processable.

## The practices that came before multimodal LLMs

The fresh literature review should begin from established practices rather than model capability. The principal traditions to investigate are:

### Quantitative and qualitative content analysis

Researchers defined units of analysis, sampled documents or media, developed coding categories, trained human coders, assessed reliability, examined validity, and linked coded variables to substantive claims. Images and transcripts did not become comparable merely because both received labels.

### Visual sociology and visual methods

Photographs and video have been treated as records produced from particular positions, institutions, technologies, and selections. Researchers analyze composition, social context, circulation, elicited interpretations, and what remains outside the frame. The source and production of an image are part of its evidentiary meaning.

### Social semiotics and multimodal discourse analysis

Meaning can be distributed across words, layout, gesture, gaze, sound, and image. Modes interact rather than contributing independent interchangeable features. A caption can redirect the interpretation of an image, and a transcript can remove timing, emphasis, overlap, or tone.

### Conversation analysis, interaction analysis, and sociophonetic approaches

Audio and audiovisual records preserve sequence, pauses, overlap, prosody, voice quality, and embodied conduct that a transcript may omit. Transcription is an analytic representation, not a neutral copy of a recording. Measurement choices determine which interactional features remain available.

### Documentary, archival, and observational practice

Researchers establish provenance, sampling frames, dates, locations, creators, permissions, and chains of custody. These practices matter before any human or automated coding begins.

### Measurement and validation across data types

Across these traditions, common questions recur: What is the construct? What is the unit? How was the material selected and produced? Which features can carry evidence about the construct? What is lost in transformation? What human or external evidence can test the measure? Which errors affect the final inference?

These traditions provide the benchmark for assessing multimodal foundation models. Stage 2 should identify the most appropriate foundational and current references rather than assuming that the three existing readings are sufficient.

## Provisional direction for the Stage 2 review

The literature review should test, rather than assume, the following direction:

- retain at least one strong current visual-measurement paper;
- add a foundational methodological anchor on visual or multimodal evidence;
- find credible work on speech/audio or audiovisual social measurement;
- investigate whether current multimodal-model evaluations test sociologically meaningful constructs or mainly technical benchmarks;
- distinguish combining modalities from converting every modality into text;
- identify a cumulative applied problem in which text, image, and audio offer overlapping but non-equivalent evidence;
- keep copyright, privacy, consent, provenance, and accessibility connected to the evidentiary design rather than placing them in a generic ethics slide.

## Stage 2 — Fresh literature review

### Search logic

The review tested four questions:

1. How did sociologists decide what photographs, video, recordings, and transcripts could count as evidence before multimodal foundation models?
2. What new operation does a multimodal model actually perform: direct measurement, description, transcription, representation, clustering, or fusion?
3. What human or external evidence is used to validate the resulting measure?
4. Which failures are shared across modalities and which arise from the production and representation of a particular medium?

Priority was given to peer-reviewed primary sources and official publisher versions. The review also considered access, length, and whether a paper gives students a concrete research design rather than a generic inventory of model capabilities.

## Candidate foundational and methodological readings

### Pauwels (2023), “Society in Sight”

**Source:** [International Review of Sociology](https://doi.org/10.1080/03906701.2023.2263256)

1. **Material:** A methodological history and synthesis of visual social science, illustrated with found, researcher-produced, and participant-produced images and visual essays.
2. **Question:** What distinguishes visual social science, how has it developed, and what modes of producing and analyzing visual evidence are available?
3. **Method:** Integrative methodological review with four applied vignettes.
4. **Finding or argument:** Images can be collected, produced, elicited, analyzed, and used to communicate research, but these modes create different relations among researcher, participant, representation, and claim. New technologies widen visual research without removing epistemological or institutional constraints.
5. **Teaching job:** Establish that “an image” is not a natural unit of evidence. Who made it, why, where it circulated, and how it entered the corpus precede automated analysis.

**Assessment:** Best concise sociological foundation located. Assign selected sections rather than an entire visual-methods book.

### Rose (2022/2023), *Visual Methodologies*, fifth edition

**Source:** [SAGE](https://uk.sagepub.com/en-gb/eur/visual-methodologies/book277282)

1. **Material:** Visual objects and practices across composition, semiology, discourse, audiences, digital circulation, and participatory production.
2. **Question:** How should researchers design critical visual-methods projects and relate images to the contexts and power relations through which they are produced and interpreted?
3. **Method:** Methods textbook synthesizing several traditions and worked examples.
4. **Finding or argument:** No single visual method exhausts an image's meaning; the site of production, the image itself, its circulation, and its audiences can all matter.
5. **Teaching job:** Supply precise vocabulary for explaining why a model's description of visible content is only one possible analytic operation.

**Assessment:** Excellent instructor resource and possible short excerpt, but assigning it alongside Pauwels would duplicate the foundational role.

### Becker (1995), “Visual Sociology, Documentary Photography, and Photojournalism”

**Source:** [Visual Sociology](https://doi.org/10.1080/14725869508583745)

1. **Material:** Photographs read across visual sociology, documentary photography, and photojournalism.
2. **Question:** Why does the same photographic object acquire different meaning in different worlds of production and use?
3. **Method:** Comparative conceptual analysis of photographic genres and their organizational histories.
4. **Finding or argument:** Visual meaning depends heavily on institutional, historical, and organizational context rather than residing wholly in the pixels.
5. **Teaching job:** Provide a short, memorable statement of the context problem that a vision-language description may suppress.

**Assessment:** Useful optional excerpt or lecture quotation; too narrow to serve as the only foundational reading.

### Davidson (2009), “Transcription: Imperatives for Qualitative Research”

**Source:** [International Journal of Qualitative Methods](https://doi.org/10.1177/160940690900800206)

1. **Material:** Three decades of methodological literature on converting recorded talk and interaction into transcripts.
2. **Question:** How is transcription understood, conducted, and reported, and why is it routinely underdescribed?
3. **Method:** Methodological review organized around definitions, practice, and reporting.
4. **Finding or argument:** Transcripts are selective, partial, theoretically informed representations. Different research purposes can require markedly different transcripts of the same recording, and transcription choices must be reported.
5. **Teaching job:** Prevent students from treating speech-to-text as lossless conversion. It supplies the human-method analogue for examining what automated transcription retains and removes.

**Assessment:** Strong in-class methodological evidence or a short required excerpt if the audio paper proves too technically dense.

## Candidate current visual and multimodal-model readings

### Law and Roberto (2025), “Generative Multimodal Models for Social Science”

**Source:** [Sociological Methods & Research](https://doi.org/10.1177/00491241251339673)

1. **Material:** 1,101 satellite and streetscape images from 367 sites associated with spatial and social division in U.S. cities.
2. **Question:** Can generative multimodal models identify built-environment features relevant to residential segregation, and how should social scientists organize large-scale image analysis?
3. **Method:** A framework covering curation, discovery, measurement, and inference; GPT-4o labels are compared with expert labels, with repeated model runs and reliability and validity checks.
4. **Finding:** For well-defined labels, GPT-4o performs reasonably well against experts, but recall is weaker than precision for some tasks and ambiguous labels remain difficult. Image collection, manual screening, repeated runs, human validation, bias, ethics, copyright, and reproducibility remain consequential.
5. **Teaching job:** Demonstrate a credible end-to-end social-science image-analysis workflow in which model capability is only one stage.

**Assessment:** Retain as a likely required reading, using selected sections. It is the clearest bridge from Weeks 1–2 to multimodal evidence.

### Arminio et al. (2026), “Leveraging VLLMs for Visual Clustering”

**Source:** [Social Science Computer Review](https://doi.org/10.1177/08944393251376703)

1. **Material:** 11,873 Instagram images concerned with climate-change communication.
2. **Question:** Does clustering VLLM-generated image descriptions improve connotative semantic validity and interpretability relative to CNN-based clustering?
3. **Method:** GPT-4-turbo produces connotative textual descriptions; text embeddings and CNN features generate competing clusters; expert coders evaluate denotative and connotative similarity; evaluators match cluster descriptions to image samples.
4. **Finding:** The VLLM pipeline produces stronger connotative clustering and readily interpretable cluster descriptions, while the CNN pipeline remains marginally stronger on denotative similarity. Cluster granularity remains a researcher decision.
5. **Teaching job:** Make the transformation from image to text visible and contestable. It shows both what an intermediate description enables and how it can privilege connotation over literal similarity.

**Assessment:** Strong in-class paper and possible required substitute for Law and Roberto if the session focuses on image-to-text conversion. Assigning both in full would make the week too visually dominant.

### Maranca et al. (2025), “Correcting the Measurement Errors of AI-Assisted Labeling in Image Analysis”

**Source:** [Sociological Methods & Research](https://doi.org/10.1177/00491241251333372)

1. **Material:** Applications concerning perceived violence in protest images, Black Lives Matter images on Twitter, and U.S. news images of immigrant caravans.
2. **Question:** How can researchers obtain valid downstream estimates when automated image labels contain error?
3. **Method:** Design-based supervised learning combines large quantities of automated labels with a smaller probability sample of expert annotations.
4. **Finding:** Even small labeling errors can bias estimates and invalidate confidence intervals; expert-labeled samples can correct downstream inference while retaining much of the efficiency of automation.
5. **Teaching job:** Carry Week 2's downstream-error lesson into images and show that “multimodal” does not create a new exemption from measurement-error correction.

**Assessment:** Use in class rather than assign. Its central statistical lesson overlaps deliberately with Week 2, and students need not reproduce DSL.

### Davidson (2026), “Multimodal Large Language Models Can Make Context-Sensitive Hate Speech Evaluations Aligned with Human Judgement”

**Source:** [Nature Human Behaviour](https://doi.org/10.1038/s41562-025-02360-w)

1. **Material:** Simulated social-media posts varying slurs, textual context, and visual demographic cues, together with judgments from 1,854 human participants.
2. **Question:** Can multimodal models apply a hate-speech policy contextually, and how do textual and visual identity cues affect their decisions?
3. **Method:** Conjoint experiments systematically vary post attributes and compare several models with human judgments.
4. **Finding:** Larger models often align closely with human judgments and respond to context, but demographic and lexical biases persist; prompts alter rather than eliminate context sensitivity, and some models react strongly to visual identity cues.
5. **Teaching job:** Provide a genuinely multimodal measurement design in which adding a visual cue changes a consequential classification. It also shows how factorial variation can diagnose which modality drives the output.

**Assessment:** Best current substantive in-class application. It may become required if accessible selected sections are available, but its paywall and proximity to the Week 2 annotation problem argue for using its design and figures in class.

### Greene et al. (2025), “Digital Divides in Scene Recognition”

**Source:** [Humanities and Social Sciences Communications](https://doi.org/10.1057/s41599-025-04719-w)

1. **Material:** Nearly one million user-submitted and Airbnb photographs of homes from more than 200 countries and all 3,320 U.S. counties, excluding images containing people.
2. **Question:** Do scene-recognition systems perform differently across socioeconomic contexts?
3. **Method:** Compare several CNNs, CLIP associations, and GPT-4V scene labels across socioeconomic conditions.
4. **Finding:** Lower-SES homes receive less accurate, less certain, and more potentially offensive classifications; the pattern persists in a multimodal foundation model.
5. **Teaching job:** Show that errors can be socially patterned even when no human face appears in the image. The bias can lie in how places and material environments are represented.

**Assessment:** Excellent optional empirical aside if the cumulative example concerns neighborhood conditions; do not add it merely as a generic bias slide.

## Candidate audio and audiovisual readings

### Mestre and Ryan (2026), “Potential and Pitfalls of Audio as Data for Political Research”

**Source:** [Political Analysis](https://doi.org/10.1017/pan.2025.10031)

1. **Material:** Forty-five televised U.S. presidential and vice-presidential debates from 1960–2020: 67.5 hours of recordings and 47,150 initially unaligned transcript sentences.
2. **Question:** How can social scientists align speech and text, represent auditory information, and avoid naive interpretation of audio-derived measures?
3. **Method:** Four progressive applications: forced audio–text alignment, low-level speech features such as pitch and energy, custom classifiers using MFCCs and embeddings, and off-the-shelf emotion recognition.
4. **Finding or contribution:** Transcripts omit consequential features of delivery, but different audio representations retain different information and introduce different burdens. Alignment, noise, language and accent variation, privacy, and interpretation all require explicit validation.
5. **Teaching job:** Give audio equal methodological standing and let students distinguish words spoken, how they were spoken, temporal alignment, and a model's emotion label.

**Assessment:** Add as a likely required reading, assigning the introduction, “alignment crisis,” feature table, and conclusion rather than every technical section.

### Knox and Lucas (2021), “A Dynamic Model of Speech for the Social Sciences”

**Source:** [American Political Science Review](https://doi.org/10.1017/S000305542000101X)

1. **Material:** Audio and transcripts from U.S. Supreme Court oral arguments.
2. **Question:** Can the dynamics of vocal tone reveal judicial skepticism and interactional sequences that transcript-only analysis misses?
3. **Method:** A semi-supervised statistical model represents many time-varying auditory features and latent modes of speech.
4. **Finding or argument:** Speech flow and vocal delivery contain information absent from words alone; collapsing utterances into a few average features also discards substantial temporal information.
5. **Teaching job:** Supply a strong pre-foundation-model example showing that the “same words” are not equivalent evidence when delivery and sequence matter.

**Assessment:** Use as a concise in-class predecessor to Mestre and Ryan. The full paper is too technically demanding for the assigned load.

### Koenecke et al. (2020), “Racial Disparities in Automated Speech Recognition”

**Source:** [Proceedings of the National Academy of Sciences](https://doi.org/10.1073/pnas.1915768117)

1. **Material:** 19.8 hours of sociolinguistic interviews with 42 white and 73 Black speakers from five U.S. cities, matched on age and gender.
2. **Question:** Do five commercial speech-recognition systems transcribe Black and white speakers equally accurately?
3. **Method:** Human transcripts provide reference evidence; word-error rates are compared across groups and identical phrases.
4. **Finding:** Average word-error rates were 0.35 for Black speakers and 0.19 for white speakers across the five systems, with disparities traced primarily to acoustic rather than lexical differences.
5. **Teaching job:** Demonstrate that converting audio into text can introduce socially patterned missingness and distortion before any later LLM analysis begins.

**Assessment:** Strong short in-class evidence. It should motivate a subgroup error check in the eventual example rather than become an isolated fairness aside.

### Reece et al. (2023), “The CANDOR Corpus”

**Source:** [Science Advances open-access version](https://pmc.ncbi.nlm.nih.gov/articles/PMC10065445/)

1. **Material:** 1,656 naturalistic video-chat conversations: more than seven million words and 850 hours of audio, video, transcripts, vocal and facial measures, and post-conversation surveys.
2. **Question:** How can a large public multimodal corpus support the scientific study of conversation, including the question of what distinguishes a good conversationalist?
3. **Method:** Synchronized recording, automated and human processing, turn segmentation, multimodal feature extraction, surveys, and qualitative review.
4. **Finding or contribution:** Multiple levels of representation enable different questions, but results depend on segmentation and alignment choices. Raw media, processed media, transcripts, derived features, and participant judgments are not interchangeable evidence.
5. **Teaching job:** Show what a genuine multimodal research record looks like and why consent, identifiability, synchronization, units, and transformations must be documented.

**Assessment:** Use briefly in class as a data-architecture example. Sustained analysis of conversational interaction belongs in Week 6.

### “Careless Whisper” (Koenecke et al., 2024)

**Source:** [ACM FAccT](https://doi.org/10.1145/3630106.3658996)

1. **Material:** Speech segments used to examine unsupported text generated by Whisper, including comparison between speakers with aphasia and a control group.
2. **Question:** When does speech-to-text generate words without support in the audio, and who is more exposed to that failure?
3. **Method:** Human identification and categorization of transcription hallucinations with group comparisons.
4. **Finding:** Whisper can insert unsupported and potentially harmful material, with unequal hallucination rates for speakers with aphasia.
5. **Teaching job:** Show that an apparently fluent transcript may contain fabricated evidence, not merely omitted acoustic information.

**Assessment:** Optional extension. Koenecke et al. (2020) is simpler for the core class; this paper is useful if the cumulative example includes an invented phrase.

## Cross-cutting findings from the review

### Technical access does not create evidentiary equivalence

A single model interface may accept text, images, and audio, but the input modes enter through different encoders, transformations, sampling processes, and loss mechanisms. “The model processed all three” is a capability statement, not a validation argument.

### Conversion is itself a measurement operation

Image-to-text description, speech-to-text transcription, audio embeddings, and visual clustering do not simply standardize source material. Each selects and constructs features. Arminio et al. deliberately prioritize connotative over denotative similarity; Davidson shows that transcripts are selective; Mestre and Ryan distinguish several non-equivalent audio representations.

### The unit of analysis is modality-dependent

An image, image region, social-media post, utterance, 25-millisecond audio window, conversational turn, and full video are different units. A common row in a Python list does not resolve the choice. Alignment errors can connect the wrong words, speaker, image, or moment.

### Validation evidence must match the claim

Human image labels can test object or construct coding; pair judgments can test cluster meaning; human transcripts can test ASR; participant surveys may test perceived conversational quality; downstream corrections can address estimate bias. None is a universal gold standard.

### Error can be socially patterned before the focal LLM call

Image sampling, camera position, platform circulation, offensive scene categories, transcription, language, accent, disability, and source availability can all create patterned error. Model output evaluation must therefore include the provenance and transformation chain.

### Richer input may increase both information and exposure

Images of people and voices are more readily identifiable than many text records. Law and Roberto could distribute code but not their copyrighted street imagery. CANDOR required explicit consent acknowledging identification risk. Mestre and Ryan note that cloud transcription can transfer protected audio to third-party servers. FHIBE is important precisely because its human images were consensually collected rather than repurposed from scraped benchmarks.

## Initial reading architecture before the sensory-experience extension

### Required readings

1. **Pauwels (2023), selected sections.** Establishes the sociological history and the difference among found, researcher-produced, and participant-produced visual evidence.
2. **Law and Roberto (2025), selected framework, application, validation, and conclusion sections.** Shows a complete generative-multimodal image-analysis workflow and its research-design obligations.
3. **Mestre and Ryan (2026), introduction, alignment section, feature table, and conclusion.** Gives audio equal methodological status and explains why a transcript, acoustic feature, embedding, and emotion label are different representations.

This is approximately comparable to the previous weekly load if sections are assigned rather than complete papers.

### In-class evidence

- **Arminio et al. (2026):** image-to-text conversion and the denotation/connotation trade-off.
- **Maranca et al. (2025):** image-label error carried into downstream estimates.
- **Davidson (2026):** factorial variation of textual and visual context in a consequential classification task.
- **Koenecke et al. (2020):** socially patterned speech-to-text error.
- **Davidson (2009):** a transcript as a selective analytic representation.
- **Reece et al. (2023):** raw, processed, and derived modalities in one research corpus.

### Optional or instructor-only material

- Rose, *Visual Methodologies*, for deeper visual-methods framing.
- Becker (1995) for institutional context and photographic meaning.
- Knox and Lucas (2021) for dynamic speech modeling.
- Greene et al. (2025) for socioeconomic scene-recognition bias.
- Koenecke et al. (2024), “Careless Whisper,” for unsupported transcription content.
- FHIBE (2025) for consent-based human-image benchmarking and intersectional evaluation.

## Why the original required list should change

The original list contains three strong papers, but all three are visual-computational. Retaining Law and Roberto while moving Maranca and Arminio into the lecture produces a more balanced assigned load. Pauwels establishes what visual evidence meant before generative models; Mestre and Ryan supplies the missing audio method; the two visual papers remain available exactly where their empirical designs clarify the class example.

The proposed list does not require a generic survey of multimodal-model architectures. The technical fact that models accept several media types can be explained directly. Scarce reading time should instead be spent on how source material becomes evidence and how that process is validated.

## Questions left for Stage 3 synthesis

The literature supports the direction but does not yet settle the cumulative example. The synthesis should compare a small number of candidate designs against four tests:

1. Can the same sociological construct plausibly be assessed from connected text, image, and audio records?
2. Does each modality add genuinely different information rather than serving as decorative duplication?
3. Can students inspect the raw or responsibly adapted source material without copyright, privacy, or accessibility problems?
4. Can the Python remain basic while representing alignment, modality-specific evidence, human checks, and non-equivalent missingness?

No slides, workbook, task, syllabus, or reading guide have been revised during Stages 1–2.

## Stage 2 extension — sensory experience, social worlds, and world models

The initial review still began too late in the representational chain. It asked what an image, recording, or transcript can support, but not what kind of human experience became available to be recorded in the first place. Recent work on AI “world models” makes that omission especially useful to address. These models invite an explicit comparison between a learned predictive representation of selected signals and the embodied, intersubjective, culturally organized worlds studied by social scientists.

The extension therefore adds a prior question:

> What part of a lived social situation can enter a record, what part survives its conversion into data, and what part is represented by a model?

The conceptual chain for the session should become:

**lived social situation → selected sensory trace → research representation → model representation → measurement claim**

Each arrow is a consequential research operation. A camera frames; a microphone samples; a transcript selects; an annotation imposes a category; an embedding preserves some relations and suppresses others; a model output turns those representations into a proposed claim.

## Classical and contemporary social-science anchors

### Simmel (1908/1997), “Sociology of the Senses”

**Source:** *Simmel on Culture: Selected Writings*, edited by David Frisby and Mike Featherstone (SAGE), pp. 109–120. A public historical version is available as [“Sociology of the Senses: Visual Interaction”](https://cuny.manifoldapp.org/read/georg-simmel-some-collected-works/section/8895b310-16c0-4ef8-8b27-de3e4988526d).

1. **Question:** How do seeing, hearing, bodily presence, and reciprocal perception help constitute social relations?
2. **Argument:** Sensory contact is not merely information delivered to otherwise complete individuals. Different senses organize different forms of proximity, reciprocity, recognition, and knowledge of others.
3. **Teaching job:** Establish that the senses are socially consequential before they are data modalities. A model may receive pixels and waveforms without occupying the reciprocal relation Simmel is describing.
4. **Caution:** The essay contains historically specific assumptions and sensory hierarchies. It should be read as a generative early question, not as a complete or timeless account of sensory life.

**Assessment:** Best short classic for the required reading. It gives the week a recognizably sociological starting point without returning to Blumer.

### Mead (1934), *Mind, Self, and Society*

**Source:** [University of Chicago Press definitive edition](https://press.uchicago.edu/ucp/books/book/chicago/M/bo20099389.html); a public version of the relevant discussion is [“Social Attitudes and the Physical World”](https://www.d.umn.edu/cla/faculty/jhamlin/4111/Blumer/George%20Herbert%20Mead%20-%20Mind%2C%20Self%2C%20and%20Society.htm).

1. **Question:** How do mind, meaning, and self emerge within organized social acts?
2. **Argument:** Meaning is not simply a property stored inside a sign or an isolated organism; it arises through conduct involving others and the environment.
3. **Teaching job:** Complicate the idea that adding more sensory channels necessarily supplies social meaning. A representation of an object is not yet participation in the social act through which it matters.

**Assessment:** Use as an instructor-led classic connection rather than an additional required reading. It makes the grounding question sociological, but a short extract would require substantial setup.

### Schutz (1932/1967), *The Phenomenology of the Social World*

**Source:** [Northwestern University Press](https://nupress.northwestern.edu/9780810103900/phenomenology-of-the-social-world/)

1. **Question:** How do actors inhabit an intersubjective world of everyday experience and interpret the actions and intended meanings of others?
2. **Argument:** The social world is already meaningful to its participants. Social-scientific constructs are therefore representations of actors' interpretations, not direct copies of an objective world.
3. **Teaching job:** Distinguish a computational “world model” from the social-scientific lifeworld. Predicting likely observable states is not identical to grasping intended meaning or actors' stocks of knowledge.

**Assessment:** Important framing for the lecture, but too abstract for the core assigned load in this methods course.

### Goodwin (2017), *Co-Operative Action*

**Source:** [Cambridge University Press](https://www.cambridge.org/core/books/co-operative-action/409E1455713D43131F04C3F6B6815FF7); see the summary of [Part III, “Embodied Interaction”](https://www.cambridge.org/core/books/abs/cooperative-action/embodied-interaction/84C25ACD00D6C4ECA73EA2E4250A6EB4).

1. **Material:** Video-based studies of talk, bodies, tools, graphic fields, and historically shaped material settings.
2. **Argument:** Human action is not lodged in one modality. Participants assemble temporally unfolding action from interdependent semiotic resources, each of which makes a distinct contribution.
3. **Teaching job:** Provide the strongest empirical bridge to multimodal evidence. Text, gaze, gesture, objects, and the material surround cannot simply be converted into independent features and added together.

**Assessment:** Use a concrete episode and paper image in class. This is more teachable than making phenomenology carry the whole argument and should inform the eventual worked example.

### Vannini, Waskul, and Gottschalk (2012), *The Senses in Self, Society, and Culture*

**Source:** [Routledge](https://www.routledge.com/The-Senses-in-Self-Society-and-Culture-A-Sociology-of-the-Senses/Vannini-Waskul-Gottschalk/p/book/9780415731041)

1. **Material:** A synthesis of classical and contemporary sensory sociology organized around bodies, rituals, identity, place, time, sensory orders, media, and material culture.
2. **Argument:** Sensory experience is bodily and material but also culturally classified, socially trained, unequally valued, and organized through collective practices.
3. **Teaching job:** Broaden the inventory beyond sight and hearing. Smell, taste, touch, temperature, pain, proprioception, and bodily affect may matter socially even when they are absent from the week's files and current model interfaces.

**Assessment:** Best instructor reference for mapping the tradition. A selected introductory chapter could substitute for Simmel if the original proves inaccessible, but assigning both would duplicate their teaching role.

### Pink (2015), *Doing Sensory Ethnography*, second edition

**Source:** [SAGE](https://uk.sagepub.com/en-gb/hkg/doing-sensory-ethnography/book242776)

1. **Material:** Multisensory ethnographic research into embodied experience, practice, place, and digital life.
2. **Argument:** The senses are interconnected, and knowledge is produced through the researcher's situated and emplaced participation rather than extracted intact from a sensory channel.
3. **Teaching job:** Make the methodological problem concrete: a recording can support analysis, but it does not reproduce the bodily and relational conditions in which the encounter occurred.

**Assessment:** Optional or instructor-led. It is particularly useful if the cumulative example uses a field encounter rather than platform media.

## Grounding and world-model research

### Harnad (1990), “The Symbol Grounding Problem”

**Source:** [*Physica D*](https://doi.org/10.1016/0167-2789(90)90087-6)

1. **Question:** How can symbols acquire meaning for a system rather than depend indefinitely on other symbols and meanings supplied by people?
2. **Argument:** Pure symbol-to-symbol relations are insufficient; Harnad proposes grounding symbolic representations in nonsymbolic iconic and categorical representations tied to sensory projections.
3. **Teaching job:** Supply the intellectual precursor to current claims that multimodality or embodiment “grounds” AI.

**Assessment:** Instructor background. The core question is useful, but the cognitive-science machinery need not become a fourth technical reading.

### Bender and Koller (2020), “Climbing towards NLU”

**Source:** [ACL Anthology](https://aclanthology.org/2020.acl-main.463/)

1. **Question:** Can a system trained only on linguistic form learn linguistic meaning?
2. **Argument:** Text prediction can learn relations among forms, but communicative meaning concerns relations between forms and communicative intentions. Task performance should not be casually reported as human-like understanding.
3. **Teaching job:** Give students a clear language-only baseline against which multimodal and world-model claims can be assessed.

**Assessment:** Useful short counterpoint in class; Week 4 should not become a general debate about whether models understand language.

### Bisk et al. (2020), “Experience Grounds Language”

**Source:** [ACL Anthology](https://aclanthology.org/2020.emnlp-main.703/)

1. **Question:** What kinds of physical and social experience are missing when language research relies on text alone?
2. **Method or contribution:** A conceptual framework organizes increasingly demanding forms of grounding, from text and pixels through perception, embodiment, action, and social interaction.
3. **Argument:** Successful communication relies on shared experience of physical and social worlds; adding images is only an early step toward that broader problem.
4. **Teaching job:** Provide a direct bridge from Simmel's sociological question to current AI research and help students compare “more modalities” with “more experience.”

**Assessment:** Assign selected framework pages alongside Simmel as one short paired reading block.

### Ha and Schmidhuber (2018), “World Models”

**Source:** [arXiv](https://arxiv.org/abs/1803.10122); the authors also provide an [interactive article](https://worldmodels.github.io/).

1. **Material:** Reinforcement-learning environments represented through a compressed visual model and a learned model of temporal dynamics.
2. **Question:** Can an agent learn a compact predictive representation of its environment and use simulated futures to choose actions?
3. **Finding or contribution:** Policies trained partly inside a learned simulation can transfer back to the task environment.
4. **Teaching job:** Introduce “world model” in a precise and accessible sense: a useful compressed model for prediction and action, not a complete duplicate of the world and not evidence of lived experience.

**Assessment:** Use the interactive diagram in the lecture, not as a required technical paper.

### Girdhar et al. (2023), “ImageBind”

**Source:** [official Meta AI overview](https://ai.meta.com/blog/imagebind-six-modalities-binding-ai/)

1. **Material:** Images, text, audio, depth, thermal data, and inertial measurements mapped into one shared representation space.
2. **Question:** Can several sensory and sensor modalities be aligned without obtaining training data for every possible pair?
3. **Finding or contribution:** Natural pairings with images can align six modalities and support cross-modal retrieval and recognition.
4. **Teaching job:** Give students a concrete example of a common representation while making the central warning explicit: proximity in an embedding space is not equivalence of evidence and is not the same as a human having a unified sensory experience.

**Assessment:** Best technical visual for explaining shared multimodal representations. Use a figure and a small conceptual exercise rather than assigning the full paper.

### Assran et al. (2025), “V-JEPA 2”

**Source:** [official research paper page](https://ai.meta.com/research/publications/v-jepa-2-self-supervised-video-models-enable-understanding-prediction-and-planning/)

1. **Material:** More than one million hours of internet video followed by less than 62 hours of robot video for action-conditioned post-training.
2. **Question:** Can a video model learn representations useful for understanding motion, predicting future states, and planning robot actions in unfamiliar environments?
3. **Finding or contribution:** The learned latent predictor performs strongly on video tasks and supports zero-shot reaching, grasping, and pick-and-place planning with image goals.
4. **Teaching job:** Represent the current frontier and sharpen the sociological question: physical prediction and control are significant achievements, but what would count as a model of a *social* world?

**Assessment:** Current in-class endpoint. It should prompt comparison, not a detailed architecture lesson.

### Gurnee and Tegmark (2024), “Language Models Represent Space and Time”

**Source:** [ICLR paper](https://openreview.net/pdf/c50ebbefe4d77434016a143c31d247f30948dd6c.pdf)

1. **Material:** Internal representations in Llama-2 models tested with places, historical figures, artworks, and news headlines.
2. **Question:** Do text-trained models develop coherent internal representations of spatial and temporal relations?
3. **Finding:** The authors identify robust linear representations of space and time across scales and entity types.
4. **Teaching job:** Prevent an overly simple “text models know nothing about the world” conclusion. Models can recover real structure from patterned language, while the class can still ask which aspects of social experience those representations support.

**Assessment:** Optional nuance. It is useful for keeping the comparison empirical rather than settling it by definition.

## What the comparison adds to Week 4

### A “world” is not just a larger list of modalities

Current systems can align additional sensor streams and learn regularities that support prediction. The social-science traditions above draw attention to phenomena that may not be present in those streams at all: first-person sensation, pain, fatigue, memory, attention, practical familiarity, reciprocal awareness, intended meaning, moral evaluation, cultural classification, institutional position, and history.

This does not establish that models can never represent such phenomena. It establishes the research-design question: **what observation or trace would warrant the claim that they do?**

### Human experience and research evidence should not be collapsed

Social scientists never have unmediated access to another person's whole experience. Interviews, observations, photographs, recordings, fieldnotes, and administrative records are already selective representations. The important contrast is therefore not “whole human truth versus useless machine data.” It is between different situated ways of producing evidence, each with different access, losses, and validation possibilities.

### Prediction is an achievement but not the only social-science criterion

A world model may be good if it predicts a future video state or supports a successful action. Social scientists may also ask whether an account reconstructs actors' meanings, identifies a mechanism, distinguishes social positions, explains historical change, or describes an experience adequately. Week 4 should make those criteria visible before asking a model to classify a record.

### Multimodality can still exclude much of the sensorium

The files in a typical LLM workflow privilege text, sight, and recorded sound. Touch, smell, taste, temperature, bodily strain, proprioception, and interoception are usually absent or indirectly represented. Even within image and audio, camera placement, microphone range, platform compression, segmentation, and transcription govern what survives.

## Revised reading architecture for Review Gate 1

### Required readings

1. **Experience and grounding packet:** Simmel (1908/1997), “Sociology of the Senses,” plus selected framework pages from Bisk et al. (2020), “Experience Grounds Language.” The pair asks what sensory contact does in social relations and what AI researchers mean when they say language needs grounding.
2. **Law and Roberto (2025), selected framework, application, validation, and conclusion sections.** A concrete end-to-end example of turning visual records into a social-science measure.
3. **Mestre and Ryan (2026), introduction, alignment section, feature table, and conclusion.** A concrete account of how words, delivery, timing, acoustic features, and model outputs become different audio representations.

The paired opening replaces Pauwels in the required list rather than increasing the weekly load. Pauwels remains important in-class methodological context. Readings should be distributed as selected extracts so the total remains broadly comparable with other weeks.

### Principal in-class sequence

1. **Simmel, Mead, and Schutz:** seeing, hearing, meaning, social acts, and the intersubjective lifeworld.
2. **Goodwin, Pink, and Pauwels:** how researchers study embodied situations and produce partial visual, audio, textual, and fieldnote records.
3. **Davidson on transcription:** how one record becomes another and what disappears.
4. **ImageBind:** how several sensor modalities can occupy a shared learned representation.
5. **World Models and V-JEPA 2:** how compressed representations support prediction and action.
6. **Law and Roberto plus Mestre and Ryan:** what these transformations permit social scientists to measure and how the resulting claims can be checked.

The transition question should be stated in ordinary language:

> A model can learn enough regularity to predict what happens next. Is that the same as having a world? What else would a social scientist want to know about the situation?

### Implication for Stage 3

The eventual worked example should begin with one short, inspectable social situation rather than three unrelated modality labels. Students should compare at least an image or video frame, a short audio segment, a transcript, and a fieldnote or participant account. The Python should help them record what each representation contains and omits. It should not imply that code recreates sensory experience or resolves the interpretation.

No downstream course artifact was revised during that extension.

## Stage 2 second extension — observing action in violent and violence-threatening situations

Instructor review rejected the bus-stop and public-hearing teaching examples because the social process did not arise clearly enough from the focal sociological literature. A targeted review identified a stronger center: the micro-sociology of violence and the methodological tradition of reconstructing situations from video, audio, photographs, field observation, interviews, and documentary evidence.

The same review also clarified that Collins must not appear as the origin of sociological observation. The class should first locate his argument within a broader lineage concerned with sensory reciprocity, social acts, co-presence, sequence, fieldnotes, and professionally organized vision.

### Goffman (1983), “The Interaction Order”

**Source:** [*American Sociological Review*](https://doi.org/10.2307/2095141)

1. **Material:** The 1982 ASA presidential address synthesizing face-to-face encounters, co-presence, bodily displays, talk, mutual monitoring, and the relation between interaction and wider social organization.
2. **Question:** What distinctive social order is produced when people are physically co-present and mutually available to one another?
3. **Argument:** The organization of encounters is a substantive sociological domain. Glances, gestures, bodily position, accessibility, boundaries, and spoken exchange are not residual details beneath structure.
4. **Teaching job:** Give students a general vocabulary for observing the confrontation before the class specializes in violence.

**Assessment:** Use a short excerpt or lecture framing. Assigning the full address alongside Collins and video methodology would overload the week.

### Sacks, Schegloff, and Jefferson (1974), “A Simplest Systematics for the Organization of Turn-Taking for Conversation”

**Source:** [*Language*](https://doi.org/10.2307/412243)

1. **Material:** Naturally occurring conversation examined through detailed transcription.
2. **Question:** How is turn-taking organized as a locally managed, party-administered, interactionally controlled system?
3. **Argument:** Talk is sequentially organized and sensitive to recipients. Timing, overlap, response, and position within a sequence are constitutive features rather than removable noise.
4. **Teaching job:** Establish the general reason for preserving ordered moments and aligned audio before the Python loop appears.

**Assessment:** Teach through a very small transcript fragment; do not assign the full technical paper.

### Emerson, Fretz, and Shaw (2011), *Writing Ethnographic Fieldnotes*, second edition

**Source:** [University of Chicago Press](https://press.uchicago.edu/ucp/books/book/chicago/W/bo12182616.html)

1. **Material:** Worked examples of participation, observation, jottings, scenes, dialogue, movement, and the production and revision of fieldnotes.
2. **Question:** How does an ethnographer's embodied participation and selective noticing become an accumulating written research record?
3. **Argument:** Fieldnotes do not reproduce experience from memory. Researchers learn to notice, select, describe, and write scenes through practical and theoretical choices.
4. **Teaching job:** Prevent “human observation” from becoming an unexamined gold standard against which machine representation is judged.

**Assessment:** Instructor-led example or short optional excerpt.

### Goodwin (1994), “Professional Vision”

**Source:** [*American Anthropologist*](https://doi.org/10.1525/aa.1994.96.3.02a00100)

1. **Material:** Video and discourse from archaeological fieldwork and legal argument concerning the Rodney King videotape.
2. **Question:** How do professional communities create and contest the objects of knowledge that organize their work?
3. **Method:** Close analysis of coding schemes, highlighting practices, graphic representations, talk, and visual evidence.
4. **Argument:** Seeing is socially organized. Coding and highlighting transform a complex perceptual field into professionally relevant events, with consequences for expertise and power.
5. **Teaching job:** Provide the decisive bridge between classic observational sociology and AI-assisted visual coding. Human observers also use learned categories, but those categories and practices can be studied and contested.

**Assessment:** Strong candidate for the short required observation packet alongside Simmel. It is more directly connected to violence, representation, and coding than a general sensory-methods excerpt.

### Collins (2008), *Violence: A Micro-sociological Theory*

**Source:** [Princeton University Press/JSTOR](https://www.jstor.org/stable/j.ctt4cg9d3); [publisher chapter preview](https://assets.press.princeton.edu/chapters/s8547.pdf)

1. **Material:** Heterogeneous evidence including photographs, video, ethnography, interviews, forensic reconstruction, and detailed accounts of violent and violence-threatening encounters.
2. **Question:** Why is face-to-face violence relatively difficult, and which situational pathways allow actors to overcome the barrier created by confrontational tension and fear?
3. **Method:** Comparative micro-sociological reconstruction of sequences and interactional configurations across several forms of violence.
4. **Argument:** Motivations, grievances, and violent dispositions do not translate automatically into violent action. Many confrontations stall or remain incompetent; violence becomes possible through situational patterns such as attacking a weak victim, audience support, sudden dominance, or forward panic.
5. **Teaching job:** Supply the central substantive theory. It requires students to observe temporal, embodied situations rather than infer violent character from a person, group, or final frame.

**Assessment:** Use selected introductory material and the concise 2013 article below rather than assigning the entire book.

### Collins (2013), “Entering and Leaving the Tunnel of Violence”

**Source:** [*Current Sociology*](https://doi.org/10.1177/0011392112456500)

1. **Material:** Close ethnographic observations, photographs, videos, and interviews concerning violence-threatening and violent situations.
2. **Question:** How do participants enter, remain within, and leave an altered interactional and perceptual state during violence?
3. **Method:** Micro-sociological theoretical synthesis grounded in fine-grained situational evidence.
4. **Argument:** Confrontational tension and fear commonly inhibit violence. When situational pathways overcome that barrier, violent action remains embodied, temporally compressed, perceptually distorted, and frequently uncontrolled.
5. **Teaching job:** Give graduate students an assignable statement of the theory and connect sensory experience directly to the visual and audio evidence problem.

**Assessment:** Strongest required Collins reading for the available load.

### Nassauer (2019), *Situational Breakdowns*

**Source:** [Oxford University Press](https://academic.oup.com/book/34941)

1. **Material:** Protest marches and uprisings that end peacefully or violently in Germany and the United States, together with robbery cases; evidence includes video, photographs, text, interviews, and documentary material.
2. **Question:** Why do routine interactions sometimes break down into surprising outcomes such as protest violence while apparently threatening situations often remain peaceful?
3. **Method:** Fine-grained comparison of unfolding situations, interactional combinations, background conditions, and contrasting outcomes.
4. **Argument:** Situational sequences can redirect motivations and strategies. Spatial struggles, communication problems, threat, uncertainty, police management, and shifting control combine differently in escalation and non-escalation.
5. **Teaching job:** Provide comparison cases and prevent the Collins example from becoming a post hoc reading of one dramatic episode.

**Assessment:** Use selected empirical sequences and figures in class. The book is too long to add in full.

### Nassauer and Legewie (2021), “Video Data Analysis”

**Source:** [*Sociological Methods & Research* bibliographic record](https://www.fachportal-paedagogik.de/literatur/vollanzeige.html?FId=eric_ej1282093), DOI [10.1177/0049124118769093](https://doi.org/10.1177/0049124118769093)

1. **Material:** A methodological synthesis of found and researcher-generated video studies across sociology and neighboring social sciences.
2. **Question:** How can researchers use proliferating recordings of naturally occurring situations as systematic social-science evidence?
3. **Method or contribution:** A framework covering research questions, sampling, collection, preparation, segmentation, coding, analysis, interpretation, validation, and ethics.
4. **Argument:** Video permits repeated and fine-grained observation of temporal, embodied action, but it remains positioned, selected, incomplete, and theory-laden. It must be analyzed through a transparent design.
5. **Teaching job:** Supply the established human-method process that the Python evidence sequence and model outputs must map onto.

**Assessment:** Required selected sections. It is the clearest methodological anchor for the new cumulative example.

### Legewie, Nassauer, and Kühne (2026), “Sampling in Video-Based Social Sciences”

**Source:** [*Sociological Methods & Research*](https://doi.org/10.1177/00491241261426862)

1. **Material:** Review of sampling and generalizability in 52 inference-oriented video studies, with three applied sampling scenarios.
2. **Question:** What sampling designs are needed when video analysis moves from close reconstruction toward large-N and computational inference?
3. **Method or contribution:** A sampling decision framework adapted to the availability, selection, heterogeneity, and technical infrastructure of contemporary video corpora.
4. **Argument:** More recordings and more powerful computer-vision tools do not solve selection. Violent and newsworthy episodes, available angles, platform circulation, missing lead-up, and non-recorded peaceful situations can distort the population of observed situations.
5. **Teaching job:** Connect Collins and qualitative video reconstruction to the 2026 computational frontier and the course's recurring distinction between an observed case and a population claim.

**Assessment:** Use its decision tree or central sampling problem in class. It need not add another full required paper.

## Revised reading architecture after the situational turn

### Required readings

1. **Collins (2013), “Entering and Leaving the Tunnel of Violence,” selected in full or with a short extract from the 2008 book introduction.** Establishes the substantive theory and the importance of bodily, emotional, and sensory dynamics.
2. **Nassauer and Legewie (2021), selected framework sections.** Establishes how social scientists construct video evidence, temporal units, comparisons, and validity claims.
3. **Short sociological-observation packet:** Simmel's “Sociology of the Senses” plus a selected concrete section from Goodwin (1994) or Goodwin (2017). Connects sensory reciprocity, professional vision, coding, and embodied multimodal action.

This configuration preserves the approximate reading load by moving Law and Roberto and Mestre and Ryan from full required selections into concentrated in-class evidence. The course chapter supplies the broader multimodal-model background.

### Principal in-class evidence

- **Nassauer (2019):** paired escalation and non-escalation sequences.
- **Legewie, Nassauer, and Kühne (2026):** why available violent footage is not a sample of confrontations.
- **Goodwin (2017):** action assembled through temporally coordinated talk, bodies, and environment.
- **Mead, Goffman, conversation analysis, and Emerson, Fretz, and Shaw:** the broader lineage of social acts, interaction order, sequence, and fieldnote production.
- **Bisk et al. (2020):** the technical grounding ladder from text and pixels toward embodiment, action, and social interaction.
- **Law and Roberto (2025):** curation, measurement, repeated model output, and validation for images.
- **Mestre and Ryan (2026):** transcript, alignment, acoustic features, and embeddings as different representations of audio.
- **ImageBind (2023):** shared representation across sensor modalities.
- **V-JEPA 2 (2025):** prediction and planning from video representations.

### Revised synthesis implication

The cumulative example should be a non-graphic, instructor-authored protest confrontation with a common setup and paired escalation/de-escalation endings. Students reconstruct ordered action from several records, compare human and model observations, and identify the evidentiary gap between next-state prediction and a Collins-inspired situational explanation.

This second extension and cumulative example were approved in instructor discussion on August 21, 2026. Stage 3 synthesis has been revised accordingly.
