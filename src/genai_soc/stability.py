"""Small prompt-stability helpers supplied to students after the manual trace."""

from __future__ import annotations

from collections import Counter


def inter_prompt_pss(label_rows: list[list[str]]) -> float:
    """Return nominal Krippendorff alpha across complete prompt-label rows.

    Each inner list contains the labels produced by one prompt variant in the
    same item order. The Session 2 workbook treats prompt variants as raters.
    This deliberately small helper accepts complete data only; it is not a
    replacement for the full prompt-stability package used in research.
    """
    if len(label_rows) < 2:
        raise ValueError("Provide labels from at least two prompt variants.")

    item_count = len(label_rows[0])
    if item_count == 0 or any(len(row) != item_count for row in label_rows):
        raise ValueError("Every prompt row must contain the same non-zero items.")

    prompt_count = len(label_rows)
    comparisons_per_item = prompt_count * (prompt_count - 1)
    observed_disagreements = 0

    for item_index in range(item_count):
        item_labels = [row[item_index] for row in label_rows]
        for first in item_labels:
            for second in item_labels:
                if first != second:
                    observed_disagreements += 1

    observed = observed_disagreements / (item_count * comparisons_per_item)

    all_labels = [label for row in label_rows for label in row]
    label_counts = Counter(all_labels)
    total = len(all_labels)
    expected = sum(
        count * (total - count) for count in label_counts.values()
    ) / (total * (total - 1))

    if expected == 0:
        return 1.0
    return 1 - (observed / expected)
