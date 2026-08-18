# Session 4 — What counts as evidence across text, image, and audio?

**Date:** Wednesday, September 23, 2026 · 9:30 a.m.–12:15 p.m.  
**Course movement:** Observe  
**Methodological domain:** Multimodal measurement  
**Chapter anchor:** *AI and Research Methods*, §10.2 and multimodal discussion in §10.7

## Substantive question

What counts as evidence across text, image, and audio?

## Learning objectives

By the end, students should be able to:

1. state the inferential target: create comparable records while preserving what must be checked differently for text, image, and audio.
2. explain the reading disagreement in their own words;
3. identify the Python type of every major input and output in the worked trace;
4. explain each line or small block of `normalize_multimodal_records`;
5. use the validation diagnostic to bound a sociological claim.

## Required readings

- [Law & Roberto (2025), generative multimodal models](https://doi.org/10.1177/00491241251339673)
- [Maranca et al. (2025), correcting image-label errors](https://doi.org/10.1177/00491241251333372)
- [Arminio et al. (2026), visual clustering with VLLMs](https://doi.org/10.1177/08944393251376703)

## Lecture argument

A common data schema aids comparison but cannot erase modality-specific evidence and error. Multimodal models can make images searchable and interpretable; design-based correction shows why annotation error still enters downstream estimates.

## Computational trace

Students move from visible synthetic inputs through `normalize_multimodal_records` to a printed output and explicit checks. The required task uses no live API. Every code block is read as **input → Python type → operation → output → research meaning**.

## Weekly completion task

Normalize three modality records and report missing modality-specific fields. Submit a prediction, working code, interpreted check, and 100–150 word reading-linked claim. Completion marks only; missing elements may be supplied within one week.

## Validation focus

A missing transcript, image source, or audio duration disappears when all modalities are squeezed into one generic `content` field.
