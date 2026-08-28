# Session 9 reading guide — Generative agent-based models I

## The disagreement to carry into class

Classic ABM explanation emphasizes transparent rules; generative agents add memory, reflection, and language policies whose model tendencies may shape the macro result.

Do not summarize the papers serially. Compare the inferential target, the role assigned to an LLM, the human/reference evidence, and the failure mode each design can or cannot reveal.

| Reading | Ask while reading | Bring to the code |
|---|---|---|
| [Macy & Willer (2002), from factors to actors](https://doi.org/10.1146/annurev.soc.28.110601.141117) | What inference does the paper seek? | What evidence could disconfirm it? |
| [Park et al. (2023), generative agents](https://doi.org/10.1145/3586183.3606763) | What inference does the paper seek? | What evidence could disconfirm it? |
| [Chuang et al. (2024), LLM opinion dynamics](https://doi.org/10.18653/v1/2024.findings-naacl.211) | What inference does the paper seek? | What evidence could disconfirm it? |

## Before class

Bring one passage that supports the strongest claim you think is warranted and one passage that makes you qualify it. Complete this sentence: **The output is useful for ___, but it would be invalid evidence for ___ unless ___.**

## Reading → code

The workbook implements `synchronous_update`. Its input is small enough to inspect manually. Predict the output, then decide which claim from the readings the check clarifies—and which larger claim it cannot settle.
