# Session 2 literature audit — LLM annotation as measurement

**Status:** Stage 1 review for instructor discussion. No slide sequence should be treated as settled until the synthesis and session architecture are approved.

## What the current draft gets right

The existing Session 2 materials contain a useful applied thread: a model labels public comments about a rezoning proposal, two conditional comments are incorrectly classified as support, and the apparent support rate changes. Stuhler, Dang Ton, and Ollion provide a strong sociological example of turning codebooks into promptbooks. Chae and Davidson provide a useful comparison of model and training choices.

The problem is that these elements are not yet organized around a sufficiently explicit account of measurement. The current deck moves quickly from task types to model comparisons, prompt construction, accuracy, and metrics. It gives too little attention to three questions now central in the literature:

1. What exactly is the construct, and where in the pipeline is its validity established?
2. What happens when the “human reference” is itself produced with LLM assistance or contains reasonable disagreement?
3. What can happen to a regression, prevalence estimate, or group comparison when apparently accurate labels contain patterned error?

## The literature now falls into four connected debates

### 1. A text classifier is part of a measurement pipeline

**Park, Ju Yeon, and Jacob M. Montgomery. 2025. “Toward a Framework for Creating Trustworthy Measures with Supervised Machine Learning for Text.”** *Political Science Research and Methods*. [DOI](https://doi.org/10.1017/psrm.2025.10042).

- Organizes text measurement into stages including label acquisition, model fitting, and out-of-sample imputation.
- Treats validation and reporting as requirements at several points in the pipeline, rather than as one final accuracy number.
- Offers a bridge from established text-as-data practice to LLM annotation without pretending that LLMs create an entirely new measurement problem.
- **Possible course role:** conceptual backbone or optional foundation. Its pipeline can structure the session even if the whole paper is not assigned.

**Desai, Meera, Dallas Card, and Abigail Z. Jacobs. 2026. “Validating LLMs in Social Science: Epistemic Threats and Emerging Norms.”** [arXiv](https://arxiv.org/abs/2607.07915).

- Reviews 2,143 papers from eight flagship social-science journals and identifies 50 LLM measurement tasks in 27 papers.
- Finds that LLM-produced measures often enter the main analysis, while validation practices remain limited and inconsistent.
- Directly connects current practice to construct-validity traditions and shows that the validation gap is empirical, not merely hypothetical.
- **Possible course role:** a very current opening motivation or selected extract. It gives the session a field-level problem rather than a collection of isolated technical warnings.

### 2. Prompt and model choices change the labels

**Stuhler, Oscar, Cat Dang Ton, and Étienne Ollion. 2025. “From Codebooks to Promptbooks: Extracting Information from Text with Generative Large Language Models.”** *Sociological Methods & Research* 54(3):794–848. [DOI](https://doi.org/10.1177/00491241251336794).

- Shows how a sociological codebook becomes an inspectable promptbook in an obituary information-extraction study.
- Demonstrates that variables within one corpus pose different problems: direct extraction, sparse search, categorization, and distributed interpretation.
- Finds substantively patterned errors and shows why simple methods can remain preferable for some variables.
- **Possible course role:** retain as a required sociological application. It is strongest when taught as a study of task definition and error structure, not simply as evidence that prompting works.

**Barrie, Christopher, Elli Palaiologou, and Petter Törnberg. 2024. “Prompt Stability Scoring for Text Annotation with Large Language Models.”** [arXiv](https://arxiv.org/abs/2407.02039).

- Treats robustness to small, substantively equivalent prompt changes as a reliability problem rather than as an informal prompt-engineering exercise.
- Adapts ideas from intra- and inter-coder reliability to define the Prompt Stability Score (PSS), distinguishing repeatability under one prompt from agreement across prompt variants.
- Applies the framework to six datasets and twelve outcomes, covering roughly 3.1 million classifications and 300 million input tokens.
- Finds that stability is lower when the construct is poorly delimited or the data are unsuitable, and that stability can decline even at relatively low temperatures.
- Provides the `promptstability` Python package and recommends preserving prompt variants and their resulting labels as part of the research record.
- **Possible course role:** make this a central paper and code-to-reading bridge. Students can classify the same comments with several substantively equivalent prompts, calculate a simple agreement/stability diagnostic, and inspect which cases change. This also makes the instructor's own active contribution to the area visible.

**Chae, Youngjin, and Thomas Davidson. 2026. “Large Language Models for Text Classification: From Zero-Shot Learning to Instruction-Tuning.”** *Sociological Methods & Research* 55(2):501–567. [DOI](https://doi.org/10.1177/00491241251325243).

- Compares ten models and four regimes for stance classification.
- Shows that larger prompted models can perform well with few labeled examples, while smaller fine-tuned models can remain competitive and less costly.
- **Possible course role:** move from a main required reading to a targeted technical comparison or optional reading. It is valuable, but a long model-regime comparison can pull the session away from its central measurement argument.

**Stoltz, Dustin S., Marshall A. Taylor, and Sanuj Kumar. 2026. “Selecting Language Models for Social Science: Start Small, Start Open, and Validate.”** [arXiv](https://arxiv.org/abs/2601.10926).

- Treats model selection as a question of validity, reliability, reproducibility, and replicability rather than benchmark rank alone.
- Recommends beginning with smaller, open models and constructing delimited, task-specific benchmarks.
- **Possible course role:** optional or concluding model-selection reading. It also links Session 2 forward to the later replication session.

**Heseltine, Michael. 2025–2026. “Comparing Large Language Models for Text Classification: Model Selection Across Tasks, Texts, and Languages.”** [OSF record](https://doi.org/10.31219/osf.io/jvgc5).

- Compares 32 models across several task types, seven languages, and ten country contexts.
- Finds substantial task- and language-specific differences, including cases where open models are competitive and smaller models struggle on more complex or non-English tasks.
- **Possible course role:** current optional evidence on model transportability. Better used to challenge the phrase “best model” than to anchor the week.

### 3. Human labels are produced through a social process

**Schroeder, Hope, Deb Roy, and Jad Kabbara. 2025. “Just Put a Human in the Loop? Investigating LLM-Assisted Annotation for Subjective Tasks.”** *Findings of ACL 2025*:25771–25795. [DOI](https://doi.org/10.18653/v1/2025.findings-acl.1323).

- Uses a preregistered experiment with 350 annotators and 7,000 annotations across four conditions, two models, and two datasets.
- LLM suggestions do not make annotators faster, but they increase confidence and substantially shift the label distribution toward the model suggestions.
- “Human-approved” labels can therefore inherit model influence and make later model evaluations look stronger.
- **Possible course role:** strong substantive and methodological counterweight to a simple human-versus-model validation story. This is the best candidate for making annotation visible as social interaction and epistemic authority.

**Pangakis, Nicholas, and Samuel Wolken. 2025. “Keeping Humans in the Loop: Human-Centered Automated Annotation with Generative AI.”** *ICWSM 2025*. [Article PDF](https://ojs.aaai.org/index.php/ICWSM/article/download/35883/38037/39951).

- Develops a human-centered annotation workflow grounded in human validation labels rather than blind replacement.
- **Possible course role:** practical extension or comparison with Schroeder et al.; not necessary as an additional full required reading.

**Pangakis, Nicholas, Samuel Wolken, and Neil Fasching. 2023. “Automated Annotation with Generative AI Requires Validation.”** [arXiv](https://arxiv.org/abs/2306.00176).

- Replicates 27 annotation tasks across 11 datasets and finds large task-to-task variation.
- Establishes the practical rule that annotation performance must be validated for the exact task and dataset.
- **Possible course role:** useful background and workflow reference. Its main lesson is now better developed by the newer human-centered and validity literature.

### 4. Good first-stage accuracy can still produce bad downstream inference

**Egami, Naoki, Musashi Hinck, Brandon M. Stewart, and Hanying Wei. 2026. “Using Large Language Model Annotations for the Social Sciences: A General Framework of Using Predicted Variables in Downstream Analyses.”** Conditionally accepted, *American Journal of Political Science*. [Author page and preprint](https://brandonstewart.org/publication/using-large-language-model-annotations-social-sciences/).

- Shows that treating predicted variables as if they were observed without error can produce biased estimates and invalid confidence intervals even when annotation accuracy exceeds 90 percent.
- Proposes design-based supervised learning, which combines predicted labels with a probability sample of expert annotations.
- Makes the inferential target—not classifier performance—the criterion for deciding whether labels are adequate.
- **Possible course role:** add as a required or carefully selected reading. This provides the missing hinge from the toy classification task to an actual social-scientific estimate.

## Provisional reading decisions

| Reading | Provisional decision | Reason |
|---|---|---|
| Course chapter §10.2 | Keep required | Provides the course-specific overview and shared vocabulary. |
| Stuhler, Dang Ton & Ollion | Keep required | Best sociological application of codebook → promptbook and patterned error. |
| Egami, Hinck, Stewart & Wei | Add required or assign selected sections | Supplies the missing downstream-inference argument. |
| Schroeder, Roy & Kabbara | Add selected sections or make a central in-class paper | Prevents “human validation” from being treated as neutral and automatic. |
| Chae & Davidson | Move to selected extract or optional | Useful model/regime evidence, but too dominant in the current draft relative to measurement and inference. |
| Barrie, Palaiologou & Törnberg | Add as a central required or selected reading | Supplies the prompt-stability framework, directly motivates a reproducible prompt-variation exercise, and makes the instructor's contribution to the field visible. |
| Park & Montgomery | Use as conceptual scaffolding; optional reading | Gives the full measurement pipeline without overloading the required list. |
| Desai, Card & Jacobs | Use in opening; consider selected extract | Very current evidence that validation practice in published social science is limited. |
| Stoltz, Taylor & Kumar | Optional / bridge forward | Strong on model choice and reproducibility; overlaps later replication material. |
| Heseltine | Optional | Useful new comparative evidence, but not needed for the central argument. |

## What is missing from the current Session 2 deck

The revised deck should not be organized paper by paper. The audit suggests that the session needs a measurement pipeline that each paper changes:

`construct → codebook/reference labels → prompt/model → predicted labels → downstream estimate or claim`

The existing rezoning case can remain, but it should be used to expose a failure at every link:

- Does “support” include conditional acceptance?
- Who decided the human label, and were they shown the model suggestion?
- Do substantively equivalent prompt variants produce stable labels, and which cases lower the Prompt Stability Score?
- Which cases become false positives, and are the errors patterned?
- How does the error change prevalence, group differences, or a regression coefficient?
- What validation sample or correction design would support the final claim?

This gives the week a coherent sociological argument: annotation is not clerical preprocessing. It is the construction of a variable through rules, people, models, and validation decisions, and those decisions shape the evidence available for later inference.
