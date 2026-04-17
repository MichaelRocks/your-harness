# AGENTS.md

This repository contains `{{PROJECT_NAME}}`. Product description:
`{{PRODUCT_DESCRIPTION}}`. Use this file as a routing layer plus a small set of
non-negotiable operating rules. Put detailed, durable knowledge under `docs/`.

## Start Here

1. Open `docs/index.md`.
2. Read `docs/core/workflow.md` before changing tracked files.
3. Read the most relevant stack or domain doc before implementing:
   - Backend: `docs/playbooks/backend.md`
   - Frontend: `docs/playbooks/frontend.md`
   - Mobile: `docs/playbooks/mobile.md`
   - DevOps/platform: `docs/playbooks/devops.md`
   - Operations/incident response: `docs/operations/index.md`
4. If the task changes architecture, behavior contracts, testing strategy, or
   reliability/security posture, read the matching docs in `docs/`.
5. If the task adds or changes functionality, choose the planning skill before
   implementation:
   - `$plan-small-change` for small, contained work that only needs a brief
     approval plan in chat
   - `$plan-medium-large-change` for medium/large work that should save a plan
     file before coding

## Non-Negotiables

- Save a change plan before code. Create a file in
  `docs/plans/active/YYYY-MM-DD-short-slug.md`.
- Use `docs/plans/lightweight-template.md` for small changes. Use
  `docs/plans/PLANS.md` for multi-step, risky, or multi-hour work.
- Incident reports live in `docs/operations/incidents/`, but they do not
  replace the required change plan when tracked files change.
- Keep the plan live while working. Record progress, hypotheses, findings,
  decisions, and validation results as they happen.
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

- Planning rules and templates: `docs/plans/`
- Repo-wide engineering rules: `docs/core/`
- Architecture and boundaries: `docs/architecture/`
- Behavior contracts and journeys: `docs/specs/`
- Testing, observability, reliability, security: `docs/quality/`
- Operations, incidents, runbooks: `docs/operations/`
- Stack-specific guidance: `docs/playbooks/`
- Cross-cutting decisions: `docs/decisions/`
- External references: `docs/references/`
- Generated artifacts: `docs/generated/`

## Where Knowledge Lives

- Put a rule in `AGENTS.md` only if it changes how the agent should approach
  most tasks in the repository.
- Put repo-wide detail in `docs/core/`.
- Put system structure, layering, and dependency rules in `docs/architecture/`.
- Put user-visible or system-visible behavior in `docs/specs/`.
- Put testing, observability, reliability, and security practices in
  `docs/quality/`.
- Put incident reports, runbooks, and recovery procedures in
  `docs/operations/`.
- Put stack-specific patterns in `docs/playbooks/`.
- Put durable decisions with tradeoffs in `docs/decisions/`.
- Put transient work notes in the active/completed plan or incident report
  unless they become durable guidance or deferred debt.

## Per-Change Workflow

1. Read `docs/index.md` and the relevant detailed docs.
2. Explore the current system before proposing edits.
3. Create the plan file in `docs/plans/active/`.
4. Record the change description, expected behavior, hypotheses, and validation
   approach.
5. Write failing tests for observable behavior before code when executable
   behavior is changing.
6. Implement the smallest root-cause fix that satisfies the plan.
7. Add or improve observability if the change affects diagnosis or operations.
8. Run the relevant automated checks and direct behavior validation.
9. Promote durable findings into `AGENTS.md` or the right doc under `docs/`.
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
