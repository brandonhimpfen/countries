# Sources and Methodology

This dataset follows ISO 3166-1 country code elements.

## Primary scope

The dataset includes ISO 3166-1 country and territory code elements. This includes sovereign countries, dependent territories, and special areas that have assigned ISO code elements.

This dataset is not intended to be a list of only sovereign states, only United Nations member states, or only internationally recognized countries.

## References

- ISO 3166 country codes: https://www.iso.org/iso-3166-country-codes.html
- United Nations member states: https://www.un.org/en/about-us/member-states
- UN Membership Research Guide: https://research.un.org/en/unmembers/currentmembers

## Update approach

Future updates should be based on changes to ISO 3166-1. Generated files in `dist/` should be recreated after the canonical dataset changes.

Recommended update process:

1. Update `data/countries.csv`.
2. Run `python scripts/generate.py`.
3. Run `python scripts/validate.py`.
4. Review the diff before publishing a release.
