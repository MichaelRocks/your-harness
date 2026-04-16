# Workflow

This is the required change loop for repository work.

## 1. Orient Before Editing

- Read `docs/index.md`, then the most relevant detailed docs.
- Explore the existing system first. Build a concrete picture of the current
  behavior, boundaries, and failure mode before proposing changes.

## 2. Save a Plan Before Code

- Create `docs/plans/active/YYYY-MM-DD-short-slug.md` before editing tracked
  files.
- Use `docs/plans/lightweight-template.md` for small, contained changes.
- Use `docs/plans/PLANS.md` for multi-step, risky, or multi-hour work.
- Capture the change description, expected observable behavior, hypotheses,
  validation plan, and intended observability changes.
- Incident reports belong in `docs/operations/incidents/` and capture live
  operational response notes.
- If incident mitigation changes tracked files, still create or update a normal
  change plan in `docs/plans/active/`. Incident reports do not replace plans.

## 3. Write Failing Tests First

- When executable behavior changes, start by writing a failing test that covers
  real behavior.
- Prefer the lowest-cost test that still exercises the real contract at risk.
- Add unit tests only when they support the broader behavior-level confidence.

For documentation-only changes, validate the reader-facing behavior instead:
link correctness, navigation, consistency, and whether the docs support the
intended workflow.

## 4. Implement the Smallest Complete Fix

- Fix the root cause.
- Keep the design explicit and maintainable.
- Avoid speculative abstraction unless the change genuinely needs it now.

## 5. Improve Observability While the Context Is Fresh

- Add or refine logs, metrics, traces, dashboards, or alerts where they will
  help future debugging or operations.
- Do not remove or bypass instrumentation to hide a failure mode.

## 6. Validate the Change

- Run automated tests and checks relevant to the change.
- Validate the real behavior directly where possible: user flows, API behavior,
  job execution, deployment behavior, operational signals, or documentation
  navigation.
- Record what was run and what was observed in the plan.

## 7. Promote Durable Knowledge

- Move lasting rules into `AGENTS.md` only if they affect most tasks.
- Otherwise update the appropriate document under `docs/`.
- Promote incident takeaways into the right durable home: `docs/operations/`
  for operator-facing recovery material, other `docs/` areas for new defaults
  or contracts, and `docs/plans/tech-debt.md` for deferred follow-up work.
- Record deferred work in `docs/plans/tech-debt.md`.

## 8. Close the Loop

- Update the plan with outcomes, surprises, decisions, and follow-ups.
- Move the plan from `docs/plans/active/` to `docs/plans/completed/`.
- Leave the repository easier to understand and operate.
