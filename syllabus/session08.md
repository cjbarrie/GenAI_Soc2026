# Session 8 — Can LLMs recover missing or unobserved social worlds?

**Date:** Wednesday, October 28, 2026 · 9:30 a.m.–12:15 p.m.  
**Course movement:** Simulate  
**Methodological domain:** Opinion prediction, validation, and limits  
**Chapter anchor:** *AI and Research Methods*, §§10.4.4–10.4.5 and §10.9

## Substantive question

Can LLMs recover missing or unobserved social worlds?

## Learning objectives

By the end, students should be able to:

1. state the inferential target: score individual error, aggregate error, and group-gap error separately.
2. explain the reading disagreement in their own words;
3. identify the Python type of every major input and output in the worked trace;
4. explain each line or small block of `score_inferential_targets`;
5. use the validation diagnostic to bound a sociological claim.

## Required readings

- [Kim & Lee (2026), AI-augmented surveys](https://arxiv.org/abs/2305.09620)
- [Xie et al. (2026), statistical realism](https://doi.org/10.1073/pnas.2538145123)
- [Ashokkumar et al. (2026), predicting experiment results](https://doi.org/10.1038/s41586-026-10742-x)

## Lecture argument

Validation must be chosen for the inferential target: individuals, aggregates, associations, and effects are different achievements. AI-augmented surveys seek unasked opinions; population realism and experiment forecasting show that success on one statistical target need not transfer to another.

## Computational trace

Students move from visible synthetic inputs through `score_inferential_targets` to a printed output and explicit checks. The required task uses no live API. Every code block is read as **input → Python type → operation → output → research meaning**.

## Weekly completion task

Calculate three target-specific errors from matched human and synthetic records. Submit a prediction, working code, interpreted check, and 100–150 word reading-linked claim. Completion marks only; missing elements may be supplied within one week.

## Validation focus

A strong aggregate correlation is presented as evidence that individual opinions or causal effects have been recovered.
