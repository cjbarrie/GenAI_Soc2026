# Session 7 data

`gss_2024_polviews_profiles.csv` contains 28 records selected from the official 2024 GSS public-use Stata file, Release 3a (July 2026).

- The file is restricted to the cross-sectional sample (`sample == 13`).
- Cases have valid values for `age`, `sex`, `race`, `degree`, `partyid`, `region`, and `polviews`.
- Four cases were selected from each observed `POLVIEWS` category with fixed random seeds (`20261022` through `20261028`).
- Numeric profile fields were converted to their published labels.
- `observed_polviews` is retained only as the held-out comparison. It must not be included in a model prompt.

This is a deliberately balanced teaching subset, not a probability sample or an estimate of the U.S. distribution. The full source file is available from [NORC’s GSS Stata download page](https://gss.norc.org/get-the-data/stata.html).
