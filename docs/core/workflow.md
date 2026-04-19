# Workflow

This is the required change loop for maintaining the `your-harness` plugin and
its shipped scaffold.

## 1. Orient Before Editing

- Read `docs/index.md`, then the most relevant detailed docs.
- Explore the existing system first. Build a concrete picture of the current
  helper behavior, skill prompts, and shipped template before proposing
  changes.

## 2. Save a Plan Before Code

- Create `docs/plans/active/YYYY-MM-DD-short-slug.md` before editing tracked
  files.
- Use `docs/plans/lightweight-template.md` for small, contained changes.
- Use `docs/plans/PLANS.md` for multi-step, risky, or multi-hour work.
- Capture the change description, expected observable behavior, hypotheses,
  validation plan, intended observability changes, a concise planned-change
  summary, and explicit tasks.
- Every saved plan must contain a task checklist. For large work, the overview
  still needs a task-based roadmap instead of phase names alone.
- Keep detailed execution steps in the task checklist rather than duplicating
  them in the planned-change summary.
- Mark each task as done in the saved plan as soon as the work finishes.
- If the change affects generated user-project content, record whether the
  source of truth is a root maintainer doc or `assets/harness-template/`.

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
- Prefer shared helper logic in `shared/` with thin skill-facing
  CLI wrappers under `scripts/`.

## 5. Improve Observability While the Context Is Fresh

- Add or refine logs, metrics, traces, dashboards, or alerts where they will
  help future debugging or operations.
- Do not remove or bypass instrumentation to hide a failure mode.
- Keep helper output legible enough to show copied files, skipped files, and
  conflicts without reading implementation details.

## 6. Validate the Change

- Run automated tests and checks relevant to the change.
- Validate the real behavior directly where possible: skill invocation flow,
  helper CLI behavior, plugin metadata validity, and documentation navigation.
- Record what was run and what was observed in the plan.

## 7. Promote Durable Knowledge

- Move lasting rules into `AGENTS.md` only if they affect most tasks.
- Otherwise update the appropriate document under `docs/`, `references/`, or
  `assets/harness-template/`.
- Record deferred work in `docs/plans/tech-debt.md`.

## 8. Close the Loop

- Update the plan with outcomes, surprises, decisions, and follow-ups.
- Move the plan from `docs/plans/active/` to `docs/plans/completed/`.
- Leave the repository easier to understand and operate.
