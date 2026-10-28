# Session 9 architecture: LLMs at work

**Date:** Wednesday, 4 November 2026, 9:30 a.m.–12:15 p.m.
**Status:** approval gate 3 build complete; awaiting instructor review before publication

## Intended endpoint

Students should leave able to answer four questions in ordinary language:

1. What evidence would show improved performance, retained knowledge or a change in a worker's organizational position?
2. Why can the same LLM system become part of different working arrangements?
3. How do expertise, discretion and authority differ in the teaching example?
4. What exactly enters and leaves the Week 9 Python function?

The bounded substantive claim is:

> Evidence of improved performance during LLM assistance is not evidence, by itself, of retained knowledge, worker expertise, discretion or authority. The same measured performance improvement could accompany different distributions of all four.

The computational endpoint is that students can explain `call_review_assistant(messages, route)` by replacing each parameter with an actual value, tracing both model calls and identifying where the worker's choice changes the program.

## Connection to the course

Weeks 7 and 8 asked whether model-generated responses reproduce observed human outcomes. Week 9 changes the unit of analysis. The model now supplies advice inside a labour process, and the empirical question concerns workers, tasks and organizations rather than synthetic respondents.

The continuity is methodological: students must still define the target, preserve the raw model return and compare the output with external evidence. The new issue is organizational: a technically identical model call can redistribute knowledge, discretion and visibility at work.

## Cumulative example and provenance

The example adapts the statistical task in Wiles et al. A general consultant reviews an AI interpretation of an unfamiliar mortgage-prediction model. The numerical results and AI analysis are instructor-authored, contain no participant data and are not presented as findings from the paper.

### Customer message

> The model is 80% accurate on 200 held-out historical cases. Always predicting no mortgage is 60% accurate, and the model has 20 false negatives among 80 observed mortgage cases.

### Internal policy

> The model is 80% accurate, so it is ready to guide an investment strategy. Its score shows that increasing a couple's score causes them to take out a mortgage. It also performs much better than the current baseline, which is no better than chance.

### Organizational comparison and implemented workflow

- In **draft mode**, the assistant reviews the claims and writes a proposed client note.
- In **coach mode**, the assistant asks questions and identifies missing evidence but leaves the assessment and client note to the consultant.

The lecture compares these two configurations. The coding exercise then implements coach mode as a short work process. The worker reads the first reply and chooses whether to ask the model again, escalate to the data-science team or begin writing. The supplied path asks a follow-up question. The worker then records a final action and reason.

Draft mode may leave the worker with permission to edit or reject the response even though the system has performed much of the reasoning. Coach mode may require the worker to perform more reasoning without increasing the worker's formal authority. The comparison therefore separates:

| Dimension | Question |
|---|---|
| Expertise | Who actually performs the substantive reasoning? |
| Discretion | Who chooses how the task is carried out? |
| Authority | Who has the right to make the final decision? |

### Output contract

The response contains:

```python
{
    "baseline_comparison": "model_outperforms_baseline",
    "causal_claim": "not_supported",
    "decision_status": "needs_more_information",
    "explanation": ["..."],
    "questions_for_worker": ["..."],
    "data_science_escalation": "..."
}
```

The model output is checked against three stated requirements. It should compare 0.80 with the 0.60 baseline, reject the unsupported causal claim and avoid treating accuracy alone as evidence that the model is ready for an investment decision. A valid dictionary and passing checks do not establish productivity, learning, worker consent or autonomy.

## 165-minute class architecture

