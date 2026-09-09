# Session 5 synthesis — Can generated media isolate a causal construct?

**Status:** Stage 3 methodological synthesis completed on 2026-08-21. The central argument, reading roles, cumulative study, code mapping, and limits are ready for Review Gate 2.

## Central argument

Sociologists have long constructed vignettes, applications, profiles, messages, and controlled interactions to turn a theoretical distinction into an observable comparison. Generative models can now produce many versions of this material quickly and in several media. That is a genuine expansion of research capacity, but it does not establish that the resulting treatments isolate the construct named by the researcher.

The session's central claim is:

> A generative model can produce candidate stimuli. The researcher still has to show what differs across the treatment conditions, what else changed, how candidates were retained, and how far the resulting comparison can generalize.

Students should leave able to explain why correct random assignment does not repair ambiguous treatment content, why one message cannot automatically stand for a theoretical condition, and why screening rules produce an auditable decision rather than proof of construct validity.

## The main distinction

A **treatment condition** is a theoretical category in the research design. A **stimulus** is one material realization of that category.

In the cumulative study:

- `rights`, `economics`, and `family` are treatment conditions;
- one short immigrant-rights message is one candidate stimulus;
- several retained messages form the stimulus pool for a condition;
- a participant is assigned to a condition and then sees one stimulus from that pool;
- the outcome is the participant's reported policy support.

If one unusually compelling message produces an effect, that does not by itself show that the frame produced the effect. The study needs a reason for treating the message as an instance of the frame and a design that acknowledges variation among messages.

## Six things students must keep separate

### 1. Construct definition

What is the theoretical distinction? What belongs inside each category? What would count as a poor or ambiguous realization?

### 2. Stimulus generation

Who or what produced the candidate material? Which model, prompt, seed, source text, constraints, and revision process were used?

### 3. Stimulus selection and validation

Which candidates were retained? According to which rules and evidence? Were intended and unintended differences assessed independently of the outcome?

### 4. Treatment assignment

How are participants assigned to conditions and, when several stimuli exist, to particular messages within conditions?

### 5. Outcome measurement and estimation

What response is measured, and what comparison is estimated?

### 6. Generalization

Does the conclusion concern the exact messages shown, messages produced through this procedure, or a wider theoretical class of frames?

The current Session 5 materials conflate the first three stages and barely represent the others. The rebuild must make the sequence explicit.

## What sociologists did before generative models

### Laboratory and small-group experiments constructed social conditions

Experimental sociology and sociological social psychology created controlled situations to study status, influence, expectations, cooperation, exchange, and group processes. The key historical lesson is not a specific apparatus. It is that the material setup embodies a theoretical claim about which social difference matters and which background conditions have been stabilized.

Jackson and Cox provide a concise overview of laboratory, field, and survey experiments in sociology. This history belongs in one orientation slide rather than a separate mini-lecture.

Salganik, Dodds, and Watts's Music Lab should make that orientation concrete. Participants encountered the same forty-eight unfamiliar songs in separate artificial cultural markets, while the interface varied whether they could see other people's downloads. The example shows, in an immediately visible form, that the delivery environment is part of the treatment: the screen organizes what participants can know about the actions of others. It also supplies a direct sociological result—parallel worlds can produce different cultural winners—before the lecture moves from a constructed market to constructed vignettes.

The short historical orientation should then distinguish five ways sociologists have materialized a treatment:

1. **a standardized partner:** expectation-states researchers controlled status information and an ostensible partner's responses;
2. **a human confederate:** Ridgeway and Erickson trained partners to enact deferential or nondeferential interaction, while Piliavin and colleagues staged an emergency through assigned roles, props, timing, and performance;
3. **a written or recorded vignette:** Emerson and colleagues constructed neighborhood descriptions, while Krysan and colleagues used video to vary what a neighborhood looked like;
4. **a trained audit tester:** Pager sent matched applicants into actual labor-market encounters;
5. **an artificial social system:** Music Lab built separate markets and varied the social information visible within them.

These are not interchangeable. A vignette fixes the exposure but asks participants to judge a represented situation. A confederate or tester enters a live encounter but introduces performance and interactional variation. An artificial system can standardize an interface while allowing collective outcomes to unfold. Generated media inherits different problems depending on which form it is being used to replace or extend.

### Factorial surveys constructed social situations from dimensions and levels

The factorial-survey tradition combined survey context with experimental variation. Researchers specified dimensions, defined possible levels, generated or sampled combinations, wrote vignettes, and asked respondents to judge the resulting people or situations.

