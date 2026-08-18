# Session 2 — What can an LLM output validly measure?

**Wednesday, September 9, 2026 · 9:30 a.m.–12:15 p.m.**  
**Course movement:** Observe · Annotation and measurement

## The question

An LLM can turn text into labels quickly. Under what conditions can those labels function as sociological measurements—and what happens when its errors are patterned rather than random?

## Learning objectives

By the end of the session, students should be able to:

1. distinguish text classification, information extraction, measurement, and downstream inference;
2. translate a sociological codebook into a promptbook with explicit labels, edge cases, and output requirements;
3. trace a complete annotation record from a Python string and message list to raw and parsed output;
4. compute and interpret a confusion matrix, precision, recall, and F1 for a focal class;
5. explain why aggregate accuracy may conceal substantively consequential, non-random error;
6. propose a validation design matched to an inferential target.

## Required preparation

- Barrie, Christopher, Lisa P. Argyle, James Bisbee, et al. 2026. “AI and Research Methods,” §§10.2.1–10.2.5. Focus on the relation among task definition, model choice, validation, and inference.
- Stuhler, Oscar, Cat Dang Ton, and Étienne Ollion. 2025. “From Codebooks to Promptbooks: Extracting Information from Text with Generative Large Language Models.” *Sociological Methods & Research* 54(3):794–848. [DOI](https://doi.org/10.1177/00491241251336794).
- Chae, Youngjin, and Thomas Davidson. 2026. “Large Language Models for Text Classification: From Zero-Shot Learning to Instruction-Tuning.” *Sociological Methods & Research* 55(2):501–567. [DOI](https://doi.org/10.1177/00491241251325243).

Before class, bring one annotation problem from your own research interests. Write one sentence naming the construct and one sentence describing an ambiguous case.

## In class

- Compare the inferential jobs performed by classification and information extraction.
- Reconstruct how a codebook becomes a promptbook.
- Examine the performance/cost tradeoff among prompting, fine-tuning, and instruction-tuning.
- Trace a small OpenRouter-compatible research record using cached output.
- Audit stance labels for synthetic neighborhood-rezoning comments.
- Diagnose why two conditional statements inflate estimated support despite apparently high accuracy.

## Completion task

Complete `session02_task.py`: count true positives, false positives, false negatives, and true negatives for support; calculate precision, recall, and F1; and write a 100–150 word claim/evidence note tied to one required reading. You may use AI with responsibility and disclosure, but you must be able to explain the completed code line by line.

## Optional extension

Run the same records through one hosted and one local model. Preserve both raw outputs and compare disagreement, latency, research metadata, and support-rate estimates. Neither model is a gold standard.

