# Instructor notes — Session 6: Conversational and personalized treatments

## Intended endpoint

Students should leave able to defend this bounded claim: **In conversation, assignment is fixed but exposure emerges turn by turn from both participants.** They should also explain `summarize_exposure` line by line without live AI assistance.

## 165-minute plan

- **9:30–9:42 — retrieval and course map:** locate the session in **Intervene**; restate last week's validation habit.
- **9:42–10:15 — reading disagreement:** compare inferential targets rather than collecting findings.
- **10:15–10:38 — study anatomy:** input, transformation, evidence, failure mode, claim.
- **10:38–10:48 — break.**
- **10:48–11:00 — code block 1:** inspect inputs and types; students predict before execution.
- **11:00–11:12 — code block 2:** trace initialization and the first loop/decision.
- **11:12–11:20 — code block 3:** print output; connect each field to research meaning.
- **11:20–11:45 — paired completion task:** driver reads; navigator explains every line and predicts each check; swap roles halfway.
- **11:45–12:05 — validation diagnostic:** interpret a failure as a case, not merely a failed assertion.
- **12:05–12:15 — exit record:** claim, evidence, uncertainty, next skill.

No instructor coding segment exceeds twelve minutes.

## Required code language

Before typing, say: **input value and type → operation → output value and type → research meaning**. Avoid “this just processes the data.” Ask students to name exactly what changes and what stays unchanged.

- `summary` starts as a state dictionary containing counters and an empty ordered list.
- The loop reads one turn at a time, preserving conversational order.
- The f-string converts `user` into the key `user_turns` and `assistant` into `assistant_turns`.
- The membership check prevents a repeated topic from being counted as a new kind of exposure.

## Likely sticking points

- Brackets: pause and distinguish list position `items[0]` from dictionary key `record["field"]`.
- Assignment: `=` gives a name to a value; `==` asks whether two values are equal.
- Loops: trace the first iteration with actual values before describing the general pattern.
- Functions: arguments enter; local variables change; `return` produces the output.
- Validation: a passing software check confirms the coded expectation, not the sociological claim.

## Completion standard

Prediction; functioning small algorithm; passing checks plus one interpreted disagreement/failure; 100–150 word connection to a required reading. Syntax elegance is irrelevant.

## Contingency

If environment setup fails, pair students around the rendered notebook and have them trace the provided output. Hardware or API access must not determine completion.
