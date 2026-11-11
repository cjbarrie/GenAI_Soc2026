# Instructor notes — Session 10: Writing, influence and relationships

## Intended endpoint

Students should be able to explain why an LLM-mediated condolence creates at least three empirical objects: generated writing, the sender's process and the recipient's interpretation. They should use Goffman, Garfinkel, Hochschild, Zelizer and Gershon without treating them as interchangeable accounts of authenticity.

## 165-minute plan

- **9:30–9:42 — opening case:** compare four production histories for the same condolence message.
- **9:42–10:00 — Goffman and Garfinkel:** establish the expected interpersonal act and use breaching demonstrations to make its background rules visible.
- **10:00–10:23 — Hochschild:** move from public expression to feeling rules, surface acting, deep acting and possible forms of offloading.
- **10:23–10:40 — Zelizer and Gershon:** use concrete exchanges to establish relational meaning, then treat AI assistance as part of the production medium.
- **10:40–10:48 — opening-case discussion:** ask what changes if a model mimics the sender's voice perfectly.
- **10:48–10:58 — break.**
- **10:58–11:32 — reading discussion:** reconstruct Hohenstein's two studies and Williams-Ceci's outcome; compare all three readings using the opening case.
- **11:32–12:08 — Python walkthrough:** fixed facts, default Boolean parameter, keyword arguments, route call, `enumerate()`, returned record and researcher notes.
- **12:08–12:15 — close:** name what the demonstration shows and the human outcomes still requiring evidence.

## Core explanations

### Goffman

Treat condolence as a public interpersonal act. Silence, delay or a conspicuously generic response can be interpreted as evidence about the relationship. Goffman identifies the visible performance; he does not establish the sender's private feeling.

### Garfinkel

Use only documented demonstrations: acting like a lodger at home, demanding precise clarification of ordinary remarks and bargaining over fixed prices. Garfinkel called these demonstrations rather than conventional experiments. Keep this as a brief sidebar rather than treating the condolence case as a breaching experiment.

The “call your friend to say good night” trend is a useful contemporary sidebar. In the widely circulated version, an adult man calls a male friend only to wish him good night. Friends often laugh, become suspicious or check that he is safe. Do not present this as a scientific study or as evidence about men in general. Its teaching value is that participants themselves display the norm: affection is not necessarily objectionable, but a purposeless bedtime call is treated as requiring an explanation within these friendships.

### Hochschild

Name the evidence: retrospective written protocols concerning attempts to manage emotion. Explain surface acting as a change in expression and deep acting as an attempt to change feeling. An LLM may supply words, facilitate reflection or allow the sender to avoid the expressive task. The message alone cannot distinguish these processes.

### Zelizer and Gershon

Do not define relational work as tone adjustment. Use ordinary transfers: the same sum can be reimbursement, a gift or repayment depending on the relationship and shared understanding. State the limit directly: Zelizer studies economic exchange rather than AI-mediated messages. Gershon supplies the more direct bridge because media ideologies concern what a medium communicates in addition to its literal content. AI assistance becomes part of the production history that may be known, suspected or concealed.

## Contemporary studies

For Hohenstein, draw the actual-use/suspected-use distinction precisely. Random access encouraged use and supports the instrumented actual-use estimates. Suspicion was measured after the interaction and the corresponding association is not a randomized disclosure effect. The outcomes are conversation language and immediate partner ratings, not long-term relationship maintenance.

For Williams-Ceci, establish the writer outcome before showing the effect. The experiment shows that biased suggestions can shift the writer's reported attitude. It does not test whether another person was persuaded.

## Python language

For each block say: **input value and type → operation → output value and type → sociological meaning → unobserved outcome**.

- Each situation dictionary stores the relationship and supplied facts.
- Students record their proposed action before seeing model advice.
- The f-string turns one situation into a prompt string.
- `enumerate()` supplies the position and situation on each iteration.
- The function returns a record containing the raw and parsed model response.
- A default Boolean records whether the student would follow the advice.
- The final audit dictionary keeps the student's before and after responses separate from the model return.

The live route is the ordinary path. Use `USE_RECORDED = True` only for an outage. In the recorded contingency, students should not invent new relationship labels because no recorded return exists for them.

## Completion standard

The recording must show one situation dictionary, the student's response before the model call, one raw return, the parsed output and a completed audit dictionary. The student must explain the default value, one keyword-argument call, the first `enumerate()` iteration, one connection to a required or core historical reading and the writer or recipient evidence needed for a stronger claim. Code elegance is not graded.
