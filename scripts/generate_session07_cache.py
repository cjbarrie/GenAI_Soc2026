"""Generate the instructor's cached Session 7 teaching records with local Ollama.

The profiles below are balanced, instructor-authored teaching cases. They are not
GSS respondents, census microdata, or a probability sample. The resulting records
are model predictions used to demonstrate how elicitation changes a distribution.
"""

from __future__ import annotations

import json
import random
import re
import urllib.request
from datetime import date
from pathlib import Path


MODEL = "llama3.2:3b"
OLLAMA_URL = "http://127.0.0.1:11434/api/chat"
SEED = 20261021
OUTPUT = Path(__file__).resolve().parents[1] / "data" / "session07" / "cached_synthetic_responses.json"

QUESTION = (
    "Some people think that the government in Washington ought to reduce the income "
    "differences between the rich and the poor, perhaps by raising the taxes of wealthy "
    "families or by giving income assistance to the poor. Others think that the government "
    "should not concern itself with reducing this income difference between the rich and "
    "the poor. Here is a scale from 1 to 7. Think of a score of 1 as meaning that the "
    "government ought to reduce the income differences between rich and poor, and a score "
    "of 7 meaning that the government should not concern itself with reducing income "
    "differences. What score between 1 and 7 comes closest to the way you feel?"
)

PROFILES = [
    {"age": 24, "gender": "woman", "education": "high school", "party_id": "Democrat"},
    {"age": 24, "gender": "man", "education": "bachelor's degree", "party_id": "Republican"},
    {"age": 29, "gender": "woman", "education": "some college", "party_id": "independent"},
    {"age": 29, "gender": "man", "education": "graduate degree", "party_id": "Democrat"},
    {"age": 34, "gender": "woman", "education": "bachelor's degree", "party_id": "independent"},
    {"age": 34, "gender": "man", "education": "high school", "party_id": "Republican"},
    {"age": 41, "gender": "woman", "education": "graduate degree", "party_id": "Republican"},
    {"age": 41, "gender": "man", "education": "some college", "party_id": "Democrat"},
    {"age": 49, "gender": "woman", "education": "high school", "party_id": "independent"},
    {"age": 49, "gender": "man", "education": "bachelor's degree", "party_id": "Democrat"},
    {"age": 57, "gender": "woman", "education": "some college", "party_id": "Republican"},
    {"age": 57, "gender": "man", "education": "graduate degree", "party_id": "independent"},
    {"age": 66, "gender": "woman", "education": "bachelor's degree", "party_id": "Republican"},
    {"age": 66, "gender": "man", "education": "high school", "party_id": "Democrat"},
    {"age": 74, "gender": "woman", "education": "graduate degree", "party_id": "independent"},
    {"age": 74, "gender": "man", "education": "some college", "party_id": "Republican"},
]


def call_ollama(prompt: str) -> str:
    payload = {
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "stream": False,
        "options": {"temperature": 0.7, "seed": SEED},
    }
    request = urllib.request.Request(
        OLLAMA_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(request, timeout=180) as response:
        body = json.load(response)
    return body["message"]["content"].strip()


def profile_text(profile: dict[str, object]) -> str:
    return ", ".join(f"{name}: {value}" for name, value in profile.items())


def parse_forced(text: str) -> tuple[int | None, str]:
    matches = re.findall(r"(?<!\d)[1-7](?!\d)", text)
    if len(matches) == 1:
        return int(matches[0]), "ok"
    return None, "ambiguous" if matches else "no_scale_value"


def parse_probabilities(text: str) -> tuple[dict[str, float] | None, str]:
    match = re.search(r"\{.*\}", text, flags=re.DOTALL)
    if not match:
        return None, "no_json_object"
    try:
        values = json.loads(match.group(0))
        probabilities = {str(point): float(values[str(point)]) for point in range(1, 8)}
    except (json.JSONDecodeError, KeyError, TypeError, ValueError):
        return None, "invalid_probabilities"
    total = sum(probabilities.values())
    if total <= 0 or any(value < 0 for value in probabilities.values()):
        return None, "invalid_probabilities"
    normalized = {point: value / total for point, value in probabilities.items()}
    return normalized, "ok"


def sampled_answer(probabilities: dict[str, float], rng: random.Random) -> int:
    points = list(range(1, 8))
    weights = [probabilities[str(point)] for point in points]
    return rng.choices(points, weights=weights, k=1)[0]


def main() -> None:
    rng = random.Random(SEED)
    records = []
    for index, profile in enumerate(PROFILES, start=1):
        base = f"Profile: {profile_text(profile)}\n\nSurvey question: {QUESTION}\n\n"

        forced_prompt = base + "Answer as the described respondent. Return exactly one integer from 1 to 7 and no other text."
        forced_raw = call_ollama(forced_prompt)
        forced_value, forced_status = parse_forced(forced_raw)
        records.append(
            {
                "profile_id": f"teaching_{index:03d}",
                "profile_source": "instructor_authored_balanced_teaching_set",
                "profile": profile,
                "question_id": "EQWLTH",
                "model": MODEL,
                "access_route": "ollama_local",
                "prompt_id": "eqwlth_forced_v1",
                "elicitation": "forced_choice",
                "query_date": date.today().isoformat(),
                "raw_response": forced_raw,
                "parsed_response": forced_value,
                "parser_status": forced_status,
                "random_seed": SEED,
            }
        )

        probability_prompt = base + (
            'Answer as the described respondent. Return only a JSON object with keys "1" through "7" '
            "and numeric probabilities that express uncertainty across every response option and sum to 1."
        )
        probability_raw = call_ollama(probability_prompt)
        probabilities, probability_status = parse_probabilities(probability_raw)
        sampled_value = sampled_answer(probabilities, rng) if probabilities else None
        records.append(
            {
                "profile_id": f"teaching_{index:03d}",
                "profile_source": "instructor_authored_balanced_teaching_set",
                "profile": profile,
                "question_id": "EQWLTH",
                "model": MODEL,
                "access_route": "ollama_local",
                "prompt_id": "eqwlth_probabilities_v1",
                "elicitation": "reported_probabilities",
                "query_date": date.today().isoformat(),
                "raw_response": probability_raw,
                "probabilities": probabilities,
                "parsed_response": sampled_value,
                "parser_status": probability_status,
                "random_seed": SEED,
            }
        )

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(records, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {len(records)} records to {OUTPUT}")


if __name__ == "__main__":
    main()
