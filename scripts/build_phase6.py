"""Archive/scaffold utility for explicitly selected course sessions.

This script is no longer the owner of any reviewed course artifact. It refuses to
run unless the caller names each session and explicitly acknowledges overwrite.
Use it only to scaffold a session that will subsequently receive literature-led
editorial review.
"""

from __future__ import annotations

import ast
import argparse
import json
import re
from hashlib import sha1
from pathlib import Path
from textwrap import dedent, indent


ROOT = Path(__file__).resolve().parents[1]


SESSIONS = [
    {
        "n": 1, "date": "September 2", "slug": "research_technology",
        "title": "What kind of research technology is an LLM?", "domain": "Foundations, Python data, and course map",
        "movement": "Observe", "anchor": "Introduction and §10.7 (PDF pp. 1–2 and 34–35)",
        "papers": [
            ("Davidson & Karell (2025), integrating GenAI into social science", "https://doi.org/10.1177/00491241251339184"),
            ("Alvero et al. (2026), GenAI in sociological research", "https://sociologicalscience.com/articles-v13-3-45/"),
        ],
        "thesis": "An LLM becomes a research technology only when its input, transformation, output, and validation record are visible.",
        "tension": "Capability maps show where models enter research; disciplinary evidence asks what becomes easier, what becomes hidden, and who bears the checking work.",
        "target": "Describe one model-assisted operation without mistaking its output for evidence.",
        "failure": "A persuasive answer is copied into an analysis while the model, settings, prompt, raw response, and validation decision remain unknown.",
        "task": "Build one complete research record from a prompt, settings, and cached response.",
        "function": "build_research_record", "signature": "prompt, settings, cached_response",
        "doc": "Return a nested dictionary that preserves the input, configuration, raw output, and an empty validation field.",
        "body": '''return {
        "input": {"prompt": prompt, "type": type(prompt).__name__},
        "configuration": settings.copy(),
        "raw_output": cached_response,
        "validation": None,
    }''',
        "checks": '''record = build_research_record("Summarize this excerpt", {"temperature": 0}, "A cached summary")
assert record["input"]["type"] == "str"
assert record["configuration"]["temperature"] == 0
assert record["raw_output"] == "A cached summary"
assert record["validation"] is None''',
        "example": '''prompt = "Summarize this synthetic fieldnote"
settings = {"temperature": 0, "model": "cached-demo"}
cached_response = "The note describes informal mutual aid."
record = build_research_record(prompt, settings, cached_response)
print(record)''',
        "plain": ["The three arguments are existing Python objects: two strings and one dictionary.", "`settings.copy()` makes a new dictionary so later edits do not silently alter the saved record.", "The returned dictionary nests related fields under names a researcher can inspect.", "`None` means validation has not happened; it does not mean the output is valid."],
    },
    {
        "n": 3, "date": "September 16", "slug": "qualitative_interpretation",
        "title": "What does interpretation mean when an LLM assists qualitative research?", "domain": "Qualitative analysis",
        "movement": "Observe", "anchor": "§§10.1.4–10.1.5",
        "papers": [
            ("Than et al. (2025), qualitative coding with generative LLMs", "https://doi.org/10.1177/00491241251339188"),
            ("Ibrahim & Voyer (2026), technological reflexivity", "https://doi.org/10.1177/14687941251390794"),
            ("Nguyen & Welch (2026), analyzing—or just chatting?", "https://doi.org/10.1177/10944281251377154"),
        ],
        "thesis": "A theme is auditable only when it remains linked to source evidence and an interpretive decision.",
        "tension": "Workflow accounts emphasize assisted coding; reflexive and critical accounts disagree about whether ambiguity is a defect, a resource, or evidence of epistemic limits.",
        "target": "Produce provisional themes while retaining the quotation that warrants each theme assignment.",
        "failure": "A fluent memo names a theme but fabricates, paraphrases, or loses the source passage on which the interpretation depends.",
        "task": "Link proposed qualitative themes to exact supporting excerpts and reject unsupported labels.",
        "function": "link_themes_to_evidence", "signature": "excerpts, proposals",
        "doc": "Return accepted theme records and a list of rejected proposal IDs.",
        "body": '''excerpt_by_id = {item["id"]: item["text"] for item in excerpts}
    accepted = []
    rejected = []
    for proposal in proposals:
        source_text = excerpt_by_id.get(proposal["excerpt_id"])
        quote = proposal.get("quote")
        if source_text is None or not quote or quote not in source_text:
            rejected.append(proposal["excerpt_id"])
        else:
            accepted.append({
                "theme": proposal["theme"],
                "quote": quote,
                "excerpt_id": proposal["excerpt_id"],
            })
    return accepted, rejected''',
        "checks": '''excerpts = [{"id": 1, "text": "Neighbors shared childcare when shifts changed."}, {"id": 2, "text": "I stopped attending after the fee increased."}]
proposals = [{"excerpt_id": 1, "theme": "mutual aid", "quote": "shared childcare"}, {"excerpt_id": 2, "theme": "trust", "quote": "everyone trusted staff"}]
accepted, rejected = link_themes_to_evidence(excerpts, proposals)
assert accepted[0]["theme"] == "mutual aid"
assert accepted[0]["quote"] == "shared childcare"
assert rejected == [2]''',
        "example": '''excerpts = [{"id": 1, "text": "Neighbors shared childcare when shifts changed."}]
proposals = [{"excerpt_id": 1, "theme": "mutual aid", "quote": "shared childcare"}]
accepted, rejected = link_themes_to_evidence(excerpts, proposals)
print("accepted:", accepted)
print("rejected:", rejected)''',
        "plain": ["The first dictionary comprehension builds a lookup: excerpt ID → full source text.", "The loop considers one proposed interpretation at a time.", "The `if` branch rejects missing excerpts, empty quotations, and quotations not found verbatim in the source.", "The output separates auditable proposals from records that require human review."],
    },
    {
        "n": 4, "date": "September 23", "slug": "multimodal_evidence",
        "title": "What counts as evidence across text, image, and audio?", "domain": "Multimodal measurement",
        "movement": "Observe", "anchor": "§§10.1.1 and 10.1.5",
        "papers": [
            ("Law & Roberto (2025), generative multimodal models", "https://doi.org/10.1177/00491241251339673"),
            ("Maranca et al. (2025), correcting image-label errors", "https://doi.org/10.1177/00491241251333372"),
            ("Arminio et al. (2026), visual clustering with VLLMs", "https://doi.org/10.1177/08944393251376703"),
        ],
        "thesis": "A common data schema aids comparison but cannot erase modality-specific evidence and error.",
        "tension": "Multimodal models can make images searchable and interpretable; design-based correction shows why annotation error still enters downstream estimates.",
        "target": "Create comparable records while preserving what must be checked differently for text, image, and audio.",
        "failure": "A missing transcript, image source, or audio duration disappears when all modalities are squeezed into one generic `content` field.",
        "task": "Normalize three modality records and report missing modality-specific fields.",
        "function": "normalize_multimodal_records", "signature": "records",
        "doc": "Return normalized records with a list of missing required fields for each modality.",
        "body": '''required = {"text": ["text"], "image": ["path", "source"], "audio": ["path", "duration_seconds"]}
    normalized = []
    for record in records:
        modality = record["modality"]
        missing = [field for field in required[modality] if record.get(field) in (None, "")]
        normalized.append({
            "id": record["id"],
            "modality": modality,
            "content": record.get("text") or record.get("path"),
            "missing": missing,
        })
    return normalized''',
        "checks": '''records = [{"id": 1, "modality": "text", "text": "A caption"}, {"id": 2, "modality": "image", "path": "block.jpg", "source": "city archive"}, {"id": 3, "modality": "audio", "path": "meeting.wav", "duration_seconds": None}]
normalized = normalize_multimodal_records(records)
assert normalized[0]["content"] == "A caption"
assert normalized[1]["missing"] == []
assert normalized[2]["missing"] == ["duration_seconds"]''',
        "example": '''records = [{"id": 1, "modality": "text", "text": "Storefront signs in Spanish"}, {"id": 2, "modality": "image", "path": "street.jpg", "source": "synthetic"}, {"id": 3, "modality": "audio", "path": "meeting.wav", "duration_seconds": None}]
for item in normalize_multimodal_records(records):
    print(item)''',
        "plain": ["`required` is a dictionary whose values are lists of fields needed for each modality.", "The loop reads the modality before choosing its validation rule.", "The list comprehension keeps only required fields whose value is missing.", "The output keeps a common surface schema plus an explicit record of what modality-specific evidence is absent."],
    },
    {
        "n": 5, "date": "September 30", "slug": "treatment_generation",
        "title": "Can generated media isolate a causal construct?", "domain": "Treatment and stimulus generation",
        "movement": "Intervene", "anchor": "§10.2, especially §§10.2.3–10.2.5",
        "papers": [
            ("Dafoe, Zhang & Caughey (2018), information equivalence", "https://doi.org/10.1017/pan.2018.9"),
            ("Evsyukova, Rusche & Mill (2025), LinkedOut", "https://doi.org/10.1093/qje/qjae035"),
            ("Bai et al. (2025), LLM-generated policy messages", "https://doi.org/10.1038/s41467-025-61345-5"),
        ],
        "thesis": "Generating many stimuli increases design capacity only if intended and nuisance variation are inspected separately.",
        "tension": "AI-generated profiles and messages enable scale; information equivalence asks whether conditions differ only in the information the design intends to manipulate.",
        "target": "Construct a treatment set whose accepted variants satisfy a predeclared fidelity rule.",
        "failure": "Condition labels are randomized correctly, but tone or length changes alongside the causal construct.",
        "task": "Construct factorial treatment records and filter variants that violate a fidelity bound.",
        "function": "construct_treatments", "signature": "frames, tones, length_by_variant, max_words",
        "doc": "Return accepted factorial treatments and rejected condition names.",
        "body": '''accepted = []
    rejected = []
    for frame in frames:
        for tone in tones:
            condition = f"{frame}_{tone}"
            words = length_by_variant[condition]
            record = {"condition": condition, "frame": frame, "tone": tone, "words": words}
            if words <= max_words:
                accepted.append(record)
            else:
                rejected.append(condition)
    return accepted, rejected''',
        "checks": '''lengths = {"gain_neutral": 38, "gain_warm": 44, "loss_neutral": 39, "loss_warm": 61}
accepted, rejected = construct_treatments(["gain", "loss"], ["neutral", "warm"], lengths, 50)
assert len(accepted) == 3
assert rejected == ["loss_warm"]
assert accepted[0]["condition"] == "gain_neutral"''',
        "example": '''lengths = {"gain_neutral": 38, "gain_warm": 44, "loss_neutral": 39, "loss_warm": 61}
accepted, rejected = construct_treatments(["gain", "loss"], ["neutral", "warm"], lengths, 50)
print("accepted:", accepted)
print("rejected:", rejected)''',
        "plain": ["The outer loop chooses one frame; the inner loop pairs it with every tone.", "The f-string creates a stable condition name used to retrieve its word count.", "Each dictionary is one treatment record, not the treatment text itself.", "The conditional applies the rule declared before looking at outcomes."],
    },
    {
        "n": 6, "date": "October 7", "slug": "conversational_treatments",
        "title": "What changes when the model becomes an interactant?", "domain": "Conversational and personalized treatments",
        "movement": "Intervene", "anchor": "Selected §§10.2 and 10.5",
        "papers": [
            ("Hackenburg et al. (2025), levers of conversational persuasion", "https://doi.org/10.1126/science.aea3884"),
            ("Lin et al. (2025), human–AI voter dialogues", "https://doi.org/10.1038/s41586-025-09771-9"),
            ("Yin, Jia & Wakslak (2024), AI and feeling heard", "https://doi.org/10.1073/pnas.2319112121"),
        ],
        "thesis": "In conversation, assignment is fixed but exposure emerges turn by turn from both participants.",
        "tension": "Persuasion studies isolate model and dialogue levers; relational studies show that disclosure and perceived authorship can change the treatment itself.",
        "target": "Represent the experienced interaction rather than recording only the assigned condition.",
        "failure": "A study labels everyone as receiving the same treatment despite different numbers, topics, and factual claims across conversations.",
        "task": "Convert ordered dialogue turns into a transparent exposure summary.",
        "function": "summarize_exposure", "signature": "turns",
        "doc": "Count speaker turns and collect the topics actually encountered in order.",
        "body": '''summary = {"user_turns": 0, "assistant_turns": 0, "topics": []}
    for turn in turns:
        role_key = f"{turn['role']}_turns"
        summary[role_key] += 1
        topic = turn.get("topic")
        if topic and topic not in summary["topics"]:
            summary["topics"].append(topic)
    return summary''',
        "checks": '''turns = [{"role": "user", "text": "What about rent?", "topic": "housing"}, {"role": "assistant", "text": "Here is one policy.", "topic": "housing"}, {"role": "user", "text": "And transit?", "topic": "transit"}]
summary = summarize_exposure(turns)
assert summary["user_turns"] == 2
assert summary["assistant_turns"] == 1
assert summary["topics"] == ["housing", "transit"]''',
        "example": '''turns = [{"role": "user", "text": "What about rent?", "topic": "housing"}, {"role": "assistant", "text": "Here is one policy.", "topic": "housing"}, {"role": "user", "text": "And transit?", "topic": "transit"}]
print(summarize_exposure(turns))''',
        "plain": ["`summary` starts as a state dictionary containing counters and an empty ordered list.", "The loop reads one turn at a time, preserving conversational order.", "The f-string converts `user` into the key `user_turns` and `assistant` into `assistant_turns`.", "The membership check prevents a repeated topic from being counted as a new kind of exposure."],
    },
    {
        "n": 7, "date": "October 21", "slug": "synthetic_representation",
        "title": "Whose attitudes and experiences do synthetic populations represent?", "domain": "Silicon sampling and representation",
        "movement": "Simulate", "anchor": "§10.3",
        "papers": [
            ("Kozlowski & Evans (2025), simulating subjects", "https://doi.org/10.1177/00491241251337316"),
            ("Boelaert et al. (2025), machine bias in opinion polls", "https://doi.org/10.1177/00491241251330582"),
            ("Wang, Morgenstern & Dickerson (2025), identity flattening", "https://doi.org/10.1038/s42256-025-00986-z"),
        ],
        "thesis": "Matching a group mean is compatible with erasing the dispersion that constitutes social heterogeneity.",
        "tension": "Simulated subjects promise collective representation; polling and identity studies show topic-specific bias and compressed within-group variation.",
        "target": "Compare human and synthetic distributions at the group level without reducing fit to one mean.",
        "failure": "The reported average matches while synthetic respondents repeat nearly identical answers within every identity group.",
        "task": "Calculate group means and population variances for human and synthetic records.",
        "function": "group_summaries", "signature": "records",
        "doc": "Return count, mean, and population variance for every source-by-group combination.",
        "body": '''grouped = {}
    for record in records:
        key = (record["source"], record["group"])
        grouped.setdefault(key, []).append(record["response"])
    summaries = {}
    for key, values in grouped.items():
        mean = sum(values) / len(values)
        variance = sum((value - mean) ** 2 for value in values) / len(values)
        summaries[key] = {"n": len(values), "mean": mean, "variance": variance}
    return summaries''',
        "checks": '''records = [{"source": "human", "group": "A", "response": 1}, {"source": "human", "group": "A", "response": 5}, {"source": "synthetic", "group": "A", "response": 3}, {"source": "synthetic", "group": "A", "response": 3}]
summary = group_summaries(records)
assert summary[("human", "A")]["mean"] == 3
assert summary[("synthetic", "A")]["mean"] == 3
assert summary[("human", "A")]["variance"] == 4
assert summary[("synthetic", "A")]["variance"] == 0''',
        "example": '''records = [{"source": "human", "group": "A", "response": 1}, {"source": "human", "group": "A", "response": 5}, {"source": "synthetic", "group": "A", "response": 3}, {"source": "synthetic", "group": "A", "response": 3}]
for key, values in group_summaries(records).items():
    print(key, values)''',
        "plain": ["A tuple `(source, group)` is used as one dictionary key so the two dimensions stay together.", "`setdefault` creates an empty list the first time a key appears, then every response is appended.", "The second loop summarizes each list only after grouping is complete.", "Equal means beside unequal variances make flattening visible."],
    },
    {
        "n": 8, "date": "October 28", "slug": "opinion_prediction",
        "title": "Can LLMs recover missing or unobserved social worlds?", "domain": "Opinion prediction, validation, and limits",
        "movement": "Simulate", "anchor": "§§10.3.4–10.3.6 and §10.7",
        "papers": [
            ("Kim & Lee (2026), AI-augmented surveys", "https://arxiv.org/abs/2305.09620"),
            ("Xie et al. (2026), statistical realism", "https://doi.org/10.1073/pnas.2538145123"),
            ("Ashokkumar et al. (2026), predicting experiment results", "https://doi.org/10.1038/s41586-026-10742-x"),
        ],
        "thesis": "Validation must be chosen for the inferential target: individuals, aggregates, associations, and effects are different achievements.",
        "tension": "AI-augmented surveys seek unasked opinions; population realism and experiment forecasting show that success on one statistical target need not transfer to another.",
        "target": "Score individual error, aggregate error, and group-gap error separately.",
        "failure": "A strong aggregate correlation is presented as evidence that individual opinions or causal effects have been recovered.",
        "task": "Calculate three target-specific errors from matched human and synthetic records.",
        "function": "score_inferential_targets", "signature": "records",
        "doc": "Return individual MAE, aggregate mean error, and absolute error in the A–B group gap.",
        "body": '''individual_errors = [abs(row["human"] - row["synthetic"]) for row in records]
    individual_mae = sum(individual_errors) / len(individual_errors)
    human_mean = sum(row["human"] for row in records) / len(records)
    synthetic_mean = sum(row["synthetic"] for row in records) / len(records)
    means = {}
    for source in ("human", "synthetic"):
        for group in ("A", "B"):
            values = [row[source] for row in records if row["group"] == group]
            means[(source, group)] = sum(values) / len(values)
    human_gap = means[("human", "A")] - means[("human", "B")]
    synthetic_gap = means[("synthetic", "A")] - means[("synthetic", "B")]
    return {
        "individual_mae": individual_mae,
        "aggregate_error": abs(human_mean - synthetic_mean),
        "group_gap_error": abs(human_gap - synthetic_gap),
    }''',
        "checks": '''records = [{"group": "A", "human": 5, "synthetic": 3}, {"group": "A", "human": 1, "synthetic": 3}, {"group": "B", "human": 2, "synthetic": 2}, {"group": "B", "human": 2, "synthetic": 2}]
scores = score_inferential_targets(records)
assert scores["individual_mae"] == 1
assert scores["aggregate_error"] == 0
assert scores["group_gap_error"] == 0''',
        "example": '''records = [{"group": "A", "human": 5, "synthetic": 3}, {"group": "A", "human": 1, "synthetic": 3}, {"group": "B", "human": 2, "synthetic": 2}, {"group": "B", "human": 2, "synthetic": 2}]
print(score_inferential_targets(records))''',
        "plain": ["The first list contains one absolute individual error per matched record.", "Two means are computed across the whole dataset for the aggregate target.", "The nested loops compute separate source-by-group means before constructing each group gap.", "The returned dictionary prevents one score from silently standing in for all inferential targets."],
    },
    {
        "n": 9, "date": "November 4", "slug": "abm_updates",
        "title": "How can micro-level interactions generate macro-level order?", "domain": "Generative agent-based models I",
        "movement": "Simulate", "anchor": "§§10.4.1–10.4.3",
        "papers": [
            ("Macy & Willer (2002), from factors to actors", "https://doi.org/10.1146/annurev.soc.28.110601.141117"),
            ("Park et al. (2023), generative agents", "https://doi.org/10.1145/3586183.3606763"),
            ("Chuang et al. (2024), LLM opinion dynamics", "https://doi.org/10.18653/v1/2024.findings-naacl.211"),
        ],
        "thesis": "An emergent pattern is interpretable only when actor state, observation, policy, update timing, and stopping rules are explicit.",
        "tension": "Classic ABM explanation emphasizes transparent rules; generative agents add memory, reflection, and language policies whose model tendencies may shape the macro result.",
        "target": "Implement one synchronous update so every agent responds to the same prior state.",
        "failure": "Updating a dictionary in place lets later agents observe a future state, creating an accidental order effect.",
        "task": "Write and test one synchronous threshold-update step for a small network.",
        "function": "synchronous_update", "signature": "states, neighbors, threshold",
        "doc": "Return a new state dictionary; adopt 1 when the prior-state neighbor mean reaches the threshold.",
        "body": '''next_states = states.copy()
    for agent, neighbor_ids in neighbors.items():
        neighbor_values = [states[neighbor] for neighbor in neighbor_ids]
        neighbor_mean = sum(neighbor_values) / len(neighbor_values)
        next_states[agent] = 1 if neighbor_mean >= threshold else 0
    return next_states''',
        "checks": '''states = {"a": 0, "b": 1, "c": 1}
neighbors = {"a": ["b", "c"], "b": ["a", "c"], "c": ["a", "b"]}
updated = synchronous_update(states, neighbors, 0.5)
assert updated == {"a": 1, "b": 1, "c": 1}
assert states == {"a": 0, "b": 1, "c": 1}
assert updated is not states''',
        "example": '''states = {"a": 0, "b": 1, "c": 1}
neighbors = {"a": ["b", "c"], "b": ["a", "c"], "c": ["a", "b"]}
print("before:", states)
print("after:", synchronous_update(states, neighbors, 0.5))
print("original still unchanged:", states)''',
        "plain": ["`states.copy()` creates the future state without changing the prior state.", "The loop visits each agent and retrieves the IDs of its neighbors.", "The list comprehension looks every neighbor up in the old `states` dictionary.", "Only after computing from prior state does the function assign the agent's next value."],
    },
    {
        "n": 10, "date": "November 11", "slug": "collective_intelligence",
        "title": "When can agent diversity and debate produce collective intelligence?", "domain": "Generative ABMs II and sociology of AI",
        "movement": "Simulate", "anchor": "§§10.4.4–10.4.5",
        "papers": [
            ("Ashery et al. (2025), conventions and collective bias", "https://doi.org/10.1126/sciadv.adu9368"),
            ("Barrie & Törnberg (2025), observational equivalence to leakage", "https://arxiv.org/abs/2505.23796"),
            ("Kim et al. (2026), societies of thought", "https://arxiv.org/abs/2601.10825"),
        ],
        "thesis": "Convergence becomes evidence of emergence only after plausible inherited or leaked solutions are probed.",
        "tension": "Population experiments and societies-of-thought studies attribute collective outcomes to interaction; the leakage critique shows that the same observation can have a non-emergent explanation.",
        "target": "Compare repeated outcomes across interaction structures and a predeclared contamination probe.",
        "failure": "One compelling trajectory is interpreted as collective intelligence without repeated runs or a no-interaction baseline.",
        "task": "Summarize repeated group outcomes and flag a contamination probe that matches the target answer.",
        "function": "compare_interaction_runs", "signature": "runs, target_answer",
        "doc": "Return structure means, run counts, and IDs whose probe answer already equals the target.",
        "body": '''values_by_structure = {}
    contaminated = []
    for run in runs:
        values_by_structure.setdefault(run["structure"], []).append(run["outcome"])
        if run.get("probe_answer") == target_answer:
            contaminated.append(run["id"])
    summary = {}
    for structure, values in values_by_structure.items():
        summary[structure] = {"n": len(values), "mean": sum(values) / len(values)}
    return summary, contaminated''',
        "checks": '''runs = [{"id": 1, "structure": "debate", "outcome": 8, "probe_answer": "unknown"}, {"id": 2, "structure": "debate", "outcome": 10, "probe_answer": "42"}, {"id": 3, "structure": "solo", "outcome": 6, "probe_answer": "unknown"}]
summary, contaminated = compare_interaction_runs(runs, "42")
assert summary["debate"] == {"n": 2, "mean": 9}
assert summary["solo"]["mean"] == 6
assert contaminated == [2]''',
        "example": '''runs = [{"id": 1, "structure": "debate", "outcome": 8, "probe_answer": "unknown"}, {"id": 2, "structure": "debate", "outcome": 10, "probe_answer": "42"}, {"id": 3, "structure": "solo", "outcome": 6, "probe_answer": "unknown"}]
print(compare_interaction_runs(runs, "42"))''',
        "plain": ["The first dictionary groups outcomes by interaction structure.", "The same loop performs a separate contamination check; it does not remove cases silently.", "The second loop summarizes repeated runs rather than selecting the most impressive trajectory.", "The function returns performance and probe evidence separately so the researcher must interpret both."],
    },
    {
        "n": 11, "date": "November 18", "slug": "agentic_provenance",
        "title": "Who—or what—produces research data in an agentic workflow?", "domain": "Research agents, tools, and provenance",
        "movement": "Delegate and audit", "anchor": "§10.5",
        "papers": [
            ("Lu et al. (2026), end-to-end automation of AI research", "https://doi.org/10.1038/s41586-026-10265-5"),
            ("Nature Machine Intelligence (2026), multi-agent systems need transparency", "https://www.nature.com/articles/s42256-026-01183-2"),
        ],
        "thesis": "Delegation is scientifically useful only when every claim can be traced backward to a resolvable source and recorded transformation.",
        "tension": "End-to-end systems automate search, code, analysis, and writing; transparency arguments ask whether multiplying agents adds justified capability or merely obscures responsibility.",
        "target": "Produce a deduplicated claim/source table that a human can verify without rerunning the agent.",
        "failure": "Several agents repeat the same unsupported claim, creating apparent corroboration without independent evidence.",
        "task": "Deduplicate collected sources while rejecting claims without a URL and exact excerpt.",
        "function": "build_provenance_table", "signature": "records",
        "doc": "Keep the first complete record for each claim-and-URL pair and return rejected record IDs.",
        "body": '''seen = set()
    accepted = []
    rejected = []
    for record in records:
        if not record.get("url") or not record.get("excerpt"):
            rejected.append(record["id"])
            continue
        key = (record["claim"], record["url"])
        if key not in seen:
            seen.add(key)
            accepted.append(record)
    return accepted, rejected''',
        "checks": '''records = [{"id": 1, "claim": "Turnout rose", "url": "https://example.org/a", "excerpt": "turnout rose by two points"}, {"id": 2, "claim": "Turnout rose", "url": "https://example.org/a", "excerpt": "turnout rose by two points"}, {"id": 3, "claim": "Trust fell", "url": "", "excerpt": "trust fell"}]
accepted, rejected = build_provenance_table(records)
assert [row["id"] for row in accepted] == [1]
assert rejected == [3]
assert accepted[0]["url"] == "https://example.org/a"''',
        "example": '''records = [{"id": 1, "claim": "Turnout rose", "url": "https://example.org/a", "excerpt": "turnout rose by two points"}, {"id": 2, "claim": "Turnout rose", "url": "https://example.org/a", "excerpt": "turnout rose by two points"}, {"id": 3, "claim": "Trust fell", "url": "", "excerpt": "trust fell"}]
print(build_provenance_table(records))''',
        "plain": ["A set named `seen` stores claim-and-URL pairs already accepted.", "The first conditional rejects a record whose source cannot be resolved or checked.", "`continue` skips the rest of the current loop iteration after recording the rejection.", "A duplicate is ignored only after its provenance key is compared, not because its wording looks similar."],
    },
    {
        "n": 12, "date": "November 25", "slug": "replication_studio",
        "title": "What can we reproduce, and what remains opaque?", "domain": "Low-stakes replication and project studio",
        "movement": "Delegate and audit", "anchor": "§10.7",
        "papers": [
            ("Feuerriegel et al. (2026), GUIDE-LLM reporting checklist", "https://doi.org/10.1038/s41562-026-02492-7"),
            ("Barrie, Palmer & Spirling (2025), replication for language models", "https://arthurspirling.org/documents/BarriePalmerSpirling_TrustMeBro.pdf"),
        ],
        "thesis": "A discrepancy is useful evidence when the changed configuration fields are isolated rather than hidden by the word replication.",
        "tension": "Reporting checklists make workflows inspectable; model/provider dependence means even apparently deterministic reruns may not recreate an earlier transformation.",
        "target": "Compare two replication records and classify the visible sources of dependence.",
        "failure": "A changed answer is called randomness even though the model identifier, provider route, or prompt also changed.",
        "task": "Produce a discrepancy report from cached and rerun configurations.",
        "function": "compare_replication_records", "signature": "original, rerun",
        "doc": "Return changed configuration fields, whether output changed, and an interpretable dependence label.",
        "body": '''fields = ["model", "provider", "prompt", "temperature", "date"]
    changed_fields = [field for field in fields if original.get(field) != rerun.get(field)]
    output_changed = original.get("output") != rerun.get("output")
    if not output_changed:
        label = "same recorded output"
    elif any(field in changed_fields for field in ["model", "provider", "prompt"]):
        label = "workflow dependence"
    else:
        label = "unresolved run dependence"
    return {"changed_fields": changed_fields, "output_changed": output_changed, "label": label}''',
        "checks": '''original = {"model": "m1", "provider": "p1", "prompt": "Q", "temperature": 0, "date": "2025", "output": "A"}
same = compare_replication_records(original, original.copy())
rerun = {**original, "model": "m2", "date": "2026", "output": "B"}
changed = compare_replication_records(original, rerun)
assert same["label"] == "same recorded output"
assert changed["changed_fields"] == ["model", "date"]
assert changed["label"] == "workflow dependence"''',
        "example": '''original = {"model": "m1", "provider": "p1", "prompt": "Q", "temperature": 0, "date": "2025", "output": "A"}
rerun = {**original, "model": "m2", "date": "2026", "output": "B"}
print(compare_replication_records(original, rerun))''',
        "plain": ["`fields` declares in advance which configuration elements will be compared.", "The list comprehension retains only fields whose values differ across the two dictionaries.", "Output difference is calculated separately from configuration difference.", "The final condition labels visible workflow dependence before invoking unexplained stochasticity."],
    },
    {
        "n": 13, "date": "December 2", "slug": "model_audits",
        "title": "What culture, ideology, and hierarchy are encoded in models?", "domain": "Auditing LLMs as objects of study",
        "movement": "Delegate and audit", "anchor": "§10.6, especially §§10.6.1–10.6.4",
        "papers": [
            ("Waight et al. (2026), state media control and LLMs", "https://doi.org/10.1038/s41586-026-10506-7"),
            ("Buyl et al. (2026), ideology of model creators", "https://doi.org/10.1038/s44387-025-00048-0"),
            ("Kim et al. (2026), consciousness assertions and human values", "https://arxiv.org/abs/2607.28607"),
        ],
        "thesis": "An output difference is an audit finding; explaining its social cause requires a stronger design.",
        "tension": "Cross-national and creator-geography comparisons identify patterned outputs; causal triangulation and the provisional consciousness study raise different evidentiary thresholds for explaining those patterns.",
        "target": "Predeclare and summarize a factorial audit across model, language, and user frame.",
        "failure": "A single English prompt difference is attributed to national culture, creator ideology, or alignment policy without isolating alternatives.",
        "task": "Create factorial audit conditions and summarize the observed response by condition.",
        "function": "factorial_audit", "signature": "models, languages, frames, responses",
        "doc": "Return every requested condition with its observed response and report missing conditions.",
        "body": '''conditions = []
    missing = []
    for model in models:
        for language in languages:
            for frame in frames:
                key = (model, language, frame)
                if key in responses:
                    conditions.append({
                        "model": model,
                        "language": language,
                        "frame": frame,
                        "response": responses[key],
                    })
                else:
                    missing.append(key)
    return conditions, missing''',
        "checks": '''responses = {("m1", "en", "neutral"): 2, ("m1", "es", "neutral"): 3}
conditions, missing = factorial_audit(["m1"], ["en", "es"], ["neutral"], responses)
assert len(conditions) == 2
assert conditions[1]["language"] == "es"
assert missing == []
_, missing_two = factorial_audit(["m1"], ["en"], ["neutral", "student"], responses)
assert missing_two == [("m1", "en", "student")]''',
        "example": '''responses = {("m1", "en", "neutral"): 2, ("m1", "es", "neutral"): 3}
conditions, missing = factorial_audit(["m1"], ["en", "es"], ["neutral"], responses)
print("observed:", conditions)
print("missing:", missing)''',
        "plain": ["Three nested loops construct the Cartesian product one factor at a time.", "A tuple is the exact key for one model-language-frame condition.", "The membership check distinguishes an unobserved condition from a response value of zero.", "The outputs describe what was observed and what is missing; neither output supplies a causal explanation."],
    },
]


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def safe_id(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def normalize_code_block(text: str) -> str:
    """Give a triple-quoted block a common baseline, including its first line."""
    return dedent("    " + text)


def explain_python_line(line: str) -> str:
    """Return a beginner-facing explanation of one line's Python mechanics."""
    code = line.strip()
    if code.startswith("def "):
        return "`def` creates a reusable function. The names inside parentheses are the input names; the colon starts its indented body."
    if code.startswith('"""'):
        return "The triple-quoted text documents what the function promises to return; Python does not execute it as an instruction."
    if code.startswith("for "):
        return "`for` repeats the indented block once for each item on the right of `in`; the name after `for` holds the current item."
    if code.startswith("if ") or code.startswith("elif "):
        return "This is a Boolean test. Python runs the indented block only when the expression before the colon is `True`."
    if code == "else:":
        return "`else` handles the remaining cases for which the preceding test was `False`."
    if code.startswith("return ") or code == "return {":
        return "`return` ends the function and sends this value back to the line that called it."
    if code in {"}", "]", ")"}:
        return "This closing bracket ends the collection or function call opened above."
    if ".append(" in code:
        return "`.append(...)` adds one new item to the end of the named list; the list itself changes."
    if ".setdefault(" in code:
        return "`.setdefault(key, value)` creates the key only when it is absent, then returns the value stored under that key."
    if "+=" in code:
        return "`+=` reads the current value, adds the value on the right, and stores the result back under the same name."
    if " = " in code:
        left, right = code.split(" = ", 1)
        if " for " in right and right[:1] in "[{":
            return f"This comprehension repeats the expression before `for` and stores the resulting collection under `{left}`; read it as a compact loop."
        return f"`=` evaluates the expression on the right, then gives that value the name `{left}`. It does not test equality."
    if code.startswith(('"', "'")) and ":" in code:
        return "This is one dictionary entry: the quoted text is the key and the expression after the colon supplies its value."
    return "Read the brackets and function calls from the inside out; this line contributes one value or action to the surrounding block."


def line_guide(function_code: str) -> str:
    rows = []
    for number, line in enumerate(function_code.splitlines(), start=1):
        visible = line.strip().replace("`", "\\`")
        if visible:
            rows.append(f"{number}. `{visible}`  \n   {explain_python_line(line)}")
    return "\n".join(rows)


def traced_example(session: dict) -> str:
    """Insert explicit input/type displays immediately before the function call."""
    example = session["example"]
    lines = example.splitlines()
    tree = ast.parse(example)
    call = next(
        node
        for node in ast.walk(tree)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == session["function"]
    )
    call_index = call.lineno - 1
    argument_names = [argument.strip() for argument in session["signature"].split(",")]
    argument_expressions = [ast.get_source_segment(example, argument) for argument in call.args]
    type_lines = [
        f'print("input {name}:", type({expression}).__name__, repr({expression}))'
        for name, expression in zip(argument_names, argument_expressions, strict=True)
    ]
    return "\n".join(lines[:call_index] + type_lines + lines[call_index:])


def solution_code(session: dict) -> str:
    return f'''"""Worked solution for Session {session['n']}.

Read the function in this order: arguments → initial objects → loop/decision
→ return value. The comments name the research meaning of each operation.
"""


def {session['function']}({session['signature']}):
    """{session['doc']}"""
{indent(normalize_code_block(session['body']), '    ')}


def run_checks():
{indent(session['checks'], '    ')}


if __name__ == "__main__":
    run_checks()
    print("All Session {session['n']} checks passed.")
'''


def task_code(session: dict) -> str:
    notes = "\n".join(f"# {i + 1}. {line}" for i, line in enumerate(session["plain"]))
    return f'''"""Session {session['n']} completion task — {session['task']}

Complete means: predict → implement → run checks → interpret → connect to a reading.
This receives a completion mark, not a code-polish score.
"""


def {session['function']}({session['signature']}):
    """{session['doc']}"""
    # TODO: replace the next line with your small, explicit solution.
    raise NotImplementedError("Complete {session['function']}")


# Before coding, explain the intended algorithm aloud:
{notes}


def run_checks():
{indent(session['checks'], '    ')}


# OPTIONAL EXTENSION (not required for completion):
# Add one small synthetic case designed to trigger the characteristic failure.
# Predict the result before running it, then explain whether the existing output
# makes that failure visible or whether the research record needs another field.


if __name__ == "__main__":
    run_checks()
    print("All checks passed. Now interpret one success or failure.")
'''


def make_notebook(session: dict) -> dict:
    def md(text: str) -> dict:
        cell_id = sha1(("markdown\0" + text).encode()).hexdigest()[:12]
        return {"cell_type": "markdown", "id": cell_id, "metadata": {}, "source": text}

    def code(text: str) -> dict:
        cell_id = sha1(("code\0" + text).encode()).hexdigest()[:12]
        return {"cell_type": "code", "id": cell_id, "execution_count": None, "metadata": {}, "outputs": [], "source": text}

    function_only = f"def {session['function']}({session['signature']}):\n    \"\"\"{session['doc']}\"\"\"\n" + indent(normalize_code_block(session["body"]), "    ")
    papers = "\n".join(f"- [{name}]({url})" for name, url in session["papers"])
    walk = "\n".join(f"{i + 1}. {line}" for i, line in enumerate(session["plain"]))
    detailed_guide = line_guide(function_only)
    example_with_types = traced_example(session)
    cells = [
        md(f"# Session {session['n']} — {session['title']}\n\n**Research target:** {session['target']}\n\nThis notebook follows **question → input → type → transformation → raw output → check → research meaning**. Before each code cell, predict what Python object will come out. After it runs, explain it without relying on syntax jargon."),
        md(f"## Why the code is here\n\n**Course claim:** {session['thesis']}\n\n**Characteristic failure:** {session['failure']}\n\nThe code is a deliberately small research algorithm. It is not evidence that an LLM is valid."),
        md("## 1. Meet the input objects\n\nRead brackets first: `[]` marks a list; `{}` marks a dictionary; quotation marks mark a string. `type(...)` asks Python what kind of object a value is. The cell below uses no live model."),
        code(session["example"].split("\n")[0] + "\nprint(type(" + session["example"].split(" = ")[0] + "))"),
        md(f"## 2. Name the algorithm before running it\n\n**Input names:** `{session['signature']}`. The trace below prints the exact value and Python type for every input before calling the function.\n\n**Operation:** `{session['function']}`.\n\n**Output:** an inspectable Python object. Read the `return` line to identify its type and contents.\n\n**Check:** the explicit assertions in Section 5.\n\n**Research meaning, in four steps**\n\n{walk}\n\n### Read every line of Python\n\n{detailed_guide}\n\nThe numbered guide explains Python mechanics. The four-step walkthrough explains why those mechanics belong in this research design; neither substitutes for the other."),
        code(function_only),
        md("### Pause and say it aloud\n\nPoint to each argument in the function header. Say what value enters it, what type that value has, what changes inside the function, and what `return` sends back. If you cannot do that yet, reread the four numbered sentences before editing code."),
        md("## 3. Run one trace\n\nThe next cell creates tiny synthetic inputs and prints the complete returned object. Printing before summarizing makes unexpected fields and values visible."),
        code(example_with_types),
        md("## 4. Connect the output to the research question\n\nA correct Python result means the declared transformation ran. It does **not** establish construct validity, representativeness, causality, emergence, or reproducibility. Interpret the output beside the inferential target and failure mode above."),
        md("## 5. Run executable checks\n\nAn `assert` states an expectation. If the statement after `assert` is `True`, Python continues silently. If it is `False`, Python stops at that exact expectation. Read the left and right sides before running."),
        code(session["checks"] + "\nprint('All worked-example checks passed.')"),
        md(f"## 6. Your completion task\n\nOpen `assessments/weekly_coding/session{session['n']:02d}_task.py`. {session['task']} Submit: (1) your prediction, (2) working code, (3) passing checks plus an interpreted diagnostic, and (4) a 100–150 word connection to one required reading."),
        md("## Optional extension\n\nAdd one small synthetic case designed to trigger the characteristic failure named at the start of this notebook. Predict the returned object before running it. Then explain whether the current output makes the failure visible or whether the research record needs another field. This is optional and is not part of the completion mark."),
        md(f"## Required readings speak to this code\n\n{papers}\n\nWrite one sentence beginning: **This algorithm makes ___ visible, but the reading shows it cannot by itself establish ___.**"),
        md("## Oral-assessment rehearsal\n\nChoose four consecutive lines from the function. Explain every name and bracket, predict the returned value, then change one input and predict exactly what changes. Accurate plain language is better than unexplained technical vocabulary."),
        md("## AI-use disclosure\n\nIf a tool materially assisted you, record: tool/model; what you used it for; what you incorporated; and how you checked it. You remain responsible for every claim and line of code."),
    ]
    return {"cells": cells, "metadata": {"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"}, "language_info": {"name": "python", "version": "3.11"}}, "nbformat": 4, "nbformat_minor": 5}


