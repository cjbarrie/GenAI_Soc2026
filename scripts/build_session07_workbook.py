"""Build the Session 7 workbook from explicit, beginner-oriented cells."""

import json
import textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "workbook" / "session07" / "session07_synthetic_representation.ipynb"


def md(text):
    text = textwrap.dedent(text).strip()
    return {"cell_type": "markdown", "metadata": {}, "source": [line + "\n" for line in text.splitlines()]}


def code(text):
    text = textwrap.dedent(text).strip()
    return {"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [], "source": [line + "\n" for line in text.splitlines()]}


cells = [
    md("""
    # Session 7 workbook — two ways to predict GSS answers

    We will make two live model-based predictions:

    1. **Aggregate prediction:** one model call predicts the seven-category U.S. ideology distribution.
    2. **Profile prediction:** repeated calls predict held-out `POLVIEWS` answers for real records selected from the 2024 GSS public-use file.

    For every block, identify the **input**, its Python **type**, the **operation**, the **output**, and the claim the result does or does not support. We use OpenRouter because one SDK and one key can route requests to several model providers. You remain responsible for the prompt, data sent to the provider, model choice, cost, and interpretation.
    """),
    md("""
    ## 1. Set up the OpenRouter client

    The instructor will provide access to an API key. Place it in the environment as `OPENROUTER_API_KEY`; do not paste it into a notebook that may be shared.

    If needed, run `%pip install openrouter pandas matplotlib` once and restart the kernel.
    """),
    code("""
    import json
    import os
    from pathlib import Path

    import matplotlib.pyplot as plt
    import pandas as pd
    from openrouter import OpenRouter

    api_key = os.environ["OPENROUTER_API_KEY"]
    client = OpenRouter(api_key=api_key)
    MODEL = "openai/gpt-5.2"

    print("Client type:", type(client).__name__)
    print("Model:", MODEL)
    """),
    md("""
    **Inputs:** the key is a string read from the environment; `MODEL` is another string. **Output:** `client` is an `OpenRouter` object that can send requests. Creating it does not yet call a model or spend credits.
    """),
    md("## 2. Use the question people were actually asked"),
    code('''
    polviews_question = """I'm going to show you a seven-point scale on which the
    political views that people might hold are arranged from extremely liberal--point 1--
    to extremely conservative--point 7. Where would you place yourself?"""

    labels = {
        1: "extremely liberal",
        2: "liberal",
        3: "slightly liberal",
        4: "moderate, middle of the road",
        5: "slightly conservative",
        6: "conservative",
        7: "extremely conservative",
    }

    print(polviews_question)
    print(labels)
    '''),
    md("""
    `polviews_question` is one string. `labels` is a dictionary whose integer keys are response codes and whose string values explain those codes. The prompt wording matches the GSS wording.
    """),
    md("## 3. Exercise A — ask for an aggregate distribution"),
    code("""
    distribution_schema = {
        "type": "object",
        "properties": {
            "percentages": {
                "type": "array",
                "items": {"type": "number", "minimum": 0, "maximum": 100},
                "minItems": 7,
                "maxItems": 7,
            }
        },
        "required": ["percentages"],
        "additionalProperties": False,
    }

    response_format = {
        "type": "json_schema",
        "json_schema": {
            "name": "ideology_distribution",
            "strict": True,
            "schema": distribution_schema,
        },
    }
    """),
    md("""
    `distribution_schema` permits one dictionary with one key, `percentages`, pointing to exactly seven numbers between 0 and 100. `response_format` gives the schema a name and requests strict structured output. It constrains the form of the answer; it does not make the percentages accurate.
    """),
    code('''
    aggregate_prompt = f"""Use the exact survey question below.

    Predict the percentage of 2024 U.S. adults in each response category from 1 to 7.
    Return the percentages in scale order. They should sum to 100.

    QUESTION:
    {polviews_question}
    """

    print(aggregate_prompt)
    '''),
    md("""
    **Input:** the f-string inserts `polviews_question` into the instruction. **Output:** `aggregate_prompt` is one complete string. Read it before sending it: this is the full information supplied to the model.
    """),
    code("""
    aggregate_response = client.chat.send(
        model=MODEL,
        messages=[{"role": "user", "content": aggregate_prompt}],
        response_format=response_format,
        provider={"require_parameters": True},
        stream=False,
    )

    aggregate_text = aggregate_response.choices[0].message.content
    aggregate_prediction = json.loads(aggregate_text)

    print("Raw structured text:", aggregate_text)
    print("Parsed dictionary:", aggregate_prediction)
    """),
    md("""
    `messages` is a list containing one dictionary. `client.chat.send(...)` sends it to OpenRouter. The response contains a list named `choices`; `[0]` selects the first answer; `.message.content` retrieves its JSON string. `json.loads` converts that string into a Python dictionary.
    """),
    md("## 4. Check and compare the aggregate prediction"),
    code("""
    predicted_percentages = aggregate_prediction["percentages"]

    assert len(predicted_percentages) == 7
    assert all(0 <= value <= 100 for value in predicted_percentages)
    assert abs(sum(predicted_percentages) - 100) < 0.1

    gss_percentages = [4.4, 13.3, 11.6, 36.3, 12.1, 16.3, 5.9]
    comparison = pd.DataFrame({
        "scale": range(1, 8),
        "model_prediction": predicted_percentages,
        "gss_valid_percent": gss_percentages,
    })
    comparison
    """),
    md("""
    The assertions test the output structure and arithmetic. The dataframe puts the model prediction beside the 2024 GSS unweighted valid-response percentages. A match is evidence about this specific aggregate prediction—not evidence that the model created representative individuals.
    """),
    code("""
    comparison.plot(
        x="scale",
        y=["model_prediction", "gss_valid_percent"],
        kind="bar",
        figsize=(10, 4),
    )
    plt.ylabel("Percent")
    plt.title("Aggregate model prediction and 2024 GSS valid responses")
    plt.show()
    """),
    md("## 5. Exercise B — load actual GSS profile records"),
    code("""
    profile_path = Path("../../data/session07/gss_2024_polviews_profiles.csv")
    gss = pd.read_csv(profile_path)

    profile_columns = ["case_id", "age", "sex", "race", "degree", "partyid", "region"]
    profiles = gss[profile_columns].copy()
    held_out = gss[["case_id", "observed_polviews"]].copy()

    print("profiles shape:", profiles.shape)
    print("held_out shape:", held_out.shape)
    profiles.head()
    """),
    md("""
    The source file contains 28 public-use GSS records, four selected from each observed ideology category. `profiles` deliberately excludes `observed_polviews`; `held_out` keeps it for later comparison. This balanced teaching subset is not a population sample and must not be used to estimate the U.S. distribution.
    """),
    md("## 6. Define the structured output for one profile"),
    code("""
    profile_schema = {
        "type": "object",
        "properties": {
            "category": {"type": "integer", "minimum": 1, "maximum": 7},
            "probabilities": {
                "type": "array",
                "items": {"type": "number", "minimum": 0, "maximum": 1},
                "minItems": 7,
                "maxItems": 7,
            },
        },
        "required": ["category", "probabilities"],
        "additionalProperties": False,
    }

    profile_response_format = {
        "type": "json_schema",
        "json_schema": {
            "name": "profile_prediction",
            "strict": True,
            "schema": profile_schema,
        },
    }
    """),
    md("One answer must contain an integer category and seven probabilities. The schema checks their types and ranges. We separately check that the probabilities sum to one."),
    code('''
    def make_profile_prompt(profile):
        profile_text = profile.to_dict()
        return f"""Predict how the person described below answered the exact survey item.
        Return one category from 1 to 7 and probabilities for all seven categories in scale order.

        PROFILE:
        {profile_text}

        QUESTION:
        {polviews_question}
        """

    first_prompt = make_profile_prompt(profiles.iloc[0])
    print(first_prompt)
    '''),
    md("""
    `profiles.iloc[0]` selects the first row as a pandas Series. `.to_dict()` turns it into a dictionary. The function returns one string. Confirm that `observed_polviews` is absent before sending anything.
    """),
    md("## 7. Make one profile prediction before using a loop"),
    code("""
    first_response = client.chat.send(
        model=MODEL,
        messages=[{"role": "user", "content": first_prompt}],
        response_format=profile_response_format,
        provider={"require_parameters": True},
        stream=False,
    )

    first_result = json.loads(first_response.choices[0].message.content)
    assert abs(sum(first_result["probabilities"]) - 1) < 0.001
    print(first_result)
    """),
    md("Before moving on, name the current value and type of `first_response`, `first_result`, `first_result[\"category\"]`, and `first_result[\"probabilities\"]`."),
    md("## 8. Repeat the same operation across profiles"),
    code("""
    prediction_records = []

    # Use .head(6) for a short class run. Remove .head(6) to query all 28 profiles.
    for _, profile in profiles.head(6).iterrows():
        prompt = make_profile_prompt(profile)
        response = client.chat.send(
            model=MODEL,
            messages=[{"role": "user", "content": prompt}],
            response_format=profile_response_format,
            provider={"require_parameters": True},
            stream=False,
        )
        result = json.loads(response.choices[0].message.content)
        prediction_records.append({
            "case_id": int(profile["case_id"]),
            "predicted_polviews": result["category"],
            "probabilities": result["probabilities"],
            "model": MODEL,
            "prompt_id": "polviews_persona_v1",
        })

    predictions = pd.DataFrame(prediction_records)
    predictions
    """),
    md("""
    On each iteration, `profile` is one Series. The model returns one structured answer. `.append(...)` adds one dictionary to `prediction_records`. After six iterations, `predictions` has six rows. The loop does not change the original GSS file.
    """),
    md("## 9. Join predictions to answers the model did not see"),
    code("""
    profile_comparison = predictions.merge(
        held_out,
        on="case_id",
        validate="one_to_one",
    )

    profile_comparison["correct"] = (
        profile_comparison["predicted_polviews"]
        == profile_comparison["observed_polviews"]
    )

    accuracy = profile_comparison["correct"].mean()
    print("Exact-match accuracy:", accuracy)
    profile_comparison[["case_id", "predicted_polviews", "observed_polviews", "correct"]]
    """),
    md("""
    `merge` joins rows using `case_id`. `validate="one_to_one"` stops the code if an ID appears twice. The comparison produces Booleans. `.mean()` treats `True` as 1 and `False` as 0, returning the proportion exactly predicted.

    Accuracy is only one validation target. Also inspect distributions, errors by profile fields, prompt stability, and performance against simple baselines.
    """),
    md("""
    ## 10. Completion task

    1. Run the aggregate prediction and plot it beside the published GSS distribution.
    2. Change one inconsequential phrase in the aggregate instruction and record what changes.
    3. Run the profile prediction for at least six cases.
    4. Explain, line by line, how one response moves from the model call into `profile_comparison`.
    5. Report exact-match accuracy and compare predicted and observed category counts.
    6. In 150–200 words, explain why the aggregate and profile exercises validate different claims.
    7. Disclose model, access route, prompt version, query date, and any material AI assistance.

    Be ready to explain any four consecutive code lines orally, including the current value and Python type of every named object.
    """),
]

notebook = {
    "cells": cells,
    "metadata": {
        "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
        "language_info": {"name": "python", "version": "3"},
    },
    "nbformat": 4,
    "nbformat_minor": 5,
}

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
OUTPUT.write_text(json.dumps(notebook, indent=2) + "\n", encoding="utf-8")
print(f"Wrote {OUTPUT}")