| Time | Section | Main question | Student activity | Evidence of understanding |
|---|---|---|---|---|
| 9:30–9:45 | Consulting case and exact LLM operation | What is the assistant being asked to do? | Read the model results, questionable AI analysis, prompt and one returned object | Students name the input, output and assessment left to the worker |
| 9:42–10:20 | Historical lecture | How can technology redistribute knowledge, control and information at work? | Follow a cumulative argument across original sources from Marx and Braverman, Burawoy, Barley and Zuboff | Students explain how each stage changes the question carried into the next |
| 10:20–10:30 | Break |  |  |  |
| 10:30–11:15 | Reading discussion | What do the three required papers actually establish? | Compare unit, design and outcome; then separate expertise, discretion and authority in the teaching case | Students distinguish assisted performance, retained knowledge and organizational position |
| 11:15–11:25 | Contemporary evidence synthesis | What can we say across the papers? | Revisit the results and state one bounded conclusion | Students identify which claims require evidence the papers do not provide |
| 11:25–12:05 | Python and LLM walkthrough | What can the worker decide after receiving model advice? | Trace the first call, choose the next step, make an optional follow-up call and record a final decision | Students explain every input, type, operation, output and worker choice |
| 12:02–12:15 | Reflection, unassisted question and close | What did the assistant change about the work? | Inspect the work record, answer the accuracy question and return to the opening case | Students distinguish model reasoning, worker decisions and organizational visibility |

The opening lecture is 50 minutes including the concrete LLM operation. The middle 45 minutes are reserved for discussion of the assigned readings. The final 50 minutes develop the code, with ten minutes to rerun and close.

## Role of every source

### Historical lecture sources

| Source | Teaching job | Evidence required on screen |
|---|---|---|
| Marx, *Capital*, vol. 1, ch. 15 | Place machinery inside capitalist production and control rather than treating technology as an autonomous cause | Original book or reputable full text and a checked passage on the capitalist application of machinery |
| Braverman, *Labor and Monopoly Capital* | Explain management's attempt to separate conception from execution and monopolize knowledge of the labour process | Original book, scientific-management material and a complete checked passage |
| Burawoy, *Manufacturing Consent* | Show how the organization of production generates workplace games, incentives and consent; workers are not passive recipients of managerial design | Original book and a legible source passage or diagram on “making out” |
| Barley (1986) | Demonstrate that the same technology can be enacted through different occupational relations | Published title page, comparative design, operational-decision figure and clandestine-teaching example |
| Zuboff, *In the Age of the Smart Machine* | Explain that computerization can perform work while generating new information about it | Original book and one workplace case supporting automate/informate |

### Required contemporary papers

| Paper | Teaching job | Result to show |
|---|---|---|
| Brynjolfsson, Li and Raymond (2025) | Show an actual LLM assistant inside live customer-support work | Interface; staggered rollout; approximately 15% average increase in issues resolved per hour; larger gains among less experienced workers |
| Wiles et al. (2026) | Supply a separate design that directly distinguishes assisted capability from retained knowledge | Task-performance figure followed by the post-experiment technical-knowledge result |

Barley is both a required reading and part of the historical lecture. It should not be repeated as a separate paper summary during discussion.

## Reading discussion

The discussion should use the consulting case throughout.

### Question 1 — What counts as skill in each paper?

- In Barley, where does practical knowledge appear during CT work?
- In Brynjolfsson, what outcomes indicate improved performance?
- In Wiles et al., what additional evidence is used to test retained knowledge?

The aim is to stop the class from using productivity, expertise and learning interchangeably.

### Question 2 — Where does occupational knowledge reside?

Compare the technologists' “clandestine teaching” in Barley with the customer-service assistant trained on earlier conversations and the consultants working with ChatGPT in Wiles et al. Ask whether knowledge remains with workers, becomes an organizational asset, or is distributed across workers and systems.

### Question 3 — What can workers decide?

For each study, identify who performs the reasoning, who can choose how to carry out the task and who has the right to make the final decision. Apply all three questions to draft and coach mode in the mortgage-model review. Do not infer that permission to edit necessarily means the consultant exercised the expertise embodied in the answer.

### Question 4 — Why do less experienced workers sometimes gain more?

Consider at least three interpretations: access to codified expertise, standardization towards an organizational norm and a lower starting baseline. Ask what evidence would distinguish them.

### Question 5 — Would Barley expect the same assistant to have the same effect elsewhere?

Specify which occupational relations, incentives, training arrangements and performance measures could change the result. This question moves from Barley's hospitals to the limits of the one-firm customer-service study.

### Question 6 — Which version would we deploy?

