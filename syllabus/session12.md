# Session 12 — What can we reproduce, and what remains opaque?

**Date:** Wednesday, November 25, 2026 · 9:30 a.m.–12:15 p.m.  
**Course movement:** Delegate and audit  
**Methodological domain:** Low-stakes replication and project studio  
**Chapter anchor:** *AI and Research Methods*, §10.7

## Substantive question

What can we reproduce, and what remains opaque?

## Learning objectives

By the end, students should be able to:

1. state the inferential target: compare two replication records and classify the visible sources of dependence.
2. explain the reading disagreement in their own words;
3. identify the Python type of every major input and output in the worked trace;
4. compare two saved trajectory dictionaries field by field;
5. use the validation diagnostic to bound a sociological claim.

## Required readings

- [Feuerriegel et al. (2026), GUIDE-LLM reporting checklist](https://doi.org/10.1038/s41562-026-02492-7)
- [Barrie, Palmer & Spirling (2025), replication for language models](https://arthurspirling.org/documents/BarriePalmerSpirling_TrustMeBro.pdf)

## Lecture argument

A discrepancy is useful evidence when the changed configuration fields are isolated rather than hidden by the word replication. Reporting checklists make workflows inspectable; model/provider dependence means even apparently deterministic reruns may not recreate an earlier transformation.

## Computational trace

Planned: students load the Week 11 trajectory, rerun the same question with at most three calls, save every event and compare route, model, prompt, parameters, tool results and final claim.

## Weekly completion task

Planned: submit a narrated screen recording explaining which inputs were held fixed, which fields changed and what the discrepancy can establish. Upload it through the [recording guide and Box folder](https://cjbarrie.github.io/GenAI_Soc2026/recording-and-submission.html) by 5:00 p.m. Eastern on the Tuesday before the next class. This remains a low-stakes holiday-week task.

## Validation focus

A changed answer is called randomness even though the model identifier, provider route, or prompt also changed.
