# Session 9 reading guide — LLMs at work

## The question to carry into class

When an LLM helps someone do their job, what changes: their performance, their knowledge, or their position within the organization?

## Read the three articles for different kinds of evidence

| Reading | What it observes | Question for discussion |
|---|---|---|
| Barley (1986) | Work interactions and operational decisions around the same CT scanner in two hospitals | Why did the technology become part of different occupational arrangements? |
| Brynjolfsson, Li & Raymond (2025) | Customer-support performance while an LLM assistant was available | Which outcomes improved, for whom, and what was not tested? |
| Wiles et al. (2026) | Assisted data-science performance and a later technical-knowledge test without ChatGPT | What is the difference between doing a task with assistance and retaining the underlying knowledge? |

## Before class

Bring one passage or figure from each article. For every item, write down:

1. the unit of analysis;
2. the observed outcome;
3. the strongest claim it supports;
4. one claim for which it is insufficient evidence.

## Questions for the room

- Where does occupational knowledge reside in each study?
- Who performs the reasoning, who chooses the procedure and who has the final authority?
- Why might less experienced workers gain more from assistance?
- Would Barley expect the same assistant to have the same effect in another workplace?
- How should the consulting assistant be configured when a general consultant reviews unfamiliar technical work?

## Reading to code

The workbook implements coach mode as a short workplace interaction. The consultant reads the first response, chooses whether to ask the model again, consult the data-science team or begin writing, and then records a final action. This makes the worker's place in the process visible rather than treating them as the recipient of a completed output. Barley helps us examine the resulting division of labour. Zuboff directs attention to the new record of the worker's question and decision. A final unassisted question preserves Wiles et al.’s distinction between successful assisted work and evidence that a worker learned.