Wallander's review supplies the sociological history and its enduring tension:

- orthogonal variation can help separate attributes that co-occur in observational data;
- combinations that are statistically useful may be socially implausible;
- detailed realism can help respondents understand a situation while introducing more information;
- judgments of fictitious objects do not automatically generalize to judgments or behaviour in the world.

Jasso makes the design logic especially concrete: dimensions and levels create a vignette universe, while substantive knowledge determines which combinations are possible and meaningful.

### Audit and correspondence studies constructed matched cases

Audit studies place comparable applications, profiles, or trained testers into actual institutional processes. Correll, Benard, and Paik varied parental status in otherwise comparable application materials, connected the manipulation to status-characteristics theory, and examined both evaluator judgments and employer behaviour.

The methodological inheritance is direct. Researchers must decide what “otherwise comparable” means. A name, photograph, extracurricular activity, employment history, phrase, or mode of presentation can carry additional information. Constructing the materials is therefore part of the causal design.

Pager's criminal-record audit and later correspondence studies make the same general demand in other substantive domains. They need not each receive a paper slide; the tradition should be named so that LinkedOut is understood as a new production method inside an established sociology of discrimination.

### Researchers wrote, sampled, pretested, and revised messages

Message experiments traditionally used researcher-written, professionally produced, sampled, or adapted materials. Slater, Peter, and Valkenburg show why messages have both defined features and remaining heterogeneity. Choosing a message is also a sampling decision when the claim is meant to extend beyond the exact words shown.

This literature prevents the class from treating “generate five and choose the best” as an innocent convenience. Selection changes the treatment-production process and therefore belongs in the research record.

## What generative systems change

### Candidate production becomes faster and broader

A researcher can request many textual variants, create matched images, revise a local region of an image, alter tone or reading level, and produce materials for languages or settings that would previously have required more time and specialist labour.

### The material can vary in less transparent ways

Whole-message generation does not merely substitute one named dimension. It can change length, syntax, emotionality, factual density, examples, implied speaker, social stereotypes, and the background beliefs a respondent forms.

### Selection becomes a larger and more consequential stage

More candidates create more opportunities to inspect variation, but also more opportunities to cherry-pick. Human selection can improve relevance or quality while making the treatment depend on an unrecorded evaluator preference.

### Visual and multimodal treatments become easier to produce

Schwitter explicitly extends factorial-survey practice to AI-generated visual vignettes. The paper demonstrates candidate production, selective editing, and human pretesting of realism and social attributes. It also asks whether a visual format is theoretically warranted at all.

LinkedOut uses a larger generation and rating pipeline to construct profile images for a field experiment. Its contribution to this class is the validation process, not the novelty of synthetic faces.

### The instrument can change while data collection is underway

Velez's crowdsourced adaptive survey turns participant open-ended responses into structured items, filters them, and adds them to an evolving question bank. An adaptive algorithm changes which items later participants are likely to receive. This is not yet a free-form AI interview, but it shows why adaptation requires versioned instruments and logged selection probabilities. Turn-by-turn probing remains Session 6's central problem.

## What does not change

- The researcher must define the construct before interpreting an output as its realization.
- The treatment must be represented in material participants actually receive.
- Rival differences must be anticipated and investigated.
- Human judgment remains necessary but must itself be structured and documented.
- Random assignment concerns who receives treatment; it does not define what the treatment contains.
- Outcome differences do not retroactively validate a treatment manipulation.
- Ethical review applies to both the content and the production process.
- Reproducibility requires saving candidate outputs and decisions, not only the final stimulus.

## The distinct job of each source

