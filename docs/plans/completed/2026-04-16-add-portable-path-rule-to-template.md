# Add portable path rule to template

## Change Summary

Add the same documentation portability rule used in the plugin maintainer docs
to the shipped harness template so generated repositories avoid user-specific
absolute filesystem paths in their durable docs.

## Expected Behavior

- The harness template docs explicitly require portable path examples.
- The rule lives in the template's durable documentation guidance rather than
  only in transient plans.
- `assets/harness-template/` remains free of user-specific absolute paths.

## Hypotheses / Findings

- Finding: the shipped template currently does not contain hardcoded absolute
  paths.
- Finding: the template's `docs/core/knowledge-management.md` is the right
  durable home for this rule.

## Planned Tests

- Search `assets/harness-template/` for absolute path patterns after the edit.
- Review the updated template docs for clarity and consistency.

## Planned Observability

- No new observability; this is a documentation policy update.

## Completion Notes

- Added the documentation portability rule to
  `assets/harness-template/docs/core/knowledge-management.md`.
- Added the same rule to `assets/harness-template/docs/index.md` so it is
  visible in the template docs router.
- Validation:
  - `rg -n '/Users/|/home/|/root/|[A-Za-z]:\\\\|~/' assets/harness-template`
