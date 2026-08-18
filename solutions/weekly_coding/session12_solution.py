"""Worked solution for Session 12.

Read the function in this order: arguments → initial objects → loop/decision
→ return value. The comments name the research meaning of each operation.
"""


def compare_replication_records(original, rerun):
    """Return changed configuration fields, whether output changed, and an interpretable dependence label."""
    fields = ["model", "provider", "prompt", "temperature", "date"]
    changed_fields = [field for field in fields if original.get(field) != rerun.get(field)]
    output_changed = original.get("output") != rerun.get("output")
    if not output_changed:
        label = "same recorded output"
    elif any(field in changed_fields for field in ["model", "provider", "prompt"]):
        label = "workflow dependence"
    else:
        label = "unresolved run dependence"
    return {"changed_fields": changed_fields, "output_changed": output_changed, "label": label}


def run_checks():
    original = {"model": "m1", "provider": "p1", "prompt": "Q", "temperature": 0, "date": "2025", "output": "A"}
    same = compare_replication_records(original, original.copy())
    rerun = {**original, "model": "m2", "date": "2026", "output": "B"}
    changed = compare_replication_records(original, rerun)
    assert same["label"] == "same recorded output"
    assert changed["changed_fields"] == ["model", "date"]
    assert changed["label"] == "workflow dependence"


if __name__ == "__main__":
    run_checks()
    print("All Session 12 checks passed.")