| Source | Material and question | Specific job in Session 5 | Decision it changes |
|---|---|---|---|
| Jackson and Cox (2013) | Experimental designs used across sociology | Establishes disciplinary continuity in one overview slide | Begin with sociological experimental practice rather than model capability |
| Salganik, Dodds, and Watts (2006) | Parallel artificial music markets with and without visible social information | Makes the construction of a sociological experimental setting visible | Treat the interface and information display as substantive parts of the treatment |
| Berger, Cohen, and Zelditch (1972) | Controlled task interaction with status cues and an ostensible partner | Locates scripted interaction inside a major sociological research program | Separate fixed partner behavior from later adaptive-agent treatments |
| Ridgeway and Erickson (2000) | Confederate partners enacting deferential or nondeferential behavior | Provides the focal sociological example of a performed interaction treatment and treatment-fidelity check | Keep words, interaction style, confederate assignment, and performance coding analytically distinct |
| Piliavin, Rodin, and Piliavin (1969) | Staged subway emergencies using a victim, model, and observers | Shows how a human performance carries a field treatment | Include role, timing, demeanor, setting, and recording in the treatment description |
| Wallander (2009) | Review of 106 factorial-survey articles in sociology | Introduces dimensions, vignette construction, control, realism, and fictitious judgments | Define dimensions and possible combinations before generating prose |
| Emerson, Yancey, and Chai (2001) | Factorial descriptions of neighborhoods and residential choice | Gives the written vignette a concrete sociology of segregation application | Identify both racial composition and the contextual features it may proxy |
| Krysan et al. (2009) | Video neighborhood treatments | Shows that richer media can add realism and new nuisance cues | Inspect the entire audiovisual scene rather than only its intended category |
| Correll, Benard, and Paik (2007) | Matched application materials in laboratory and audit studies | Shows construction as part of a sociological theory of work, family, and status | Specify what must remain comparable across treatments |
| Pager (2003) | Matched testers applying for real entry-level jobs | Shows how people and materials jointly carry a treatment into an institution | Document tester matching, training, rotation, and field recording |
| Dafoe, Zhang, and Caughey (2018) | Survey-experimental information and background beliefs | Supplies the language of information equivalence and placebo tests | Record plausible inferences and nuisance dimensions, not just intended labels |
| Slater, Peter, and Valkenburg (2015) | Populations and heterogeneous features of messages | Explains why a theoretical condition needs more than one convenient message | Create multiple candidates per condition and retain candidate IDs |
| Bai et al. (2025) | Human, LLM, and human-selected LLM policy messages | Provides the main current text-generation experiment and makes selection visible | Record source and selection route; inspect length and perceived message features |
| Schwitter (2025) | Generated and edited visual factorial vignettes with human pretesting | Provides the explicit historical bridge from factorial surveys to generative media | Use generation only when the medium serves the construct; pretest perception |
| Evsyukova, Rusche, and Mill (2025) | Synthetic profile images in a networking field experiment | Supplies a visual validation pipeline inside an audit-study lineage | Generate a candidate pool and compare intended and unintended ratings |
| Velez (2025) | Participant-generated items in an evolving survey question bank | Shows how the instrument can adapt during fieldwork | Log source responses, converted items, filters, bank versions, and selection probabilities |

## Recommended reading configuration

### Required

1. **Wallander (2009), selected sections:** abstract, introduction, discussion of design/realism, and conclusion.
2. **Dafoe, Zhang, and Caughey (2018):** full article.
3. **Bai et al. (2025):** main article, with attention to conditions, message pools, human selection, outcomes, and reported message differences.

This provides two methods-oriented readings and one applied generated-message study. It remains within the established weekly reading load.

### Taught through slides or short excerpts

- Jackson and Cox: one disciplinary-orientation slide.
- Salganik, Dodds, and Watts: the constructed social-system example.
- Berger, Cohen, and Zelditch: a brief inset on standardized partners.
- Ridgeway and Erickson: the focal sociological confederate experiment.
- Piliavin, Rodin, and Piliavin: a brief field-setting comparison.
- Jasso: one dimensions-and-levels explanation.
- Emerson, Yancey, and Chai: the substantive study behind the displayed neighborhood vignette.
- Krysan et al.: a short bridge from written to recorded vignettes.
- Correll, Benard, and Paik: the main historical sociological application.
- Pager: the trained-tester extension of the audit-study tradition.
- Slater et al.: the message-population question.
- Schwitter: the explicit factorial-survey-to-generation bridge.
- LinkedOut: the generated-image validation pipeline.
- Velez: one worked contrast between a fixed pool and an evolving question bank.

No source should appear only because it is relevant. Every source above changes a later judgment, activity, or code object.

## Cumulative sociological study

### Research question

> How do rights, economics, and family framing contests change support for immigrant legal status?

The worked example adapts the three domains in Bloemraad, Silva, and Voss (2016). The candidate texts are synthetic course materials rather than the article's original treatments, and the course does not claim to reproduce its estimates.

### Intended conditions

**Rights frame:** contrasts human-rights claims with claims that citizenship should determine political membership.

**Economics frame:** contrasts immigrants' economic contributions with claims about jobs and public costs.

**Family frame:** contrasts deportation and separation with keeping parents and children together.

Each domain contains a framing contest rather than a one-sided slogan. The theoretical contrast is the domain foregrounded in the message.

