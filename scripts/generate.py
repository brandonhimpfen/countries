#!/usr/bin/env python3
"""Generate distribution files from data/countries.csv."""

from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "countries.csv"
DIST_DIR = ROOT / "dist"
JSON_FILE = ROOT / "data" / "countries.json"
YAML_FILE = ROOT / "data" / "countries.yaml"

FIELDS = ["name", "official_name", "common_name", "alpha_2", "alpha_3", "numeric", "flag"]


def read_rows() -> list[dict[str, str]]:
    with DATA_FILE.open(newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    return sorted(rows, key=lambda row: row["name"])


def write_csv(rows: list[dict[str, str]]) -> None:
    with DATA_FILE.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)


def write_json(rows: list[dict[str, str]]) -> None:
    JSON_FILE.write_text(json.dumps(rows, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def yaml_quote(value: str) -> str:
    if value == "":
        return '""'
    return json.dumps(value, ensure_ascii=False)


def write_yaml(rows: list[dict[str, str]]) -> None:
    lines: list[str] = []
    for row in rows:
        lines.append(f"- name: {yaml_quote(row['name'])}")
        for field in FIELDS[1:]:
            lines.append(f"  {field}: {yaml_quote(row[field])}")
    YAML_FILE.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_dist(rows: list[dict[str, str]]) -> None:
    DIST_DIR.mkdir(exist_ok=True)
    names = [row["name"] for row in rows]

    (DIST_DIR / "countries.txt").write_text("\n".join(names) + "\n", encoding="utf-8")
    (DIST_DIR / "countries-comma.txt").write_text(", ".join(names) + "\n", encoding="utf-8")
    (DIST_DIR / "typeahead.json").write_text(json.dumps(names, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (DIST_DIR / "country-codes-alpha-2.txt").write_text("\n".join(row["alpha_2"] for row in rows) + "\n", encoding="utf-8")
    (DIST_DIR / "country-codes-alpha-3.txt").write_text("\n".join(row["alpha_3"] for row in rows) + "\n", encoding="utf-8")


def main() -> None:
    rows = read_rows()
    write_csv(rows)
    write_json(rows)
    write_yaml(rows)
    write_dist(rows)
    print(f"Generated files for {len(rows)} ISO 3166-1 entries.")


if __name__ == "__main__":
    main()
