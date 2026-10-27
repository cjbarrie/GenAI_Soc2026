# Session 9 synthesis: LLMs at work

**Prepared:** 27 October 2026
**Status:** approval gate 2 revised after instructor feedback; no final slides have been drafted

## Sociological question

**When an LLM helps someone do their job, what changes: their performance, their knowledge, or their position within the organization?**

The class should not use “impact on work” as if it named one outcome. The readings distinguish several:

- performance while assistance is available;
- knowledge that remains when assistance is removed;
- the expertise exercised while carrying out the task;
- discretion over how a task is carried out;
- authority to make the final decision;
- organizational visibility into the labour process;
- employment, wages, hours and task allocation.

## Bounded claim for the class

Students should be able to defend the following claim by the end:

> Evidence of improved performance during LLM assistance is not evidence, by itself, of retained knowledge, worker expertise, discretion or authority. The same measured performance improvement could accompany different distributions of all four.

Brynjolfsson, Li and Raymond identify improvements in measured performance while customer-support workers had access to assistance. Wiles et al. use a different setting, population, set of tasks and design to test knowledge without assistance and find no evidence of greater technical knowledge on that measure. Their juxtaposition demonstrates why performance and knowledge must be distinguished. It does **not** establish that the performance gains in Brynjolfsson, Li and Raymond occurred without learning. The organizational distinctions follow from the historical literature, especially Braverman, Burawoy, Barley and Zuboff. The class will not claim an economy-wide employment effect or a universal direction of deskilling.

## Cumulative example

### Setting

Use an instructor-authored customer-support case at a fictional subscription-software company. A customer sees one completed annual charge and a second pending authorization and says that the unavailable money is urgently needed. The available record does not yet establish two settled charges. The worker has access to:

1. the customer's message;
2. a short internal policy on pending charges, completed duplicate charges and hardship escalation;
3. an LLM assistant configured by the employer;
4. a choice to accept, edit or reject what the system returns.

The internal policy states that a pending authorization is not a completed payment; agents cannot manually release it; a duplicate-charge refund requires two distinct settled transaction identifiers; and financial hardship can be escalated immediately but does not itself authorize a refund. The case is close enough to the setting in Brynjolfsson, Li and Raymond to make the system intelligible, but it is not reconstructed from that firm's proprietary data. Every appearance must label it **instructor-authored teaching material**.

### Two assistance modes

- **Draft mode:** the model returns a recommended action and a customer-facing reply.
- **Coach mode:** the model returns the checks the worker should make and the policy evidence to consult, without writing the final reply.

The wording, policy and model can remain constant while the assistance mode changes. This lets the class ask whether a system supplies an answer or helps a worker reason through the decision. It does not make coach mode intrinsically more autonomous: the organization can still prescribe the workflow and reserve final authority elsewhere.

### Expertise, discretion and authority

The exercise must keep three dimensions separate:

| Dimension | Question |
|---|---|
| Expertise | Who actually performs the substantive reasoning? |
| Discretion | Who chooses how the task is carried out? |
| Authority | Who has the right to make the final decision? |

Draft mode can preserve formal permission to edit or reject the answer while the system performs much of the reasoning. Coach mode can require more worker reasoning while leaving organizational authority unchanged. Neither interface therefore provides a simple measure of autonomy.

### Exact first model operation

The model receives one customer message, one policy passage and one mode instruction. It returns six fields:

```text
known_facts
uncertainties
recommended_action
policy_evidence
worker_guidance
customer_reply
```

In coach mode, `customer_reply` must be `null`. In draft mode, it contains the proposed reply. The raw response is preserved before the fields are read into Python. The substantive check asks whether the output distinguishes the completed payment from the pending authorization, withholds an unsupported refund and recognizes hardship escalation as a separate action.

### What the example can and cannot show

It can show how an organization configures assistance, how the configuration changes the work returned to the employee, how the response can be checked against a policy and how interaction records could make the work visible to management.

It cannot show that real workers became more productive, learned, consented to the system, lost discretion or experienced deskilling. Those claims require evidence from workers and workplaces.

## How the historical lineage changes the example

