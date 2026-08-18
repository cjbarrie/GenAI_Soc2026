# Session 5 — Can generated media isolate a causal construct?

**Date:** Wednesday, September 30, 2026 · 9:30 a.m.–12:15 p.m.  
**Course movement:** Intervene  
**Methodological domain:** Treatment and stimulus generation  
**Chapter anchor:** *AI and Research Methods*, §10.3, especially §§10.3.3–10.3.5

## Substantive question

Can generated media isolate a causal construct?

## Learning objectives

By the end, students should be able to:

1. state the inferential target: construct a treatment set whose accepted variants satisfy a predeclared fidelity rule.
2. explain the reading disagreement in their own words;
3. identify the Python type of every major input and output in the worked trace;
4. explain each line or small block of `construct_treatments`;
5. use the validation diagnostic to bound a sociological claim.

## Required readings

- [Dafoe, Zhang & Caughey (2018), information equivalence](https://doi.org/10.1017/pan.2018.9)
- [Evsyukova, Rusche & Mill (2025), LinkedOut](https://doi.org/10.1093/qje/qjae035)
- [Bai et al. (2025), LLM-generated policy messages](https://doi.org/10.1038/s41467-025-61345-5)

## Lecture argument

Generating many stimuli increases design capacity only if intended and nuisance variation are inspected separately. AI-generated profiles and messages enable scale; information equivalence asks whether conditions differ only in the information the design intends to manipulate.

## Computational trace

Students move from visible synthetic inputs through `construct_treatments` to a printed output and explicit checks. The required task uses no live API. Every code block is read as **input → Python type → operation → output → research meaning**.

## Weekly completion task

Construct factorial treatment records and filter variants that violate a fidelity bound. Submit a prediction, working code, interpreted check, and 100–150 word reading-linked claim. Completion marks only; missing elements may be supplied within one week.

## Validation focus

Condition labels are randomized correctly, but tone or length changes alongside the causal construct.
