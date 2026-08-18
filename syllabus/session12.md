# Session 12 — What can we reproduce, and what remains opaque?

**Date:** Wednesday, November 25, 2026 · 9:30 a.m.–12:15 p.m.  
**Course movement:** Delegate and audit  
**Methodological domain:** Low-stakes replication and project studio  
**Chapter anchor:** *AI and Research Methods*, §10.8

## Substantive question

What can we reproduce, and what remains opaque?

## Learning objectives

By the end, students should be able to:

1. state the inferential target: compare two replication records and classify the visible sources of dependence.
2. explain the reading disagreement in their own words;
3. identify the Python type of every major input and output in the worked trace;
4. explain each line or small block of `compare_replication_records`;
5. use the validation diagnostic to bound a sociological claim.

## Required readings

- [Feuerriegel et al. (2026), GUIDE-LLM reporting checklist](https://doi.org/10.1038/s41562-026-02492-7)
- [Barrie, Palmer & Spirling (2025), replication for language models](https://arthurspirling.org/documents/BarriePalmerSpirling_TrustMeBro.pdf)

## Lecture argument

A discrepancy is useful evidence when the changed configuration fields are isolated rather than hidden by the word replication. Reporting checklists make workflows inspectable; model/provider dependence means even apparently deterministic reruns may not recreate an earlier transformation.

## Computational trace

Students move from visible synthetic inputs through `compare_replication_records` to a printed output and explicit checks. The required task uses no live API. Every code block is read as **input → Python type → operation → output → research meaning**.

## Weekly completion task

Produce a discrepancy report from cached and rerun configurations. Submit a prediction, working code, interpreted check, and 100–150 word reading-linked claim. Completion marks only; missing elements may be supplied within one week.

## Validation focus

A changed answer is called randomness even though the model identifier, provider route, or prompt also changed.
