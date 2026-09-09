# Session 2 synthesis — What makes an LLM label usable as a measure?

**Status:** Stage 2 synthesis for instructor review. This identifies the intellectual structure of the session; it is not yet a slide outline.

## Central argument

An LLM does not simply discover a variable that was already sitting inside a text. Researchers construct that variable through a sequence of decisions about the concept, the coding rules, the prompt, the reference procedure, the validation sample, and the intended analysis.

The session should therefore follow this chain:

`construct → codebook/reference procedure → prompt variants + model → predicted labels → downstream estimate or claim`

The central teaching claim is:

> An LLM-generated label becomes usable as a sociological measure only when the construct, reference procedure, prompt stability, error pattern, and downstream use have been evaluated for the exact research task.

This is stronger than “validate the model.” It tells students what must be validated, why the checks differ, and how the result of one check changes the next research decision.

## Revised historical spine

The session should not begin as if annotation appeared with LLMs. Its sociology-specific prehistory is part of the argument:

1. **Rule-based content and narrative analysis:** Franzosi shows how sociologists translate narrative accounts into structured relations among actors and actions. The codebook links a theoretical construct to repeatable decisions about text.
2. **Human coding teams:** researchers train coders, compare decisions, adjudicate disagreement, and revise rules. This establishes the reference procedure from which later automation inherits both strengths and ambiguities.
3. **Distributed crowd work:** MTurk and Prolific make it easier to assign small coding tasks to many workers. They change recruitment, scale, monitoring, and labour conditions; they do not remove the need for a construct, unit, categories, and quality checks.
4. **Supervised text classifiers:** models learn a mapping from documents to the labels humans already produced. The labelled training set remains central.
5. **Prompted LLM annotation:** researchers can give written rules and a new text directly to a general-purpose model. This reduces the need for task-specific training while making prompt specification, model access, response structure, and stability part of the measurement procedure.

This history should be shown through one concrete comment and one continuous question: who or what applies the same coding rule, and what new evidence is required when that arrangement changes?

## Five cumulative lessons

### 1. Before asking whether the label is accurate, define what it is meant to measure

The first task is not model selection. It is specifying the construct, unit of analysis, permitted categories, boundary cases, and intended use.

Stuhler, Dang Ton, and Ollion show why the same corpus can contain quite different measurement problems. Extracting a stated age, locating sparse evidence of military service, and summarizing an occupation are not interchangeable tasks. Turning a codebook into a promptbook is valuable because it makes previously tacit rules inspectable. It does not, by itself, establish that those rules represent the construct well.

The rezoning case should therefore begin with a genuine measurement choice:

- **Construct:** explicit support for adopting a particular proposal.
- **Unit:** one public comment by one speaker.
- **Boundary case:** a speaker who likes more housing but supports the proposal only if specified conditions change.
- **Downstream use:** estimating the proportion of speakers who explicitly support adoption.

If the construct instead becomes “openness to more housing,” the same conditional statement may receive a different defensible label. The correct code is not contained in the sentence independently of the research question.

### 2. The prompt is part of the measurement instrument

Barrie, Palaiologou, and Törnberg provide the central reliability argument. Semantically equivalent prompts should not produce substantially different variables. They adapt intra- and inter-coder reliability to distinguish:

- **intra-prompt stability:** whether repeated use of the same prompt produces consistent labels;
- **inter-prompt stability:** whether substantively equivalent prompt variants produce consistent labels.

Prompt Stability Score makes prompt robustness an inspectable diagnostic rather than an informal exercise in trying several prompts and choosing the one that performs best.

The important conceptual distinction is:

- **Stability is not validity.** A prompt can consistently produce the wrong label.
- **Instability is diagnostic.** It may indicate an unclear construct, an underspecified boundary rule, unsuitable source text, or a brittle model/task combination.

The course code should therefore preserve prompt variants and compare their outputs case by case. Students should not be asked to implement Krippendorff's alpha from scratch. They can first calculate a transparent proportion of cases with identical labels across variants, inspect disagreements, and then use a supplied helper to connect this intuition to PSS.

### 3. A “human reference” is also produced through a measurement process

The simple story—models generate labels and humans provide ground truth—is inadequate for subjective social-science constructs.

