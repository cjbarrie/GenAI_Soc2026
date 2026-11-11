"""Offline checks for the Week 11 report-materials routine."""


def build_conditions(report_text, role_cues, ai_use_labels):
    conditions = []
    for role_cue in role_cues:
        for ai_use_label in ai_use_labels:
            condition = {
                "condition_id": len(conditions) + 1,
                "role_cue": role_cue,
                "ai_use_label": ai_use_label,
                "report_text": report_text,
            }
            conditions.append(condition)
    return conditions


def run_checks():
    report = "RivalCo's plan costs $18; our comparable plan costs $20."
    role_cues = ["Senior director", "Junior analyst"]
    ai_use_labels = ["AI use not mentioned", "AI editing reported"]
    conditions = build_conditions(report, role_cues, ai_use_labels)

    assert len(conditions) == 4
    assert [record["condition_id"] for record in conditions] == [1, 2, 3, 4]
    assert [(record["role_cue"], record["ai_use_label"]) for record in conditions] == [
        ("Senior director", "AI use not mentioned"),
        ("Senior director", "AI editing reported"),
        ("Junior analyst", "AI use not mentioned"),
        ("Junior analyst", "AI editing reported"),
    ]
    assert all(record["report_text"] == report for record in conditions)


if __name__ == "__main__":
    run_checks()
    print("All Session 11 checks passed.")
