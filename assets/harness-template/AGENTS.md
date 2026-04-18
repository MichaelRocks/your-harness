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
5. If the task adds or changes functionality, categorize it before
   implementation:
   - Small: a brief plan in chat, approval, then implementation
   - Medium: one saved plan file, approval, then implementation
   - Large: an overview plus one file per phase, approval, then phased
     implementation unless the whole plan is explicitly approved

## Non-Negotiables

- Categorize functionality changes as small, medium, or large before
  implementation.
- Small changes start with a short plan in chat, then wait for approval before
  implementation.
- Medium changes save one plan file in
  `docs/plans/active/YYYY-MM-DD-short-slug.md`, then wait for approval before
  implementation.
- Large changes save a plan folder in
  `docs/plans/active/YYYY-MM-DD-short-slug/` with `overview.md` plus one file
  per phase, then wait for approval before implementation.
- Ask clarifying questions whenever a plan still has unclear requirements,
  constraints, success criteria, or sequencing.
- Unless the user explicitly approves the whole large change end to end, pause
  after each phase and ask for permission before continuing.
- Incident reports live in `docs/operations/incidents/`, but they do not
  replace the normal small/medium/large change-planning workflow when tracked
  files change.
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
- When the change is complete, move any saved plan file or plan folder to
  `docs/plans/completed/` and capture outcomes plus follow-up debt.

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
3. Categorize the change as small, medium, or large.
4. Ask clarifying questions before finalizing the plan when key details are
   still unclear.
5. Create any required saved plan file or plan folder in `docs/plans/active/`.
6. Record the change description, expected behavior, hypotheses, and validation
   approach.
7. Write failing tests for observable behavior before code when executable
   behavior is changing.
8. Implement the smallest root-cause fix that satisfies the approved plan.
9. Add or improve observability if the change affects diagnosis or operations.
10. Run the relevant automated checks and direct behavior validation.
11. Promote durable findings into `AGENTS.md` or the right doc under `docs/`.
12. Finish any saved plan, capture outcomes and follow-ups, then move it to
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
