# Session 2 reading guide — A label is not yet a measure

## Read the papers as a sequence

The readings add four separate requirements to the same research workflow:

1. **The chapter:** begin with the inferential target and preserve the complete measurement record.
2. **Stuhler, Dang Ton, and Ollion:** make the coding rules and output requirements explicit in a promptbook.
3. **Barrie, Palaiologou, and Törnberg:** test whether repeated or equivalent prompts produce a stable variable.
4. **Egami, Hinck, Stewart, and Wei:** determine whether the remaining annotation errors compromise the estimate made with those labels.

Do not reduce the disagreement to “which method is most accurate?” The papers address different stages of the measurement chain.

## Questions to annotate while reading

### Chapter §10.2

1. What is the difference between evaluating a classifier and validating a measure for a particular downstream use?
2. Which metadata would another researcher need to interpret or reproduce a label?
3. Why can apparently strong agreement conceal consequential errors?

### Stuhler, Dang Ton, and Ollion

1. What does a promptbook add to an ordinary codebook?
2. How do age, military service, education, and occupation differ as information problems?
3. When is an LLM methodological overkill?
4. Does writing a promptbook merely document a construct, or can it change the construct by forcing tacit decisions into the open?

### Barrie, Palaiologou, and Törnberg

1. What is held constant and varied in intra-prompt stability?
2. What is held constant and varied in inter-prompt stability?
3. Why is stability necessary but insufficient for validity?
4. What might low stability reveal about the construct, boundary rules, source material, or model/task combination?

### Egami, Hinck, Stewart, and Wei

1. Why can more than 90% or even 95% annotation accuracy still produce biased estimates or invalid confidence intervals?
2. What is gained by independently expert-coding a probability sample rather than an arbitrary validation subset?
3. Which part of their solution is a sampling-design idea, and which part is an estimator?
4. For Session 2, what should a beginner understand without implementing the doubly robust estimator?

## Bring to class

Complete this record for one annotation problem from your own research interests:

```text
Construct:
Unit of analysis:
One difficult boundary case:
Downstream quantity or comparison:
One reasonable alternative prompt wording:
```

## Reading-to-code map

| Reading idea | Where it appears in the workbook |
|---|---|
| Codebook → promptbook | `CODEBOOK`, prompt strings, and `messages` |
| Prompt variation | `prompt_variants` dictionary and cached variant annotations |
| Case-level instability | `labels_by_comment`, `set`, and `unstable_ids` |
| Prompt Stability Score | supplied `inter_prompt_pss` helper and returned float |
| Independent comparison | `reference_source`, Boolean comparisons, and confusion counts |
| Patterned error | the two conditional false positives |
| Downstream consequence | reference support rate of 4/12 versus predicted 6/12 |

## Brief in-class asides

Schroeder, Roy, and Kabbara show that LLM suggestions can influence human annotators, so a human-reviewed label is not necessarily an independent benchmark. Agarwal, Naaman, and Vashistha show that autocomplete can also change the style and cultural content of the source text. Together they motivate recording both `reference_source` and `text_production_mode`.

These papers are not additional required reading for this week.
