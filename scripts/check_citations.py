"""Validate BibTeX structure and optionally compare DOI metadata with Crossref."""

from __future__ import annotations

import argparse
import json
import re
from difflib import SequenceMatcher
from pathlib import Path
from urllib.parse import quote

import requests


ROOT = Path(__file__).resolve().parents[1]
BIB = ROOT / "references.bib"
ENTRY_PATTERN = re.compile(r"(?ms)^@(\w+)\{([^,]+),\n(.*?)\n\}")
FIELD_PATTERN = re.compile(r"(?ms)^\s*(\w+)\s*=\s*\{(.*?)\},?\s*$")


def normalize(text: str) -> str:
    text = re.sub(r"[{}\\]", "", text).lower()
    return " ".join(re.findall(r"[a-z0-9]+", text))


def entries() -> list[dict[str, object]]:
    parsed = []
    for entry_type, key, body in ENTRY_PATTERN.findall(BIB.read_text(encoding="utf-8")):
        fields = {name.lower(): value.replace("\n", " ").strip() for name, value in FIELD_PATTERN.findall(body)}
        parsed.append({"type": entry_type.lower(), "key": key, "fields": fields})
    return parsed


def structural_problems(records: list[dict[str, object]]) -> list[str]:
    problems: list[str] = []
    keys = [str(record["key"]) for record in records]
    if len(keys) != len(set(keys)):
        problems.append("duplicate BibTeX key")
    dois: list[str] = []
    for record in records:
        fields = record["fields"]
        assert isinstance(fields, dict)
        for required in ("author", "title", "year"):
            if not fields.get(required):
                problems.append(f"{record['key']}: missing {required}")
        if record["type"] == "article" and not fields.get("journal"):
            problems.append(f"{record['key']}: article missing journal")
        if fields.get("doi"):
            doi = str(fields["doi"]).lower()
            dois.append(doi)
            if not fields.get("url"):
                problems.append(f"{record['key']}: DOI entry missing URL")
        if fields.get("archiveprefix", "").lower() == "arxiv":
            eprint = str(fields.get("eprint", ""))
            if eprint not in str(fields.get("url", "")):
                problems.append(f"{record['key']}: arXiv URL does not contain eprint")
    if len(dois) != len(set(dois)):
        problems.append("duplicate DOI")
    return problems


def crossref_check(record: dict[str, object], timeout: float) -> dict[str, object]:
    fields = record["fields"]
    assert isinstance(fields, dict)
    doi = str(fields["doi"])
    url = "https://api.crossref.org/works/" + quote(doi, safe="")
    try:
        response = requests.get(
            url,
            headers={"User-Agent": "GenAI-Sociology-course-citation-check/2026 (academic maintenance)"},
            timeout=timeout,
        )
        response.raise_for_status()
        message = response.json()["message"]
        crossref_title = " ".join(message.get("title", []))
        ratio = SequenceMatcher(None, normalize(str(fields["title"])), normalize(crossref_title)).ratio()
        bib_author = normalize(str(fields.get("author", ""))).split()
        crossref_authors = message.get("author", [])
        first_family = normalize(str(crossref_authors[0].get("family", ""))).split() if crossref_authors else []
        # Crossref often supplies no author for unsigned journal editorials.
        author_match = not crossref_authors or bool(first_family and any(token in bib_author for token in first_family))
        category = "ok" if ratio >= 0.78 and author_match else "mismatch"
        return {
            "key": record["key"], "doi": doi, "category": category,
            "title_similarity": round(ratio, 3), "first_author_match": author_match,
            "crossref_title": crossref_title,
        }
    except (requests.RequestException, KeyError, ValueError, IndexError) as error:
        return {"key": record["key"], "doi": doi, "category": "error", "error": str(error)}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--external", action="store_true", help="compare DOI metadata with Crossref")
    parser.add_argument("--timeout", type=float, default=20.0)
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()

    records = entries()
    problems = structural_problems(records)
    online = [crossref_check(record, args.timeout) for record in records if args.external and record["fields"].get("doi")]
    failures = [item for item in online if item["category"] != "ok"]
    report = {"entries": len(records), "structural_problems": problems, "crossref": online}
    if args.json:
        output = args.json if args.json.is_absolute() else ROOT / args.json
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")

    print(f"Bibliography entries: {len(records)}; structural problems: {len(problems)}")
    if args.external:
        print(f"Crossref DOI records: {len(online)}; mismatches/errors: {len(failures)}")
    for problem in problems:
        print("BIBLIOGRAPHY", problem)
    for failure in failures:
        print("CROSSREF", failure)
    if problems or failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
