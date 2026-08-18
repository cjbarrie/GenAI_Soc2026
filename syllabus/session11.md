# Session 11 — Who—or what—produces research data in an agentic workflow?

**Date:** Wednesday, November 18, 2026 · 9:30 a.m.–12:15 p.m.  
**Course movement:** Delegate and audit  
**Methodological domain:** Research agents, tools, and provenance  
**Chapter anchor:** *AI and Research Methods*, §10.6

## Substantive question

Who—or what—produces research data in an agentic workflow?

## Learning objectives

By the end, students should be able to:

1. state the inferential target: produce a deduplicated claim/source table that a human can verify without rerunning the agent.
2. explain the reading disagreement in their own words;
3. identify the Python type of every major input and output in the worked trace;
4. explain each line or small block of `build_provenance_table`;
5. use the validation diagnostic to bound a sociological claim.

## Required readings

- [Lu et al. (2026), end-to-end automation of AI research](https://doi.org/10.1038/s41586-026-10265-5)
- [Nature Machine Intelligence (2026), multi-agent systems need transparency](https://www.nature.com/articles/s42256-026-01183-2)

## Lecture argument

Delegation is scientifically useful only when every claim can be traced backward to a resolvable source and recorded transformation. End-to-end systems automate search, code, analysis, and writing; transparency arguments ask whether multiplying agents adds justified capability or merely obscures responsibility.

## Computational trace

Students move from visible synthetic inputs through `build_provenance_table` to a printed output and explicit checks. The required task uses no live API. Every code block is read as **input → Python type → operation → output → research meaning**.

## Weekly completion task

Deduplicate collected sources while rejecting claims without a URL and exact excerpt. Submit a prediction, working code, interpreted check, and 100–150 word reading-linked claim. Completion marks only; missing elements may be supplied within one week.

## Validation focus

Several agents repeat the same unsupported claim, creating apparent corroboration without independent evidence.
