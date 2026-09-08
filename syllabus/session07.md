# Session 7 — Whose attitudes do synthetic respondents represent?

**Date:** Wednesday, October 21, 2026 · 9:30 a.m.–12:15 p.m.  
**Course movement:** Simulate  
**Methodological domain:** Synthetic respondents and population representation
**Chapter anchor:** *AI and Research Methods*, §10.3

## Substantive question

What kind of evidence is produced when a model answers a survey question as if it were a person?

## Learning objectives

By the end, students should be able to:

1. distinguish a human respondent, aggregate prediction, demographic persona and interview-grounded agent;
2. explain how survey design links responses to a population claim;
3. identify which feature of human data a validation statistic checks;
4. trace every input, type, update and output in a structured OpenRouter or Ollama call;
5. distinguish validation of an aggregate prediction from validation of held-out profile predictions.

## Required readings

- [Kozlowski & Evans (2025), simulating subjects](https://doi.org/10.1177/00491241251337316)
- [Boelaert et al. (2025), machine bias in opinion polls](https://doi.org/10.1177/00491241251330582)
- [Wang, Morgenstern & Dickerson (2025), identity flattening](https://doi.org/10.1038/s42256-025-00986-z)

## Lecture argument

A synthetic respondent is a model output conditioned on a description or record, not a sampled member of the described social group. Matching a mean or majority answer does not show that the model preserves a full distribution, within-group heterogeneity, subgroup relationships or the social process that produced human responses.

## Computational trace

Students give a deidentified public-use profile and exact `POLVIEWS` item to a hosted or local model. A JSON schema requires one predicted category and seven probabilities. Students inspect the raw JSON, parsed dictionary, probability list, length and sum, then reveal the held-out answer. Every block is read as **input → Python type → operation → output → research meaning → limit**.

## Weekly completion task

Change one profile field, rerun with the chosen route and submit a narrated screen recording explaining every input, schema field, call argument and returned value. Explain why valid structure is not evidence of representativeness. Upload it through the [recording guide and Box folder](https://cjbarrie.github.io/GenAI_Soc2026/recording-and-submission.html) by 5:00 p.m. Eastern on the Tuesday before the next class. Completion marks only.

## Validation focus

Structured output validates the form of the returned record, not its substantive accuracy. Aggregate fit, held-out individual accuracy, within-group variation and population representation remain separate targets.
