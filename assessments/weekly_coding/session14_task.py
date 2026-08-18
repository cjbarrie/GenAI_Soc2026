"""Session 14 completion task — Return a missing-evidence checklist and a bounded revision prompt for one project claim.

Complete means: predict → implement → run checks → interpret → connect to a reading.
This receives a completion mark, not a code-polish score.
"""


def audit_project_claim(project):
    """Check six required research-design fields and return missing names plus a revision prompt."""
    # TODO: replace the next line with your small, explicit solution.
    raise NotImplementedError("Complete audit_project_claim")


# Before coding, explain the intended algorithm aloud:
# 1. `required` is a visible checklist, not a hidden grading rule.
# 2. The list comprehension flags absent keys and empty values while retaining their declared order.
# 3. The conditional changes the revision advice depending on whether evidence is missing.
# 4. The output does not approve the claim; it tells the researcher what must be bounded or supplied.


def run_checks():
    partial = {"claim": "The model measures trust", "inferential_target": "meeting-level trust", "input": ["synthetic excerpt"], "transformation": "classification", "validation": None, "replication_record": {}}
    audit = audit_project_claim(partial)
    assert audit["missing"] == ["validation", "replication_record"]
    assert "validation" in audit["revision"]
    complete = {**partial, "validation": {"human_reference": True}, "replication_record": {"model": "m1"}}
    assert audit_project_claim(complete)["missing"] == []


if __name__ == "__main__":
    run_checks()
    print("All checks passed. Now interpret one success or failure.")
