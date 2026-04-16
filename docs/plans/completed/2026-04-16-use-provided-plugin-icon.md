# Use provided image as plugin icon

## Change Summary

Replace the temporary `your-harness` plugin icon with the provided PNG asset
and update plugin metadata to reference that image for both small and large UI
icon slots.

## Expected Behavior

- The plugin manifest points at the provided PNG for both composer and logo use.
- The plugin-level `agents/openai.yaml` points at the provided PNG for both
  small and large icons.
- The repo asset under `assets/your-harness.png` matches the provided image.

## Hypotheses / Findings

- Finding: `.codex-plugin/plugin.json` and `agents/openai.yaml` still point at a
  placeholder SVG for the small icon.
- Finding: `assets/your-harness.png` is currently a placeholder 1x1 PNG.

## Planned Tests

- Validate `.codex-plugin/plugin.json` after the metadata update.
- Confirm `assets/your-harness.png` matches the provided file and has the
  expected dimensions.

## Planned Observability

- No new observability; validation is asset and metadata integrity only.

## Completion Notes

- Updated `.codex-plugin/plugin.json` so both `composerIcon` and `logo`
  reference `./assets/your-harness.png`.
- Updated `agents/openai.yaml` so both `icon_small` and `icon_large`
  reference `./assets/your-harness.png`.
- Replaced the placeholder asset with the provided PNG image.
- Validation:
  - `python3 -m json.tool .codex-plugin/plugin.json`
  - `file assets/your-harness.png`
  - `shasum -a 256 <provided-png> assets/your-harness.png`
