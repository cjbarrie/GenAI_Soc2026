# Session 9 — How can micro-level interactions generate macro-level order?

**Date:** Wednesday, November 4, 2026 · 9:30 a.m.–12:15 p.m.  
**Course movement:** Simulate  
**Methodological domain:** Generative agent-based models I  
**Chapter anchor:** *AI and Research Methods*, §§10.4.1–10.4.3

## Substantive question

How can micro-level interactions generate macro-level order?

## Learning objectives

By the end, students should be able to:

1. state the inferential target: implement one synchronous update so every agent responds to the same prior state.
2. explain the reading disagreement in their own words;
3. identify the Python type of every major input and output in the worked trace;
4. explain every parameter and return value of `choose_action`;
5. use the validation diagnostic to bound a sociological claim.

## Required readings

- [Macy & Willer (2002), from factors to actors](https://doi.org/10.1146/annurev.soc.28.110601.141117)
- [Park et al. (2023), generative agents](https://doi.org/10.1145/3586183.3606763)
- [Chuang et al. (2024), LLM opinion dynamics](https://doi.org/10.18653/v1/2024.findings-naacl.211)

## Lecture argument

An emergent pattern is interpretable only when actor state, observation, policy, update timing, and stopping rules are explicit. Classic ABM explanation emphasizes transparent rules; generative agents add memory, reflection, and language policies whose model tendencies may shape the macro result.

## Computational trace

Planned: students use the course's first small function, `choose_action(state, observation, route, temperature)`, to send an agent state and observation to a model and return one structured action. Each parameter is first replaced by a literal value so its role is visible.

## Weekly completion task

Planned: change one observation and submit a narrated screen recording explaining the function call, each parameter, the model return and the updated state. Upload to the Box folder supplied by the instructor.

## Validation focus

Updating a dictionary in place lets later agents observe a future state, creating an accidental order effect.