### What should remain comparable

- policy position;
- policy details;
- length range;
- reading difficulty;
- factual specificity;
- presence of numerical claims;
- emotional intensity;
- warmth;
- implied speaker and audience;
- terminology used for immigrants and legal status;
- directness of the call for support.

Some of these features may partly constitute a frame rather than act as pure nuisances. That ambiguity is pedagogically useful. Students must explain which differences belong to the construct and which would create a rival interpretation.

### Candidate pool

The teaching dataset contains twelve short messages: four candidates per condition. Required work uses cached text. Each candidate has:

- a stable ID;
- full text;
- assigned condition;
- generator and model route;
- prompt version;
- word count;
- illustrative ratings for the intended frame, the strongest competing frame, warmth, emotionality, readability, and factual density;
- a flag for unsupported quantitative claims;
- an instructor-authored note explaining a deliberately planted problem.

At least four candidates should fail for different reasons:

1. a weak intended frame;
2. the intended and a competing frame both expressed strongly, making the condition ambiguous;
3. an unsupported numerical claim;
4. a large nuisance difference such as unusually emotional or gendered language.

The failures must be substantively interpretable, not arbitrary boundary cases inserted only to exercise an `if` statement.

### Provenance

The proposal, messages, ratings, participant responses, and results used in class are instructor-authored synthetic teaching materials or cached model outputs created specifically for the course. The deck must state this before displaying them.

The illustrative ratings are not evidence from an actual pretest. Students will conduct a small classroom rating exercise to understand the procedure, but that convenience exercise cannot validate a treatment for field research.

### Outcome

The hypothetical outcome is policy support measured after exposure on a 0–10 scale. No participant outcome is needed for the main code task because construction and validation occur before assignment and estimation. A small synthetic outcome table may appear near the end solely to show why even a clean difference in means cannot repair ambiguous stimuli.

## Validation plan for the worked study

### Step 1: define the intended distinction

Write ordinary-language definitions and examples before generating candidates.

### Step 2: predeclare candidate-level rules

Illustrative rules might require:

- intended-frame rating at or above a stated threshold;
- competing-frame rating below a stated threshold;
- word count within a range;
- no unsupported quantitative claim;
- no stigmatizing terminology.

The exact thresholds are teaching choices, not universal standards.

### Step 3: preserve every decision

A rejected candidate remains in the dataset with one or more rejection reasons. It is not deleted from the research history.

### Step 4: compare retained pools

After candidate-level screening, compare the three condition pools on:

- number retained;
- average word count;
- average warmth;
- average emotionality;
- average readability;
- average factual density.

A pool-level imbalance generates a warning for human review. It does not mechanically prove or disprove information equivalence.

### Step 5: distinguish pretest questions

Pretesting can ask:

- Do respondents perceive the intended frame?
- What else do they infer about the proposal or speaker?
- How realistic, clear, and credible is the message?
- Which unintended characteristics differ by condition?

These are not all “manipulation checks.” Some concern construct interpretation, some concern nuisance differences, and some concern material quality.

## Human-method-to-code mapping

| Human research activity | Python representation | What is lost or thinned |
|---|---|---|
| Define the two frames | strings and a small definitions dictionary | theoretical reasoning and disagreement about category boundaries |
| Assemble candidate stimuli | a list of dictionaries | production context not stored in the selected fields |
| Give each candidate an identity | `candidate_id` string | identity does not ensure complete provenance |
| Record pretest evidence | numeric and Boolean dictionary values | rater composition, uncertainty, disagreement, and interpretation |
| Apply predeclared checks | conditionals inside a function | judgment about whether a rule is appropriate |
| Preserve rejection reasons | a list of reason strings | reasons remain simplified summaries |
| Retain passing candidates | `.append()` to an accepted list | acceptance is not proof of validity |
| Compare condition pools | counts and simple means | distributional shape and message-level uncertainty |
| Revisit a flagged imbalance | printed warning plus human review | the code cannot decide whether a difference belongs to the construct |

The code should be described as an audit trail for decisions, not an automated validator.

## Beginner Python progression

### Reused from Sessions 1–4

- strings, integers, floats, and Booleans;
- dictionaries and key lookup;
- lists and indexing;
- loops;
- conditionals;
- `.append()`;
- functions, arguments, and `return`;
- reading a printed result;
- distinguishing a passing software test from evidence for a sociological claim.

### New or deepened in Session 5