The room chooses draft mode, coach mode or a third design. Each proposal must state the intended outcome and the evidence needed to determine whether the system improved performance, supported learning, changed discretion or altered authority.

### Methodological caution during discussion

Brynjolfsson, Li and Raymond and Wiles et al. must not be combined into a cross-study causal claim. The former identify performance changes during workplace assistance. The latter test unassisted knowledge in a different experiment. Their juxtaposition clarifies the outcomes that research should distinguish; it does not show whether the customer-support agents learned.

## Reading-to-code map

| Reading | Code object | Research connection |
|---|---|---|
| Barley | `worker_next_step` and the two model calls | The worker and system divide the review between them; compare expertise, discretion and authority separately |
| Brynjolfsson et al. | the situated model replies | The model supplies advice during the task; our exercise does not estimate a performance effect |
| Wiles et al. | `model_results`, `ai_analysis` and the final unassisted question | A successful assisted review does not test unassisted knowledge |
| Zuboff | `work_record` containing both replies, the worker question and final decision | Passing work through the system creates information about the task and worker response |

## Human-method-to-code map

| Workplace activity | Python representation | What is thinner in the code |
|---|---|---|
| Organization supplies technical evidence | `model_results` dictionary | A few summary figures omit the data, modelling choices and decision context |
| Earlier AI analysis is presented for review | `ai_analysis` string | The text records claims but not how they were produced |
| System begins in coach mode | `assistant_instruction` string | Actual interface design, incentives and training are not represented |
| Assistant returns a suggestion | raw response string and parsed dictionary | Fluency does not show accuracy or usefulness to a worker |
| Worker chooses the next step | `worker_next_step` string and an `if/elif` branch | A selected string cannot reproduce workplace pressure or organizational authority |
| Worker asks for more help | two messages appended to the conversation | A follow-up may support understanding or move more reasoning to the model |
| Worker makes a final decision | `worker_final_action` and `worker_reason` strings | The example records a choice but cannot establish meaningful discretion |
| Organization retains a record | `work_record` dictionary | The example shows possible visibility, not actual managerial use |

## Python progression and complete flow

### What is new

- the first student-edited `def` statement;
- function parameters;
- local variables;
- `return`;
- calling the same function again after a worker decision.

### What is deliberately reused

- strings;
- dictionaries;
- lists of messages;
- `if/else` for the visible OpenRouter/Ollama route;
- JSON parsing;
- Boolean checks;
- preserving the raw response.

### Digestible execution order

1. Store the model results in a dictionary and print its value and type.
2. Store the AI-written analysis in a string and identify the claims requiring review.
3. Store the coach instruction and explain which work remains with the consultant.
4. Convert the results dictionary to text, build the complete prompt and show the exact text sent to the model.
5. Build the message list and inspect the first dictionary.
6. Execute the selected route with both route branches visible.
7. Print the raw response before parsing.
8. Parse the six requested fields into a dictionary.
9. Inspect the baseline, causal and decision-status fields.
10. Check that 0.80 is compared with the stated 0.60 baseline.
11. Check that held-out predictive evidence is not treated as causal evidence.
12. Check that accuracy alone is not treated as sufficient for a deployment decision.
13. Repeat the already-understood call inside `call_review_assistant(messages, route)`.
14. Replace both parameters with the actual values entering the first call.
15. Show the first returned dictionary and its type.
16. Store three available worker actions and select one in `worker_next_step`.
17. If the worker asks again, append the first reply and a follow-up question to `messages`.
18. Call the same function with the three-message conversation.
19. If the worker escalates or starts writing, store `None` instead of making another call.
20. Record the worker's final action and reason.
21. Save the model replies and worker choices together in `work_record`.
22. Reflect on model reasoning, worker choice, organizational visibility and later unassisted knowledge.
23. Answer one new accuracy question without model assistance.

No loop, class, initializer, pandas object or hidden model helper is introduced. A small supplied route utility may prevent duplicated authentication code, but the actual request arguments and response extraction remain visible.

## Proposed title-only slide sequence

