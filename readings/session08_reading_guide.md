# Session 8 reading guide — Opinion prediction, validation, and limits

## The disagreement to carry into class

AI-augmented surveys seek unasked opinions; population realism and experiment forecasting show that success on one statistical target need not transfer to another.

Do not summarize the papers serially. Compare the inferential target, the role assigned to an LLM, the human/reference evidence, and the failure mode each design can or cannot reveal.

| Reading | Ask while reading | Bring to the code |
|---|---|---|
| [Kim & Lee (2026), AI-augmented surveys](https://arxiv.org/abs/2305.09620) | What inference does the paper seek? | What evidence could disconfirm it? |
| [Xie et al. (2026), statistical realism](https://doi.org/10.1073/pnas.2538145123) | What inference does the paper seek? | What evidence could disconfirm it? |
| [Ashokkumar et al. (2026), predicting experiment results](https://doi.org/10.1038/s41586-026-10742-x) | What inference does the paper seek? | What evidence could disconfirm it? |

## Before class

Bring one passage that supports the strongest claim you think is warranted and one passage that makes you qualify it. Complete this sentence: **The output is useful for ___, but it would be invalid evidence for ___ unless ___.**

## Reading → code

The workbook implements `score_inferential_targets`. Its input is small enough to inspect manually. Predict the output, then decide which claim from the readings the check clarifies—and which larger claim it cannot settle.
