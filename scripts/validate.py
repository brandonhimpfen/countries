#!/usr/bin/env python3
"""Validate the countries dataset and generated distribution files."""

from __future__ import annotations

import csv
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "countries.csv"
DIST_DIR = ROOT / "dist"
JSON_FILE = ROOT / "data" / "countries.json"
YAML_FILE = ROOT / "data" / "countries.yaml"

FIELDS = ["name", "official_name", "common_name", "alpha_2", "alpha_3", "numeric", "flag"]
ALPHA_2 = re.compile(r"^[A-Z]{2}$")
ALPHA_3 = re.compile(r"^[A-Z]{3}$")
NUMERIC = re.compile(r"^[0-9]{3}$")


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    sys.exit(1)


def read_rows() -> list[dict[str, str]]:
    with DATA_FILE.open(newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        if reader.fieldnames != FIELDS:
            fail(f"Unexpected CSV fields: {reader.fieldnames}")
        return list(reader)


def assert_unique(rows: list[dict[str, str]], field: str) -> None:
    values = [row[field] for row in rows]
    duplicates = sorted({value for value in values if values.count(value) > 1})
    if duplicates:
        fail(f"Duplicate values in {field}: {duplicates}")


def validate_rows(rows: list[dict[str, str]]) -> None:
    if len(rows) != 249:
        fail(f"Expected 249 ISO 3166-1 entries, found {len(rows)}")

    if rows != sorted(rows, key=lambda row: row["name"]):
        fail("Rows must be sorted alphabetically by name")

    for field in ["name", "alpha_2", "alpha_3", "numeric"]:
        assert_unique(rows, field)

    for row in rows:
        if not row["name"]:
            fail("Every row must have a name")
        if not ALPHA_2.match(row["alpha_2"]):
            fail(f"Invalid alpha_2 for {row['name']}: {row['alpha_2']}")
        if not ALPHA_3.match(row["alpha_3"]):
            fail(f"Invalid alpha_3 for {row['name']}: {row['alpha_3']}")
        if not NUMERIC.match(row["numeric"]):
            fail(f"Invalid numeric code for {row['name']}: {row['numeric']}")


def validate_generated_files(rows: list[dict[str, str]]) -> None:
    names = [row["name"] for row in rows]

    json_rows = json.loads(JSON_FILE.read_text(encoding="utf-8"))
    if json_rows != rows:
        fail("data/countries.json does not match data/countries.csv")

    expected_names = "\n".join(names) + "\n"
    if (DIST_DIR / "countries.txt").read_text(encoding="utf-8") != expected_names:
        fail("dist/countries.txt is out of date")

    expected_comma = ", ".join(names) + "\n"
    if (DIST_DIR / "countries-comma.txt").read_text(encoding="utf-8") != expected_comma:
        fail("dist/countries-comma.txt is out of date")

    typeahead = json.loads((DIST_DIR / "typeahead.json").read_text(encoding="utf-8"))
    if typeahead != names:
        fail("dist/typeahead.json is out of date")

    alpha_2 = (DIST_DIR / "country-codes-alpha-2.txt").read_text(encoding="utf-8")
    if alpha_2 != "\n".join(row["alpha_2"] for row in rows) + "\n":
        fail("dist/country-codes-alpha-2.txt is out of date")

    alpha_3 = (DIST_DIR / "country-codes-alpha-3.txt").read_text(encoding="utf-8")
    if alpha_3 != "\n".join(row["alpha_3"] for row in rows) + "\n":
        fail("dist/country-codes-alpha-3.txt is out of date")

    if not YAML_FILE.read_text(encoding="utf-8").startswith("- name:"):
        fail("data/countries.yaml appears to be invalid or empty")


def main() -> None:
    rows = read_rows()
    validate_rows(rows)
    validate_generated_files(rows)
    print(f"Validation passed for {len(rows)} ISO 3166-1 entries.")


if __name__ == "__main__":
    main()
