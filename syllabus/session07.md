# Session 7 — Whose attitudes do synthetic respondents represent?

**Date:** Wednesday, October 21, 2026 · 9:30 a.m.–12:15 p.m.  
**Methodological domain:** Synthetic respondents and population representation

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

- [Kozlowski and Evans (2025), “Simulating Subjects”](https://doi.org/10.1177/00491241251337316), complete article.
- [Boelaert et al. (2025), “Machine Bias”](https://doi.org/10.1177/00491241251330582), complete article.
- [Igarashi, Kano and Miwa (2025), “ChatGPT versus Humans in Judging Discriminatory Scenarios”](https://doi.org/10.1057/s41599-025-06054-6), complete article.

## Lecture argument

Igarashi, Kano and Miwa ask Japanese respondents and GPT-4 to judge the same experimentally varied cases of unequal treatment. That applied case lets us compare not just average severity ratings but whether humans and a model respond similarly to ethnicity, gender, sexuality and different justifications for unequal treatment. Kozlowski and Evans and Boelaert et al. help us specify what kind of resemblance that comparison can establish.

## Computational trace

Students give a deidentified public-use profile and exact `POLVIEWS` item to a hosted or local model. A JSON schema requires one predicted category and seven probabilities. Students inspect the raw JSON, parsed dictionary, probability list, length and sum, then reveal the held-out answer. Every block is read as **input → Python type → operation → output → research meaning → limit**.

## Weekly completion task

Change one profile field, rerun with the chosen route and submit a narrated screen recording explaining every input, schema field, call argument and returned value. Explain why valid structure is not evidence of representativeness. Upload it through the [recording and submission guide](https://cjbarrie.github.io/GenAI_Soc2026/recording-and-submission.html) by 5:00 p.m. Eastern on the Tuesday before the next class. Completion marks only.

## Validation focus

Structured output validates the form of the returned record, not its substantive accuracy. Aggregate fit, held-out individual accuracy, within-group variation and population representation remain separate targets.
