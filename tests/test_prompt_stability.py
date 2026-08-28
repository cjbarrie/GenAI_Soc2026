import pytest

from src.genai_soc.stability import inter_prompt_pss


def test_session02_prompt_variants_have_expected_pss():
    rows = [
        ["SUPPORT", "OPPOSE", "SUPPORT", "SUPPORT", "SUPPORT", "UNCLEAR", "OPPOSE", "SUPPORT", "OPPOSE", "UNCLEAR", "SUPPORT", "OPPOSE"],
        ["SUPPORT", "OPPOSE", "UNCLEAR", "SUPPORT", "SUPPORT", "UNCLEAR", "OPPOSE", "SUPPORT", "OPPOSE", "UNCLEAR", "UNCLEAR", "OPPOSE"],
        ["SUPPORT", "OPPOSE", "UNCLEAR", "SUPPORT", "SUPPORT", "UNCLEAR", "OPPOSE", "SUPPORT", "OPPOSE", "UNCLEAR", "SUPPORT", "OPPOSE"],
    ]

    assert round(inter_prompt_pss(rows), 3) == 0.835


def test_perfect_stability_returns_one():
    assert inter_prompt_pss([["A", "B"], ["A", "B"]]) == 1.0


def test_mismatched_rows_are_rejected():
    with pytest.raises(ValueError):
        inter_prompt_pss([["A"], ["A", "B"]])