Schroeder, Roy, and Kabbara show that presenting annotators with LLM suggestions can shift the resulting label distribution toward the model while increasing annotator confidence. In their experiment, this did not make annotators faster. Human approval therefore does not necessarily supply an independent check: it can transmit the model's influence into the benchmark used to evaluate the model.

The session should distinguish:

- an independently produced expert or human-reference procedure;
- an AI-assisted adjudication procedure;
- genuine disagreement or ambiguity among reasonable coders;
- clerical review of format or evidence;
- substantive review of the construct and label.

This is the week's main substantive-sociological contribution. Annotation is a distribution of epistemic authority among investigators, annotators, model providers, and the model output. “Human in the loop” names an arrangement of authority; it is not automatically a validation design.

A short paired aside should extend the provenance question to the source text. Agarwal, Naaman, and Vashistha find that autocomplete suggestions made Indian and American participants' writing more similar and moved measured features of Indian writing toward unassisted American writing. The point for this session is narrow but important: if the comments being classified were written with AI assistance, the corpus may itself be a hybrid human–model product. Researchers may need to record both `reference_source` and `text_production_mode`, particularly before interpreting group differences in voice, style, or cultural expression. The newer Williams-Ceci et al. attitude experiments and Bhat et al. account of “reactive writing” can appear as optional extensions rather than additional core readings.

### 4. Accuracy summarizes cases; the error pattern explains what the measure does

Aggregate accuracy, precision, recall, and F1 remain useful, but none can show by itself whether the errors are sociologically consequential.

The Stuhler et al. study shows task- and subgroup-patterned error. The rezoning example should make the same point in a simpler setting: both false positives should arise from conditional statements containing favorable language. The shared failure is theoretically meaningful—the classifier identifies positive language about housing but underweights the condition that determines stance toward the proposal.

Students should therefore move through three levels of validation:

1. **Case level:** which texts changed or were misclassified, and what do they have in common?
2. **Category level:** which classes have poor precision or recall?
3. **Substantive-quantity level:** how do those errors change the prevalence, group comparison, trend, or relationship the study reports?

A better prompt may reduce the errors. A new `CONDITIONAL` category may represent the construct better. Or the research question may need to change. Error analysis can revise theory and measurement, not merely tune a classifier.

### 5. The required validation depends on what researchers do with the labels next

Egami, Hinck, Stewart, and Wei supply the endpoint missing from the current draft. Predicted labels are usually not the final result; they become dependent variables, independent variables, subgroup counts, prevalence estimates, trends, or inputs to other analyses.

They show that directly treating predicted variables as error-free can produce biased coefficients and invalid confidence intervals even when annotation accuracy is above 90 or 95 percent. Small error rates are not harmless when errors correlate with variables used in the downstream analysis.

This changes the practical question from:

> Is the classifier accurate enough?

to:

> What evidence and research design make this particular downstream estimate credible?

For beginners, the session should explain the design logic without teaching the full doubly robust estimator. Students need to understand that a probability sample of independently expert-coded documents can be combined with large-scale predicted labels, and that the sampling design matters. The technical implementation of design-based supervised learning can remain optional or appear later.

## Four checks that must remain distinct

| Check | Question | A passing result does **not** establish |
|---|---|---|
| Construct validity | Do the rules and categories represent the intended concept? | That the model applies them consistently or accurately. |
| Prompt stability / reliability | Do repeated or equivalent prompts yield similar labels? | That the stable labels are substantively correct. |
| Reference agreement / predictive performance | Do model labels match an independently produced reference sample? | That the remaining errors are harmless for the final analysis. |
| Downstream inferential validity | Does the analysis account for annotation error well enough to support the estimate or claim? | That the construct or reference process was well chosen. |

The slides should repeatedly return to this distinction. It prevents “validation” from becoming a vague word that means any favorable statistic.

## The productive disagreements among the papers

The literature should be taught as a sequence of complications rather than as a consensus list:

1. **Stuhler et al.:** greater promptbook explicitness can improve and document a coding process.
2. **Barrie et al.:** one explicit prompt is insufficient if equivalent specifications produce different variables.
3. **Schroeder et al.:** a human check is insufficient if the model helped produce the labels used as the check.
4. **Egami et al.:** high agreement is insufficient if the remaining errors distort the downstream estimand and its uncertainty.

