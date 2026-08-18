# Session 11 reading guide — Research agents, tools, and provenance

## The disagreement to carry into class

End-to-end systems automate search, code, analysis, and writing; transparency arguments ask whether multiplying agents adds justified capability or merely obscures responsibility.

Do not summarize the papers serially. Compare the inferential target, the role assigned to an LLM, the human/reference evidence, and the failure mode each design can or cannot reveal.

| Reading | Ask while reading | Bring to the code |
|---|---|---|
| [Lu et al. (2026), end-to-end automation of AI research](https://doi.org/10.1038/s41586-026-10265-5) | What inference does the paper seek? | What evidence could disconfirm it? |
| [Nature Machine Intelligence (2026), multi-agent systems need transparency](https://www.nature.com/articles/s42256-026-01183-2) | What inference does the paper seek? | What evidence could disconfirm it? |

## Before class

Bring one passage that supports the strongest claim you think is warranted and one passage that makes you qualify it. Complete this sentence: **The output is useful for ___, but it would be invalid evidence for ___ unless ___.**

## Reading → code

The workbook implements `build_provenance_table`. Its input is small enough to inspect manually. Predict the output, then decide which claim from the readings the check clarifies—and which larger claim it cannot settle.
