"""Offline checks for the Week 11 report-materials routine."""


def build_conditions(report_text, shared_profile, class_background_cues, disclosure_lines):
    conditions = []
    for background in class_background_cues:
        for disclosure_line in disclosure_lines:
            reader_text = "\n\n".join(
                part for part in [shared_profile, background["text"], disclosure_line, report_text]
                if part
            )
            condition = {
                "condition_id": len(conditions) + 1,
                "class_background": background["label"],
                "ai_disclosed": bool(disclosure_line),
                "report_text": report_text,
                "reader_text": reader_text,
            }
            conditions.append(condition)
    return conditions


def run_checks():
    report = "RivalCo's plan costs $18; our comparable plan costs $20."
    shared_profile = "Alex Harper is a market research analyst with three years of experience."
    class_background_cues = [
        {"label": "working-class upbringing", "text": "Parents held hourly-paid jobs."},
        {"label": "professional-class upbringing", "text": "Parents held professional jobs."},
    ]
    disclosure_lines = ["", "Alex reports using ChatGPT to edit the report."]
    conditions = build_conditions(report, shared_profile, class_background_cues, disclosure_lines)

    assert len(conditions) == 4
    assert [record["condition_id"] for record in conditions] == [1, 2, 3, 4]
    assert [(record["class_background"], record["ai_disclosed"]) for record in conditions] == [
        ("working-class upbringing", False),
        ("working-class upbringing", True),
        ("professional-class upbringing", False),
        ("professional-class upbringing", True),
    ]
    assert all(record["report_text"] == report for record in conditions)
    assert all(record["reader_text"].startswith(shared_profile) for record in conditions)


if __name__ == "__main__":
    run_checks()
    print("All Session 11 checks passed.")
