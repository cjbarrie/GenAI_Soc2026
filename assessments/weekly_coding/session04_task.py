"""Session 4 completion task — Normalize three modality records and report missing modality-specific fields.

Complete means: predict → implement → run checks → interpret → connect to a reading.
This receives a completion mark, not a code-polish score.
"""


def normalize_multimodal_records(records):
    """Return normalized records with a list of missing required fields for each modality."""
    # TODO: replace the next line with your small, explicit solution.
    raise NotImplementedError("Complete normalize_multimodal_records")


# Before coding, explain the intended algorithm aloud:
# 1. `required` is a dictionary whose values are lists of fields needed for each modality.
# 2. The loop reads the modality before choosing its validation rule.
# 3. The list comprehension keeps only required fields whose value is missing.
# 4. The output keeps a common surface schema plus an explicit record of what modality-specific evidence is absent.


def run_checks():
    records = [{"id": 1, "modality": "text", "text": "A caption"}, {"id": 2, "modality": "image", "path": "block.jpg", "source": "city archive"}, {"id": 3, "modality": "audio", "path": "meeting.wav", "duration_seconds": None}]
    normalized = normalize_multimodal_records(records)
    assert normalized[0]["content"] == "A caption"
    assert normalized[1]["missing"] == []
    assert normalized[2]["missing"] == ["duration_seconds"]


# OPTIONAL EXTENSION (not required for completion):
# Add one small synthetic case designed to trigger the characteristic failure.
# Predict the result before running it, then explain whether the existing output
# makes that failure visible or whether the research record needs another field.


if __name__ == "__main__":
    run_checks()
    print("All checks passed. Now interpret one success or failure.")
