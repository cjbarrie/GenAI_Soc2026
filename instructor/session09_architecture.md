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

The computational endpoint is that students can explain `request_assistance(customer_message, policy_text, assistance_mode, route)` by replacing each parameter with an actual value, tracing every local object and identifying the returned dictionary.

## Connection to the course

Weeks 7 and 8 asked whether model-generated responses reproduce observed human outcomes. Week 9 changes the unit of analysis. The model now supplies advice inside a labour process, and the empirical question concerns workers, tasks and organizations rather than synthetic respondents.

The continuity is methodological: students must still define the target, preserve the raw model return and compare the output with external evidence. The new issue is organizational: a technically identical model call can redistribute knowledge, discretion and visibility at work.

## Cumulative example and provenance

The example is an instructor-authored customer-support case at a fictional subscription-software company. It contains no participant data and makes no claim about a real firm.

### Customer message

> My bank shows two entries for my annual plan. One has completed and the other still says pending. The pending amount has reduced the money available for my rent tomorrow. Have I been charged twice, and can you refund it today?

### Internal policy

> A pending authorization is not a completed payment and normally disappears within three to five business days. Agents cannot manually release or refund a pending authorization. A duplicate-charge refund requires two distinct settled transaction identifiers. A customer reporting immediate financial hardship may be escalated to a supervisor, but escalation does not itself authorize a refund.

### Organizational comparison

- In **draft mode**, the assistant recommends an action and writes the customer-facing reply.
- In **coach mode**, the assistant lists the checks and relevant policy evidence but leaves the final reply to the worker.

