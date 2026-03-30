# Boundaries Template

Document the intentional seams in the system.

## Boundary Questions

- What are the main subsystems or modules?
- What responsibilities does each one own?
- Which interactions are allowed directly?
- Which interactions must go through stable interfaces?
- Where should state live, and who may mutate it?

## Template

```md
## Subsystem

- Owns:
- Must not own:
- Public interface:
- Allowed callers:
- Forbidden shortcuts:
- Notes on testing and observability:
```

## Review Rule

When a change crosses a boundary, update this document or the matching
architecture doc so the new rule is explicit.
