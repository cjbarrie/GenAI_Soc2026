# Instructor notes — Session 14: Project symposium and course synthesis

## Intended endpoint

Students should leave able to defend this bounded claim: **The strongest course outcome is not a more confident claim, but a claim whose scope matches its actual evidence.** They should also explain `audit_project_claim` line by line without live AI assistance.

## 165-minute plan

- **9:30–9:42 — retrieval and course map:** locate the session in **Delegate and audit**; restate last week's validation habit.
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

- `required` is a visible checklist, not a hidden grading rule.
- The list comprehension flags absent keys and empty values while retaining their declared order.
- The conditional changes the revision advice depending on whether evidence is missing.
- The output does not approve the claim; it tells the researcher what must be bounded or supplied.

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
