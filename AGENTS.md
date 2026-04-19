# AGENTS.md

This repository ships the `your-harness` Codex plugin. Keep this file short.
Treat it as a routing layer plus a small set of non-negotiable operating rules.
Put detailed maintenance knowledge under `docs/`.

## Start Here

1. Open `docs/index.md`.
2. Read `docs/core/workflow.md` before changing tracked files.
3. Read `README.md` for local plugin usage and package layout.
4. If the task changes shipped scaffold behavior, read
   `assets/harness-template/AGENTS.md` and the matching docs under
   `assets/harness-template/docs/`.
5. If the task changes skill behavior, read the relevant skill under `skills/`
   plus the shared references under `references/`.

## Non-Negotiables

- Save a change plan before code. Create a file in
  `docs/plans/active/YYYY-MM-DD-short-slug.md`.
- Use `docs/plans/lightweight-template.md` for small changes. Use
  `docs/plans/PLANS.md` for multi-step, risky, or multi-hour work.
- Keep the shipped scaffold canonical in `assets/harness-template/`. Do not
  treat the repo root docs as the source copied into user projects.
- Keep skills, helper scripts, and template docs aligned when behavior changes.
- Every saved plan must include a concise planned-change summary and an
  explicit task checklist. Large-change roadmaps still need explicit tasks,
  not just phase names.
- Keep the plan live while working. Record progress, hypotheses, findings,
  decisions, and validation results as they happen, and mark each completed
  task done as soon as it is finished.
- Write tests before implementation when changing executable behavior. Start
  with a failing test that exercises observable system behavior.
- Validate the real behavior of the system, not only internal invariants.
- Do not hide bugs by weakening assertions, suppressing failures, removing
  instrumentation, or changing the observation path just to make a symptom
  disappear.
- Fix the root cause or document why that is not yet possible.
- Add or improve logs, metrics, traces, dashboards, or alerts when they would
  materially improve debugging or operations.
- Keep designs boring in the positive sense: legible, inspectable, and easy to
  maintain. Avoid needless abstraction and cleverness.
- Promote durable knowledge to the right docs before closing the change.
- When the change is complete, move the plan file to `docs/plans/completed/`
  and capture outcomes plus follow-up debt.

## Read Map

- Plugin usage and local installation: `README.md`
- Planning rules and templates: `docs/plans/`
- Repo-wide engineering rules: `docs/core/`
- Shipped harness template: `assets/harness-template/`
- Skill prompts and conflict policy: `references/`
- Tests and helper implementations: `tests/`, `shared/`, `scripts/`

## Where Knowledge Lives

- Put a rule in `AGENTS.md` only if it changes how the agent should approach
  most tasks in the repository.
- Put plugin-maintainer workflow detail in `docs/core/`.
- Put shipped user-project workflow and templates in `assets/harness-template/`.
- Put skill prompting defaults and merge policy in `references/`.
- Put helper logic in `shared/` and thin CLIs in `scripts/`.
- Put transient work notes in the active/completed plan unless they become
  durable guidance or deferred debt.

## Per-Change Workflow

1. Read `docs/index.md` and the relevant detailed docs.
2. Explore the current system before proposing edits.
3. Create the plan file in `docs/plans/active/`.
4. Record the change description, expected behavior, hypotheses, and validation
   approach, plus a concise planned-change summary and explicit tasks.
5. Write failing tests for observable behavior before code when helper or skill
   behavior is changing.
6. Implement the smallest root-cause fix that satisfies the plan.
7. Update the shipped template and maintainer docs together when defaults move.
8. Run the relevant automated checks and direct behavior validation.
9. Promote durable findings into `AGENTS.md`, `docs/`, `references/`, or
   `assets/harness-template/` as appropriate.
10. Finish the plan, capture outcomes and follow-ups, then move it to
   `docs/plans/completed/`.

## Quality Bar

- Prefer interfaces and tests that reflect real user, system, or operator
  behavior.
- Prefer simple designs with explicit boundaries.
- Make failures legible. Good error messages and telemetry are part of the
  feature.
- Leave the repository easier to understand than you found it.

## Documentation Maintenance

- Keep `AGENTS.md` compact; target about 100-150 lines.
- Use `docs/index.md` as the main router for detailed guidance.
- Cross-link related docs instead of repeating large sections.
- If a section is stack-specific or task-specific, it does not belong here.

## Future Repositories

- This template ships with one root `AGENTS.md`.
- Larger repos and monorepos may add nested `AGENTS.md` files in subtrees.
- A more local `AGENTS.md` may add constraints for its subtree, but it should
  not silently contradict the root contract.
