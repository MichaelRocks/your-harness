# Enforcement Policy

This scaffold defines what future automation should enforce. It does not yet
ship runnable CI jobs or repository scripts for these checks.

## Required Future Checks

### Planning Discipline

- Small-change chat plans are conversational and are not directly enforceable
  from repository files.
- Fail when a medium change saves no plan file in `docs/plans/active/` or
  `docs/plans/completed/`.
- Fail when a large change saves no plan folder with `overview.md` plus phase
  files in `docs/plans/active/` or `docs/plans/completed/`.
- Fail when a saved medium or large plan is missing required validation and
  outcome sections.
- Warn or fail when a large change collapses into one lightweight plan file
  instead of a phased plan set.

### Documentation Integrity

- Fail on broken relative links inside `AGENTS.md` and `docs/`.
- Fail when `AGENTS.md` grows beyond the agreed compact size threshold.
- Fail when required indexes or templates referenced from `docs/index.md` are
  missing.

### Quality Policy

- Fail when tests are removed or weakened without a documented rationale.
- Fail when a behavior change lands without evidence of relevant validation.
- Warn when observability-sensitive changes do not mention telemetry impact.

### Freshness and Closure

- Warn on stale files left in `docs/plans/active/`.
- Warn when completed plans omit outcomes, follow-ups, or knowledge promotion.
- Warn when deferred debt is mentioned in a plan but not captured in
  `docs/plans/tech-debt.md`.

## Suggested Implementation Approach

- Start with link checking and simple content-shape validation.
- Add diff-aware checks later so CI can require a plan for code changes.
- Keep policy checks legible; avoid turning the harness into an opaque gate.
