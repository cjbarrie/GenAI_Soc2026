# Instructor notes — Session 11: Language, inequality and institutional power

## Central question

How does language become a source of inequality when people and institutions use LLMs?

The class distinguishes three outcomes that should not be collapsed:

1. **Representation:** whether generated language resembles observed human communication.
2. **Evaluation:** whether a model attaches different judgments to meaning-matched linguistic forms.
3. **Institutional consequence:** how an output enters advice, ranking or an allocation rule.

The bounded conclusion is that language-model disparities become consequential through linguistic markets, model design and institutional use. A paired model comparison identifies a conditional output difference; it does not by itself show that a person lost an opportunity or establish the historical mechanism that produced the association.

## 165-minute plan

- **9:30–9:42 — opening object:** introduce the published AAE/SAE habitual pair, the fixed occupation task and the three outcomes.
- **9:42–10:15 — sociological lineage:** Bourdieu on linguistic markets; Flores and Rosa on racialized listening; matched guise as a way to study evaluation.
- **10:15–10:32 — institutional evidence:** Purnell et al. on housing inquiries and Koenecke et al. on speech recognition. Keep allocation and transcription outcomes separate.
- **10:32–10:47 — representation:** Pagan et al. on model-generated social-media replies. Ask what a plausible reply can still fail to reproduce.
- **10:47–10:57 — break.**
- **10:57–11:27 — required-reading discussion:** Hofmann et al. design, matched and non-matched analyses, overt and covert stereotypes, and the distinction between association and deployment.
- **11:27–11:50 — training data and power:** Waight et al. corpus evidence, controlled additional pretraining, commercial audits and observational country comparison.
- **11:50–12:08 — coding walkthrough:** trace one published meaning-matched pair through a fixed occupation task, the route-specific model call and the comparison record.
- **12:08–12:15 — closing discussion:** name the evidence needed for representation, evaluation and institutional consequence.

## Reading jobs

- **Bourdieu (1977):** establishes that linguistic competence has no fixed value outside a social market and connects recognized language with authority and material returns.
- **Hofmann et al. (2024):** supplies the focal matched-guise model audit and separates overt from covert stereotypes.
- **Waight et al. (2026):** shows how corpus analysis, controlled additional training and deployed-model audits can be combined when investigating training-data influence.

Flores and Rosa, Purnell et al., Koenecke et al., Pagan et al., and Bowker and Star provide supporting extensions rather than a second required-reading list.

## Questions for the reading discussion

1. What does translation between AAE and SAE hold constant, and what social information does it remove?
2. What alternative explanations return in the non-meaning-matched analysis?
3. How would Bourdieu and Flores–Rosa interpret the same paired result differently?
4. Which parts of Waight et al.'s argument depend on controlled intervention, and which depend on observational extension?
5. What additional evidence would be required before making a claim about hiring, housing, education or criminal justice?

## Coding task

The task uses three published habitual-aspect pairs from Hofmann et al.'s authors' repository. Students ask one model to select an occupation from a fixed list for each AAE and SAE form. The program preserves the exact text, route, model, raw return and parsed fields before building a paired comparison.

Before each block, use this language:

**input value and type → operation → output value and type → sociological meaning → what the result does not establish**

The new syntax is deliberately limited to a small function and loop. Trace the first call with literal values before showing parameters. The student changes one published pair and reruns the complete comparison. They should inspect the raw return before discussing the pair.

Do not describe the exercise as a replication of Hofmann et al. It adapts published linguistic material to a smaller occupation-selection demonstration. A single run is not an estimate of a stable disparity, and the model's explanation is not evidence of its internal mechanism.

## Likely sticking points

- A dictionary key retrieves a named value; a list index retrieves a position.
- A function parameter receives a value when the function is called.
- The loop repeats the same operation for each paired record.
- JSON parsing checks that the return has the requested shape; it does not validate the judgment.
- Meaning matching narrows the comparison but does not erase all social information carried by a linguistic form.

## Completion evidence

Students submit a narrated recording showing one changed pair, the raw and parsed return, and the paired comparison. They must explain the input and output of each operation and state one bounded finding plus at least two pieces of evidence that would be needed before making an institutional claim.

If a live route fails, the recorded return supports code tracing only. It should be identified as a contingency, not presented as new empirical evidence.
