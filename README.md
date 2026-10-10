# Countries Dataset

[![Support Open Work](https://img.shields.io/badge/Support-Open%20Work-0A0A0A?style=flat&logo=github)](https://github.com/brandonhimpfen/support) 
[![DOI](https://zenodo.org/badge/365576488.svg)](https://doi.org/10.5281/zenodo.20141608)
[![GitHub Sponsor](https://srv-cdn.himpfen.io/badges/github/github-flat.svg)](https://github.com/sponsors/brandonhimpfen) 
[![Buy Me a Coffee](https://srv-cdn.himpfen.io/badges/buymeacoffee/buymeacoffee-flat.svg)](https://buymeacoffee.com/brandonhimpfen) 
[![Ko-Fi](https://srv-cdn.himpfen.io/badges/kofi/kofi-flat.svg)](https://ko-fi.com/brandonhimpfen) 
[![PayPal](https://srv-cdn.himpfen.io/badges/paypal/paypal-flat.svg)](https://paypal.me/brandonhimpfen)

A clean, UTF-8 encoded country and territory reference dataset based on ISO 3166-1 country code elements.

This repository provides country and territory names with ISO alpha-2, alpha-3, and numeric codes in CSV, JSON, YAML, plain text, comma-separated text, and typeahead-friendly JSON formats.

## What is included

The canonical dataset is available at:

```text
data/countries.csv
```

Generated distribution files are available in:

```text
dist/
```

The dataset currently contains 249 ISO 3166-1 entries. ISO 3166-1 includes sovereign countries and some dependent territories or special areas. It should not be treated as a list of only sovereign states, only United Nations member states, or only travel destinations.

## Files

| File | Purpose |
|---|---|
| `data/countries.csv` | Canonical tabular dataset |
| `data/countries.json` | Canonical JSON dataset |
| `data/countries.yaml` | Canonical YAML dataset |
| `dist/countries.txt` | One country or territory name per line |
| `dist/countries-comma.txt` | Comma-separated country and territory names |
| `dist/typeahead.json` | Array of names for autocomplete and typeahead use |
| `dist/country-codes-alpha-2.txt` | ISO alpha-2 codes, one per line |
| `dist/country-codes-alpha-3.txt` | ISO alpha-3 codes, one per line |

## Dataset fields

| Field | Description |
|---|---|
| `name` | ISO English short name |
| `official_name` | Official ISO name when available |
| `common_name` | Common English name when available |
| `alpha_2` | ISO 3166-1 alpha-2 code |
| `alpha_3` | ISO 3166-1 alpha-3 code |
| `numeric` | ISO 3166-1 numeric code |
| `flag` | Unicode flag emoji derived from the alpha-2 code when available |

## Usage examples

### JavaScript

```js
import countries from "./data/countries.json" assert { type: "json" };

const canada = countries.find((country) => country.alpha_2 === "CA");
console.log(canada.name);
```

### Python

```python
import csv

with open("data/countries.csv", encoding="utf-8") as file:
    countries = list(csv.DictReader(file))

canada = next(country for country in countries if country["alpha_2"] == "CA")
print(canada["name"])
```

## Data quality

This repository is designed to be easy to validate and reuse:

- UTF-8 encoded files
- one canonical CSV source
- generated JSON, YAML, and text outputs
- validation for duplicate names and codes
- validation for ISO code formats
- validation that generated files match the canonical dataset

Run validation with:

```bash
python scripts/validate.py
```

Regenerate the JSON, YAML, and distribution files with:

```bash
python scripts/generate.py
```

## Sources and scope

The dataset follows ISO 3166-1 country code elements. The scope is country and territory code elements, not a political recognition statement.

Useful references:

- ISO 3166 country codes: https://www.iso.org/iso-3166-country-codes.html
- United Nations member states: https://www.un.org/en/about-us/member-states
- UN membership research guide: https://research.un.org/en/unmembers/currentmembers

## License

This repository is released under the MIT License. See `LICENSE` for details.
