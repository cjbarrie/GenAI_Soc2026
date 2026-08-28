"""Check internal course links offline and external links on request.

The default run is deterministic and network-free. Use ``--external`` during a
release audit; restricted responses such as 403 and 429 count as reachable but
are reported separately from ordinary successes.
"""

from __future__ import annotations

import argparse
import json
import re
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from urllib.parse import urlparse

import requests


ROOT = Path(__file__).resolve().parents[1]
TEXT_SUFFIXES = {".md", ".qmd", ".bib", ".py", ".json", ".toml"}
SKIP_PARTS = {".git", ".venv", "_build"}
URL_PATTERN = re.compile(r"https?://[^\s<>\"'\]]+")
MARKDOWN_LINK_PATTERN = re.compile(r"!?\[[^]]*\]\(([^)]+)\)")
SOURCE_PATH_PATTERN = re.compile(r"Source:\s+(\.\.?/[^\s|]+)")
INTENTIONAL_HOSTS = {"localhost", "127.0.0.1", "example.org"}
RESTRICTED_BUT_REACHABLE = {401, 403, 405, 406, 429}


def text_files() -> list[Path]:
    return [
        path
        for path in ROOT.rglob("*")
        if path.is_file()
        and path.suffix in TEXT_SUFFIXES
        and not any(part in SKIP_PARTS for part in path.parts)
    ]


def clean_url(raw: str) -> str:
    """Remove Markdown/JSON punctuation accidentally captured after a URL."""
    url = raw.split("\\n", 1)[0].split("\\r", 1)[0]
    return url.rstrip("\\`.,;:)}>")


def external_urls(files: list[Path]) -> list[str]:
    urls: set[str] = set()
    for path in files:
        for raw in URL_PATTERN.findall(path.read_text(encoding="utf-8", errors="ignore")):
            url = clean_url(raw)
            if urlparse(url).hostname not in INTENTIONAL_HOSTS:
                urls.add(url)
    return sorted(urls)


def internal_problems(files: list[Path]) -> list[str]:
    problems: list[str] = []
    for path in files:
        if path.suffix not in {".md", ".qmd"}:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        targets = [match.strip().split()[0].strip("<>") for match in MARKDOWN_LINK_PATTERN.findall(text)]
        targets.extend(SOURCE_PATH_PATTERN.findall(text))
        for target in targets:
            if target.startswith(("http://", "https://", "#", "mailto:")):
                continue
            relative = target.split("#", 1)[0]
            if relative and not (path.parent / relative).resolve().exists():
                problems.append(f"{path.relative_to(ROOT)} -> {target}")
    return sorted(set(problems))


def fetch(url: str, timeout: float) -> dict[str, object]:
    headers = {"User-Agent": "GenAI-Sociology-course-link-check/2026 (academic maintenance)"}
    try:
        response = requests.get(url, headers=headers, timeout=timeout, allow_redirects=True, stream=True)
        status = response.status_code
        final_url = response.url
        response.close()
        category = "ok" if status < 400 else "restricted" if status in RESTRICTED_BUT_REACHABLE else "broken"
        return {"url": url, "status": status, "category": category, "final_url": final_url}
    except requests.RequestException as error:
        return {"url": url, "status": None, "category": "error", "error": str(error)}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--external", action="store_true", help="also make live HTTP requests")
    parser.add_argument("--timeout", type=float, default=20.0)
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--json", type=Path, help="write the complete report to this path")
    args = parser.parse_args()

    files = text_files()
    internal = internal_problems(files)
    results: list[dict[str, object]] = []
    if args.external:
        urls = external_urls(files)
        with ThreadPoolExecutor(max_workers=args.workers) as executor:
            futures = {executor.submit(fetch, url, args.timeout): url for url in urls}
            for future in as_completed(futures):
                results.append(future.result())
        results.sort(key=lambda item: str(item["url"]))

    report = {"internal_problems": internal, "external_results": results}
    if args.json:
        output = args.json if args.json.is_absolute() else ROOT / args.json
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")

    print(f"Internal links checked: {len(files)} files; problems: {len(internal)}")
    for problem in internal:
        print("BROKEN INTERNAL", problem)
    if args.external:
        counts = {category: sum(item["category"] == category for item in results) for category in ("ok", "restricted", "broken", "error")}
        print(f"External links checked: {len(results)}; {counts}")
        for item in results:
            if item["category"] in {"broken", "error"}:
                print("EXTERNAL FAILURE", item)

    if internal or any(item["category"] in {"broken", "error"} for item in results):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
