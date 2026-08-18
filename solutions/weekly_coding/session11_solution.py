"""Worked solution for Session 11.

Read the function in this order: arguments → initial objects → loop/decision
→ return value. The comments name the research meaning of each operation.
"""


def build_provenance_table(records):
    """Keep the first complete record for each claim-and-URL pair and return rejected record IDs."""
    seen = set()
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
    return accepted, rejected


def run_checks():
    records = [{"id": 1, "claim": "Turnout rose", "url": "https://example.org/a", "excerpt": "turnout rose by two points"}, {"id": 2, "claim": "Turnout rose", "url": "https://example.org/a", "excerpt": "turnout rose by two points"}, {"id": 3, "claim": "Trust fell", "url": "", "excerpt": "trust fell"}]
    accepted, rejected = build_provenance_table(records)
    assert [row["id"] for row in accepted] == [1]
    assert rejected == [3]
    assert accepted[0]["url"] == "https://example.org/a"


if __name__ == "__main__":
    run_checks()
    print("All Session 11 checks passed.")
