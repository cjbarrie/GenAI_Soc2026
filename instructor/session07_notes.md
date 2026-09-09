# Instructor notes — Session 7: synthetic respondents and population representation

## Intended endpoint

Students should be able to explain why a generated answer conditioned on a demographic profile is not an observation from a sampled group member. They should identify the validation target in a paper or comparison and explain `response_distribution` line by line.

## 165-minute plan

- **9:30–9:40 — opening puzzle:** answer immediately that identical distributions remain uninterpretable without provenance.
- **9:40–10:16 — what came before:** GSS item; survey-inference chain; Kish; Groves and Lyberg; Deming; Simulmatics; Orcutt and Schelling; Bourdieu; McCall.
- **10:16–10:34 — what changes when the model answers:** exact prompt, raw text, parser and saved record; three distinct synthetic designs.
- **10:34–10:48 — positive proposition:** Argyle, Kozlowski and Evans, and Park.
- **10:48–10:58 — break.**
- **10:58–11:35 — validation evidence:** majority versus distribution; polling, flattening, matched personas, baselines and cross-societal error.
- **11:35–11:53 — cumulative GSS example:** compare the unweighted human benchmark with actual cached local-model outputs; formulate a bounded claim.
- **11:53–12:10 — local route and Python:** client/server/model/response; trace filtering, counting and conversion to proportions.
- **12:10–12:15 — close and oral rehearsal:** identify the opening datasets and explain four consecutive lines.

## Required code language

For every block, use this order: **input value and type → operation → output value and type → research meaning → limit**.

- `records` is a list of dictionaries, not “the data” in the abstract.
- `record["elicitation"]` retrieves a string used by the `if` comparison.
- `.append(record)` changes `selected`; it does not change the original record.
- the counts dictionary begins with all seven keys so zero-count categories remain visible;
- `return` gives the caller a new proportions dictionary;
- the assertions check arithmetic, not population representation.

## Live and cached model routes

The cached file is `data/session07/cached_synthetic_responses.json`. It contains 32 records generated on 25 August 2026 with local `llama3.2:3b`: sixteen forced choices and sixteen probability reports whose sampled answers use seed `20261021`. The profiles are balanced instructor-authored teaching cases, not human microdata.

If Ollama is available, demonstrate one live request. If it is unavailable or slow, show the printed request and response objects. No completion mark depends on hardware, network access or a live model.

## Completion and oral standard

Completion requires a prediction, working function, passing checks, a 100–150 word bounded comparison and disclosure of material AI assistance. For the oral component, give the student one input record and four consecutive loop lines. Ask for every current value and type, what changes, and what would happen if the response or elicitation label changed.

## Retrospective after collaborative review

### What worked well

- The lecture became much stronger once it began with a concrete population-distribution puzzle and then asked what kind of procedure could have produced each distribution.
- The longer prehistory gave the topic a sociological and survey-methodological lineage. Deming, Kish, Simulmatics, Bourdieu, Zaller and McCall each worked when they were introduced through a specific source object and assigned a distinct job in the argument.
- Historical objects were more effective than generic web previews. The Simulmatics memorandum, the de Sola Pool, Zaller and Lepore book covers, and the first page of Deming made the history visible without asking a later paper to stand in for the original material.
- Paper sections worked best when the deck first defined the design in ordinary language and then showed the exact published finding. The repaired Argyle sequence is the model: explain how ANES profiles were constructed and queried, then show the published vote-intention results and distinguish the full sample from independents.
- The strongest empirical slides used a focused crop with highlighting rather than a full unreadable page. They told students which rows, cells or sentences mattered and why.
- Separating overall agreement from subgroup performance produced a genuinely sociological question about heterogeneity rather than treating one headline statistic as sufficient validation.
- The local-model section was useful when it showed concrete objects moving through the system: profile and question, request dictionary, generated response, structured fields and saved record.
- The Python progression remained accessible when it reused lists, dictionaries, loops and conditionals and stated the research job before introducing syntax.
- Removing redundant recent papers improved the arc. Chen et al. and Abeliuk remain useful additional reading, but the lecture did not need every paper that reached a similar caution.

### What did not work on the first pass

- The basic method—persona-based or profile-conditioned generation—was introduced too late. Several early tables therefore required students to understand “silicon sampling” before the deck had shown what the model actually receives and produces.
- Some opening language announced an abstract “central distinction” instead of posing the harder inferential question. It was more useful to ask what a synthetic distribution can support and what comparison would justify that claim.
- The initial sequence put Groves and Lyberg before Deming and blurred their different contributions. Chronology and cumulative teaching purpose both needed to be checked.
- Several slides contained instructor-facing production notes, bridge announcements, defensive captions or generic warnings. Phrases such as “reason for using it here,” “this slide summarizes,” “direct bridge,” and “role today” did not belong in visible lecture copy.
- Too many visual choices were provisional: preprint screenshots when published PDFs existed, publisher or library pages instead of source material, a generic archive view rather than the Simulmatics document, and an early Argyle figure that described prompt construction rather than the vote-intention finding being discussed.
- Some screenshots contained large margins, incomplete text or evidence too small to read. The source was technically present but was not usable as projected evidence.
- A few captions ambiguously resembled quotations or repeated information already visible in the title and citation.
- Some reconstructed plots and teaching distributions did not identify their provenance plainly enough. A visual made for the course must say that it is an instructor-created illustration and state what values it represents.
- Terms such as `L1`, `L2`, “cached,” “structured output,” profile, condition and distribution appeared before or without a beginner-facing definition.
- The first technical treatment was unclear about the model's task. Asking a model for an aggregate distribution and asking it to answer for individual survey profiles are different designs and must be introduced separately.
- The initial local-model plan overemphasized cached records even though the intended classroom activity is a live call. A fallback remains useful for teaching preparation, but it should not dominate the student-facing account.
- The close initially used abstract language instead of answering the opening question directly and then naming the next week's distinct problem.

### Decisions to carry into earlier-week revisions and future builds

1. Define the focal LLM procedure with one exact input and output near the beginning, before any history or validation framework assumes that knowledge.
2. Fix the empirical examples and obtain their published PDFs before writing slides around them. If a source is unavailable, ask for it rather than inserting a temporary web image that may survive into review.
3. For every focal paper, decide in advance which actual figure, table, quotation or instrument supports the teaching claim. Do not use a methods figure when the slide discusses a result.
4. Introduce the design in plain language before presenting its findings. Condition labels and model-specific terminology never substitute for explaining what participants, profiles or prompts actually received.
5. Use original historical objects where possible. Later historical scholarship can supply interpretation and citation, but it should not automatically be the visual proxy for the earlier object.
6. Mark course-generated data and graphics directly and neutrally. State the source values, what was simulated or reconstructed, and what the illustration cannot establish.
7. Read the deck once only for visible production language and remove presenter instructions, construction notes, bridge announcements and defensive methodological captions.
8. Crop every source at semantic boundaries and inspect it at projection size. Highlight the exact evidence and remove margins that do not help students read it.
9. Prune repeated papers. A paper remains in the main deck only if it changes the question, comparison, standard or procedure; otherwise place it in additional reading.
10. Distinguish separate computational designs explicitly: aggregate estimation, profile-conditioned individual answers and probability-valued structured outputs.
11. Show structured output as a response contract with named fields, types and one real returned object—not as unexplained SDK syntax.
12. End by returning to the exact opening object and answering its question in ordinary language. Use the final slide to state the next problem, not to add a new slogan.
