# Session 5 literature review — Stage 1 audit and orientation

**Status:** Local-material audit and fresh literature review completed on 2026-08-21. The proposed reading architecture and cumulative study are ready for Review Gate 1; synthesis and slide architecture have not yet begun.

## Proposed session question

> Can generated media isolate a causal construct?

Session 5 begins the **Intervene** part of the course. Sessions 1–4 asked how model outputs and social records become evidence. This session changes the researcher's role: students now consider using generated material to create the exposure whose effect they want to estimate.

The initial methodological problem is therefore not simply whether a model can produce a plausible profile, image, or message. It is whether the resulting treatment conditions differ in the intended construct while avoiding unintended differences that supply rival explanations.

## Current artifact audit

| Artifact | Current state | Main issue |
|---|---|---|
| `syllabus/session05.md` | Names information equivalence, LinkedOut, LLM-generated persuasion, and a factorial construction task. | The basic direction is promising, but the substantive study, treatment, outcome, and validation evidence remain unspecified. |
| `readings/session05_reading_guide.md` | Lists three required readings in a generic comparison table. | The entries do not explain the material, design, result, disagreement, or distinct teaching job of any paper. |
| `instructor/session05_notes.md` | Provides a 165-minute generic scaffold and beginner-code reminders. | It does not specify the lecture's historical starting point, cumulative example, paper evidence, class activities, or actual sequence of design decisions. |
| `slides/session05/session05.qmd` | Fourteen-slide release scaffold. | It contains no established experimental-methods lineage, no worked study, no stimulus examples, no paper images, no empirical results, and no clear route through the class. Several labels remain placeholders: “methodological opportunity” and “validation or counterclaim.” |
| `workbook/session05/session05_treatment_generation.ipynb` | Executed beginner notebook with a nested-loop trace and oral rehearsal. | The Python explanation is stronger than the research design. It combines condition labels and filters on word count, but does not contain generated media, intended-construct ratings, nuisance measures, revision, provenance, or a treatment text/image students can inspect. |
| `assessments/weekly_coding/session05_task.py` | One-function completion task. | The task can be completed without understanding stimulus generation or information equivalence. “Fidelity” is reduced to a maximum word-count rule. |
| `solutions/weekly_coding/session05_solution.py` | Correct small factorial-record constructor. | It records only frame, tone, and word count; it cannot reveal whether a treatment expresses the intended construct or introduces a confound. |
| `tests/test_session05_solution.py` | One smoke test calling `run_checks()`. | It does not test the factorial combinations, boundary condition, input preservation, rejection reasons, or a substantive fidelity failure. |
| Data and visual assets | None specific to Session 5. | The class has no inspectable treatment corpus, human ratings, cached generation record, paper screenshot, or provenance statement. |

## What is worth retaining

1. **The broad question is right.** The session should ask whether generated stimuli isolate the construct the researcher intends to manipulate.
2. **Information equivalence is an appropriate methodological anchor.** It gives precise language for intended information, unintended information, and rival interpretations of a treatment contrast.
3. **A real applied experiment should remain central.** The current LinkedOut paper is a strong candidate because generated profile images are part of an actual discrimination/network experiment rather than a hypothetical capability demonstration.
4. **Persuasive-message generation is relevant but needs a defined job.** Bai et al. may supply a second treatment type, a result about message generation, or a comparison between researcher selection and direct model output. It should not become a disconnected second example.
5. **The beginner Python mechanics are usable.** Dictionaries, lists, nested loops, f-strings, conditionals, `.append()`, functions, and assertions can support an experimental-design task if the objects represent meaningful treatment evidence.
6. **Required work should remain cached and local.** Live generation can be an optional demonstration; completion must not depend on model access or credits.

## What failed in the current design

### 1. It begins with generated-media capability rather than experimental practice

Students are not first shown how sociologists and political methodologists designed survey experiments, audit studies, factorial vignettes, stimulus pretests, manipulation checks, or treatment validation before generative AI. Without that foundation, “fidelity” appears to be a new AI problem rather than a familiar causal-design problem intensified by scalable generation.

### 2. The readings have no distinct teaching jobs

The deck says that the papers “make the methodological burden visible” and “disagree about success,” but it never states the designs, materials, outcomes, or actual disagreement. The reading guide asks the same generic questions of every paper. Students cannot tell why one paper follows another.

### 3. There is no cumulative study

Profile images, policy messages, factorial frames, tones, and word counts appear beside one another without a single research question linking them. The code looks like a general combinatorics exercise rather than part of a study whose causal claim matters.

