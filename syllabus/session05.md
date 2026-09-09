# Session 5 — Can generated media isolate a causal construct?

**Date:** Wednesday, September 30, 2026 · 9:30 a.m.–12:15 p.m.  
**Methodological domain:** experimental treatments and generated stimuli

## Substantive question

How do rights, economic, and family framing contests change support for immigrant legal status—and what would have to be true of the messages before that comparison was interpretable?

The candidate messages are cached course outputs created with an LLM and lightly edited by the instructor. Their scores and flags are instructor-authored mock annotations, not LLM judgments or human pretest data. Python calculates word counts from the displayed text. None of these course materials are evidence from an actual policy experiment.

## Why this follows Sessions 1–4

- Sessions 1–4 examined records that already existed or had already been produced.
- Session 5 begins the intervention part of the course: the researcher constructs what a participant will encounter.
- Session 6 then makes the treatment interactive and asks what changes when the exposure develops through conversation.

## Learning objectives

By the end, students should be able to:

1. explain how sociologists have constructed treatments through standardized partners, confederates, vignettes, audit testers, and artificial social systems;
2. distinguish a theoretical condition from one stimulus used to represent it;
3. explain why information equivalence, message sampling, and human selection matter for generated treatments;
4. separate generation, selection, validation, assignment, outcome measurement, and generalization;
5. review one candidate message manually and record every rejection reason;
6. explain `review_candidates` line by line as exact input and type → operation → exact output and type → sociological meaning → limit; and
7. interpret a condition-level warning without treating it as an automated validity verdict.

## Required readings

1. [Wallander (2009), “25 Years of Factorial Surveys in Sociology”](https://doi.org/10.1016/j.ssresearch.2009.03.004), complete article.
2. [Dafoe, Zhang, and Caughey (2018), “Information Equivalence in Survey Experiments”](https://doi.org/10.1017/pan.2018.9), complete article.
3. [Bloemraad, Silva, and Voss (2016), “Rights, Economics, or Family?”](https://doi.org/10.1093/sf/sov123), complete article.

The slides also use shorter examples from experimental sociology and adjacent survey research, including Emerson, Yancey, and Chai's neighbourhood vignette; Music Lab; confederate experiments; audit studies; Bai et al.'s generated policy messages; generated visual vignettes; and Velez's crowdsourced adaptive surveys. These are not additional required readings.

## Lecture argument

Bloemraad, Silva and Voss show how substantive theory is translated into rights, economic and family frames, and how the same frame can resonate differently across respondents. Wallander and Dafoe et al. supply the design language for examining that translation. Generative models can produce many messages quickly, but each candidate still has to represent the intended construct without introducing other consequential differences.

## Computational trace

Students hold factual material fixed and ask a model to generate one candidate with a named frame. The code introduces named generation parameters and makes the candidate available for the substantive and causal-confound checks developed in class.

The code creates an audit trail. It does not determine whether the theoretical definitions, human ratings, or screening rules are adequate.

## Weekly completion task

Run the model call once with a rights frame and once with an economics frame while holding the facts and call settings fixed. Submit a narrated screen recording explaining the strings, each named call parameter, the returned text and semantic differences that could act as causal confounds. Connect the review to one reading and upload it through the [recording and submission guide](https://cjbarrie.github.io/GenAI_Soc2026/recording-and-submission.html) by 5:00 p.m. Eastern on the Tuesday before the next class.

The task receives a completion mark. Syntax elegance and video editing are not assessed. AI use is permitted with responsibility and disclosure, but each student must be able to explain every submitted line and output without AI assistance.

## Preparation for the oral component

Be ready to answer:

- Which strings enter the prompt, and which one changes on the second run?
- What values do `model`, `messages`, `temperature` and `max_tokens` supply?
- How is the generated text retrieved from the returned object?
- Which wording differences could confound the intended contrast?
- Why does a generated candidate still require human review and pretesting?
