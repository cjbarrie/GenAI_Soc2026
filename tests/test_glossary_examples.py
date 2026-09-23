"""Keep every offline field-guide Python example independently runnable."""

from __future__ import annotations

import re
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
GLOSSARY = ROOT / "coursebook" / "glossary"
PAGES = sorted(path for path in GLOSSARY.glob("*.qmd") if path.name != "index.qmd")


def examples() -> list[tuple[str, str]]:
    collected: list[tuple[str, str]] = []
    for page in PAGES:
        text = page.read_text(encoding="utf-8")
        for number, source in enumerate(re.findall(r"```python\n(.*?)\n```", text, re.DOTALL), start=1):
            collected.append((f"{page.stem}-{number}", source))
    return collected


CASES = examples()


@pytest.mark.parametrize(("name", "source"), CASES, ids=[name for name, _ in CASES])
def test_glossary_example_runs(name: str, source: str) -> None:
    namespace: dict[str, object] = {}
    exec(compile(source, f"<glossary:{name}>", "exec"), namespace, namespace)
