# Session 3 literature audit — LLMs in qualitative interpretation

**Status:** Stage 1 review for instructor discussion. The current slides and exercise are a scaffold, not an approved session design.

## What the current draft gets right

The existing materials make one useful demand: an LLM-proposed theme should remain linked to the source material and to a researcher decision. The code is deliberately small, and its inputs and outputs can be explained to students with limited Python experience.

The problem is that the present exercise equates an exact quotation with an auditable interpretation. Its function accepts a proposal whenever the supplied quotation appears verbatim in the source excerpt. That is a retrieval check. It can identify a fabricated or altered quotation, but it cannot tell us whether:

- the quotation actually supports the proposed theme;
- the theme represents a pattern rather than one striking passage;
- contradictory or deviant cases have been considered;
- the sequence and context of an account have been preserved;
- an alternative interpretation is more plausible; or
- the researcher's own role in producing the interpretation is visible.

The two one-sentence excerpts in the current draft also lack a recognizable research setting. Students are asked to evaluate an interpretation before they know who was interviewed, why the material was collected, what the unit of analysis is, or what the research question is. This repeats the problem corrected in Session 2: a result appears before the provenance and stakes of the example are established.

## The literature now falls into four connected debates

### 1. LLMs can assist parts of a qualitative workflow without performing the whole analysis

