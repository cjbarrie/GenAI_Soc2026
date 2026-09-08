# Session 2 — When can an LLM label count as a measure?

**Wednesday, September 9, 2026 · 9:30 a.m.–12:15 p.m.**  
**Course movement:** Observe · Annotation and measurement

## The question

An LLM can turn text into labels quickly. What evidence do we need before those labels can function as sociological measurements or support a downstream claim?

## Learning objectives

By the end of the session, students should be able to:

1. define the construct, unit, boundary rules, and intended use of a text-derived variable;
2. explain how a codebook becomes a promptbook;
3. distinguish intra-prompt stability, inter-prompt stability, and validity;
4. trace one label through strings, dictionaries, lists, indexing and equality comparisons;
5. compare hosted and local labels with an independently produced human reference; and
6. explain why high accuracy may still yield a misleading substantive estimate.

## Required preparation

- Barrie, Christopher, Lisa P. Argyle, James Bisbee, et al. 2026. “AI and Research Methods,” §§10.1.1–10.1.5.
- Stuhler, Oscar, Cat Dang Ton, and Étienne Ollion. 2025. “From Codebooks to Promptbooks: Extracting Information from Text with Generative Large Language Models.” *Sociological Methods & Research* 54(3):794–848. [DOI](https://doi.org/10.1177/00491241251336794).
- Barrie, Christopher, Elli Palaiologou, and Petter Törnberg. 2024. “Prompt Stability Scoring for Text Annotation with Large Language Models.” [arXiv](https://arxiv.org/abs/2407.02039).
- Egami, Naoki, Matthew Hinck, Brandon M. Stewart, and Hanying Wei. 2026. “Using Large Language Model Annotations for the Social Sciences: A General Framework of Using Predicted Variables in Statistical Analyses.” Selected introduction, Figure 1, high-accuracy result, and design discussion. [Paper](https://brandonstewart.org/publication/using-large-language-model-annotations-social-sciences/).

Before class, bring one annotation problem from your own research interests. Write down its construct, unit of analysis, one difficult boundary case, and the downstream quantity or comparison the labels would support.

## In class

- Define explicit support in a synthetic rezoning study.
- Compare three reasonable prompt variants and identify unstable cases.
- Use Prompt Stability Score as a reliability diagnostic.
- Consider how AI assistance can influence source texts and human reference labels.
- Trace every Python input, type, operation, and output.
- Inspect false positives and follow them into the estimated support rate.
- Design an independent validation sample appropriate to the intended claim.

## Completion task

Run the same annotation request through both OpenRouter and Ollama. Change only the comment, rerun both routes and submit a narrated screen recording explaining the codebook, message list, each return shape and the three comparisons. Upload it through the [recording guide and Box folder](https://cjbarrie.github.io/GenAI_Soc2026/recording-and-submission.html) by 5:00 p.m. Eastern on the Tuesday before the next class.

Weekly work receives completion marks. Code elegance and video editing are not assessed. You may use AI with responsibility and disclosure, but you must be able to explain every submitted line and output without assistance.

## Optional extensions

- Agarwal, Dhruv, Mor Naaman, and Aditya Vashistha. 2025. “AI Suggestions Homogenize Writing Toward Western Styles and Diminish Cultural Nuances.” [Paper](https://arxiv.org/abs/2409.11360).
- Williams-Ceci, Sterling, et al. 2026. “Biased AI Writing Assistants Shift Users’ Attitudes on Societal Issues.” [Open-access article](https://pmc.ncbi.nlm.nih.gov/articles/PMC12978215/).
- Repeat the comparison with a second model tag, preserving the exact prompt, output, model/runtime metadata and disagreement pattern.
