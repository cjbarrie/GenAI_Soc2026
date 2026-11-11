# Week 10 implemented architecture

## Central question

What happens to social relationships when people use LLMs to help them communicate, interpret others and manage interpersonal interactions?

The lecture keeps three outcomes separate:

- what language the system produces;
- how assistance may influence the writer;
- how a recipient interprets the communicative act.

The deck does not cover AI companionship, artificial confidants or the replacement of human emotional support.

## Required readings

1. Zelizer (2012), “How I Became a Relational Economic Sociologist and What Does That Mean?”
   - Teaching job: establishes how ties, transactions, media and meanings are matched.
2. Hohenstein et al. (2023), “Artificial Intelligence in Communication Impacts Language and Social Relationships.”
   - Teaching job: distinguishes randomized access to smart replies, recorded use, suspected use, conversational language and partner judgments.
3. Williams-Ceci et al. (2026), “Biased AI Writing Assistants Shift Users’ Attitudes on Societal Issues.”
   - Teaching job: identifies influence on the writer during composition rather than persuasion of a recipient.

Goffman, Garfinkel, Hochschild and Gershon provide the main lecture background. Illouz and Katz and Lazarsfeld are not part of the implemented deck or reading list.

## Cumulative example

A close colleague’s mother has died. The sender knew she had been ill but never met her. The sender wants to send a private message before the funeral and can offer to take the seminar notes that week.

The substantive facts remain fixed while the lecture varies how the message was produced:

- written without assistance;
- drafted by an LLM and substantially revised;
- copied from an LLM without revision;
- generated and sent automatically by a system trained on the sender’s writing.

The same words do not establish the same production process, feeling, effort or recipient interpretation.

## Timed class architecture (165 minutes)

### 0–18 minutes: the condolence case and the analytic problem

- Show one plausible generated message.
- Compare four production histories for the same words.
- Separate evidence about the message, sender and recipient.

### 18–36 minutes: Goffman and Garfinkel

- Use Goffman to treat condolence as an interactional obligation involving face and an appropriate line.
- Use Garfinkel’s clarification demands, acting as a lodger at home and bargaining over fixed prices as a short sidebar on breaching demonstrations.
- Use the social-media trend of men calling male friends simply to say good night as a contemporary illustration, clearly labelled as an example rather than research evidence.
- Return to the main argument without treating the condolence case as a breaching experiment.

### 36–61 minutes: Hochschild

- Establish the evidence in the 1979 article: 261 written protocols.
- Define feeling rules and emotion work from the primary text.
- Explain Hochschild’s extension of Goffman from visible conduct to attempts to manage feeling.
- Distinguish surface acting from deep acting.
- Compare formulation, reflection, expression and delegation of the act itself as different kinds of offloading.

### 61–78 minutes: Zelizer and Gershon

- Use the same £50 transfer as reimbursement, gift or loan repayment to make Zelizer’s relational argument concrete.
- State explicitly that extending Zelizer from economic exchange to condolence is a course application rather than her direct object.
- Use Gershon’s account of media ideologies to connect relationship-specific meaning to the medium and production process.
- Ask what changes if an AI system can mimic the sender’s voice perfectly.

### 78–88 minutes: break

### 88–120 minutes: contemporary studies

- State the gap: the papers test bounded parts of AI-mediated communication rather than providing a sociology of established relationships.
- Hohenstein et al.: design, actual versus suspected use, partner ratings and randomized suggestion valence.
- Williams-Ceci et al.: interface, experimental conditions, writer outcomes and limits.
- Compare what each study observes and what remains unobserved.

### 120–137 minutes: reading discussion

- When does assistance help someone fulfil an obligation, and when does it delegate the obligation?
- Which Hohenstein estimates are causal and which are correlational?
- What design would be required to study recipient interpretation in an established relationship?
- What evidence would distinguish stylistic assistance from emotion work or relational repair?

### 137–160 minutes: Python walkthrough

- Students record their intended action before seeing model advice.
- A small `audit_situation()` function sends one structured prompt.
- A loop applies the same function to condolence, workplace-credit and private-information cases.
- The raw return is preserved before JSON parsing.
- Students compare the proposed action with their own judgment and store the comparison in an audit dictionary.
- The exercise introduces a default Boolean parameter, keyword arguments, `enumerate()` and a returned dictionary.

### 160–165 minutes: return to the opening case

Generated text is observable. Emotion work, relational appropriateness and consequences for the relationship require evidence from people and interactions.

## Artifact alignment

The current slides, course-book chapter, Python page, notebook, downloadable task, solution, recorded fixtures, reading guide and instructor notes all use the condolence case and the same three audit situations. Any future change to a situation identifier or schema must be made across all of these artifacts.
