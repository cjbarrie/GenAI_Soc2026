"""Commented reference solution for the Session 4 completion task.

The function records adjacent changes in an ordered list of moments. It does
not infer intentions, responsibility, or a causal mechanism.
"""


def trace_sequence(moments):
    """Return adjacent distance changes and alignment warnings for review."""
    previous_moment = None
    observed_changes = []
    alignment_warnings = []

    for current_moment in moments:
        if previous_moment is not None:
            if current_moment["distance"] != previous_moment["distance"]:
                observed_changes.append(
                    {
                        "time": current_moment["time"],
                        "from": previous_moment["distance"],
                        "to": current_moment["distance"],
                        "source": current_moment["source_record"],
                    }
                )

        if current_moment.get("transcript_aligned") is False:
            alignment_warnings.append(current_moment["time"])

        previous_moment = current_moment

    return {
        "moments_checked": len(moments),
        "observed_changes": observed_changes,
        "alignment_warnings": alignment_warnings,
        "ready_for_human_review": len(alignment_warnings) == 0,
        "warning": "A documented sequence does not establish the cause of violence.",
    }


def run_checks():
    """Run a small example whose result can be checked by hand."""
    moments = [
        {
            "time": 0,
            "distance": "separated",
            "source_record": "ANGLE_A_00_00_00_02",
            "transcript_aligned": True,
        },
        {
            "time": 4,
            "distance": "narrowing",
            "source_record": "ANGLE_A_00_04_00_06",
            "transcript_aligned": True,
        },
        {
            "time": 6,
            "distance": "compressed",
            "source_record": "ANGLE_A_00_06_00_08",
            "transcript_aligned": False,
        },
    ]

    result = trace_sequence(moments)
    assert result["moments_checked"] == 3
    assert result["observed_changes"] == [
        {
            "time": 4,
            "from": "separated",
            "to": "narrowing",
            "source": "ANGLE_A_00_04_00_06",
        },
        {
            "time": 6,
            "from": "narrowing",
            "to": "compressed",
            "source": "ANGLE_A_00_06_00_08",
        },
    ]
    assert result["alignment_warnings"] == [6]
    assert result["ready_for_human_review"] is False
    assert "does not establish" in result["warning"]


if __name__ == "__main__":
    run_checks()
    print("All Session 4 checks passed. The sequence still requires interpretation.")
