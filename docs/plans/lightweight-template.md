# Lightweight Plan Template

Use this template for small, contained, low-risk changes. The plan still must
exist before code starts.

## File Placement

- Create the file in `docs/plans/active/`.
- Use the naming scheme `YYYY-MM-DD-short-slug.md`.
- Move it to `docs/plans/completed/` when done.

## Template

```md
# Short change title

## Change Summary

One paragraph describing the problem, scope, and intended outcome.

## Expected Behavior

- What should be true after the change from the outside

## Hypotheses / Findings

- Hypothesis or confirmed finding

## Planned Tests

- Failing test to write first
- Additional automated checks
- Real behavior validation

## Planned Observability

- Logs, metrics, traces, dashboards, or alerts to add or review

## Completion Notes

- Final outcome
- Follow-up debt or docs to update
```

## When To Escalate To a Full ExecPlan

Switch to `docs/plans/PLANS.md` if the change becomes cross-cutting, risky,
hard to estimate, or likely to take multiple iterations.
