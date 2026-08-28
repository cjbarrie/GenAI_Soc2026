# Session 7 reading guide — Synthetic respondents and population representation

## The disagreement to carry into class

The papers agree that LLMs can produce plausible individual-shaped responses. They test different claims about what those responses preserve: majority direction, full distributions, within-group variation, individual answers or culturally situated experience.

Do not summarize the papers serially. Compare the inferential target, the role assigned to an LLM, the human/reference evidence, and the failure mode each design can or cannot reveal.

| Reading | Ask while reading | Bring to the code |
|---|---|---|
| [Kozlowski & Evans (2025), simulating subjects](https://doi.org/10.1177/00491241251337316) | Which human capacities or contexts may be missing from a text-trained stand-in? | Which feature would the proposed simulation need to preserve? |
| [Boelaert et al. (2025), machine bias in opinion polls](https://doi.org/10.1177/00491241251330582) | Does error have one direction, or change by topic? | Why do we need the whole response distribution? |
| [Wang, Morgenstern & Dickerson (2025), identity flattening](https://doi.org/10.1038/s42256-025-00986-z) | How can misportrayal and flattening occur together? | What within-group comparison should remain visible? |

## Before class

Bring one passage that supports the strongest claim you think is warranted and one passage that makes you qualify it. Complete this sentence: **The output is useful for ___, but it would be invalid evidence for ___ unless ___.**

## Reading → code

The workbook makes two live OpenRouter calls. First, one request predicts the aggregate seven-category GSS ideology distribution. Second, repeated requests predict held-out answers for a small set of actual 2024 GSS public-use profiles. Structured outputs make the expected record explicit. Before class, be ready to explain why the aggregate and profile exercises require different human comparisons.
