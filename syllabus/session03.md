# Session 3 — What can an LLM contribute to qualitative interpretation?

**Date:** Wednesday, September 16, 2026 · 9:30 a.m.–12:15 p.m.  
**Course movement:** Observe  
**Methodological domain:** Qualitative analysis  
**Chapter anchor:** *AI and Research Methods*, §§10.1.4–10.1.5

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

- [Timmermans & Tavory (2022), *Data Analysis in Qualitative Research*](https://press.uchicago.edu/ucp/books/book/chicago/D/bo133273407.html), selected material on open coding, focused coding, and analytic memoing
- [Than et al. (2025), researcher–LLM–researcher qualitative analysis](https://doi.org/10.1177/00491241251339188)
- [Ibrahim & Voyer (2026), technological reflexivity](https://doi.org/10.1177/14687941251390794)

Selected sections and the reading guide identify the required focus; students are not expected to master every model comparison or technical appendix.

## Lecture argument

Qualitative analysis is not a one-shot extraction of themes. Researchers develop interpretations through repeated reading, coding, comparison, memo-writing, attention to exceptions, and movement between data and theory. An LLM output can be useful within that process only when the researcher can trace it to the corpus, test it against context and counterevidence, consider alternatives, and document how it changed subsequent attention and judgment.

AI-moderated interviewing appears only as a clearly marked aside. Its full methodological treatment belongs to the later session on conversational methods.

## Computational trace

Students send two identified excerpts to a model and request a provisional suggestion as JSON. They inspect the raw JSON string, convert it to a Python dictionary and return to the cited excerpt. Every block is read as:

**input value and type → operation → output value and type → research meaning → limit of the check**

## Weekly completion task

Run the supplied structured-output call, change one excerpt and run it again. Submit a narrated screen recording explaining `json.dumps`, the model call, raw output, `json.loads` and field retrieval. Check the cited source and connect one interpretive limit to a reading. Upload to the Box folder supplied by the instructor.

The task receives a completion mark. Code elegance is not assessed, and missing elements may be supplied within one week.

## Validation focus

A model can cite real passages while overstating their meaning, ignoring negative cases, losing sequence, or treating one account as a corpus-level pattern. A complete research record makes those decisions inspectable; it does not make the interpretation automatically valid.
