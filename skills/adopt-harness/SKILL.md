---
name: adopt-harness
description: Use this skill when a user wants to add the your-harness workflow to an existing repository. Trigger for repos that already contain substantive code or docs and need additive adoption, automatic refactoring of template-owned docs, plus conflict reporting for non-doc files.
---

# Adopt Harness

## Overview

Add the `your-harness` workflow to an existing repository. This skill inspects
the current repo first, produces a dry-run inventory, refactors template-owned
docs toward the harness defaults, and leaves non-doc conflicts for manual
handling.

## Workflow

1. Treat the target as an existing project. Preserve current files unless a
   human explicitly decides to merge them.
2. Run the dry-run helper first:

```bash
python3 ../../scripts/adopt_harness.py \
  --target "$TARGET_REPO" \
  --project-name "Existing Project"
```

3. Review the JSON result:
   - `copied_paths` shows what would be added
   - `refactored_paths` shows existing template-owned docs that will be rewritten
   - `conflicts` shows non-doc same-path files that still need manual handling
   - `matching_paths` shows files already aligned with the shipped scaffold
4. Use [`../../references/adoption-conflict-policy.md`](../../references/adoption-conflict-policy.md)
   when deciding how to handle conflicts.
5. If dry-run results look safe, apply the additive copy:

```bash
python3 ../../scripts/adopt_harness.py \
  --target "$TARGET_REPO" \
  --project-name "Existing Project" \
  --apply
```

6. Review the created adoption plan, inspect the refactored docs, and merge any
   remaining non-doc conflicts conversationally instead of overwriting them
   blindly.

## Notes

- Apply mode creates the adoption plan before copying or refactoring template
  files.
- Existing `docs/...` files that are also owned by the harness template are
  rewritten by default during adoption.
- The helper still never overwrites existing non-doc files.
- The canonical shipped scaffold lives in `../../assets/harness-template/`.
