# Session 5 reading guide — Constructing experimental treatments

## The question to carry across the readings

> What evidence would allow us to say that two generated treatment conditions differ in the way our theory requires?

Do not read the papers as a sequence from old methods to better AI. Read them as three parts of one design problem:

1. How is a social situation represented as a treatment?
2. What else might participants infer from the representation?
3. How do multiple messages and human selection change the claim?

## Required reading 1 — Wallander on factorial surveys in sociology

Read the abstract, introduction, sections explaining dimensions and vignette universes, discussion of realism and design, and conclusion.

Factorial surveys combine experimentally varied dimensions inside descriptions of people or situations. For a respondent, a vignette is one short social case. For the researcher, it is one combination selected from a much larger set of possible cases.

Ask:

- Which dimensions and levels must be defined before a vignette can be constructed?
- When does a statistically useful combination become socially implausible?
- What does a judgment about a fictitious situation allow us to infer?
- Why is the vignette's wording part of the design rather than a cosmetic step?

**Bring to class:** identify how factorial-survey dimensions and levels become one complete vignette. In class we will return to Emerson, Yancey, and Chai's original residential-segregation study rather than treating Wallander's review as the source of that example.

**Job in the code:** a list contains several candidate treatments; each dictionary follows the same schema; the rules state what the researcher decided to inspect.

## Required reading 2 — Dafoe, Zhang, and Caughey on information equivalence

The paper asks what happens when a manipulation also changes respondents' beliefs about relevant background conditions. The intended difference can become difficult to interpret when the treatment carries additional information.

Ask:

- What is the focal information the researcher intends to vary?
- Which background beliefs might change at the same time?
- What would a placebo or pretest question reveal?
- Why does random assignment not solve an information-equivalence problem?

**Bring to class:** write one question that could reveal what respondents inferred about undocumented immigrants, citizenship, or policy consequences beyond the stated frame.

**Job in the code:** intended-frame, competing-frame, warmth, factual-density, unsupported-claim, and stigmatizing-language fields make rival differences visible enough to review. In the classroom file these are instructor-authored mock annotations, not LLM judgments or human pretest evidence. They do not exhaust what a respondent might infer.

## Required reading 3 — Bai et al. on generated policy messages

Focus on the study conditions, message pools, human selection, outcomes, and reported message differences. Distinguish:

- human-written messages;
- LLM-generated messages;
- human-selected LLM messages;
- the individual messages inside each pool; and
- the participants assigned to encounter them.

Ask:

- What exactly was randomized?
- Where did human selection enter the design?
- Which message features differed across sources?
- Does evidence that generated messages persuade identify the reason for their effect?
- What population of possible messages does the result concern?

**Job in the code:** every candidate keeps a stable ID, source, prompt version, ratings, and final decision. Rejected outputs remain in the research history.

## The comparison to bring into class

| Reading | Material | Main methodological problem | Decision it changes |
|---|---|---|---|
| Wallander | Factorial vignettes | Control, plausibility, and inference from fictitious cases | Define dimensions and possible combinations before producing prose |
| Dafoe et al. | Survey-experimental information | Respondents may infer more than the named manipulation | Record and pretest plausible competing information |
| Bai et al. | Pools of human and generated policy messages | Source, selection, and message features can be bundled | Preserve provenance and examine several candidates per condition |

## In-class evidence rather than additional required reading

The slides will introduce these examples briefly:

- Salganik, Dodds, and Watts's Music Lab as an artificial cultural market;
- Berger, Cohen, and Zelditch's standardized expectation-states situation;
- Ridgeway and Erickson's deferential and nondeferential confederates;
- Piliavin, Rodin, and Piliavin's subway field experiment as a boundary comparison;
- Emerson, Yancey, and Chai's original residential-segregation study;
- Bloemraad, Silva, and Voss's rights, economics, and family framing contests;
- Krysan and colleagues' neighborhood video experiment;
- Correll, Benard, and Paik's motherhood-penalty study;
- Pager's matched employment testers;
- Slater, Peter, and Valkenburg on message populations;
- Schwitter on generated visual vignettes; and
- LinkedOut's generated profile-image pipeline.
- Velez's crowdsourced adaptive surveys, in which participant responses enter an evolving question bank.

These examples show different answers to one question: **what carries the treatment—the setting, another person, a written case, an image, or an application moving through an institution?**

## Before class

Choose one of the three immigrant-rights frames and write:

1. a one-sentence definition of the construct;
2. two features that should remain comparable across conditions;
3. one plausible unintended inference;
4. one pretest question; and
5. one reason that a message might be rejected while remaining in the research record.

Then finish:

> Generating more messages helps with ___, but it does not establish ___ because ___.