The titles are intentionally descriptive. Parenthetical labels identify the slide's job and will not appear as visible production notes.

### Opening object and exact LLM operation

1. **LLMs at work**
2. **A consultant reviews an AI analysis of a prediction model**
3. **What the supplied results establish**
4. **The assistant receives the results, the analysis and an instruction**
5. **The assistant sits inside an existing division of labour**
6. **Draft mode writes a proposed client note**
7. **Coach mode leaves the assessment to the consultant**
8. **What has changed in the worker's job?**

Transition: the exact operation is now visible. The lecture can ask what sociology already gives us for interpreting it.

### The historical argument

8. **Marx studied machinery as part of capitalist production**
9. **Braverman examined management's control over knowledge of the labour process**
10. **Scientific management separates planning from execution**
11. **A workplace assistant can return codified practice as an instruction**

Transition: Marx and Braverman explain how technology can redistribute knowledge and control. They do not make workers passive recipients of managerial design.

12. **Burawoy studied the production quota game known as “making out”**
13. **His account of consent begins with the organization of shop-floor production**

Transition: workers develop practices and incentives within the labour process. These interactions help explain why a technology does not produce one organizational result everywhere.

14. **Barley followed the same CT scanner into two hospitals**
15. **Radiologists and technologists developed different working relations around it**
16. **The technology did not determine one occupational settlement**

Transition: Barley shows how local interaction changes the organizational result. Zuboff adds what computerization allows organizations to observe.

17. **Zuboff observed computerization inside workplaces**
18. **Computer systems performed tasks and produced new information about them**
19. **An LLM assistant can record the work it helps produce**

### The distinctions carried into the current literature

20. **Expertise, discretion and authority describe different parts of the job**
21. **The consulting case raises questions about performance, knowledge and organizational position**

Transition: the contemporary studies supply different evidence for these outcomes. They are not interchangeable tests of one general AI effect.

### Required contemporary studies

22. **Brynjolfsson, Li and Raymond studied an assistant used during customer-support chats**
23. **The assistant offered replies and links to internal documentation**
24. **The rollout allows assisted and unassisted work to be compared over time**
25. **Issues resolved per hour increased by about 15 per cent on average**
26. **Less experienced agents gained more**
27. **The study measures performance while assistance is available**
28. **Wiles and colleagues tested unfamiliar data-science work**
29. **Consultants received either ChatGPT access and training or conventional resources**
30. **ChatGPT improved performance on the assisted tasks**
31. **The later test found no evidence of greater technical knowledge without ChatGPT**
32. **This is a separate study of a different outcome**

### Break and reading discussion

33. **Break**
34. **The readings examine different aspects of skill at work**
35. **Possible explanations for the larger gains among less experienced workers**
36. **The mortgage-model review involves four kinds of work**
37. **Draft and coach modes allocate the review differently**

Transition: the discussion produces a concrete design choice. The final section implements that choice and shows exactly what is recorded.

### Python and LLM walkthrough

38. **The coding exercise uses coach mode**
39. **The complete program**
40. **The program starts with a dictionary of model results**
41. **The AI analysis is stored as a string**
42. **The coaching instruction is another string**
43. **The results dictionary becomes prompt text**
44. **The message list is the request sent to the model**
45. **The selected route sends the request to OpenRouter or Ollama**
46. **The raw return is text**
47. **JSON parsing turns the text into a dictionary**
48. **The dictionary separates the baseline, causal and decision assessments**
49. **The explanation and worker questions occupy separate fields**
50. **The first check tests the baseline comparison**
51. **The next checks test the causal claim and decision status**
52. **The worker chooses the next step**
53. **The function receives the current conversation and route**
54. **The worker receives the first reply**
55. **A follow-up preserves the earlier exchange**
56. **The worker can stop without making a second call**
57. **The worker records a final action and reason**
58. **The work record contains model and worker contributions**
59. **What changed in the work?**

### Close and completion task

60. **Answer one accuracy question without the assistant**
61. **Week 9 coding task**
62. **What can we conclude?**
63. **Questions that remain open**