Park and Montgomery provide the broader measurement pipeline connecting these problems. Desai, Card, and Jacobs show why the sequence matters now: LLM-generated measurements are already entering primary analyses while published validation practices remain limited and inconsistent.

Chae and Davidson remain useful for a narrower point: model size and training regime are choices within the measurement pipeline. They should no longer organize a major section of the session.

## What the applied example must demonstrate

The rezoning example remains useful if it becomes a single continuous research workflow rather than a toy classifier followed by disconnected metrics.

### Stage A — Define the variable

Students compare two possible targets:

- explicit support for adopting the proposal;
- openness to additional housing under some conditions.

They see that the same text can be coded differently because the constructs differ.

### Stage B — Build and vary the prompt instrument

Students inspect a codebook and two or three substantively equivalent prompt variants. Cached outputs keep the activity reproducible and free of API requirements. An optional live OpenRouter call uses the same saved input structure.

### Stage C — Measure stability

Students assemble a record containing `comment_id`, `prompt_variant`, and `label`. They use a loop to identify cases whose labels differ across variants, calculate a transparent stability proportion, and interpret a supplied PSS value.

### Stage D — Evaluate against an independent reference procedure

Students compare the model labels with independently coded reference labels. The Schroeder et al. result is then used to ask what would change if the human coders had first seen the model suggestion.

### Stage E — Follow the error into the substantive estimate

Students show how the unstable or false-positive conditional cases change the estimated level of support. They then identify what additional validation sample or correction design would be needed before making a population or subgroup claim.

## Reading-to-code alignment

| Reading contribution | Object or operation in the code | Interpretation students should make |
|---|---|---|
| Stuhler et al.: codebook → promptbook | `CODEBOOK`, boundary rule, message dictionaries | The prompt encodes a measurement decision. |
| Barrie et al.: equivalent prompts may be unstable | list of prompt variants; label comparison loop; supplied PSS helper | A prompt is a specification that must survive reasonable perturbation. |
| Schroeder et al.: AI suggestions influence human labels | `reference_source` field and independent/assisted label comparison | “Human-reviewed” does not necessarily mean independent validation. |
| Agarwal, Naaman & Vashistha: AI suggestions can reshape source text | optional `text_production_mode` field | The material being measured may already reflect model influence. |
| Egami et al.: predicted variables affect later estimates | human/model support proportions and one simple subgroup or coefficient illustration | First-stage accuracy cannot stand in for validity of the final estimate. |
| Course chapter / Park & Montgomery | complete research record and validation checklist | Every stage and decision must remain inspectable. |

## Recommended reading configuration

To keep the reading load broadly consistent:

### Required

1. Course chapter, §§10.2.1–10.2.5.
2. Stuhler, Dang Ton, and Ollion — focus on promptbooks, task differences, and non-random error rather than every model comparison.
3. Barrie, Palaiologou, and Törnberg — prompt stability framework, empirical demonstration, and recommendations.
4. Egami, Hinck, Stewart, and Wei — selected introduction, Figure 1, the high-accuracy/downstream-bias result, and the practical design logic rather than the estimator derivations.

### Taught in class through figures or selected pages

- Schroeder, Roy, and Kabbara — experimental design and the changes in confidence and label distributions.
- Desai, Card, and Jacobs — corpus of published uses and distribution of validation practices.
- Park and Montgomery — measurement-pipeline figure or framework.

### Optional

- Chae and Davidson — detailed model and training-regime comparison.
- Stoltz, Taylor, and Kumar — open/small model selection and replicability.
- Heseltine — model performance across tasks, languages, and country contexts.

## What students should be able to say at the end

A successful student explanation would sound like this:

> The model output is a proposed value for a variable, not the variable itself. We first decide what the construct and boundary rules mean. We then check whether equivalent prompts produce stable labels, compare the labels with an independently produced reference sample, inspect which cases fail, and determine whether those errors change the estimate we care about. A high accuracy score can be useful, but it cannot substitute for those other checks.

That explanation should govern the later slide sequence, workbook, completion task, and oral-assessment practice.
