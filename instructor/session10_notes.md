# Instructor notes — Session 10: Writing, influence and relationships

## Intended endpoint

Students should be able to explain why an LLM-mediated interpersonal message creates at least three empirical objects: generated writing, possible influence on the writer, and a recipient or relationship outcome. They should use Zelizer, Goffman and Hochschild to interpret the same broken-commitment case without treating the theories as interchangeable accounts of authenticity.

## 165-minute plan

- **9:30–9:42 — opening case:** show the fixed moving facts and two instructions. Ask what each prompt leaves the model to infer.
- **9:42–10:05 — Zelizer:** separate spheres, hostile worlds, *Cole v. Lucas*, connected lives and the relational meaning of delegation.
- **10:05–10:23 — Goffman:** line, face, incident, account, responsibility, proposed repair and recipient response.
- **10:23–10:42 — Hochschild:** the 261 protocols, feeling rules, emotion work, expression and interpretation.
- **10:42–10:48 — Gershon and Illouz:** medium choice and available cultural vocabularies.
- **10:48–10:58 — break.**
- **10:58–11:32 — reading discussion:** reconstruct Hohenstein's two studies and Williams-Ceci's outcome; compare all three readings using the opening case.
- **11:32–12:08 — Python walkthrough:** dictionary, instruction strings, prompt, route call, returned string, function, first loop iteration, record and researcher notes.
- **12:08–12:15 — close:** name what the demonstration shows and the human outcomes still requiring evidence.

## Core explanations

### Zelizer

Do not define relational work as tone adjustment. Start from the empirical challenge to separate spheres and hostile worlds. In *Cole v. Lucas*, the promissory notes did not carry a stable meaning independently of the legal definition of the tie. Apply this to the medium and performance of the apology: identical prose can be a different relational act if the sender reflects and revises, copies automatically, discloses assistance or conceals it.

### Goffman

Use the broken promise as an interactional incident. The work requirement is an account; it does not by itself acknowledge the late notice or the reliance. The offers are possible corrective moves. The recipient's acceptance, refusal or renegotiation is another move and cannot be inferred from the message.

### Hochschild

Name the evidence: retrospective written protocols concerning attempts to manage emotion. Keep outward expression, attempted emotion management and recipient interpretation separate. AI may reduce expressive effort; prompting could also facilitate reflection. Neither process is visible in the text alone.

## Contemporary studies

For Hohenstein, draw the actual-use/suspected-use distinction precisely. Random access encouraged use and supports the instrumented actual-use estimates. Suspicion was measured after the interaction and the corresponding association is not a randomized disclosure effect. The outcomes are conversation language and immediate partner ratings, not long-term relationship maintenance.

For Williams-Ceci, establish the writer outcome before showing the effect. The experiment shows that biased suggestions can shift the writer's reported attitude. It does not test whether another person was persuaded.

## Python language

For each block say: **input value and type → operation → output value and type → sociological meaning → unobserved outcome**.

- The facts dictionary stores only supplied information.
- The f-string turns the instruction, relationship and facts into one prompt string.
- The function receives three strings and returns one raw message string.
- The loop traces one relationship at a time and appends one record dictionary.
- Researcher notes are written after inspection and remain separate from the model return.

The live route is the ordinary path. Use `USE_RECORDED = True` only for an outage. In the recorded contingency, students should not invent new relationship labels because no recorded return exists for them.

## Completion standard

The recording must show the two-instruction comparison, the three-relationship loop, one meaningful change, the raw output and the researcher-notes object. The student must explain one connection to a required or core historical reading and state what writer or recipient evidence would be needed for a stronger claim. Code elegance is not graded.