1. **A list can hold multiple dictionaries with the same schema.** This becomes a stimulus pool.
2. **A candidate can fail more than one rule.** A `reasons` list accumulates explanations rather than stopping at the first failure.
3. **The output can have several related parts.** The function returns accepted records and rejected records with reasons.
4. **Individual and group-level checks answer different questions.** Candidate screening is followed by a small condition summary.
5. **A rule dictionary separates design choices from the loop applying them.** Students see that thresholds are inputs chosen by researchers.

### Proposed focal functions

```python
def review_candidates(candidates, rules):
    """Return accepted candidates and rejected candidates with reasons."""
```

```python
def summarize_pools(accepted):
    """Return simple condition summaries for human comparison."""
```

The first function receives a list and a dictionary and returns two lists. The second receives the retained list and returns a dictionary keyed by condition. Both functions should be traced with actual values before students see the complete definition.

## Reading-to-code alignment

| Reading lesson | Object or operation in code |
|---|---|
| Wallander: define dimensions and plausible combinations | explicit `condition`, frame definitions, and candidate schema |
| Dafoe et al.: ask what else respondents infer | nuisance rating fields, competing-frame score, and pool comparison |
| Bai et al.: generation and human selection are different conditions | `source`, `prompt_version`, and retained/rejected decision record |
| Slater et al.: a message is drawn from a wider message population | several candidates per condition and stable candidate IDs |
| Schwitter: generated material requires iterative pretesting | rating fields, revision notes, and explicit human-review warnings |
| LinkedOut: selection occurs after comparison across multiple perceived attributes | candidate pool plus intended and unintended attribute ratings |

## Likely failure modes and their stakes

### Defining the construct after seeing attractive outputs

The research question bends around whatever the model produced. This converts generation into an unrecorded exploratory process while presenting the result as a confirmatory manipulation.

### Treating surface plausibility as fidelity

A polished message can express several frames, add new facts, or change the implied speaker. Fluency is not evidence that the theoretical contrast has been isolated.

### Using one output per condition

The effect may belong to a particular wording rather than the named frame. A large participant sample does not by itself solve stimulus-specific inference.

### Selecting the “best” output without recording why

Researcher preference becomes an invisible part of the treatment. A human-in-the-loop procedure is not automatically transparent or reliable.

### Asking a model to validate its own generations

Model ratings can be exploratory diagnostics, but they are not independent evidence about how the target participant population interprets the material.

### Checking candidates but not condition pools

Every retained message can pass individual thresholds while one condition remains systematically longer, warmer, or more factual than the other.

### Treating equal means as information equivalence

Similar averages on a few measured features do not establish that all relevant background inferences are equal.

### Randomizing before the material is ready

Correct assignment balances participant characteristics. It does not clarify an underspecified or bundled exposure.

### Deleting failed candidates

The final stimulus set then hides the size and character of the search process, weakening reproducibility and inviting selective reporting.

## What should remain outside Session 5

- a full course in experimental design or causal estimands;
- detailed multilevel models with crossed participant and stimulus effects;
- implementation of optimal factorial-vignette designs;
- live image generation as required student work;
- a general repeat of API, OpenRouter, and Ollama setup from Session 1;
- adaptive conversational treatment, which belongs in Session 6;
- synthetic respondents, which belong in Session 7;
- claims that the classroom rating exercise constitutes a real pretest;
- a broad ethics survey disconnected from the treatment-production decisions.

## What students should be able to say at the end

> The model produced candidate messages, not a valid treatment by itself. We defined two frames, saved several candidates for each, recorded how they were produced, checked intended and unintended differences, and kept rejection reasons. Our code makes those decisions easier to audit. It does not prove that respondents interpret the conditions exactly as intended, and random assignment would not fix ambiguous treatment content.

Students should also be able to explain, using actual values, what `candidates`, `rules`, `accepted`, `rejected`, and `reasons` contain at each step of the focal function.

## Review Gate 2 recommendation

Approve the following before the detailed session build:

1. Use the central distinction between a theoretical condition and its material stimuli.
2. Use Wallander, Dafoe et al., and Bai et al. as the required readings.
3. Teach Correll et al. as the main classic sociological application, Schwitter as the explicit generative bridge, and LinkedOut as the visual audit-study extension.
4. Use the fictional paid-parental-leave framing study throughout.
5. Build the code around `review_candidates` and `summarize_pools`, with cached texts, explicit provenance, multiple rejection reasons, and condition-level warnings.
6. State throughout that the classroom materials and ratings are synthetic teaching records and cannot validate an actual experiment.