### 4. The code does not perform the method named by the session

`construct_treatments` builds four condition records and excludes one long variant. Word count is a possible nuisance feature, but it is not a construct-fidelity assessment. The function has no treatment content, intended-construct score, nuisance dimensions, rater evidence, rejection reason, revision history, model record, or comparison with a human-designed stimulus.

### 5. Correct randomization and valid treatment content are conflated

The current materials mention that labels can be randomized correctly while tone or length changes, but never separate:

- constructing the treatment set;
- validating what differs across conditions;
- assigning treatments to units; and
- estimating an outcome contrast.

A clean randomization procedure cannot repair a bundled or ambiguous treatment.

### 6. The deck is a scaffold rather than a lecture

Fourteen slides cannot sustain the 165-minute session. There is no roadmap, historical setup, worked treatment comparison, paper evidence, student judgment exercise, generation/revision loop, or explicit transition into Python. Titles such as “The characteristic failure is substantive” and “One small algorithm makes the design inspectable” repeat the compressed phrasing rejected in prior weeks.

### 7. Formal execution masks pedagogical thinness

The notebook executes and the smoke test passes, but those checks establish only that a small algorithm returns expected labels. This repeats the Session 4 lesson: formal correctness can coexist with an unclear research argument and an under-specified lecture.

## Starting methodological lineage for the fresh review

The literature review should begin before generative AI and determine which pieces are necessary for this audience:

1. survey experiments and causal contrasts;
2. factorial vignettes and audit/correspondence designs;
3. treatment construction and stimulus sampling;
4. manipulation checks, treatment validation, and information equivalence;
5. risks from researcher degrees of freedom and treatment heterogeneity;
6. generative systems as tools for producing, varying, selecting, or tailoring stimuli.

The purpose is not to teach a full causal-inference course. Students need enough design language to understand why a plausible stimulus can still produce an ambiguous treatment contrast.

## Questions for the fresh literature review

1. What recent social-science experiments use LLMs or image generators to construct treatment material rather than merely analyze outcomes?
2. Which studies validate generated stimuli before fielding them, and what evidence do they use: human ratings, blinded audits, embedding measures, pretests, qualitative review, or outcome-independent rules?
3. How do recent papers distinguish stimulus generation, stimulus selection, tailoring, and treatment assignment?
4. What work addresses treatment heterogeneity across multiple generated messages or images rather than treating one prompt output as the treatment?
5. Which work demonstrates contamination of intended manipulations by tone, length, realism, demographic cues, style, emotionality, readability, or factual content?
6. What methodological literature on information equivalence, treatment variation, or stimulus sampling best clarifies the causal stakes?
7. Is the strongest cumulative example generated profile images, generated policy messages, or another sociologically substantive intervention?
8. What small Python procedure would faithfully map onto the human design process while remaining explainable line by line?

## Requirements carried forward from Session 4

- Agree the cumulative study before building final slides.
- Write and review the slide-title sequence before the deck body.
- Show the route through the class when several literatures are involved.
- State why every focal paper is present and what later design or code decision it changes.
- Introduce the established human method before the generative extension.
- Use direct titles that can be spoken naturally.
- Inspect visual fidelity as well as overflow.
- Distinguish tests of code from evidence for the research claim.

## Review Gate 1 proposal

Proceed next to a fresh literature review. The review should assess the three current required readings rather than treating them as fixed, search recent primary work on generated experimental stimuli and treatment validation, and recommend one cumulative study plus a bounded reading load before methodological synthesis begins.

---

# Stage 2 — Fresh literature review

## What the literature changes about the session

The useful question is narrower than whether an LLM can write a plausible message or an image model can produce a plausible face. The session should ask:

> If we use a generative model to make experimental treatments, what evidence would let us claim that the conditions differ in the way our theory requires?

Three older experimental-design problems become more visible when generation is cheap:

1. **A treatment can carry unintended information.** Respondents infer facts that the researcher did not mean to vary.
2. **A particular message is not the same thing as a theoretical condition.** An effect may depend on one unusually strong wording, image, or example.
3. **Generation, selection, validation, assignment, and estimation are different stages.** A model may help with the first stage without supplying evidence for the others.

The recent literature is most useful when it is placed inside this established lineage. Generative AI changes the scale, speed, and variety of stimulus construction. It does not remove the need to define a construct, anticipate rival differences, sample or vary messages, validate treatments, and preserve a record of what was produced and retained.

## A more sociological account of what came before

The first review moved too quickly from a general statement about experimental practice to information equivalence and message sampling. The deck needs a recognizably sociological history of constructed treatments. That history should be selective rather than encyclopedic.

