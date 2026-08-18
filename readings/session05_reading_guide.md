# Session 5 reading guide — Treatment and stimulus generation

## The disagreement to carry into class

AI-generated profiles and messages enable scale; information equivalence asks whether conditions differ only in the information the design intends to manipulate.

Do not summarize the papers serially. Compare the inferential target, the role assigned to an LLM, the human/reference evidence, and the failure mode each design can or cannot reveal.

| Reading | Ask while reading | Bring to the code |
|---|---|---|
| [Dafoe, Zhang & Caughey (2018), information equivalence](https://doi.org/10.1017/pan.2018.9) | What inference does the paper seek? | What evidence could disconfirm it? |
| [Evsyukova, Rusche & Mill (2025), LinkedOut](https://doi.org/10.1093/qje/qjae035) | What inference does the paper seek? | What evidence could disconfirm it? |
| [Bai et al. (2025), LLM-generated policy messages](https://doi.org/10.1038/s41467-025-61345-5) | What inference does the paper seek? | What evidence could disconfirm it? |

## Before class

Bring one passage that supports the strongest claim you think is warranted and one passage that makes you qualify it. Complete this sentence: **The output is useful for ___, but it would be invalid evidence for ___ unless ___.**

## Reading → code

The workbook implements `construct_treatments`. Its input is small enough to inspect manually. Predict the output, then decide which claim from the readings the check clarifies—and which larger claim it cannot settle.
