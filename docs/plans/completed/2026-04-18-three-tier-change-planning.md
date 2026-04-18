# Three-Tier Change Planning

This ExecPlan is a living document. Keep `Progress`,
`Surprises & Discoveries`, `Decision Log`, and
`Outcomes & Retrospective` current as work proceeds.

## Purpose / Big Picture

Replace the current two-tier planning workflow with a three-tier model for
small, medium, and large functionality changes. The plugin skills and shipped
template should agree on how changes are categorized, when clarifying
questions are required, how plans are saved, and when implementation pauses
for approval or phase gates.

## Scope and Constraints

- Update the planning skills from two types to three types.
- Keep the template canonical in `assets/harness-template/`.
- Remove direct skill mentions from shipped template files.
- Preserve the repository rule that tracked-file work still uses saved plans
  before code, even if a small change starts with a chat-only approval plan.
- Large changes need durable multi-file planning guidance plus phase-by-phase
  execution pauses unless the user explicitly authorizes full-plan execution.

## Context and Orientation

- `skills/plan-small-change/SKILL.md` currently drafts a chat-only plan and
  stops after approval.
- `skills/plan-medium-large-change/SKILL.md` currently combines medium and
  large work into one saved-plan workflow and stops after approval.
- The shipped template `AGENTS.md`, `README.md`, `docs/index.md`, and
  `docs/core/workflow.md` currently mention the planning skills directly.
- The current plan templates cover a lightweight single-file plan and a full
  single-file ExecPlan, but not a multi-file phased plan model.

## Hypotheses / Open Questions

- Hypothesis:
  A new `plan-large-change` skill plus a narrowed `plan-medium-change` skill
  will be clearer than keeping a combined medium/large skill.
  Why it matters:
  The user explicitly requested three categories and different execution rules.
  How it will be tested or disproved:
  Review the skill set and docs after the edit for clean one-to-one mapping.

- Hypothesis:
  The template docs can describe categorization and expected behavior without
  naming the plugin skills directly.
  Why it matters:
  The shipped scaffold should remain plugin-agnostic at the doc level.
  How it will be tested or disproved:
  Scan template docs to confirm categorization language remains and skill names
  are removed.

- Open Question:
  Decide the exact on-disk layout for the large-change multi-file plan set.
  Why it matters:
  The user requested one high-level phase file plus one file per phase.
  How it will be tested or disproved:
  Confirm the preferred path pattern before finalizing the design.

## Plan of Work

1. Confirm the preferred file layout for large multi-file plans, then finalize
   the design.
2. Implement the new/updated skills and metadata.
3. Update the shipped template docs to describe categorization without naming
   skills directly.
4. Run direct validation and skill validation, then promote durable
   guidance and close the plan.

## Progress

- [x] 2026-04-18: Read maintainer workflow, current planning skills, template
  docs, and plan templates.
- [x] 2026-04-18: Chose a folder-based large-plan layout using
  `docs/plans/active/YYYY-MM-DD-short-slug/overview.md` plus one file per
  phase.
- [x] 2026-04-18: Replaced the two-tier planning skills with small, medium,
  and large workflows.
- [x] 2026-04-18: Updated the shipped template to describe categorization
  directly without naming skills.
- [x] 2026-04-18: Ran direct validation and closed the plan.

## Surprises & Discoveries

- Observation:
  The shipped template currently names `$plan-small-change` and
  `$plan-medium-large-change` directly in multiple files.
  Evidence:
  `assets/harness-template/AGENTS.md`, `README.md`, `docs/index.md`, and
  `docs/core/workflow.md`.
  Impact:
  The change needs both skill edits and a template-doc wording pass.

- Observation:
  The new medium and large skill descriptions initially failed validation
  because their YAML frontmatter descriptions contained unquoted colons.
  Evidence:
  `quick_validate.py` reported `Invalid YAML in frontmatter` for both skills.
  Impact:
  The descriptions needed quoting before final validation could pass.

## Decision Log

- Decision:
  Use a full ExecPlan for this work.
  Rationale:
  The change is cross-cutting and changes default workflow expectations across
  skills and generated docs.
  Date/Author:
  2026-04-18 / Codex

- Decision:
  Represent large change plans as folders under `docs/plans/active/` with an
  `overview.md` file plus one file per phase.
  Rationale:
  That layout cleanly matches the requested overview-plus-phases model and is
  easier to move intact to `docs/plans/completed/`.
  Date/Author:
  2026-04-18 / Codex

## Validation

- Real behavior validation:
  - Confirmed the template no longer names planning skills directly.
  - Confirmed the template now describes small, medium, and large categories,
    including clarifying-question behavior and the large-change phased layout.
  - Validated `skills/plan-small-change`,
    `skills/plan-medium-change`, and `skills/plan-large-change` with
    `quick_validate.py`.
- Observability reviewed or added:
  Keep the plan updated with scope, decisions, and validation evidence.

## Knowledge To Promote

- Update the relevant skill instructions and shipped template docs if the new
  categorization becomes the default workflow.

## Outcomes & Retrospective

- Replaced `plan-medium-large-change` with separate
  `plan-medium-change` and `plan-large-change` skills, and updated
  `plan-small-change` so all three skills now clarify when needed, plan using
  the repository's categorization, wait for approval, and then implement.
- Updated the shipped template docs to describe the three categories directly
  instead of naming skills.
- Updated the shipped plan guidance so medium changes use one saved plan file
  and large changes use a saved folder containing `overview.md` plus one file
  per phase.
- Validation run:
  - `python3 "$HOME/.codex/skills/.system/skill-creator/scripts/quick_validate.py" skills/plan-small-change`
  - `python3 "$HOME/.codex/skills/.system/skill-creator/scripts/quick_validate.py" skills/plan-medium-change`
  - `python3 "$HOME/.codex/skills/.system/skill-creator/scripts/quick_validate.py" skills/plan-large-change`
- Follow-up debt: none recorded.
