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
- How should our customer-support assistant be configured, and what evidence would assess that choice?

## Reading to code

The workbook holds the customer case and policy fixed while changing `assistance_mode`. This implements Barley’s warning that a technology has no single organizational form. It also preserves the distinction between a successful assisted output and evidence that a worker learned.
