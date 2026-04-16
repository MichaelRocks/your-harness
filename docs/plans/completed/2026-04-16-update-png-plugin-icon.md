# Update PNG plugin icon

## Change Summary

Replace the existing raster plugin icon with the updated provided PNG asset.

## Expected Behavior

- `assets/your-harness.png` matches the provided PNG asset.
- The existing plugin metadata continues to reference the same PNG path for the
  large/logo icon slots without further changes.

## Hypotheses / Findings

- Finding: the provided PNG has a different checksum than the current repo
  asset.
- Finding: the current metadata already points large/logo fields at
  `./assets/your-harness.png`, so only the asset file needs replacement.

## Planned Tests

- Confirm `assets/your-harness.png` matches the provided file by SHA-256.
- Confirm the copied asset remains a valid PNG with the expected dimensions.

## Planned Observability

- No new observability; validation is asset integrity only.

## Completion Notes

- Replaced `assets/your-harness.png` with the updated provided PNG asset.
- Validation:
  - `shasum -a 256 <provided-png> assets/your-harness.png`
  - `file assets/your-harness.png`
