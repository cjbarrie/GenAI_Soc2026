# Session 8 reading guide — Predicting what was not observed

## One comparison links the readings

All three readings estimate something that was not observed directly, but they do not use the same evidence or target the same quantity. Read each complete article and keep the unit of inference visible.

| Reading | Methodological role | Question to bring to class |
|---|---|---|
| [Kim & Lee (2026), “AI-Augmented Surveys”](https://arxiv.org/abs/2305.09620) | Predicts unasked items for observed respondents using their other answers. | What information about a real respondent is available to the model, and what is held out for validation? |
| [Xie et al. (2026), “Evaluating the Statistical Realism of LLM-Generated Social Science Data”](https://doi.org/10.1073/pnas.2538145123) | Tests whether synthetic data preserve more than a selected marginal statistic. | Which relationships among variables fail even when one aggregate looks plausible? |
| [Lax & Phillips (2009), “Gay Rights in the States”](https://doi.org/10.1017/S0003055409990050) | Applies multilevel regression and poststratification to state opinion and studies policy responsiveness on gay rights. | Which parts of the substantive conclusion depend on estimated opinion rather than a direct state survey? |

## Before class

For each article, write down:

1. what is observed;
2. what is predicted;
3. the unit for which the prediction is evaluated; and
4. the human or population data used as the comparison.

## Reading → code

The workbook repeats a structured prediction across five held-out survey cases. It then calculates individual accuracy and aggregate distribution error separately. Trace one profile through the loop and explain why a good aggregate result can coexist with wrong individual answers.

Ashokkumar et al. (2026) is an additional comparison about forecasting experimental results. It targets a different object and will not be treated as evidence that synthetic respondents recover individuals.
