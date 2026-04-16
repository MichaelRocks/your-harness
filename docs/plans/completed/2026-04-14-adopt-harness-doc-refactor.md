# Refactor template-owned docs during harness adoption

## Change Summary

Update `adopt-harness` so existing repositories do more than preserve legacy
docs structure. When a target repo already has files at the same `docs/` paths
as the bundled harness template, the adoption flow should refactor those
template-owned docs toward the harness defaults instead of leaving them as
manual conflicts. Non-doc conflicts should remain manual.

## Expected Behavior

- Dry-run adoption distinguishes template-owned doc refactors from true manual
  conflicts.
- Apply mode overwrites existing `docs/...` files that are also owned by the
  harness template.
- Apply mode still preserves non-doc conflicts like `AGENTS.md` for manual
  handling.
- Skill and policy docs describe the new default clearly.

## Hypotheses / Findings

- Finding: current adoption treats all same-path differences as generic
  conflicts.
- Finding: the bundled harness template owns a broad `docs/` tree, so leaving
  those paths untouched preserves legacy structure more than intended.
- Finding: refactoring only template-owned `docs/` files is the right middle
  ground between additive adoption and aggressive repo-wide normalization.

## Planned Tests

- Add a dry-run test that reports a template-owned doc path as a refactor path,
  not a conflict.
- Add an apply-mode test that overwrites an existing template-owned doc file.
- Keep the existing conflict-preservation test for non-doc files.
- Run `python3 -m unittest discover -s tests`.

## Planned Observability

- Extend adoption JSON output so users can see which paths will be refactored
  versus which remain manual conflicts.

## Completion Notes

- Updated `shared/adopt_harness.py` so existing template-owned `docs/...` files
  are classified as `refactored_paths` and rewritten during apply mode, while
  non-doc conflicts remain manual.
- Expanded `tests/test_adopt_harness.py` to cover dry-run doc refactors,
  preserved non-doc conflicts, and apply-mode doc rewrites.
- Updated `skills/adopt-harness/SKILL.md` and
  `references/adoption-conflict-policy.md` so the skill now promises doc
  refactoring for template-owned paths.
- Validation completed with:
  - `python3 -m unittest discover -s tests`
  - `python3 "$CODEX_HOME/skills/.system/skill-creator/scripts/quick_validate.py" skills/adopt-harness`
  - dry-run CLI smoke test showing `docs/index.md` under `refactored_paths`