### Experiments have a long, if uneven, place in sociology

[Jackson and Cox's review of experimental design in sociology](https://www.annualreviews.org/content/journals/10.1146/annurev-soc-071811-145443) provides the broad orientation. Sociology has used laboratory, field, and survey experiments to study mechanisms that are difficult to isolate in observational data. Small-group and expectation-states experiments constructed controlled interactions to examine how status information affects influence and evaluation. Field experiments intervened in consequential institutional settings. Survey experiments placed controlled contrasts inside larger samples.

This only needs one opening slide. Its job is to prevent students from hearing “generated treatment” as a new research genre. The generative model enters an older chain of decisions about how a theoretical difference is represented materially.

### Music Lab offers a visible, genuinely sociological experiment

[Salganik, Dodds, and Watts's Music Lab experiment](https://www.princeton.edu/~mjs3/musiclab.shtml) is the strongest opening example for the slides. The researchers placed 14,341 participants in an artificial cultural market containing the same forty-eight unfamiliar songs. Some participants made choices independently; others saw download counts from participants in one of eight separate social-influence worlds. Social influence increased inequality and made success less predictable across the parallel worlds.

The study is useful here because students can inspect the experimental object itself. The website, song list, rankings, and download counts were not simply delivery machinery. They materialized a theory of social influence. The original interface screenshots also make the craft narratable without relying on Milgram or another familiar psychology example. The opening should use Music Lab to establish that sociologists sometimes build a small social world, then move to factorial surveys and audit studies as other ways of constructing controlled social comparisons.

### Sociologists have made treatments out of different things

The opening should situate Music Lab inside a wider repertoire. The most useful classification is not simply laboratory, survey, and field. For this session, students need to see **what carries the experimental difference**.

| Form of treatment | Sociological example | What researchers constructed | What it helps us see |
|---|---|---|---|
| Standardized partner | Berger, Cohen, and Zelditch's expectation-states program | Information about another group member and a controlled sequence of agreements or disagreements | A social relationship can be partially represented through cues and scripted responses |
| Human confederate in a status experiment | Ridgeway and Erickson's status-belief experiments | Scripted choices and arguments performed in a deferential or nondeferential manner | The treatment can depend on a trained interaction style as well as fixed words |
| Field confederate team | Piliavin, Rodin, and Piliavin's subway experiment | A staged collapse, an apparent condition, a possible helping model, observer roles, and a recording protocol | The treatment is performed in a live setting and cannot be separated from timing, demeanor, and place |
| Written vignette | Emerson, Yancey, and Chai's residential-segregation factorial experiment | Neighborhood descriptions assembled from racial composition and other housing or neighborhood characteristics | A short social description can vary several theoretically relevant dimensions systematically |
| Recorded vignette | Krysan and colleagues' neighborhood video experiment | Video tours used to separate neighborhood racial composition from social-class cues | Moving images can increase realism while adding details that must be kept comparable |
| Trained audit tester | Pager's employment audit | Matched résumés, assigned criminal-record conditions, trained job applicants, standardized presentation, and outcome records | A person can carry the treatment into an actual institution |
| Artificial social system | Salganik, Dodds, and Watts's Music Lab | Interfaces, song menus, social-information displays, and parallel cultural markets | The setting and information architecture can themselves be the intervention |

This repertoire creates a direct route to generated media. An LLM-written message resembles a constructed vignette. A generated image or video resembles a visual vignette. An interactive agent begins to resemble a standardized partner or confederate. In each case, the sociological question is not only whether the object looks plausible. It is whether the material or performance instantiates the intended social difference and what else it introduces.

#### Standardized interaction partners

[Berger, Cohen, and Zelditch (1972)](https://oaktrust.library.tamu.edu/bitstreams/2b787424-7e68-4b35-8c00-2d3ef08847dc/download) used controlled task situations to test how status information organizes influence in small groups. Later versions of the standardized experimental situation often placed a participant with an ostensible partner whose responses were controlled by the research design. This is important for the course because the “other person” can be an experimental representation rather than an independently acting group member. It also creates a careful bridge to conversational agents in Session 6: standardizing a few partner responses is different from allowing a model to generate an open-ended trajectory.

#### Confederates in a public encounter

[Piliavin, Rodin, and Piliavin's 1969 subway experiment](https://pubmed.ncbi.nlm.nih.gov/5359227/) used New York subway cars as a field setting. Four-person research teams included a victim, a helping model, and two observers. The victim staged a collapse while the team varied apparent condition, race, and whether or when a model intervened. The observers recorded latency, helping, movement, and comments.

This is a useful, less clichéd alternative to Milgram because the method is visible: roles, props, timing, location, performance, and recording together produced the study. It also raises ethical and inferential questions that a polished diagram should not conceal. Passengers did not consent in advance, the event could cause distress, and a human performance can drift across trials. The teaching point is therefore not that confederates are a gold standard. It is that using a person to carry a treatment creates a distinctive standardization and evidence problem.

For the main confederate slide, [Ridgeway and Erickson's “Creating and Spreading Status Beliefs”](https://www.journals.uchicago.edu/doi/10.1086/318966) is the more firmly sociological source. In their first experiment, confederates kept their choices and arguments constant but presented them in either a confident, nondeferential manner or an uncertain, deferential manner. Several confederates were assigned across conditions, and coders who did not know the condition reviewed recordings to assess whether the performances followed the intended treatment. The paper therefore gives the class an unusually clear example of a scripted social performance, a performance check, and a theory about how interaction produces wider status beliefs. Piliavin remains the field-setting comparison rather than carrying the disciplinary argument alone.

#### Written and recorded neighborhood treatments

[Emerson, Yancey, and Chai (2001)](https://journals.sagepub.com/doi/abs/10.1177/000312240106600607) conducted a telephone factorial experiment on residential preferences with 1,663 white respondents. Their vignettes varied racial composition alongside other features that race might proxy, such as crime and housing values. This gives the Wallander figure a substantive home: students are not looking at generic filler text but at a constructed neighborhood used to study segregation.

[Krysan, Couper, Farley, and Forman (2009)](https://www.journals.uchicago.edu/doi/abs/10.1086/599248) used video to address a related question about neighborhood racial composition and social class. This is an especially useful aside for a course about generated media. Sociologists were already moving from written descriptions to controlled audiovisual representations because the mode of presentation shapes what respondents can see and infer. Video may feel more realistic, but houses, streets, people, camera movement, sound, and editing all become possible rival differences.

### Further examples for the instructor's repertoire

Two network experiments can be named if students ask whether Music Lab is unusual. [Centola's online network experiment](https://pubmed.ncbi.nlm.nih.gov/20813952/) assigned participants to constructed network structures to study the spread of health behavior. [Paluck, Shepherd, and Aronow's experiment in 56 schools](https://www.pnas.org/doi/10.1073/pnas.1514483113) selected students to promote anti-conflict norms and used school networks to examine how influence spread, including the importance of socially connected referents. Both show a distinctively sociological move: the experiment targets not only an individual's message but also the pattern of relationships through which behavior can diffuse.

These are reserve examples, not additional focal slides. Music Lab already carries the artificial-system argument, and adding another network case to the main sequence would weaken the route to vignette construction.

### Factorial surveys constructed social situations before generative AI

The most important sociological lineage for this session is the factorial survey. [Jasso's methodological account](https://journals.sagepub.com/doi/10.1177/0049124105283121) describes how researchers combine experimentally varied dimensions into fictitious people or situations and ask respondents to make judgments about them. The method has been used to study distributive justice, inequality, marital expectations, immigration, professional judgment, and other domains in which socially meaningful attributes ordinarily occur together.

[Wallander's review of 25 years of factorial surveys in sociology](https://www.sciencedirect.com/science/article/pii/S0049089X09000192) traces the approach to Rossi and colleagues and reviews 106 articles in core sociology journals. The central ambition was to combine the controlled variation of an experiment with the contextual detail of a survey vignette. Its central tension is directly relevant now: increasing control can produce implausible combinations, while increasing realism can reintroduce correlations among attributes.

**Teaching job:** Students should see that sociologists were already doing four things that later appear in the Python:

1. defining dimensions and their possible levels;
2. constructing a universe or sample of combinations;
3. excluding impossible or theoretically incoherent cases; and
4. asking what judgments can generalize beyond the exact vignettes shown.

The old factorial-survey code often generated combinations of researcher-written fragments. An LLM can now write whole messages or scenes, but that apparent fluency makes the dimensions less—not more—transparent unless the researcher checks what else changed.

### Audit studies constructed matched people and watched institutions respond

Sociological audit and correspondence studies provide the second important lineage. Rather than asking respondents to rate a hypothetical case, researchers present matched applications or people to an actual gatekeeper and vary a theoretically relevant signal.

[Correll, Benard, and Paik's study of the motherhood penalty](https://sociology.stanford.edu/publications/getting-job-there-motherhood-penalty) is especially useful for this class because it combines a laboratory experiment with an audit study. Evaluators received application materials for equally qualified candidates whose parental status differed. Mothers were judged less competent and were recommended lower salaries; the audit component then examined discrimination by actual employers. The paper connects constructed materials to status-characteristics theory and to a substantively sociological question about work and family.

Pager's criminal-record audit and later sociological field experiments make a related move: researchers construct comparable cases, vary a signal such as a criminal record, race, or parenthood, and observe an institutional response. The attraction is clear, but so is the burden. If names, photographs, work histories, wording, demeanor, or other cues differ, the study may no longer isolate the signal named in the theory.

**Teaching job:** Audit studies show why stimulus construction is part of the causal design rather than a preliminary production task. They also prepare students to understand LinkedOut as a recent extension of an established sociology of discrimination, not simply an impressive use of synthetic faces.

### A new paper makes the historical bridge explicit

[Nicole Schwitter's 2025 article on AI-generated visual vignettes](https://journals.sagepub.com/doi/10.1177/08944393251392916) begins from the factorial-survey tradition and asks when generative images improve an experiment. It describes a process of generating and selectively editing images, then validating how participants perceive their realism and relevant social attributes. Human pretesting exposed familiar artifacts and showed that realism judgments varied across both images and viewers.

This paper is unusually well suited to the lecture because it makes the transition visible:

> researcher-written vignette dimensions → visual vignettes → generated candidate images → iterative human pretesting → a bounded stimulus set

It also supplies an important caution. Images should not be used merely because generation is available. A visual treatment is warranted when visible characteristics are part of the theoretical question; otherwise it may introduce additional uncontrolled information.

### The sociological continuity

Across factorial surveys, status experiments, and audit studies, sociologists have repeatedly asked how social categories and situations are represented in a controlled comparison. Generated media changes the production technology, but the inherited questions remain:

- Which attribute is supposed to vary?
- How is that attribute embedded in a recognizable social situation?
- Which other cues have changed with it?
- Do participants perceive the intended distinction?
- Is the material realistic enough for the target setting?
- Does the inference concern these exact materials or a wider class of people, messages, and situations?

This is the bridge the opening slides should establish before introducing OpenRouter, an image model, or any generated output.

## Proposed “what came before” slide sequence

These are working titles for synthesis review, not finished slide copy. Read in order, they should tell a comprehensible story without the talk track.

| Working slide title | What the slide is doing |
|---|---|
| **This week we start constructing the material that participants will see** | Marks the course transition from observing records to intervening and defines a treatment in beginner language. |
| **The experimental difference might be carried by a text, another person, or the setting itself** | Locates standardized partners, confederates, vignettes, audit testers, and artificial social systems using documentary fragments from actual studies. |
| **Music Lab created separate markets for the same forty-eight songs** | Shows a sociological experiment in which the interface and visible choices of other participants were part of the treatment. |
| **Ridgeway and Erickson trained confederates to act deferentially or nondeferentially** | Introduces a genuinely sociological confederate experiment and separates fixed choices and arguments from performed interaction style and treatment-fidelity checks. |
| **Wallander uses a segregation study to show how factorial vignettes work** | Introduces the actual paper and identifies the displayed vignette as Emerson, Yancey, and Chai's neighborhood experiment. |
| **Researchers decide the dimensions before writing the vignettes** | Shows one small vignette as named dimensions and levels; makes the later dictionary/list structure intuitive. |
| **Some statistically useful combinations make little social sense** | Introduces the control–realism tension using Wallander and a visible pair of plausible/implausible cases. |
| **Audit studies send matched cases into real institutions** | Distinguishes judgments about hypothetical situations from institutional responses to applications or people. |
| **Correll and colleagues varied parenthood in otherwise comparable job applications** | Gives the classic application its question, materials, comparison, result, and sociological argument. The paper is visibly identified on the slide. |
| **Constructing comparable applications is part of the causal design** | Lets students identify cues that must be held stable and prepares information equivalence without naming it yet. |
| **Generative models can produce many versions of the same basic treatment** | Introduces the production change only after the human method and its burden are clear. |
| **Schwitter generated visual vignettes and then tested how people perceived them** | Shows an actual recent paper, its candidate-generation and pretest sequence, and why human ratings altered the retained set. |
| **More candidates also mean more differences to account for** | Makes the transition into Dafoe, stimulus sampling, and the cumulative paid-parental-leave example. |

This “what came before” section should occupy roughly 24–25 minutes including one short student comparison exercise. It should not become a general history of experimental sociology. Berger's standardized situation, Piliavin's subway experiment, and Krysan's video study can be handled through brief insets; Music Lab, Ridgeway and Erickson's confederate experiment, the factorial vignette, and the motherhood-penalty study receive the actual worked visuals because together they show setting, performance, description, and matching.

## Methodological foundations

### Dafoe, Zhang, and Caughey (2018): unintended information is part of the treatment

[Dafoe, Zhang, and Caughey's “Information Equivalence in Survey Experiments”](https://www.cambridge.org/core/journals/political-analysis/article/information-equivalence-in-survey-experiments/8D134C6387CD7D845249B0712775AB79) gives the session its central causal-design language. A researcher may vary one visible attribute while also changing respondents' beliefs about background features. The observed outcome difference then cannot automatically be attributed to the named construct.

**Material:** Survey-experimental treatments that vary information about a focal attribute.

**Design problem:** The treatment may also change beliefs about relevant background conditions. Dafoe and colleagues call the desired property *information equivalence* and discuss placebo tests and design strategies for diagnosing or reducing violations.

**Teaching job:** This paper lets students replace the vague question “Does the treatment look right?” with two more precise questions:

- What is supposed to differ between the conditions?
- What else might a respondent reasonably infer from that difference?

**Code consequence:** The treatment record must contain fields for the intended construct and plausible nuisance dimensions. A word-count check alone is not treatment validation.

### Slater, Peter, and Valkenburg (2015): messages are another sampled part of the study

[Slater, Peter, and Valkenburg's “Message Variability and Heterogeneity”](https://pmc.ncbi.nlm.nih.gov/articles/PMC4677678/) distinguishes defined message features from all the remaining, often idiosyncratic, ways messages differ. It asks researchers to define the population of messages about which they want to make a claim and to explain how the messages used in an experiment were selected or created.

**Material:** Verbal, visual, and multimodal messages used in communication research.

**Design problem:** A study using one message per condition cannot tell whether the effect belongs to the theoretical contrast or to those particular messages. Selecting messages is a sampling decision, much as selecting participants is.

**Teaching job:** This paper explains why inexpensive LLM variation is methodologically useful only if the researcher treats the variants as a stimulus pool and not as a menu from which to cherry-pick the most convincing output.

**Code consequence:** The notebook should create and retain multiple candidates per condition, keep stable identifiers, and report which candidates passed or failed predeclared checks.

### Westfall, Judd, and Kenny (2015): more participants do not repair a one-stimulus design

[Westfall, Judd, and Kenny's account of replication with sampled stimuli](https://journals.sagepub.com/doi/abs/10.1177/1745691614564879) makes the same inferential point in a compact statistical form: if a claim is meant to generalize beyond the exact faces, words, or messages shown, stimuli must enter the logic of sampling and replication.

This is valuable instructor background and could supply one explanatory slide. It overlaps with Slater et al., however, and assigning both would add reading without adding a sufficiently different classroom job. Slater et al. is the better required reading for this group because it develops the message problem in substantive terms before moving to design and analysis.

## Current generated-treatment studies

### Bai et al. (2025): generated persuasive messages can be studied as a pool

[Bai and colleagues' three preregistered experiments](https://www.nature.com/articles/s41467-025-61345-5) compare LLM-generated policy messages, human-written messages, human-selected LLM messages, and an irrelevant-message control. Across the studies, the generated messages moved policy support, with effects measured on a 101-point scale. The design uses many messages rather than allowing one output to stand for an entire condition; the first two studies use pools of 50 LLM and 50 human messages.

**Material:** Persuasive messages supporting policy positions.

**Design:** Participants are assigned to message-source/selection conditions and then encounter a message from the relevant pool. The human-in-the-loop condition asks people to choose among several LLM outputs.

**Result:** Generated messages can persuade, but the paper also makes selection a substantive feature of the design rather than an invisible researcher choice.

**Important complication:** Examples reported in the paper show that LLM and human messages can differ in length and perceived qualities such as evidence, logic, or empathy. Those differences may help explain effectiveness; they are not merely formatting details.

**Teaching job:** This is the main current applied reading. It allows the class to inspect what the treatment actually is, why multiple variants matter, where human selection enters, and why “LLM versus human” is itself a bundle of possible message differences.

**Code consequence:** Our example should retain the generator, prompt, condition, candidate ID, text, ratings, and selection decision. It should make a rejected candidate just as inspectable as an accepted one.

### Evsyukova, Rusche, and Mill (2025): generated images require a validation pipeline

[The LinkedOut field experiment](https://www.crctr224.de/research/discussion-papers/archive/dp482), subsequently published in the [*Quarterly Journal of Economics*](https://academic.oup.com/qje/article-abstract/140/1/283/7842027), uses synthetic profile images in a study of racial discrimination in professional networking. The researchers generated a large candidate set, constructed paired images intended to differ in perceived race while limiting other differences, validated them with human raters, and selected the final stimuli using those ratings. Black profiles' connection requests were 13 percent less likely to be accepted.

**Teaching job:** LinkedOut should remain, but as a worked visual comparison rather than a second required applied paper. It shows that validation can involve fake detection, perceived race, trust, appearance, authenticity, and intelligence—not simply whether an image file was produced successfully. It also exposes a further issue: the generator's underlying training distribution can constrain which matched stimuli are available.

**Why it is not the cumulative notebook example:** A responsible image-generation exercise would require more infrastructure, more discussion of race classification and ethics, and more visual validation than fits the beginner Python progression. The study is excellent for examining a published pipeline; it is not the best small student build.

### Velez (2025): the question bank can adapt during fieldwork

[Velez's published *Political Analysis* article](https://doi.org/10.1017/pan.2024.34) introduces crowdsourced adaptive surveys. Participants supply open-ended responses; an LLM converts those responses into structured survey items; toxicity and redundancy filters screen the items; and an adaptive algorithm changes which items later participants are likely to receive.

This belongs near the end of Session 5 because it changes the object students have just learned to audit. In the fixed examples, researchers freeze a candidate pool before assignment. In Velez's design, participant input changes a shared question bank during fieldwork. The method therefore requires an audit trail for source responses, converted items, filtering decisions, question-bank versions, and changing selection probabilities. It is adaptive survey design rather than a free-form conversational interview; that distinction provides a precise bridge into turn-by-turn AI interviewing in Session 6.

### Hewitt and colleagues (2024): effects vary across real messages

[Hewitt and colleagues' archive of 146 campaign-ad experiments](https://www.cambridge.org/core/journals/american-political-science-review/article/how-experiments-help-campaigns-persuade-voters-evidence-from-a-large-archive-of-campaigns-own-experiments/FF5BE6ED1553475F8321F7C4209357F7) contains 617 ads and more than 500,000 respondent-level observations. Its main classroom value here is not campaign strategy. It makes message-effect heterogeneity empirical: different executions of what appears to be the same broad treatment type do not necessarily have the same effect.

This is useful slide evidence for the move from “one prompt, one message” to “a defined population or pool of treatments.” It does not need to become another assigned reading.

## Proposed required reading set

The reading load remains three papers, now with a clearer sociological foundation, one precise causal-design paper, and one current application.

| Reading | Role in the session | What students should bring to class |
|---|---|---|
| Wallander (2009), introduction plus design and concluding sections | Establishes the factorial-survey tradition in sociology and its control–realism tension. | Identify the dimensions, levels, and judgment in one factorial-vignette example. |
| Dafoe, Zhang, and Caughey (2018) | Defines information equivalence and rival interpretations of a treatment contrast. | One example of something respondents could infer beyond the intended manipulation. |
| Bai et al. (2025) | Provides the main LLM-generated-message experiment. | A sketch of the conditions, the unit assigned, the message pool, the outcome, and one plausible bundled difference. |

Wallander replaces Slater et al. in the required set. Slater remains important instructor background for message populations and should appear in the synthesis when the class asks whether an effect generalizes beyond a particular wording. The replacement makes the assigned sequence more visibly sociological without increasing the reading load.

**In-class rather than required:** Correll, Benard, and Paik; Schwitter; Slater et al.; LinkedOut; and Velez. Westfall and Hewitt remain instructor background. Each slide-only source must do one visible job and should not become a separate mini-lecture.

## Proposed cumulative study

### Research question

> How do rights, economics, and family framing contests change support for immigrant legal status?

This is a recognizably sociological question about social movements, citizenship, political membership, and frame resonance. It also comes from a published sociology article whose exact treatments and heterogeneous results can be inspected directly.

### Intended treatment contrast

- **Rights frame:** human-rights claims versus claims about the rights of US citizens.
- **Economics frame:** economic contributions versus claims about American jobs and public costs.
- **Family frame:** deportation and separation versus keeping families together.

Each condition stages a contest within one domain. Candidate messages should be comparable in length, tone, readability, specificity, and factual density. The challenge is not to make them literally identical; it is to decide which differences constitute the theoretical treatment and which would support rival explanations.

### Why this example is methodologically productive

The design cannot be solved by asking a model to “make three versions.” Economics language may become more numerical or technocratic; family language may become warmer or more emotional; rights language may imply a different theory of membership. Terminology can also become stigmatizing. Those features could be mediators, parts of the construct, nuisance differences, or evidence that the construct itself has been poorly defined. Students must make and defend that decision.

### The human research process the code should mirror

1. Write the research question and define all three frames in ordinary language.
2. Specify what must remain stable across conditions.
3. Produce several candidate messages per condition, using cached outputs for required work.
4. Give every candidate a stable ID and preserve its text and provenance.
5. Inspect and rate the intended frame plus plausible nuisance dimensions.
6. Apply predeclared rules and record a reason for every rejection.
7. Compare the retained pools at the condition level rather than selecting one favourite message.
8. Only then discuss random assignment and the outcome measure.

### Proposed beginner data object

Each candidate can be one Python dictionary in a list:

```python
{
    "candidate_id": "econ_03",
    "condition": "economic_security",
    "text": "...",
    "frame_score": 4.4,
    "warmth_score": 2.8,
    "factual_density": 3.1,
    "word_count": 91,
    "source": "cached_openrouter_generation",
    "prompt_version": "v2"
}
```

This structure gives each familiar Python feature a methodological meaning:

- the list is the candidate stimulus pool;
- a dictionary is one candidate and its evidence;
- a loop reviews candidates one at a time;
- an `if` statement applies a rule chosen before inspection;
- `.append()` places a candidate and its reason in the retained or rejected record;
- a function makes the same review procedure reusable;
- the returned output is an audit trail, not a claim that the treatment is valid.

The class should first enact this procedure by hand on a small set of messages. The code then formalizes decisions students already understand.

## What the session should not claim

- Passing automated thresholds does not prove construct validity.
- An LLM rating its own output is not an adequate substitute for independent human judgment.
- Equal word counts do not establish information equivalence.
- A manipulation check measured after exposure can itself complicate the study and does not automatically identify the source of an effect.
- Producing many candidates does not solve selection bias if the researcher retains outputs opportunistically.
- A persuasive message is not necessarily a well-isolated experimental treatment.
- Random assignment protects the treatment comparison from participant confounding; it does not make ambiguous treatment content interpretable.

## Proposed lecture arc for the synthesis stage

1. **Where this sits in the course:** Sessions 1–4 studied model outputs and existing records; Session 5 asks what changes when the researcher manufactures the exposure.
2. **Experiments in sociology are not new:** briefly locate laboratory, field, and survey experiments.
3. **Factorial surveys constructed social situations:** dimensions, levels, vignette universes, realism, and judgment.
4. **Audit studies constructed matched people:** Correll et al. and the practical meaning of holding other cues constant.
5. **The basic causal problem:** the named manipulation and the actual information received are not necessarily the same.
6. **Generated media extends an existing practice:** Schwitter makes the transition from written dimensions to generated visual candidates and human pretesting explicit.
7. **Why one message per condition is weak evidence:** messages vary, and results may be stimulus-specific.
8. **Worked study:** paid-parental-leave frames, from construct definition through candidate review.
9. **Published message comparison:** Bai et al. on stimulus pools and human selection.
10. **Published visual comparison:** LinkedOut as an AI-enabled continuation of the audit-study tradition.
11. **Beginner Python:** turn the hand review into a transparent screening function.
12. **Limits and transition:** tailored, interactive treatments lead into Session 6.

## Review Gate 1 recommendation

Approve the following before synthesis:

1. Use **Wallander; Dafoe et al.; and Bai et al.** as the three required readings.
2. Build the “what came before” section around **factorial surveys and audit studies**, with only one preliminary slide locating experiments more generally in sociology.
3. Use **Correll, Benard, and Paik** as the classic sociological application and **Schwitter** as the explicit bridge to AI-generated visual vignettes.
4. Keep **LinkedOut** as a substantial in-class visual case, now presented as a continuation of audit research rather than a standalone AI example.
5. Use **paid-parental-leave framing** as the cumulative study for the lecture, workbook, and completion task.
6. Use **Velez (2025)** to distinguish a fixed stimulus pool from an evolving question bank, then reserve turn-by-turn conversational interviewing for Session 6.
7. Build the code around a cached candidate pool, transparent ratings, predeclared screening rules, and explicit rejection reasons—not live generation or a word-count-only filter.

If this architecture is approved, the next stage is methodological synthesis: write the actual claims and cautions that connect each reading to each step of the worked study, then review the slide-title sequence before building the deck.
