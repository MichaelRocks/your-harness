# Convert repo into the `your-harness` Codex plugin

## Change Summary

Convert this repository from a bare harness scaffold into a repo-root Codex
plugin named `your-harness`. Preserve the harness as a bundled canonical
template, add two explicit-use skills for bootstrapping or adopting the harness
in target repositories, and rewrite the repo-root docs so they describe plugin
maintenance and local installation instead of acting as the copied scaffold.

## Expected Behavior

- The repository installs as a local Codex plugin named `your-harness`.
- The plugin exposes `create-harness` and `adopt-harness` as explicit-use
  skills.
- The reusable harness scaffold lives in bundled assets and can be copied into
  target repositories.
- Local docs explain plugin maintenance, installation, and validation.

## Hypotheses / Findings

- Finding: The current repository is almost entirely a reusable docs scaffold
  with no existing plugin structure.
- Finding: The repo workflow requires a saved plan before changing tracked
  files.
- Finding: Python stdlib-only helper scripts were sufficient for deterministic
  template copy, placeholder substitution, additive adoption inventory, and CLI
  execution.

## Planned Tests

- Add failing tests first for the helper-script behavior:
  - empty-repo bootstrap succeeds
  - non-empty bootstrap refuses
  - adoption dry-run reports conflicts without overwriting
- Validate plugin metadata shape and local paths.
- Validate docs and asset link integrity after the repo-root rewrite.

## Planned Observability

- Keep helper-script output structured and legible so users can distinguish
  copied files, skipped files, and conflicts during bootstrap/adoption.

## Completion Notes

- Completed the repo-root `your-harness` plugin packaging with a local manifest,
  marketplace metadata, two explicit-use skills, shared Python helpers, and a
  bundled harness template under `assets/harness-template/`.
- Rewrote the repo-root routing docs for plugin maintenance while preserving the
  shipped scaffold as the canonical copy source.
- Validation completed with:
  - `python3 -m unittest discover -s tests`
- `python3 "$CODEX_HOME/skills/.system/skill-creator/scripts/quick_validate.py" skills/create-harness`
- `python3 "$CODEX_HOME/skills/.system/skill-creator/scripts/quick_validate.py" skills/adopt-harness`
  - JSON parse checks for `.codex-plugin/plugin.json` and `.agents/plugins/marketplace.json`
  - direct CLI smoke tests for `scripts/create_harness.py` and `scripts/adopt_harness.py`
