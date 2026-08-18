"""Worked solution for Session 14.

Read the function in this order: arguments → initial objects → loop/decision
→ return value. The comments name the research meaning of each operation.
"""


def audit_project_claim(project):
    """Check six required research-design fields and return missing names plus a revision prompt."""
    required = ["claim", "inferential_target", "input", "transformation", "validation", "replication_record"]
    missing = [field for field in required if project.get(field) in (None, "", [], {})]
    if missing:
        revision = "Bound the claim until these fields are supplied: " + ", ".join(missing)
    else:
        revision = "State the population, setting, model/runtime, and validation evidence directly in the claim."
    return {"missing": missing, "revision": revision}


def run_checks():
    partial = {"claim": "The model measures trust", "inferential_target": "meeting-level trust", "input": ["synthetic excerpt"], "transformation": "classification", "validation": None, "replication_record": {}}
    audit = audit_project_claim(partial)
    assert audit["missing"] == ["validation", "replication_record"]
    assert "validation" in audit["revision"]
    complete = {**partial, "validation": {"human_reference": True}, "replication_record": {"model": "m1"}}
    assert audit_project_claim(complete)["missing"] == []


if __name__ == "__main__":
    run_checks()
    print("All Session 14 checks passed.")
