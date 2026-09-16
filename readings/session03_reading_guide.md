# Session 3 reading guide — LLMs and qualitative analysis

## Start with the human method

Before asking what an LLM can do, we need an account of what qualitative researchers are already doing. The relevant process is iterative:

`familiarization → initial coding → focused coding → comparison → memoing → theme or category development → return to the corpus`

The arrows run in both directions. Researchers revise codes, reread earlier cases, seek cases that do not fit, and move between empirical material and theoretical ideas.

## Required readings

| Reading | What to look for | Question to bring to class |
|---|---|---|
| [Timmermans & Tavory (2012), “Theory Construction in Qualitative Research”](https://doi.org/10.1177/0735275112457914), complete article | How an unexpected observation becomes evidence through comparison with alternative theoretical accounts. | What makes an interpretation abductive rather than merely descriptive? |
| [Than et al. (2025)](https://doi.org/10.1177/00491241251339188), complete article | A bounded researcher–LLM–researcher workflow applied to more than 1,200 newsweekly articles. | Which task is delegated, and which decisions still belong to researchers? |
| [Viterna (2006), “Pulled, Pushed, and Persuaded”](https://doi.org/10.1086/502690), complete article | How life histories, event sequences and comparison among pathways produce an explanation of high-risk mobilization. | What would disappear if these accounts were reduced to a list of common themes? |

The complete articles are assigned; focus your notes on the methodological moves and the substantive explanation, not every technical comparison.

## Four parts of the work

1. **Retrieval:** locate passages relevant to a question.
2. **Coding:** attach a descriptive or analytic label to particular material.
3. **Theming:** develop a patterned relationship across codes and cases.
4. **Interpretation:** explain what that pattern means in context and why it is preferable to alternatives.

A theme is not simply a frequently mentioned topic. It is a claim about a pattern that matters for the research question and survives comparison with context, variation, and counterexamples.

## Before class

Bring:

1. one piece of Viterna's evidence that helps distinguish two mobilization pathways;
2. one surprising observation that could motivate an abductive explanation;
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

- [Ibrahim & Voyer (2026)](https://doi.org/10.1177/14687941251390794) — why the researcher's interaction with a chatbot belongs in the methodological account.
- [Williams-Ceci et al. (2026)](https://doi.org/10.1126/sciadv.adw5578) — an experiment on AI writing suggestions and subsequent attitudes, used here as a possible influence mechanism, not direct evidence about qualitative researchers.
- [Nguyen & Welch (2026)](https://doi.org/10.1177/10944281251377154) — why fluent organization and coding should not be mistaken for interpretation and theorization.
- [Mehta et al. (2025)](https://www.nature.com/articles/s41598-025-18969-w) — why coherent themes can still rest on weak, truncated, or altered quotations.
- [Stuart & Laryea (2026)](https://doi.org/10.1007/s11133-025-09625-w) — a current sociological account of iterative coding, analytic memoing, and the move from description toward explanation.
- [Braun & Clarke (2006)](https://doi.org/10.1191/1478088706qp063oa) and [Charmaz (2024)](https://us.sagepub.com/en-us/nam/constructing-grounded-theory/book255601) — foundational accounts of theme development and constructivist grounded-theory practice.

## One aside for a later week

[Jack, Cooper, and Flower (2026)](https://doi.org/10.1177/20597991261448157) study AI-moderated interviews. We mention it only to note that an interviewer can shape the material subsequently analyzed. The design and evaluation of AI interviewing belongs to the later conversational-methods session.