**Than, Kyi, et al. 2025. “Updating ‘The Future of Coding’: A Researcher–LLM–Researcher Approach to Qualitative Analysis.”** *Sociological Methods & Research*. [DOI](https://doi.org/10.1177/00491241251339188).

- Reanalyzes a project involving more than 1,200 U.S. newsweekly articles published between 1980 and 2012.
- The task is not simple keyword retrieval: identifying discussion of inequality often requires reading the document as a whole.
- Compares prompt structures across open and closed models and proposes a researcher–LLM–researcher workflow.
- Keeps human researchers responsible for concept refinement, prompt and coding-guide development, validation, and close reading at consequential stages.
- Suggests that disagreement across prompts or models can help target documents for human review.
- **Course role:** the constructive workflow paper. It shows a credible division of labor without treating the LLM as an autonomous qualitative analyst.

**Dunivin, Zackary O. 2025. “Scaling Hermeneutics: A Guide to Qualitative Coding with LLMs for Reflexive Content Analysis.”** *EPJ Data Science*. [Article](https://link.springer.com/article/10.1140/epjds/s13688-025-00548-8).

- Develops a hybrid workflow in which humans build and refine a codebook, validate model coding, and interpret results, while the LLM scales application of the codes.
- Finds large differences between model generations and tasks, reinforcing the need for task-specific validation.
- **Course role:** optional practical extension. It supports Than et al. but is not needed as another full required reading.

### 2. Qualitative use requires technological reflexivity, not only technical validation

**Ibrahim, Yasmin, and Andrea Voyer. 2026. “Technological Reflexivity in Qualitative Research with Large Language Models.”** *Qualitative Research*. [DOI](https://doi.org/10.1177/14687941251390794).

- Organizes technological reflexivity around model bias, researcher–algorithm interaction, critical evaluation, transparency, epistemic reflection, and ethics.
- Uses both a deductive study of politicians' Twitter self-descriptions and an inductive study of smoking in etiquette books.
- In the inductive example, the researchers read and memoed the material before sharing it with the model.
- Treats prompts and chats as part of the history of the analysis: researchers shape model outputs, but model outputs can also redirect researchers' attention.
- Shows why frequency or novelty is not enough. A model-highlighted theme can prove too marginal once the researcher returns to the corpus and its context.
- **Course role:** the reflexive backbone. It gives students concrete practices for documenting their interaction with the model and returning to the source material.

**Schroeder, Hope, et al. 2025. “Large Language Models in Qualitative Research: Uses, Tensions, and Intentions.”** *CHI 2025*. [DOI](https://doi.org/10.1145/3706598.3713120).

- Draws on interviews with qualitative researchers about current uses, hopes, and concerns.
- Surfaces questions about performance, participant interests, emerging norms, and whether models can serve as interlocutors without displacing human meaning-making.
- **Course role:** brief sociological aside. It lets the class consider how a professional community is negotiating acceptable use, rather than presenting the issue only as a technical choice.

### 3. A plausible theme and a real quotation do not establish interpretive validity

**Nguyen, Linh, and Catherine Welch. 2026. “Analyzing—or Just Chatting? The Epistemic Risks of Large Language Models in Qualitative Data Analysis.”** *Organizational Research Methods*. [DOI](https://doi.org/10.1177/10944281251377154).

- Evaluates ChatGPT-4o and dedicated qualitative-AI software using the authors' own datasets, published studies, and vendor claims.
- Distinguishes lower-order organization and coding from higher-order interpretation, causal reasoning, counterintuitive patterns, and theorization.
- Finds outputs that look professionally plausible but contain overlapping themes, omissions, thin summaries, lost chronology, and uneven use of the corpus.
- Demonstrates the key weakness in the existing course exercise: a quotation may be verbatim while its relationship to a theme remains unclear or misleading.
- Argues that “prompting harder” does not remove the category and epistemic problems, and can wrongly relocate responsibility from the tool to the user.
- **Course role:** the strong counterposition. It forces the session to specify what an LLM-supported workflow can and cannot warrant.

**Mehta, S., et al. 2025. “Comparing Large Language Model and Human Qualitative Analysis in a Study of Sexual and Reproductive Health.”** *Scientific Reports*. [Article](https://www.nature.com/articles/s41598-025-18969-w).

- Compares GPT-4o thematic analysis with experienced human analysis of interviews conducted in rural western Kenya.
- Finds that themes can appear complete while quotation support is much weaker and variable.
- Documents altered, truncated, and combined quotations that change meaning.
- Concludes that LLMs may help identify themes, keywords, or possible omissions, but are not equivalent to experienced qualitative analysis.
- **Course role:** empirical worked failure or paper screenshot. It makes “plausible theme, weak evidence” visible without adding another required reading.

### 4. Rapid adoption has outpaced transparent reporting

**Kempny, Christina, et al. 2026. “Large Language Models in Qualitative Health Research: A Scoping Review.”** *BMC Medical Research Methodology*. [Article](https://link.springer.com/article/10.1186/s12874-026-02913-1).

- Reviews 75 peer-reviewed empirical studies published through May 2025.
- Finds that most studies use LLMs for coding, theme identification, or thematic analysis, with descriptive and deductive uses more common than interpretive synthesis.
- Reports sparse disclosure of prompts, deployment configurations, temperatures, context lengths, and other parameters.
- Recommends extending qualitative reporting conventions to cover the model-assisted parts of the analysis.
- **Course role:** state-of-the-field opening and optional reading. It establishes that provenance and reporting are live methodological problems rather than course-specific caution.

**COREQ+LLM protocol. 2025.** [Protocol](https://pmc.ncbi.nlm.nih.gov/articles/PMC12508663/).

- Extends reporting-checklist work toward qualitative studies using LLMs.
- **Course role:** practical bridge to the research record students construct in code. The course should not teach checklist compliance as a substitute for reflexivity, but the checklist can make missing information concrete.

## The disagreement the class should encounter

The literature does not support a simple verdict that LLM qualitative analysis either “works” or “does not work.” It instead offers different accounts of what the activity is:

1. **Than et al.:** an LLM can take a bounded role inside a researcher-led coding workflow.
2. **Ibrahim and Voyer:** the interaction with the model becomes part of the interpretive process and must itself be examined.
3. **Nguyen and Welch:** fluent outputs can encourage a category error in which organization or plausible summarization is mistaken for qualitative interpretation.
4. **Mehta et al.:** even apparently coherent themes can rest on poor or altered evidence.

The useful teaching question is therefore not “Can an LLM do qualitative research?” It is:

> Where in a qualitative analysis can an LLM participate, and what must remain visible for the resulting interpretation to be credible?

## Provisional reading decisions

| Reading | Provisional decision | Reason |
|---|---|---|
| Course chapter §10.3 | Keep required | Gives the shared course vocabulary and workflow. |
| Than et al. | Keep required | Best constructive sociological workflow and a substantial empirical setting. |
| Ibrahim & Voyer | Keep required | Supplies technological reflexivity and concrete documentation practices. |
| Nguyen & Welch | Keep required | Provides the necessary epistemic counterargument and shows why quotations alone are insufficient. |
| Kempny et al. | Selected figure/table in class; optional paper | Current overview of actual use and reporting gaps. |
| Mehta et al. | Teach through selected results and a paper screenshot | Strong empirical demonstration of plausible themes with weak evidence. |
| Schroeder et al. | Brief aside or optional | Adds researchers' own norms and concerns without overloading the core sequence. |
| Dunivin | Optional | Useful applied extension, but overlaps the constructive role of Than et al. |
| COREQ+LLM | Practical reference | Converts provenance and reporting into fields students can inspect. |

## What is missing from the current Session 3 materials

The rebuilt week needs:

- a real research question and a small but coherent synthetic interview study;
- a distinction between retrieval, coding, theming, and interpretation;
- multiple excerpts so a “theme” can be evaluated as a pattern across cases;
- context, sequence, a negative or deviant case, and a plausible alternative interpretation;
- a record of what the model proposed, what prompt and model produced it, and what the researcher decided;
- code whose output identifies an **incomplete interpretive record**, not a mechanically “valid theme”; and
- a clear account of which parts require human reading and judgment.

The bounded claim should become:

> Source traceability is necessary, but an interpretation becomes auditable only when its supporting evidence, counterevidence, context, alternatives, model interaction, and researcher judgment remain inspectable.