The exercise holds the case and policy constant. It changes only `assistance_mode`. The comparison is about the design of assistance, not about which generated passage sounds nicer.

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
    "known_facts": ["..."],
    "uncertainties": ["..."],
    "recommended_action": "...",
    "policy_evidence": "...",
    "worker_guidance": "...",
    "customer_reply": "... or None"
}
```

The model output is checked against the policy and the mode requirement. In particular, it must not treat the pending authorization as proof of a second settled charge or promise a refund without two settled transaction identifiers. It should distinguish hardship escalation from refund authorization. A valid dictionary and a policy-consistent answer do not establish productivity, learning, worker consent or autonomy.

## 165-minute class architecture

| Time | Section | Main question | Student activity | Evidence of understanding |
|---|---|---|---|---|
| 9:30–9:42 | Customer-support case and exact LLM operation | What is the assistant being asked to do? | Read the message, policy, prompt and one returned object | Students name the input, output and decision left to the worker |
| 9:42–10:20 | Historical lecture | How can technology redistribute knowledge, control and information at work? | Follow a cumulative argument across original sources from Marx and Braverman, Burawoy, Barley and Zuboff | Students explain how each stage changes the question carried into the next |
| 10:20–10:30 | Break |  |  |  |
| 10:30–11:15 | Reading discussion | What do the three required papers actually establish? | Compare unit, design and outcome; then separate expertise, discretion and authority in the teaching case | Students distinguish assisted performance, retained knowledge and organizational position |
| 11:15–11:25 | Contemporary evidence synthesis | What can we say across the papers? | Revisit the results and state one bounded conclusion | Students identify which claims require evidence the papers do not provide |
| 11:25–12:05 | Python and LLM walkthrough | How does the organization configure and record assistance? | Trace literal values, one route-specific call, the raw response, parsing, a policy check and the first function | Students explain every input, type, operation, output and limit |
| 12:05–12:15 | Rerun, task and close | What changes when the assistance mode changes? | Run or inspect coach mode; return to the opening case | Students compare discretion across modes without claiming real worker effects |

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

The discussion should use the customer-support case throughout.

### Question 1 — What counts as skill in each paper?

- In Barley, where does practical knowledge appear during CT work?
- In Brynjolfsson, what outcomes indicate improved performance?
- In Wiles et al., what additional evidence is used to test retained knowledge?

The aim is to stop the class from using productivity, expertise and learning interchangeably.

### Question 2 — Where does occupational knowledge reside?

Compare the technologists' “clandestine teaching” in Barley with the customer-service assistant trained on earlier conversations and the consultants working with ChatGPT in Wiles et al. Ask whether knowledge remains with workers, becomes an organizational asset, or is distributed across workers and systems.

### Question 3 — What can workers decide?

For each study, identify who performs the reasoning, who can choose how to carry out the task and who has the right to make the final decision. Apply all three questions to draft and coach mode. Do not infer that permission to edit necessarily means the worker exercised the expertise embodied in the answer.

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
| Barley | `assistance_mode` | The same underlying model can be incorporated into different work arrangements; compare expertise, discretion and authority separately |
| Brynjolfsson et al. | `customer_message`, `policy_text`, generated recommendation | The model receives a live problem and organizational knowledge and returns situated advice |
| Wiles et al. | the explicit limits printed after the run | A successful assisted response does not test unassisted knowledge |
| Zuboff | `assistance_record` containing input, mode, raw return and worker decision | Passing work through the system creates information about the task and worker response |

## Human-method-to-code map

| Workplace activity | Python representation | What is thinner in the code |
|---|---|---|
| Customer presents a problem | `customer_message` string | Tone, history, interaction and consequences are compressed into text |
| Organization supplies policy | `policy_text` string | Informal practice, exceptions and tacit knowledge are omitted |
| System is configured | `assistance_mode` string | Actual interface design, incentives and training are not represented |
| Assistant returns a suggestion | raw response string and parsed dictionary | Fluency does not show accuracy or usefulness to a worker |
| Worker evaluates the suggestion | explicit policy checks and an accept/edit/reject field | Formal permission to edit does not reveal who performed the reasoning or held final authority |
| Organization retains a record | `assistance_record` dictionary | The example shows possible visibility, not actual managerial use |

## Python progression and complete flow

### What is new

- the first student-edited `def` statement;
- function parameters;
- local variables;
- `return`;
- calling the same operation after changing one argument.

### What is deliberately reused

- strings;
- dictionaries;
- lists of messages;
- `if/else` for the visible OpenRouter/Ollama route;
- JSON parsing;
- Boolean checks;
- preserving the raw response.

### Digestible execution order

1. Store the customer message in a string and print its value and type.
2. Store the policy in a second string and print its value and type.
3. Store `assistance_mode = "draft"` and explain that the string changes the organizational instruction.
4. Build the complete prompt and show the exact text sent to the model.
5. Build the message list and inspect the first dictionary.
6. Execute the selected route with both route branches visible.
7. Print the raw response before parsing.
8. Parse the six requested fields into a dictionary.
9. Inspect `known_facts` and `uncertainties` before reading the recommendation.
10. Check that the output does not treat a pending authorization as a second settled payment.
11. Check that a refund is withheld unless two settled transaction identifiers have been verified.
12. Check that hardship escalation is kept separate from refund authorization.
13. Check that draft mode returns a reply and coach mode does not.
14. Save input, mode, route, model, raw response, parsed response and a placeholder worker decision in `assistance_record`.
15. Repeat the already-understood lines inside `request_assistance(...)`.
16. Replace each parameter with the actual value entering the first call.
17. Print the local values inside the function during the first traced run.
18. Show the returned dictionary and its type.
19. Change only `assistance_mode` to `"coach"` and call the function again.
20. Compare expertise, discretion and authority across the two configurations.
21. State what the comparison cannot establish about real performance, learning or organizational control.

No loop, class, initializer, pandas object or hidden model helper is introduced. A small supplied route utility may prevent duplicated authentication code, but the actual request arguments and response extraction remain visible.

## Proposed title-only slide sequence

The titles are intentionally descriptive. Parenthetical labels identify the slide's job and will not appear as visible production notes.

### Opening object and exact LLM operation

1. **LLMs at work**
2. **A customer sees one completed charge and one pending authorization**
3. **The worker has this billing policy**
4. **The assistant receives the customer message, the policy and an instruction**
5. **Draft mode writes a proposed reply**
6. **Coach mode leaves the reply to the worker**
7. **What has changed in the worker's job?**

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
21. **The customer-support case raises questions about performance, knowledge and organizational position**

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
34. **What counts as skill in each paper?**
35. **Where does occupational knowledge reside?**
36. **Who exercises expertise, discretion and authority?**
37. **Why might less experienced workers gain more?**
38. **Would the same assistant have the same effect in another workplace?**
39. **How should the customer-support assistant be configured?**

Transition: the discussion produces a concrete design choice. The final section implements that choice and shows exactly what is recorded.

### Contemporary synthesis

40. **The papers measure different consequences of AI assistance**
41. **The existing evidence does not establish one general effect on skill or control**
42. **Our code compares two configurations rather than real worker outcomes**

### Python and LLM walkthrough

43. **The program starts with one customer message**
44. **The internal policy is stored as a second string**
45. **The assistance mode is another string**
46. **An f-string combines the three values into the model instruction**
47. **The message list is the request sent to the model**
48. **The selected route sends the request to OpenRouter or Ollama**
49. **The raw return is text**
50. **JSON parsing turns the text into a dictionary**
51. **The dictionary separates known facts from unresolved questions**
52. **The recommendation and policy evidence occupy separate fields**
53. **The first check tests whether the output invented a second completed charge**
54. **The second check tests whether the output promised an unsupported refund**
55. **The mode check tests whether the assistant performed the requested kind of work**
56. **The saved record includes the request, response and worker decision**
57. **Every line inside the function has already been run once**
58. **The function gives names to the four values that can change**
59. **The first call replaces every parameter with an actual value**
60. **`return` sends the completed record back to the notebook**
61. **Changing one argument requests coaching instead of a draft**
62. **We now compare who reasons, who chooses the procedure and who decides**
63. **This comparison does not measure productivity, learning or autonomy**

### Close and completion task

64. **Return to the pending authorization**
65. **Performance, knowledge, expertise, discretion and authority require different evidence**
66. **Week 9 coding task**

Sixty-six slides is a planning ceiling, not a target to preserve. The historical section has been reduced from twenty slides to twelve so that the class can inspect the primary evidence rather than move through author summaries. The code sequence remains granular because these are beginners encountering functions for the first time.

## Title-only transition audit

The title sequence makes the following movement without relying on body text:

`exact workplace operation → redistribution of knowledge and control → worker practices within the labour process → organizational variation → information and visibility → contemporary performance evidence → a separate retained-knowledge test → comparison in discussion → two configurations implemented in Python → return to the opening case`

No section begins with a generic course-stage map. Each historical author answers a question created by the preceding section. The contemporary studies enter only after performance, retained knowledge and control have been separated as outcomes.

## Take-home completion task

Students will use the provided Week 9 notebook or local script. They will:

1. run one complete request using their selected route;
2. explain the four function arguments using their actual values and types;
3. change only `assistance_mode` and rerun;
4. show the raw and parsed output for both modes;
5. identify one policy-supported element and one element requiring worker judgment;
6. distinguish expertise, discretion and authority in the two modes;
7. explain why the comparison does not demonstrate learning, productivity or autonomy;
8. connect that limit to one required reading;
9. submit a narrated screen recording under the naming convention in the recording guide.

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
2. Is the duplicate-charge customer-support case an acceptable cumulative example?
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
- **Does the code preserve researcher judgment?** Yes. Students compare the recommendation with the policy and identify an element still requiring worker judgment.
- **Does the close answer the opening?** Yes. It separates the kinds of evidence needed for performance, knowledge and organizational position rather than claiming that the interface establishes a real workplace effect.
- **What remains before final construction?** Source acquisition for the historical books and the two other required articles; exact figure and quotation checking; live and cached model outputs; aligned site, notebook, local script and task; rendered and end-to-end review.
