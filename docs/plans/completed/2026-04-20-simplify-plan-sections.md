# Simplify Plan Sections

This ExecPlan is a living document. Keep `Task Checklist`,
`Surprises & Discoveries`, `Decision Log`, and `Outcomes & Retrospective`
current as work proceeds.

## Purpose / Big Picture

Remove redundant plan sections from the harness contract. Saved plans should
use `Task Checklist` as the single execution tracker, and `Planned Changes`
should become a quick summary of the intended edits instead of a second
detailed task list. The result should be easier to read and less repetitive
without weakening the requirement for explicit task tracking.

## Scope and Constraints

- Update the maintainer docs, shipped template docs, planning skills, helper
  output, and tests to remove the standalone `Progress` section from the
  required plan shape.
- Rename `Planned Changes In Detail` to `Planned Changes` and rewrite its
  guidance so it is explicitly a concise high-level summary.
- Keep `Task Checklist` as the place for detailed, executable tasks and done
  markers.
- Preserve the existing saved-plan approval and validation expectations.

## Context and Orientation

- The current templates require both `Planned Changes In Detail` and
  `Task Checklist`, which duplicates implementation detail in two different
  forms.
- The helper-generated saved plan in `shared/common.py` also emits a separate
  `## Progress` section even though task state is already tracked in
  `## Task Checklist`.
- The recently added tests in `tests/test_create_harness.py` and
  `tests/test_adopt_harness.py` assert the now-redundant section names, so
  they need to move first as failing tests.

## Hypotheses / Open Questions

- Hypothesis:
  Folding execution updates into `Task Checklist` and `Completion Notes` will
  make plans easier to maintain than keeping a standalone `Progress` section.
  Why it matters:
  The user explicitly called out the overlap between task tracking and
  progress tracking.
  How it will be tested or disproved:
  Review the updated templates and generated plan output for a single clear
  execution-tracking location.

- Hypothesis:
  A concise `Planned Changes` summary will still provide enough top-level
  orientation once the detailed steps live only in `Task Checklist`.
  Why it matters:
  The user wants quick readability without duplicating the task list.
  How it will be tested or disproved:
  Inspect the final templates and helper-generated plans for clear separation
  between summary and execution detail.

## Task Checklist

- [x] Save the live plan with the new section contract and validation scope.
- [x] Add failing tests that reflect the simplified helper-generated plan
  structure.
- [x] Update maintainer planning docs and templates to remove `Progress` and
  redefine `Planned Changes` as a concise summary.
- [x] Update shipped harness template docs and plan templates with the same
  section model.
- [x] Update helper-generated plan skeletons and planning skill instructions to
  match the new section model.
- [x] Run automated validation and direct output checks.
- [x] Record outcomes and move the plan to completed.

## Surprises & Discoveries

- Observation:
  The previous contract change made the helper-generated saved-plan structure
  directly testable, which makes this follow-up simpler to validate.
  Evidence:
  `tests/test_create_harness.py` and `tests/test_adopt_harness.py` already read
  the generated plan text directly.
  Impact:
  The section-shape change can be locked down with targeted test edits first.

- Observation:
  The helper-generated plan structure was the only executable surface that
  still enforced the old `Progress` section directly.
  Evidence:
  After updating the tests first, only `shared/common.py` needed structural
  output changes for generated plans.
  Impact:
  The implementation remained small even though the wording change touched many
  docs and skill prompts.

## Decision Log

- Decision:
  Use a full ExecPlan again for this follow-up.
  Rationale:
  The change still spans maintainer docs, scaffold docs, skills, helper output,
  and tests even though the requested behavior is narrower.
  Date/Author:
  2026-04-20 / Codex

## Validation

- Automated checks:
  - `python3 -m unittest discover -s tests`
  - `python3 "$HOME/.codex/skills/.system/skill-creator/scripts/quick_validate.py" skills/plan-medium-change`
  - `python3 "$HOME/.codex/skills/.system/skill-creator/scripts/quick_validate.py" skills/plan-large-change`
- Real behavior validation:
  - Inspect the updated templates and helper-generated plan files to confirm
    they use `Planned Changes` for summary and `Task Checklist` for the
    detailed executable work.
- Observability reviewed or added:
  - Kept the live plan current while the section contract changed.

## Knowledge To Promote

- Update the maintainer docs, shipped template docs, and planning skills if the
  simplified section model becomes the new default workflow.

## Outcomes & Retrospective

- Removed the standalone `Progress` section from the maintainer templates, the
  shipped harness template, and helper-generated saved plans.
- Renamed `Planned Changes In Detail` to `Planned Changes` and rewrote the
  guidance so the section is now explicitly a quick summary instead of a second
  detailed task list.
- Kept `Task Checklist` as the single detailed execution tracker across medium
  and large plan workflows, including large-change overview roadmaps.
- Updated the helper-generated saved-plan assertions and validated the edited
  planning skills.
- Follow-up debt: none recorded.
