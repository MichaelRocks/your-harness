# Dependency Rules Template

Use this file to spell out allowed dependency directions after adopting the
scaffold in a real repository.

## Principles

- Dependencies should point toward more stable, lower-level abstractions.
- Feature code should not reach across layers for convenience.
- Shared modules should stay small and stable; they are not a dumping ground.

## Template

```md
## Layer or Package

- May depend on:
- Must not depend on:
- Why:
- Typical violation to watch for:
```

## Validation Ideas

- Import graph checks
- Architecture tests
- Code review checklists
- CI rules for forbidden dependency edges
