# Rename helper package to `shared`

## Change Summary

Rename the plugin's shared Python package from `your_harness_tools` to
`shared` so the implementation namespace is shorter and more general. Update
imports, maintainer docs, and tests to match.

## Expected Behavior

- Helper scripts import from `shared`.
- Tests import from `shared` and still pass.
- Maintainer docs reference `shared/` as the canonical helper package path.

## Hypotheses / Findings

- Finding: The current package name appears only in scripts, tests, and
  maintainer docs.
- Hypothesis: A straight directory rename plus import updates is sufficient.

## Planned Tests

- Run `python3 -m unittest discover -s tests`
- Run direct CLI smoke tests for `scripts/create_harness.py` and
  `scripts/adopt_harness.py`

## Planned Observability

- No new observability beyond keeping the helper CLI output unchanged.

## Completion Notes

- Renamed the helper package directory from `your_harness_tools/` to `shared/`.
- Updated imports in the scripts and tests, plus maintainer docs that point to
  the shared implementation location.
- Validation completed with:
  - `python3 -m unittest discover -s tests`
  - direct CLI smoke checks for `scripts/create_harness.py` and
    `scripts/adopt_harness.py`
