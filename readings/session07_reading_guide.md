# Session 7 reading guide — Synthetic respondents and population representation

## The disagreement to carry into class

The papers agree that LLMs can produce plausible individual-shaped responses. They test different claims about what those responses preserve: majority direction, full distributions, within-group variation, individual answers or culturally situated experience.

Do not summarize the papers serially. Compare the inferential target, the role assigned to an LLM, the human/reference evidence, and the failure mode each design can or cannot reveal.

| Reading | Ask while reading | Bring to the code |
|---|---|---|
| [Kozlowski & Evans (2025), simulating subjects](https://doi.org/10.1177/00491241251337316), complete article | Which human capacities or contexts may be missing from a text-trained stand-in? | Which feature would the proposed simulation need to preserve? |
| [Boelaert et al. (2025), machine bias in opinion polls](https://doi.org/10.1177/00491241251330582), complete article | Does error have one direction, or change by topic? | Why do we need the whole response distribution? |
| [Igarashi, Kano & Miwa (2025), discriminatory scenarios in Japan](https://doi.org/10.1057/s41599-025-06054-6), complete article | How do Japanese respondents and GPT-4 judge experimentally varied cases of unequal treatment? | Which similarities concern average severity, and which concern sensitivity to particular targets or justifications? |

## Before class

Bring one result from Igarashi et al. on which people and GPT-4 agree and one on which they differ. Complete this sentence: **The comparison shows ___; it does not establish that GPT-4 represents ___ .**

## Reading → code

The workbook predicts one held-out answer for a deidentified public-use profile. Igarashi et al. instead compare human and model judgments over a factorial set of discrimination scenarios. Before class, be ready to explain why similarity in average ratings and similarity in experimental effects are different validation targets.

Wang, Morgenstern and Dickerson (2025) remains an additional reading on identity flattening and within-group heterogeneity.
