"""Worked checks for the Week 8 experimental-effect benchmark."""


def score_effect_forecasts(records):
    """Return one absolute error per experiment and the mean absolute error."""
    scored = []
    error_total = 0
    for record in records:
        predicted_effect = record["predicted_treatment"] - record["predicted_control"]
        observed_effect = record["human_treatment"] - record["human_control"]
        absolute_error = abs(predicted_effect - observed_effect)
        scored.append(
            {
                "id": record["id"],
                "predicted_effect": predicted_effect,
                "observed_effect": observed_effect,
                "absolute_error": absolute_error,
            }
        )
        error_total = error_total + absolute_error
    return {"records": scored, "mae": error_total / len(scored)}


def run_checks():
    records = [
        {
            "id": "turnout",
            "predicted_control": 30.0,
            "predicted_treatment": 38.0,
            "human_control": 29.7,
            "human_treatment": 37.8,
        },
        {
            "id": "towels",
            "predicted_control": 36.0,
            "predicted_treatment": 43.0,
            "human_control": 35.1,
            "human_treatment": 44.1,
        },
        {
            "id": "disease",
            "predicted_control": 70.0,
            "predicted_treatment": 25.0,
            "human_control": 72.0,
            "human_treatment": 22.0,
        },
    ]
    scores = score_effect_forecasts(records)
    assert round(scores["records"][0]["observed_effect"], 1) == 8.1
    assert round(scores["records"][1]["absolute_error"], 1) == 2.0
    assert round(scores["mae"], 2) == 2.37


if __name__ == "__main__":
    run_checks()
    print("All Session 8 checks passed.")
