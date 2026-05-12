# Dataset Schema

The canonical dataset is `data/countries.csv`.

## Fields

| Field | Type | Required | Description |
|---|---:|---:|---|
| `name` | string | yes | ISO English short name |
| `official_name` | string | no | Official ISO name when available |
| `common_name` | string | no | Common English name when available |
| `alpha_2` | string | yes | ISO 3166-1 alpha-2 code |
| `alpha_3` | string | yes | ISO 3166-1 alpha-3 code |
| `numeric` | string | yes | ISO 3166-1 numeric code, stored as a three-character string to preserve leading zeros |
| `flag` | string | no | Unicode flag emoji derived from the alpha-2 code when available |

## Sorting

Rows are sorted alphabetically by `name`.

## Encoding

All files are UTF-8 encoded.

## Notes for implementers

The `numeric` field should be treated as a string, not an integer. Some ISO numeric codes include leading zeros.

The `name` field follows ISO short names, which means some names may differ from everyday usage. For example, `Türkiye` is used instead of `Turkey`, and `Czechia` is used as the short name while `Czech Republic` appears as the official name.
