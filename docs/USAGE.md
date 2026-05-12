# Usage Guide

This repository provides several formats so the dataset can be used in websites, apps, scripts, documentation, and data pipelines.

## Use CSV for data analysis

Use `data/countries.csv` when working with spreadsheets, databases, Python, R, or data processing tools.

## Use JSON for applications

Use `data/countries.json` when loading the full dataset in a web app or API.

Use `dist/typeahead.json` when you only need a simple list of names for autocomplete.

## Use text files for simple lists

Use `dist/countries.txt` when you need one name per line.

Use `dist/countries-comma.txt` when you need a readable comma-separated list.

## Choosing the right name field

Use `name` for most applications.

Use `official_name` when you need the formal ISO name and it is available.

Use `common_name` when the ISO dataset provides a more common English form.
