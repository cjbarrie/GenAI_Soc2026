# Session 12 reading guide — Low-stakes replication and project studio

## The disagreement to carry into class

Reporting checklists make workflows inspectable; model/provider dependence means even apparently deterministic reruns may not recreate an earlier transformation.

Do not summarize the papers serially. Compare the inferential target, the role assigned to an LLM, the human/reference evidence, and the failure mode each design can or cannot reveal.

| Reading | Ask while reading | Bring to the code |
|---|---|---|
| [Feuerriegel et al. (2026), GUIDE-LLM reporting checklist](https://doi.org/10.1038/s41562-026-02492-7) | What inference does the paper seek? | What evidence could disconfirm it? |
| [Barrie, Palmer & Spirling (2025), replication for language models](https://arthurspirling.org/documents/BarriePalmerSpirling_TrustMeBro.pdf) | What inference does the paper seek? | What evidence could disconfirm it? |

## Before class

Bring one passage that supports the strongest claim you think is warranted and one passage that makes you qualify it. Complete this sentence: **The output is useful for ___, but it would be invalid evidence for ___ unless ___.**

## Reading → code

The workbook implements `compare_replication_records`. Its input is small enough to inspect manually. Predict the output, then decide which claim from the readings the check clarifies—and which larger claim it cannot settle.
