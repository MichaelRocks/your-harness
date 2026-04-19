# Require Detailed Plan Tasks

This ExecPlan is a living document. Keep `Task Checklist`, `Progress`,
`Surprises & Discoveries`, `Decision Log`, and `Outcomes & Retrospective`
current as work proceeds.

## Purpose / Big Picture

Tighten the harness planning contract so every saved plan is task-driven and
detailed enough to execute directly. Medium plans should enumerate explicit
tasks and describe the intended edits in detail. Large plan sets should do the
same both at the roadmap level and inside each phase file. During execution,
completed tasks should be marked done as soon as they finish.

## Scope and Constraints

- Update the maintainer guidance, shipped harness template, and planning skills
  so they all require explicit tasks, detailed change descriptions, and
  in-progress task tracking.
- Update generated saved-plan skeletons created by bootstrap/adoption helpers
  so new projects start from templates that already model this behavior.
- Keep the scaffold canonical in `assets/harness-template/`.
- Do not weaken the existing approval gates for small, medium, or large
  changes.

## Context and Orientation

- `docs/plans/lightweight-template.md` is the current single-file saved-plan
  template used by medium changes and by helper-generated plan files.
- `assets/harness-template/docs/plans/PLANS.md` defines large plan sets but
  only requires a high-level phase sequence and a generic progress section.
- `skills/plan-medium-change/SKILL.md` and
  `skills/plan-large-change/SKILL.md` currently require summaries and
  validation notes, but not explicit task lists or immediate checkbox updates
  during implementation.
- `shared/common.py` writes initial saved-plan files during bootstrap and
  adoption, so it must match the strengthened planning contract.

## Hypotheses / Open Questions

- Hypothesis:
  The contract needs changes in both narrative docs and helper-generated plan
  content; updating only the docs would not guarantee the default behavior in
  new projects.
  Why it matters:
  The user asked to guarantee the behavior in projects, not only in maintainer
  documentation.
  How it will be tested or disproved:
  Inspect scaffolded plan guidance and generated plan files after the edit.

- Hypothesis:
  Requiring a dedicated task checklist plus a progress ledger will make plan
  execution clearer than relying on a free-form progress section alone.
  Why it matters:
  The requested behavior includes both explicit tasks before implementation and
  visible done markers during implementation.
  How it will be tested or disproved:
  Review the updated templates and helper output for concrete, checkable task
  items.

## Task Checklist

- [x] Update the active plan with the concrete files and validation strategy.
- [x] Add failing tests that assert helper-generated saved plans include
  explicit task sections and executable detail.
- [x] Strengthen maintainer planning docs and templates to require explicit
  task lists, detailed change descriptions, and immediate task completion
  tracking.
- [x] Strengthen the shipped harness template docs and plan templates with the
  same contract for generated user projects.
- [x] Update helper-generated saved-plan skeletons and any affected skill
  instructions to match the new contract.
- [x] Run the relevant automated and direct validation.
- [x] Record outcomes, follow-up debt, and move the plan to completed when the
  change is done.

## Progress

- [x] 2026-04-20: Read the maintainer workflow docs, current planning
  templates, shipped scaffold planning docs, relevant skills, and helper code.
- [x] 2026-04-20: Added failing tests for helper-generated saved-plan
  structure in `tests/test_create_harness.py` and
  `tests/test_adopt_harness.py`.
- [x] 2026-04-20: Updated planning docs, template docs, skills, and helper
  output.
- [x] 2026-04-20: Ran validation, recorded outcomes, and prepared to move the
  plan to completed.

## Surprises & Discoveries

- Observation:
  Bootstrap and adoption helpers both create saved plan files through
  `shared/common.py`.
  Evidence:
  `create_harness()` and `adopt_harness()` both call `write_change_plan()`.
  Impact:
  One shared code change can improve default saved-plan structure across both
  flows.

- Observation:
  Exact-string tests for the generated plan intro are sensitive to line wraps
  inside the helper output.
  Evidence:
  The first test run failed even though the sentence content was correct,
  because the helper emitted the sentence across multiple lines.
  Impact:
  The helper now writes the task-tracking instruction as one line so the saved
  plan text is stable and easier to assert directly.

## Decision Log

- Decision:
  Use a full ExecPlan for this change instead of the lightweight template.
  Rationale:
  The update is cross-cutting across maintainer docs, scaffold docs, skills,
  and helper-generated defaults.
  Date/Author:
  2026-04-20 / Codex

- Decision:
  Strengthen both the narrative plan templates and the helper-generated saved
  plan skeletons in the same change.
  Rationale:
  Updating only the docs would not guarantee the stronger plan structure in
  newly bootstrapped or adopted projects.
  Date/Author:
  2026-04-20 / Codex

## Validation

- Automated checks:
  - `python3 -m unittest discover -s tests`
  - `python3 "$HOME/.codex/skills/.system/skill-creator/scripts/quick_validate.py" skills/plan-medium-change`
  - `python3 "$HOME/.codex/skills/.system/skill-creator/scripts/quick_validate.py" skills/plan-large-change`
- Real behavior validation:
  - Inspect the updated saved-plan templates and helper-generated plan files to
    confirm they contain explicit tasks, detailed planned changes, and done
    markers.
- Observability reviewed or added:
  - Kept the live plan updated as tasks completed.

## Knowledge To Promote

- Update the maintainer docs, shipped template docs, and planning skills if the
  strengthened planning contract becomes the default workflow.

## Outcomes & Retrospective

- Strengthened the maintainer docs and the shipped harness template so saved
  medium and large plans now require detailed planned changes, explicit task
  checklists, and immediate task-state updates.
- Updated the large-plan overview contract so even the roadmap layer uses
  explicit tasks rather than phase names alone.
- Updated `shared/common.py`, `shared/create_harness.py`, and
  `shared/adopt_harness.py` so bootstrapped and adopted projects start from
  saved plans that already model the stricter structure.
- Added test coverage for the generated plan skeleton and validated the edited
  planning skills.
- Follow-up debt: none recorded.