def syllabus(session: dict) -> str:
    readings = "\n".join(f"- [{name}]({url})" for name, url in session["papers"])
    return f'''# Session {session['n']} — {session['title']}

**Date:** Wednesday, {session['date']}, 2026 · 9:30 a.m.–12:15 p.m.  
**Course movement:** {session['movement']}  
**Methodological domain:** {session['domain']}  
**Chapter anchor:** *AI and Research Methods*, {session['anchor']}

## Substantive question

{session['title']}

## Learning objectives

By the end, students should be able to:

1. state the inferential target: {session['target'].lower()}
2. explain the reading disagreement in their own words;
3. identify the Python type of every major input and output in the worked trace;
4. explain each line or small block of `{session['function']}`;
5. use the validation diagnostic to bound a sociological claim.

## Required readings

{readings}

## Lecture argument

{session['thesis']} {session['tension']}

## Computational trace

Students move from visible synthetic inputs through `{session['function']}` to a printed output and explicit checks. The required task uses no live API. Every code block is read as **input → Python type → operation → output → research meaning**.

## Weekly completion task

{session['task']} Submit a prediction, working code, interpreted check, and 100–150 word reading-linked claim. Completion marks only; missing elements may be supplied within one week.

## Validation focus

{session['failure']}
'''


def reading_guide(session: dict) -> str:
    paper_rows = "\n".join(f"| [{name}]({url}) | What inference does the paper seek? | What evidence could disconfirm it? |" for name, url in session["papers"])
    return f'''# Session {session['n']} reading guide — {session['domain']}

## The disagreement to carry into class

{session['tension']}

Do not summarize the papers serially. Compare the inferential target, the role assigned to an LLM, the human/reference evidence, and the failure mode each design can or cannot reveal.

| Reading | Ask while reading | Bring to the code |
|---|---|---|
{paper_rows}

## Before class

Bring one passage that supports the strongest claim you think is warranted and one passage that makes you qualify it. Complete this sentence: **The output is useful for ___, but it would be invalid evidence for ___ unless ___.**

## Reading → code

The workbook implements `{session['function']}`. Its input is small enough to inspect manually. Predict the output, then decide which claim from the readings the check clarifies—and which larger claim it cannot settle.
'''