| Source | Question applied to the example |
|---|---|
| Marx and Braverman | Has technology redistributed knowledge and control within production? Has practical knowledge been formalized by management and returned as instructions? |
| Burawoy | How does the organization of the labour process create practices, incentives and forms of participation around the assistant? |
| Barley | How might the same assistant become part of different occupational arrangements in different workplaces? |
| Zuboff | What new information about workers and the labour process is generated because the task passes through the assistant? |

These form a cumulative argument. Burawoy must not be reduced to a general explanation of why workers like managerial technologies: his account of consent arises from the concrete organization of production and the games workers develop within it.

## What is new about LLM assistance

The class can defend four relatively precise differences:

1. A general language model can generate situated advice for many conversational and knowledge tasks without a separately programmed response for every case.
2. The advice is probabilistic and can remain fluent when it is wrong, which makes its limits difficult for workers to judge.
3. Archives of previous interactions can be converted into recommendations during later live interactions.
4. The worker can complete a task using a generated explanation or answer without being able to reproduce the performance independently.

Scale, speed and generality matter, but they do not remove the older questions about ownership, discretion, control, skill and worker response.

## Jobs performed by the required readings

### Barley (1986)

Barley prevents the lecture from treating a model licence as a workplace outcome. The same CT scanner was incorporated differently in two radiology departments. Students should use the paper to ask which interactions, occupational boundaries and local practices mediate an LLM deployment.

### Brynjolfsson, Li and Raymond (2025)

This paper supplies an observed LLM assistant inside a workplace. It establishes the exact interface, rollout, performance measures and heterogeneity by experience. It does not provide a direct test of whether workers retained knowledge once assistance disappeared.

### Wiles et al. (2026)

This paper provides a direct test of retained knowledge in a different population, setting and task. Consultants performed unfamiliar data-science tasks better with access and training, but the post-experiment test provided no evidence of greater technical knowledge without the tool. The paper turns “upskilling” into an empirical distinction between assisted capability and retained knowledge. It cannot be used to infer whether the customer-support agents in Brynjolfsson, Li and Raymond learned.

## Reading disagreement

The readings do not offer competing yes/no answers to whether AI is beneficial. They use different evidence to answer different questions:

- Barley observes how occupational relations change around a technology.
- Brynjolfsson, Li and Raymond estimate changes in measured workplace performance during assisted work.
- Wiles et al. compare assisted performance with later unassisted knowledge in a separate experiment.

The discussion should ask which meaning of skill and which unit of analysis each paper supports. Students should not average the findings into a generic claim about productivity.

## Reading-to-code map

| Reading idea | Decision in the routine | Check |
|---|---|---|
| Barley: technology is enacted through work relations | Compare a drafting configuration with a coaching configuration | Describe the expertise exercised, discretion available and authority retained in each mode |
| Brynjolfsson et al.: an assistant provides situated recommendations | Supply a customer message and internal policy to a live model call | Check the recommendation against the policy rather than trusting fluency |
| Wiles et al.: assisted performance is not retained knowledge | Keep the code's claim at the level of generated assistance | State explicitly that the run provides no evidence of worker learning |
| Zuboff: computerization also produces information about work | Save mode, input, raw response and worker decision in a record | Identify what an employer could infer from the resulting log |

## Python progression

Week 8 introduced a loop across cases and compared OpenRouter with Ollama. Week 9 should not add another loop, pandas or a large simulation. Its new Python idea is one small function.

Students first run the routine with literal values. Only after they can identify every value and type do they place the already-understood steps inside:

```python
def request_assistance(customer_message, policy_text, assistance_mode, route):
    ...
    return assistance_record
```

The function is not introduced as cleaner software. It is introduced because the researcher wants to apply the same documented operation after changing one named input. Every argument, local value and returned field must be visible.

## Material outside the main session

- Economy-wide job forecasts and exposure indices.
- A survey of every occupation using generative AI.
- Generative-agent simulations or multi-agent systems.
- A general tutorial on function design, classes or software abstraction.
- Speech interfaces, tool use and research agents.
- Claims that the teaching example demonstrates real productivity, learning or deskilling.

These would dilute the question that the assigned readings can actually answer.
