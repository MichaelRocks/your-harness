# Add SVG plugin icon

## Change Summary

Add the provided SVG icon to the plugin assets and update plugin metadata to
use it in the small/icon-oriented slots while keeping the PNG asset for the
large/logo slot.

## Expected Behavior

- `assets/your-harness.svg` matches the provided SVG asset.
- `.codex-plugin/plugin.json` uses the SVG for `composerIcon` and keeps the PNG
  for `logo`.
- `agents/openai.yaml` uses the SVG for `icon_small` and keeps the PNG for
  `icon_large`.

## Hypotheses / Findings

- Finding: the repo currently only stores the PNG version of the icon.
- Finding: the plugin metadata currently points both small and large icon
  fields at the PNG asset.

## Planned Tests

- Validate `.codex-plugin/plugin.json` after the metadata update.
- Confirm `assets/your-harness.svg` matches the provided file.
- Confirm the updated metadata references the SVG and PNG in the intended
  fields.

## Planned Observability

- No new observability; validation is asset and metadata integrity only.

## Completion Notes

- Added `assets/your-harness.svg` from the provided SVG asset.
- Updated `.codex-plugin/plugin.json` so `composerIcon` points to the SVG and
  `logo` remains on the PNG asset.
- Updated `agents/openai.yaml` so `icon_small` points to the SVG and
  `icon_large` remains on the PNG asset.
- Validation:
  - `python3 -m json.tool .codex-plugin/plugin.json`
  - `shasum -a 256 <provided-svg> assets/your-harness.svg`
  - Verified the icon fields in both metadata files.
