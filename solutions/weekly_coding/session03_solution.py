"""Worked solution for Session 3.

Read the function in this order: arguments → initial objects → loop/decision
→ return value. The comments name the research meaning of each operation.
"""


def link_themes_to_evidence(excerpts, proposals):
    """Return accepted theme records and a list of rejected proposal IDs."""
    excerpt_by_id = {item["id"]: item["text"] for item in excerpts}
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
    return accepted, rejected


def run_checks():
    excerpts = [{"id": 1, "text": "Neighbors shared childcare when shifts changed."}, {"id": 2, "text": "I stopped attending after the fee increased."}]
    proposals = [{"excerpt_id": 1, "theme": "mutual aid", "quote": "shared childcare"}, {"excerpt_id": 2, "theme": "trust", "quote": "everyone trusted staff"}]
    accepted, rejected = link_themes_to_evidence(excerpts, proposals)
    assert accepted[0]["theme"] == "mutual aid"
    assert accepted[0]["quote"] == "shared childcare"
    assert rejected == [2]


if __name__ == "__main__":
    run_checks()
    print("All Session 3 checks passed.")
