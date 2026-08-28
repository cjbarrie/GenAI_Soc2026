# Session 3 reading guide — LLMs and qualitative analysis

## Start with the human method

Before asking what an LLM can do, we need an account of what qualitative researchers are already doing. The relevant process is iterative:

`familiarization → initial coding → focused coding → comparison → memoing → theme or category development → return to the corpus`

The arrows run in both directions. Researchers revise codes, reread earlier cases, seek cases that do not fit, and move between empirical material and theoretical ideas.

## Required readings

| Reading | What to look for | Question to bring to class |
|---|---|---|
| [Timmermans & Tavory (2022), *Data Analysis in Qualitative Research*](https://press.uchicago.edu/ucp/books/book/chicago/D/bo133273407.html), selected material on open coding, focused coding, and analytic memos | How comparison and memo-writing turn observations into a developing explanation. | What would be lost if analysis became a single request for “the main themes”? |
| [Than et al. (2025)](https://doi.org/10.1177/00491241251339188) | A bounded researcher–LLM–researcher workflow applied to more than 1,200 newsweekly articles. | Which task is delegated, and which decisions still belong to researchers? |
| [Ibrahim & Voyer (2026)](https://doi.org/10.1177/14687941251390794) | The researcher shapes model output, and the output can redirect later reading and interpretation. | What should be recorded if that interaction is part of the method? |

Selected sections keep the workload comparable with other weeks. The aim is not to master every technical comparison.

## Four parts of the work

1. **Retrieval:** locate passages relevant to a question.
2. **Coding:** attach a descriptive or analytic label to particular material.
3. **Theming:** develop a patterned relationship across codes and cases.
4. **Interpretation:** explain what that pattern means in context and why it is preferable to alternatives.

A theme is not simply a frequently mentioned topic. It is a claim about a pattern that matters for the research question and survives comparison with context, variation, and counterexamples.

## Before class

Bring:

1. one example of a code that stays close to a passage;
2. one example of a comparison that could change that code;
3. one reason a model-generated theme might look convincing too early; and
4. one part of the analytic process that would be difficult to preserve across separate LLM calls.

Complete this sentence:

> An LLM may help with ___, but the qualitative analysis still depends on the researcher repeatedly ___ .

## How the reading connects to the code

The workbook represents a deliberately simplified version of the human process:

- dictionaries keep passages with IDs and context;
- a list keeps the small corpus together;
- a lookup lets us return to cited passages;
- separate lists preserve supporting and counterexample cases;
- a claim record preserves context, an alternative interpretation, a decision, and a memo.

`trace_sources(...)` checks whether cited records exist. `check_review_readiness(...)` checks whether the researcher's review has been recorded. Neither function performs thematic analysis or returns `valid_theme = True`.

## Papers used in class

- [Nguyen & Welch (2026)](https://doi.org/10.1177/10944281251377154) — why fluent organization and coding should not be mistaken for interpretation and theorization.
- [Mehta et al. (2025)](https://www.nature.com/articles/s41598-025-18969-w) — why coherent themes can still rest on weak, truncated, or altered quotations.
- [Stuart & Laryea (2026)](https://doi.org/10.1007/s11133-025-09625-w) — a current sociological account of iterative coding, analytic memoing, and the move from description toward explanation.
- [Braun & Clarke (2006)](https://doi.org/10.1191/1478088706qp063oa) and [Charmaz (2024)](https://us.sagepub.com/en-us/nam/constructing-grounded-theory/book255601) — foundational accounts of theme development and constructivist grounded-theory practice.

## One aside for a later week

[Jack, Cooper, and Flower (2026)](https://doi.org/10.1177/20597991261448157) study AI-moderated interviews. We mention it only to note that an interviewer can shape the material subsequently analyzed. The design and evaluation of AI interviewing belongs to the later conversational-methods session.
