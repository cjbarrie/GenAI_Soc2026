"""Worked solution for Session 4.

Read the function in this order: arguments → initial objects → loop/decision
→ return value. The comments name the research meaning of each operation.
"""


def normalize_multimodal_records(records):
    """Return normalized records with a list of missing required fields for each modality."""
    required = {"text": ["text"], "image": ["path", "source"], "audio": ["path", "duration_seconds"]}
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
    return normalized


def run_checks():
    records = [{"id": 1, "modality": "text", "text": "A caption"}, {"id": 2, "modality": "image", "path": "block.jpg", "source": "city archive"}, {"id": 3, "modality": "audio", "path": "meeting.wav", "duration_seconds": None}]
    normalized = normalize_multimodal_records(records)
    assert normalized[0]["content"] == "A caption"
    assert normalized[1]["missing"] == []
    assert normalized[2]["missing"] == ["duration_seconds"]


if __name__ == "__main__":
    run_checks()
    print("All Session 4 checks passed.")