def instructor_notes(session: dict) -> str:
    prompts = "\n".join(f"- {line}" for line in session["plain"])
    return f'''# Instructor notes — Session {session['n']}: {session['domain']}

## Intended endpoint

Students should leave able to defend this bounded claim: **{session['thesis']}** They should also explain `{session['function']}` line by line without live AI assistance.

## 165-minute plan

- **9:30–9:42 — retrieval and course map:** locate the session in **{session['movement']}**; restate last week's validation habit.
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

{prompts}

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
'''


def deck(session: dict) -> str:
    source_notes = "\n".join(
        f"- {name} | Source: {('../' + url) if url.startswith('../') else url} | Accessed: 2026-08-18"
        for name, url in session["papers"]
    )
    reading_lines = "\n".join(f"- **{name.split(',')[0]}:** {('methodological opportunity' if i == 0 else 'validation or counterclaim')}" for i, (name, _) in enumerate(session["papers"]))
    code_lines = function_only = f"def {session['function']}({session['signature']}):\n" + indent(normalize_code_block(session["body"]), "    ")
    code_line_list = code_lines.splitlines()
    code_chunk_one = "\n".join(code_line_list[:7])
    code_chunk_two = "\n".join(code_line_list[7:]) or "# The full function is visible in the workbook.\n# Now inspect the returned object and the checks."
    output_hint = session["checks"].splitlines()[-1]
    return f'''---
title: "{session['title']}"
subtitle: "Session {session['n']} · {session['domain']}"
author: "Generative AI in Sociology"
date: "{session['date']}, 2026"
format:
  revealjs:
    theme: [default, ../../design/theme.scss]
    width: 1280
    height: 720
    margin: 0
    controls: false
    progress: false
    slide-number: c/t
    transition: fade
    center: false
    embed-resources: true
---

## We are learning to {session['movement'].lower()}

<div class="course-map">
<div class="active"><strong>Observe</strong><small>measure and interpret</small></div>
<div class="{'active' if session['movement'] == 'Intervene' else ''}"><strong>Intervene</strong><small>generate and converse</small></div>
<div class="{'active' if session['movement'] == 'Simulate' else ''}"><strong>Simulate</strong><small>populations and agents</small></div>
<div class="{'active' if session['movement'] == 'Delegate and audit' else ''}"><strong>Delegate & audit</strong><small>tools, provenance, power</small></div>
</div>

---

## {session['title']}

<div class="major-question">What evidence would let you answer without treating fluency as validity?</div>

---

## The inferential target comes before the metric

<div class="semantic-line">{session['target']}</div>

<div class="semantic-line warning" style="margin-top: 42px;">{session['failure']}</div>

---

## The readings make the methodological burden visible

{reading_lines}

::: {{.notes}}
[Sources]
{source_notes}
[/Sources]
:::

---

## The readings disagree about success

<div class="lead">{session['tension']}</div>

<div class="semantic-line warning" style="margin-top: 36px;">Which part of that disagreement can the week's code make inspectable?</div>

::: {{.notes}}
[Sources]
{source_notes}
[/Sources]
:::

---

## The session's bounded claim

<div class="major-question">{session['thesis']}</div>

---

## One small algorithm makes the design inspectable

**Task:** {session['task']}

1. show exact input objects;
2. name their Python types;
3. apply one visible transformation;
4. print the returned object;
5. interpret a check.

---

## Read the function header before the body

```python
def {session['function']}({session['signature']}):
    # return one documented result
```

**Return value:** {session['doc']}

<div class="semantic-line">Arguments are names for input values. `return` sends the output back.</div>

---

## Trace the first block with actual values

::: {{.compact-code}}
```python
{code_chunk_one}
```
:::

---

## Trace the next block before running it

::: {{.compact-code}}
```python
{code_chunk_two}
```
:::

<div class="semantic-line">For each line: what value enters, what changes, and what value exists afterward?</div>

---

## Four sentences explain the code

1. {session['plain'][0]}
2. {session['plain'][1]}
3. {session['plain'][2]}
4. {session['plain'][3]}

---

## A software check states one exact expectation

```python
# after the worked example in the notebook
{output_hint}
```

<div class="semantic-line warning">A passing assertion validates the coded expectation—not the larger sociological inference.</div>

---

## The characteristic failure is substantive

<div class="major-question">{session['failure']}</div>

---

## Completion task: predict, implement, interpret

1. Predict one output before execution.
2. Complete `{session['function']}`.
3. Run all supplied checks.
4. Explain one diagnostic in plain language.
5. Connect it to one required reading in 100–150 words.

---

## Revise the claim to match the evidence

<div class="major-question">This trace makes one methodological decision inspectable. What additional evidence would strengthen the sociological claim?</div>

::: {{.notes}}
[Sources]
{source_notes}
[/Sources]
:::
'''


