# Adoption Conflict Policy

Use this when running `scripts/adopt_harness.py` or reviewing its dry-run output.

## Defaults

- Never overwrite an existing file automatically
- Copy only missing scaffold files
- Refactor existing `docs/...` files that are also owned by the harness template
- Treat remaining same-path, different-content non-doc files as conflicts
- Create the adoption plan before any additive copy during apply mode

## Conflict Handling

- Preserve non-doc target repo files as the source of truth
- Use the bundled template as a reference input for a manual merge
- Prefer bridge docs or index links over mass renames when the target repo
  already has a different layout outside the template-owned doc set
- Let the harness replace template-owned docs such as `docs/index.md`,
  `docs/core/*`, `docs/plans/*`, and the other bundled scaffold docs when those
  exact paths already exist
- If a repo already has a planning or incident workflow, integrate the harness
  guidance into that structure only when it lives outside the template-owned
  doc paths
