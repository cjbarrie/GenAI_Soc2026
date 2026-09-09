# Session 3 architecture — qualitative interpretation with LLMs

**Implemented status:** rebuilt after instructor review on 26 August 2026.

## Main question

What can an LLM contribute to qualitative interpretation, and what must the researcher still do?

## Narrative arc

1. Begin with the actual study: synthetic interviews with tenants involved in mutual-aid networks after rent increases.
2. State the research question and source context before introducing coding or an LLM.
3. Establish the sociological craft of qualitative analysis through Deterding and Waters, Timmermans and Tavory, and Stuart and Laryea.
4. Use the same excerpts to distinguish indexing, analytic coding, comparison, memo-writing, countercases, sequence and explanation.
5. Explain the technical limit: a context window is not cumulative analytic memory. Use Liu et al. and LongMemEval to show unequal use and retrieval of earlier material.
6. Give the model one explicit job: receive the research question and eight labelled excerpts, then return one candidate pattern, supporting IDs and brief reasoning.
7. Introduce Mehta et al. early as evidence that generated quotations must be traced to the transcript.
8. Use Than et al. to establish a bounded researcher–LLM–researcher workflow.
9. Compare the candidate pattern with countercases and chronology and revise it.
10. Use Ibrahim and Voyer to record the researcher–model interaction and its effect on later reading.
11. After the break, trace the same process as one continuous Python program.
12. Close by explaining exactly why the final claim is narrower than the model proposal.

## Worked example

**Research question:** How do residents distinguish emergency help from political solidarity?

**Model proposal:** Mutual aid transforms practical dependence into political solidarity.

**Researcher revision:** Repeated mutual-aid exchanges sometimes created opportunities for political identification. Practical reliance could remain separate from politics or produce withdrawal when help was experienced as obligation.

The claim changes because the researcher restores source context, compares cases, follows sequence, identifies counterevidence and considers an alternative account.

## Python sequence

The code is one connected chain:

`setup → research question and excerpt records → prompt → messages → OpenRouter call → raw JSON string → proposal dictionary → source index → source check → researcher review → interaction log → final analysis record`

Every code slide states the input, Python type, operation, output, research meaning and limit. The client-setup slide makes clear that constructing a client does not transmit interview data; the network request occurs at `client.chat.send(...)`.

## Material deliberately removed

- recurring course-stage map;
- generic “qualitative work was demanding before LLMs” framing;
- Nguyen and Welch;
- AI-moderated interviewing;
- COREQ reporting section;
- class exercises and paired discussion prompts;
- generic request typologies not tied to published work;
- disconnected Python fragments.

## Checks for later revisions

- Never show an excerpt before explaining the study, source and question.
- Anchor methodological moves in the literature; do not present invented levels or checklists as disciplinary consensus.
- Use the published paper or the relevant figure, not a generic first-page image when students need to see evidence.
- Separate context length from application memory and retrieval.
- Make the model's task, complete input and returned object explicit.
- Treat generated themes as suggestions to check, not findings.
- Keep code attached to the same substantive example from beginning to end.
- Inspect paper figures at full presentation size; being in bounds is not the same as being readable.
