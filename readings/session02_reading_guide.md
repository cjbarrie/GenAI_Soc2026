# Session 2 Reading Guide — Labels Are Measurements Only After Validation

## Read for a disagreement

All three readings agree that LLMs make text coding more accessible. They place the methodological burden in different places:

- The chapter begins with the **inferential target**: what variable is being constructed, for what downstream use, and against what evidence should it be validated?
- Stuhler, Dang Ton, and Ollion show how sociologists can turn codebooks into inspectable **promptbooks**, but their obituary study also reveals task- and subgroup-patterned error.
- Chae and Davidson compare zero-shot, few-shot, fine-tuned, and instruction-tuned classification. Their comparison makes model scale only one choice among several; accuracy must be considered alongside training data, task complexity, and cost.

The shared lesson is not “LLMs can code text.” It is that a label becomes a defensible measurement only after researchers specify the construct, observe the errors, and connect those errors to the intended inference.

## Questions to annotate while reading

### Chapter §10.2

1. Where does the chapter treat a human code as a benchmark, and where does it question humans as an unquestioned gold standard?
2. Why can an impressive agreement rate be misleading for rare categories?
3. Which metadata would another researcher need to interpret or reproduce a label?

### Stuhler, Dang Ton, and Ollion

1. What does the promptbook add to an ordinary codebook?
2. Which obituary variables are explicit, which require search across a long document, and which require interpretation or inference?
3. Why does a simple rule nearly match the generative models for age, while prompting is more useful for sparse information such as military service or education?
4. What downstream coefficient or group comparison could be biased if extraction errors correlate with identity or historical period?

### Chae and Davidson

1. What changes across zero-shot, few-shot, fine-tuned, and instruction-tuned regimes?
2. When could a smaller fine-tuned model be preferable to a much larger prompted model?
3. Why is stance detection more demanding than generic sentiment classification?
4. Which comparison in the paper is closest to your own likely research use—and which is least transportable?

## Bring to class

Complete this four-line record:

```text
Construct:
Unit of analysis:
One difficult boundary case:
Downstream inference that could be harmed by patterned error:
```

## Reading-to-code map

| Reading idea | Where it appears in the workbook |
|---|---|
| Codebook → promptbook | `CODEBOOK` dictionary and `messages` list |
| Inspectable task definition | Exact input text, valid labels, and conditional-case rule |
| Model/regime choice | Optional hosted/local call and recorded model metadata |
| Accuracy is insufficient | Confusion counts plus precision/recall/F1 |
| Non-random error | Two conditional comments misread as support |
| Downstream consequence | Human support rate 33%; cached-model estimate 50% |