Sixty-six slides is a planning ceiling, not a target to preserve. The historical section has been reduced from twenty slides to twelve so that the class can inspect the primary evidence rather than move through author summaries. The code sequence remains granular because these are beginners encountering functions for the first time.

## Title-only transition audit

The title sequence makes the following movement without relying on body text:

`exact workplace operation → redistribution of knowledge and control → worker practices within the labour process → organizational variation → information and visibility → contemporary performance evidence → a separate retained-knowledge test → comparison in discussion → worker-controlled model interaction in Python → unassisted knowledge question → return to the opening case`

No section begins with a generic course-stage map. Each historical author answers a question created by the preceding section. The contemporary studies enter only after performance, retained knowledge and control have been separated as outcomes.

## Take-home completion task

Students will use the provided Week 9 notebook or local script. They will:

1. run the initial request using their selected route;
2. explain the two function arguments using their actual values and types;
3. choose a worker next step or rewrite the follow-up question;
4. show the raw and parsed output for every call actually made;
5. record and explain the worker's final decision;
6. identify one supported comparison and one claim requiring further evidence;
7. explain what the assistant did, what the worker decided and what the record makes visible;
8. answer the final accuracy question without model assistance;
9. connect the limits of the exercise to one required reading;
10. submit a narrated screen recording under the naming convention in the recording guide.

Code style and compactness are not graded. A student can earn completion by using the supplied function and explaining it accurately; they are not asked to write a function from a blank page.

## Material to remove or archive from the obsolete Week 9

- Macy and Willer as the required historical anchor;
- Park et al. on generative agents;
- Chuang et al. on opinion dynamics;
- synchronous updating;
- agent state, neighbours and emergent macro-order;
- the `choose_action` function;
- the “Simulate” course-stage label.

The obsolete files should remain untouched until the architecture is approved. During the aligned build they will be replaced or archived deliberately so a generator cannot restore them.

## Approval questions

Before final slides or code are built, confirm:

1. Should Barley, Brynjolfsson et al. and Wiles et al. remain the three complete required articles?
2. Is the adapted Wiles mortgage-model review an acceptable cumulative example?
3. Should draft mode and coach mode be the organizational comparison?
4. Is the sequence Marx → Braverman → Burawoy → Barley → Zuboff the intended historical arc?
5. Is the final function appropriately modest for the first student-edited function in the course?

## Gate 2 self-check

- **Can the argument be reconstructed from the titles?** Yes. The sequence begins with the exact operation, develops one cumulative historical argument, separates the contemporary outcomes and then implements one organizational comparison.
- **Is the LLM operation concrete early enough?** Yes. Slides 2–6 show the material, request and two output forms before the historical section.
- **Does the prehistory establish evidence as well as names?** In the final build it must. Each author has a specified primary object, passage, case or figure; no author should appear only as a portrait or book cover.
- **Does each required paper have a distinct job?** Yes. Barley addresses organizational variation, Brynjolfsson et al. assisted workplace performance and Wiles et al. directly test retained knowledge in a separate setting. The deck will not infer learning or its absence in the Brynjolfsson setting from the Wiles result.
- **Is the example accurately bounded?** Yes. It is labelled instructor-authored and supports comparison of system configurations only.
- **Does the discussion prepare the code?** Yes. It ends by choosing how the assistant should be configured; the code makes that choice an explicit string argument.
- **Is the Python addition appropriately small?** Yes. The only new syntax is a function, its parameters, local values and return. Previously taught strings, dictionaries, branches and parsing remain visible.
- **Does the code preserve worker judgment?** Yes. Students compare the recommendation with the supplied evidence and identify technical issues that still require worker or specialist judgment.
- **Does the close answer the opening?** Yes. It separates the kinds of evidence needed for performance, knowledge and organizational position rather than claiming that the interface establishes a real workplace effect.
- **What remains before final construction?** Source acquisition for the historical books and the two other required articles; exact figure and quotation checking; live and cached model outputs; aligned site, notebook, local script and task; rendered and end-to-end review.
