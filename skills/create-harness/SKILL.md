---
name: create-harness
description: Use this skill when a user wants to bootstrap the your-harness workflow into an empty repository from a product description and a short set of requirements. Trigger only for new or effectively empty projects. If the target repo already has substantive files, use `adopt-harness` instead.
---

# Create Harness

## Overview

Bootstrap a new repository with the canonical `your-harness` scaffold. This
skill gathers a small amount of project framing, then runs the bundled helper
to copy the template and create the initial live plan.

## Workflow

1. Confirm the target repository is empty enough for bootstrapping. If the repo
   already contains real project files, stop and switch to `adopt-harness`.
2. Collect the minimum project framing:
   - project name
   - product description
   - primary stacks
   - platforms
   - operations profile
   - testing posture
   - emphasis areas
   Read [`../../references/create-harness-questionnaire.md`](../../references/create-harness-questionnaire.md)
   for defaults.
3. Run the helper:

```bash
python3 ../../scripts/create_harness.py \
  --target "$TARGET_REPO" \
  --project-name "Project Name" \
  --product-description "Short product description" \
  --primary-stacks backend,frontend \
  --platforms web \
  --ops-profile standard \
  --testing-posture behavior-first \
  --emphasis-areas observability
```

4. Review the JSON result. It should include the created plan path and copied
   template files.
5. Spot-check the generated `README.md`, `AGENTS.md`, and `docs/plans/active/`
   contents in the target repo before moving on to repo-specific implementation.

## Notes

- The helper refuses non-empty repositories and tells the user to use
  `adopt-harness`.
- The canonical shipped scaffold lives in `../../assets/harness-template/`.
- Keep output rooted in the target repository; do not rewrite the plugin source
  repository while using this skill.
