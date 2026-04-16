# Remove absolute paths from docs

## Change Summary

Remove machine-specific absolute paths from the plugin's maintainer docs and
completed plan records so the documentation stays portable across machines and
install layouts.

## Expected Behavior

- `docs/` does not contain user-specific absolute filesystem paths.
- Validation examples in docs use repo-relative paths, environment variables,
  or generic placeholders instead of local absolute paths.
- Maintainer guidance makes this documentation rule explicit.

## Hypotheses / Findings

- Finding: absolute paths currently appear in completed plan records for icon
  updates and skill validation commands.
- Hypothesis: a small knowledge-management note is enough to prevent the issue
  from recurring.

## Planned Tests

- Search `docs/` for absolute path patterns after the edits.
- Review the updated plan records and guidance for clarity.

## Planned Observability

- No new observability; this is a documentation portability cleanup.

## Completion Notes

- Replaced machine-specific absolute paths in completed plan records with
  placeholders or `$CODEX_HOME`-based examples.
- Added a durable documentation rule to `docs/core/knowledge-management.md`
  requiring portable path examples in docs.
- Validation:
  - `rg -n '/Users/|/home/|/root/|[A-Za-z]:\\\\|~/' docs`
