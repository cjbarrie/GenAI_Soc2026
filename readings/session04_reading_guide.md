# Session 4 reading guide — Multimodal measurement

## The disagreement to carry into class

Multimodal models can make images searchable and interpretable; design-based correction shows why annotation error still enters downstream estimates.

Do not summarize the papers serially. Compare the inferential target, the role assigned to an LLM, the human/reference evidence, and the failure mode each design can or cannot reveal.

| Reading | Ask while reading | Bring to the code |
|---|---|---|
| [Law & Roberto (2025), generative multimodal models](https://doi.org/10.1177/00491241251339673) | What inference does the paper seek? | What evidence could disconfirm it? |
| [Maranca et al. (2025), correcting image-label errors](https://doi.org/10.1177/00491241251333372) | What inference does the paper seek? | What evidence could disconfirm it? |
| [Arminio et al. (2026), visual clustering with VLLMs](https://doi.org/10.1177/08944393251376703) | What inference does the paper seek? | What evidence could disconfirm it? |

## Before class

Bring one passage that supports the strongest claim you think is warranted and one passage that makes you qualify it. Complete this sentence: **The output is useful for ___, but it would be invalid evidence for ___ unless ___.**

## Reading → code

The workbook implements `normalize_multimodal_records`. Its input is small enough to inspect manually. Predict the output, then decide which claim from the readings the check clarifies—and which larger claim it cannot settle.
