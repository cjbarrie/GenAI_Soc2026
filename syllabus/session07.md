# Session 7 — Whose attitudes and experiences do synthetic populations represent?

**Date:** Wednesday, October 21, 2026 · 9:30 a.m.–12:15 p.m.  
**Course movement:** Simulate  
**Methodological domain:** Silicon sampling and representation  
**Chapter anchor:** *AI and Research Methods*, §10.4

## Substantive question

Whose attitudes and experiences do synthetic populations represent?

## Learning objectives

By the end, students should be able to:

1. state the inferential target: compare human and synthetic distributions at the group level without reducing fit to one mean.
2. explain the reading disagreement in their own words;
3. identify the Python type of every major input and output in the worked trace;
4. explain each line or small block of `group_summaries`;
5. use the validation diagnostic to bound a sociological claim.

## Required readings

- [Kozlowski & Evans (2025), simulating subjects](https://doi.org/10.1177/00491241251337316)
- [Boelaert et al. (2025), machine bias in opinion polls](https://doi.org/10.1177/00491241251330582)
- [Wang, Morgenstern & Dickerson (2025), identity flattening](https://doi.org/10.1038/s42256-025-00986-z)

## Lecture argument

Matching a group mean is compatible with erasing the dispersion that constitutes social heterogeneity. Simulated subjects promise collective representation; polling and identity studies show topic-specific bias and compressed within-group variation.

## Computational trace

Students move from visible synthetic inputs through `group_summaries` to a printed output and explicit checks. The required task uses no live API. Every code block is read as **input → Python type → operation → output → research meaning**.

## Weekly completion task

Calculate group means and population variances for human and synthetic records. Submit a prediction, working code, interpreted check, and 100–150 word reading-linked claim. Completion marks only; missing elements may be supplied within one week.

## Validation focus

The reported average matches while synthetic respondents repeat nearly identical answers within every identity group.
