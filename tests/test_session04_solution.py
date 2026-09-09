import json
from pathlib import Path

from solutions.weekly_coding.session04_solution import run_checks, trace_sequence


DATA_PATH = (
    Path(__file__).parents[1]
    / "data"
    / "session04"
    / "confrontation_sequences.json"
)


def load_session_data():
    with DATA_PATH.open(encoding="utf-8") as file:
        return json.load(file)


def add_alignment_flag(moments, false_at=None):
    prepared = []
    for moment in moments:
        item = dict(moment)
        item["transcript_aligned"] = moment["time"] != false_at
        prepared.append(item)
    return prepared


def test_session04_worked_solution():
    run_checks()


def test_deescalation_sequence_records_restored_distance():
    data = load_session_data()
    moments = add_alignment_flag(
        data["common_moments"] + data["deescalation_ending"]
    )

    result = trace_sequence(moments)

    assert result["moments_checked"] == 6
    assert result["observed_changes"][-1]["to"] == "restored"
    assert result["alignment_warnings"] == []
    assert result["ready_for_human_review"] is True


def test_escalation_sequence_records_contact_without_calling_it_a_cause():
    data = load_session_data()
    moments = add_alignment_flag(
        data["common_moments"] + data["escalation_ending"], false_at=6
    )

    result = trace_sequence(moments)

    assert result["observed_changes"][-1]["to"] == "contact"
    assert result["alignment_warnings"] == [6]
    assert result["ready_for_human_review"] is False
    assert "cause of violence" in result["warning"]


def test_first_moment_is_not_compared_with_a_fictional_previous_moment():
    data = load_session_data()
    one_moment = add_alignment_flag(data["common_moments"][:1])

    result = trace_sequence(one_moment)

    assert result["observed_changes"] == []
    assert result["moments_checked"] == 1


def test_dataset_provenance_and_camera_limits_are_explicit():
    data = load_session_data()

    assert "synthetic reconstruction" in data["study"]["provenance"].lower()
    assert data["positioned_records"]["camera_b"]["starts_at"] == 5
    assert "does not record" in data["positioned_records"]["camera_b"]["visible_limit"]
    assert "not testimony" in data["participant_recollections"][0]["limit"]