def build(selected_sessions: set[int]) -> None:
    for session in SESSIONS:
        n = session["n"]
        if n not in selected_sessions:
            continue
        sid = f"session{n:02d}"
        write(ROOT / "syllabus" / f"{sid}.md", syllabus(session))
        write(ROOT / "readings" / f"{sid}_reading_guide.md", reading_guide(session))
        write(ROOT / "instructor" / f"{sid}_notes.md", instructor_notes(session))
        write(ROOT / "assessments" / "weekly_coding" / f"{sid}_task.py", task_code(session))
        write(ROOT / "solutions" / "weekly_coding" / f"{sid}_solution.py", solution_code(session))
        write(ROOT / "tests" / f"test_{sid}_solution.py", f'''from solutions.weekly_coding.{sid}_solution import run_checks\n\n\ndef test_{sid}_worked_solution():\n    run_checks()\n''')
        notebook_path = ROOT / "workbook" / sid / f"{sid}_{session['slug']}.ipynb"
        notebook_path.parent.mkdir(parents=True, exist_ok=True)
        notebook_path.write_text(json.dumps(make_notebook(session), indent=1) + "\n", encoding="utf-8")
        write(ROOT / "slides" / sid / f"{sid}.qmd", deck(session))

    print(f"Scaffolded sessions: {', '.join(str(n) for n in sorted(selected_sessions))}.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--session",
        type=int,
        choices=range(1, 15),
        action="append",
        required=True,
        help="Session number to scaffold; repeat for multiple sessions.",
    )
    parser.add_argument(
        "--confirm-overwrite-scaffold",
        action="store_true",
        help="Required acknowledgment that selected source artifacts will be overwritten.",
    )
    args = parser.parse_args()
    if not args.confirm_overwrite_scaffold:
        parser.error("Refusing to overwrite reviewed work without --confirm-overwrite-scaffold")
    build(set(args.session))
