# Session 3 — What can an LLM contribute to qualitative interpretation?

**Date:** Wednesday, September 16, 2026 · 9:30 a.m.–12:15 p.m.  
**Methodological domain:** Qualitative analysis  

## Substantive question

How do sociologists move from close reading and initial codes to themes and interpretations, and where might an LLM assist—or interrupt—that iterative process?

## Learning objectives

By the end, students should be able to:

1. describe familiarization, initial and focused coding, constant comparison, memo-writing, and theme development;
2. distinguish retrieval, coding, theming, and interpretation;
3. explain why qualitative analysis depends on repeated movement between passages, cases, memos, and ideas;
4. assign an LLM a bounded role within that researcher-led workflow;
5. identify where context, cumulative memory, negative cases, and reflexivity may be lost;
6. explain route selection, JSON parsing and source lookup line by line in plain language; and
7. state exactly what each returned Boolean establishes and what it cannot establish.

## Required readings

- [Timmermans and Tavory (2012), “Theory Construction in Qualitative Research”](https://doi.org/10.1177/0735275112457914), complete article.
- [Than et al. (2025), “Updating ‘The Future of Coding’”](https://doi.org/10.1177/00491241251339188), complete article.
- [Viterna (2006), “Pulled, Pushed, and Persuaded”](https://doi.org/10.1086/502690), complete article.

## Lecture argument

Viterna's comparison of life histories shows why qualitative analysis cannot be reduced to extracting common topics: sequence, case comparison and alternative explanations are part of the substantive argument. Timmermans and Tavory give us the language of abduction for describing this movement between evidence and theory. We then use Than et al. to ask which parts of that work an LLM may assist and which still require a researcher to return to cases, context and counterevidence.

AI-moderated interviewing appears only as a clearly marked aside. Its full methodological treatment belongs to the later session on conversational methods.

## Computational trace

Students work with eight instructor-authored fictional tenant excerpts and ask when mutual aid contributes to political solidarity. They write an independent first memo, request a provisional suggestion as JSON, challenge it with a countercase, then ask what the reported evidence can and cannot establish. Each of the three model calls prints raw JSON, parses it and returns to the cited excerpt. Every block is read as:

**input value and type → operation → output value and type → research meaning → limit of the check**

## Weekly completion task

Run the three-round researcher–model exchange. Submit a narrated screen recording explaining the first memo, `json.dumps`, each message list and model call, the raw JSON, `json.loads`, the cited source check, your two replies and your own final memo. Name a countercase and one limit of these interviews. Upload it through the [recording and submission guide](https://cjbarrie.github.io/GenAI_Soc2026/recording-and-submission.html) by 5:00 p.m. Eastern on the Tuesday before the next class.

The task receives a completion mark. Code elegance is not assessed, and missing elements may be supplied within one week.

## Validation focus

A model can cite real passages while overstating their meaning, ignoring negative cases, losing sequence, or treating one account as a corpus-level pattern. A complete research record makes those decisions inspectable; it does not make the interpretation automatically valid.
