"""Session 11 completion task — Deduplicate collected sources while rejecting claims without a URL and exact excerpt.

Complete means: predict → implement → run checks → interpret → connect to a reading.
This receives a completion mark, not a code-polish score.
"""


def build_provenance_table(records):
    """Keep the first complete record for each claim-and-URL pair and return rejected record IDs."""
    # TODO: replace the next line with your small, explicit solution.
    raise NotImplementedError("Complete build_provenance_table")


# Before coding, explain the intended algorithm aloud:
# 1. A set named `seen` stores claim-and-URL pairs already accepted.
# 2. The first conditional rejects a record whose source cannot be resolved or checked.
# 3. `continue` skips the rest of the current loop iteration after recording the rejection.
# 4. A duplicate is ignored only after its provenance key is compared, not because its wording looks similar.


def run_checks():
    records = [{"id": 1, "claim": "Turnout rose", "url": "https://example.org/a", "excerpt": "turnout rose by two points"}, {"id": 2, "claim": "Turnout rose", "url": "https://example.org/a", "excerpt": "turnout rose by two points"}, {"id": 3, "claim": "Trust fell", "url": "", "excerpt": "trust fell"}]
    accepted, rejected = build_provenance_table(records)
    assert [row["id"] for row in accepted] == [1]
    assert rejected == [3]
    assert accepted[0]["url"] == "https://example.org/a"


if __name__ == "__main__":
    run_checks()
    print("All checks passed. Now interpret one success or failure.")
