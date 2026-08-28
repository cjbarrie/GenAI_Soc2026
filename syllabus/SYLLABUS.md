# Generative AI in Sociology

**Fall 2026 · NYU Sociology · Wednesdays 9:30 a.m.–12:15 p.m.**

## Course question

What inference is the researcher trying to make, and what evidence would validate the use of an LLM for that inference?

This graduate seminar studies generative AI both as a research technology and as a social object. The semester moves from measurement and interpretation through experimental intervention and social simulation to research agents, replication, and audits. The course is approximately 60% methodological and 40% substantive sociology of AI.

No prior programming course is required. Students must be willing to work through the Python foundations material and explain small pieces of code in plain language. Code sophistication is not an independent virtue.

## What students will learn

By the end, students should be able to:

1. distinguish an LLM transformation from the sociological inference built on its output;
2. formulate inferential targets for annotation, treatments, synthetic respondents, simulations, agents, and audits;
3. design validation evidence appropriate to the target and likely error process;
4. read and write small Python programs using values, collections, conditionals, loops, and functions;
5. explain every important input, type, operation, output, and research meaning in course code;
6. compare hosted and local model workflows without treating either as a gold standard;
7. preserve prompts, raw outputs, settings, model/runtime identifiers, provenance, and validation decisions;
8. design and communicate a defensible LLM-related sociological study.

## Semester map

| Movement | Sessions | Research capability | Python capability | Validation habit |
|---|---:|---|---|---|
| Evidence, measurement and interpretation | 1–4 | Turn social material into inspectable records and measures | strings, lists, dictionaries, JSON and multimodal messages | inspect inputs and source evidence |
| Experiments and research encounters | 5–6 | Generate fixed and conversational treatments | call parameters and ordered conversation state | compare intended and experienced treatments |
| Synthetic populations and social simulation | 7–10 | Represent people, distributions and interaction | schemas, loops, functions and repeated runs | validate at several levels and probe contamination |
| Research agents, replication and model audits | 11–13 | Use tools while preserving evidence; study models socially | tool records, saved JSON and parameter grids | reproduce, document dependence and bound claims |
| Presentations | 14 | Present and defend a research design | no new coding | identify validation and failure modes |

## Schedule

| Session | Date | Question | Materials |
|---:|---|---|---|
| 1 | Sep 2 | What kind of research technology is an LLM? | [Session entry](session01.md) |
| 2 | Sep 9 | What can an LLM output validly measure? | [Session entry](session02.md) |
| 3 | Sep 16 | What does interpretation mean when an LLM assists qualitative research? | [Session entry](session03.md) |
| 4 | Sep 23 | What counts as evidence across text, image, and audio? | [Session entry](session04.md) |
| 5 | Sep 30 | Can generated media isolate a causal construct? | [Session entry](session05.md) |
| 6 | Oct 7 | What changes when the model becomes an interactant? | [Session entry](session06.md) |
| — | Oct 14 | No Wednesday meeting: NYU legislative Monday | Midterm project-proposal period |
| 7 | Oct 21 | Whose attitudes and experiences do synthetic populations represent? | [Session entry](session07.md) |
| 8 | Oct 28 | Can LLMs recover missing or unobserved social worlds? | [Session entry](session08.md) |
| 9 | Nov 4 | How can micro-level interactions generate macro-level order? | [Session entry](session09.md) |
| 10 | Nov 11 | When can agent diversity and debate produce collective intelligence? | [Session entry](session10.md) |
| 11 | Nov 18 | Who—or what—produces research data in an agentic workflow? | [Session entry](session11.md) |
| 12 | Nov 25 | What can we reproduce, and what remains opaque? | [Session entry](session12.md); flexible attendance |
| 13 | Dec 2 | What culture, ideology, and hierarchy are encoded in models? | [Session entry](session13.md) |
| 14 | Dec 9 | Project presentations | [Session entry](session14.md); no new reading, lecture or weekly task |

## Typical meeting

The first part introduces the sociological problem and the methodological background. The middle part is a class discussion of the assigned readings. The final part is a guided walkthrough of the weekly coding exercise, with pauses to identify each input, operation, output and research meaning.

The normal schedule is 9:30–10:00 for framing and background, 10:00–10:50 for reading discussion, 10:50–11:00 for a break, 11:00–12:05 for the coding walkthrough, and 12:05–12:15 for questions and preparation. The exact timing can move slightly, but reading discussion occupies the middle of the class and coding occupies the final part.

## Assessment

| Component | Weight |
|---|---:|
| Weekly trace tasks: ten best submissions | 20% |
| Midterm project proposal | 20% |
| Individual oral code walkthrough | 5% |
| Final-project milestones | 10% |
| Final research-design package | 25% |
| Final presentation | 10% |
| Participation and reading preparation | 10% |

Weekly tasks receive completion marks and are submitted as narrated screen recordings. Students record themselves running the exercise and explain aloud the input and output of every operation, the model call and returned object, the named change, the methodological meaning and one limit. Recordings are uploaded to a dedicated NYU Box folder; the instructor will provide the link. Editing quality and code elegance are not assessed. Missing elements may be supplied within one week.

The midterm project proposal is released after Session 6 and submitted before Session 7. In 1,200–1,500 words, students set out a sociological question, locate it in a focused body of literature, specify the evidence and design, explain the proposed role of an LLM, and give one worked input → operation → output → validation example. The proposal also identifies likely failures, ethical issues, the reproducibility record, and the next steps toward the final project. It is a formative stage of the final project, not a Python test or a commitment to complete a full empirical study.

The separate 10–12 minute oral walkthrough follows shortly afterward and provides the direct check of code understanding. With a short code extract visible, each student explains inputs and types, every line or small block, output and one modification, and the sociological meaning. No live generative assistance is used during the oral walkthrough.

The final project is a self-designed LLM-related sociological research design and class presentation. A minimal input/output trace or proof of concept is expected where feasible; a completed empirical paper is not.

## AI use: do not outsource your learning

Generative AI use is permitted with responsibility and disclosure. These tools can help explain an error, compare approaches, or challenge an argument. They can also remove precisely the difficult work through which you learn to program, interpret evidence, and discover what you do not yet understand.

You remain responsible for every submitted claim and every line of code. If you cannot explain what a line takes as input, what it does, what it returns, and why it belongs in the research design, it is not yet ready to submit. Material assistance requires a short disclosure naming the tool/model, its purpose, what was incorporated, and how it was checked. When an LLM is part of the research method, preserve the full research record. The oral walkthrough is completed without live AI assistance. See [the full policy](AI_USE_POLICY.md).

## Computing and access

Canonical notebooks run in local JupyterLab or VS Code, with Colab as an OpenRouter-only fallback. Every student attempts both OpenRouter and Ollama by the end of Week 2, chooses either route in Weeks 3–7, and compares both routes again in Week 8. OpenRouter is the hosted gateway; Ollama is the supported local runtime. Recorded outputs remain available when access fails, but are not the normal route. Never send identifiable or sensitive research data through the shared course key.

Start with [environment setup](../docs/ENVIRONMENT_SETUP.md), [Python foundations](../workbook/00_python_foundations/README.md), and the [local-LLM guide](../docs/LOCAL_LLM_GUIDE.md).

## Participation and accessibility

Participation may take the form of a reading question, code explanation, validation critique, peer feedback, or a short written contribution. Speaking frequency alone does not determine the mark. Accessible remote or equivalent formats are available for the oral walkthrough and flexible Session 12 work.
