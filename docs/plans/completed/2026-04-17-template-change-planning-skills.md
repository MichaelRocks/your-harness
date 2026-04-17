# Add Change-Planning Skills and Template Routing

## Change Summary

Add two explicit-use plugin skills under the repository root `skills/`
directory so agents can route implementation requests into a planning-first
workflow. One skill will cover small changes with an inline, unsaved plan plus
user approval. The other will cover medium-to-large changes with a saved plan
file plus user approval. The shipped harness template will not include local
skill copies; instead its docs will point agents toward the new plugin skills
when functionality work begins. Neither skill should implement the plan
immediately.

## Expected Behavior

- The plugin ships two new change-planning skills under the root `skills/`
  directory for small and larger implementation requests.
- The small-change skill tells the agent to prepare a concise plan in chat,
  ask for approval, and avoid saving that plan to disk.
- The medium/large-change skill tells the agent to prepare a fuller plan,
  save it under `docs/plans/active/`, ask for approval, and stop before
  implementation.
- Template docs route maintainers and agents toward the new skills when the
  task is adding or changing functionality.
- Harness bootstrap/adoption flows continue to copy the canonical template
  without trying to ship a separate template-local skill set.

## Hypotheses

- Hypothesis: A small documentation update in the template `README.md`,
  `AGENTS.md`, and docs router/workflow pages will be enough to make the new
  skills discoverable without adding redundant guidance everywhere.
- Hypothesis: existing helper code for create/adopt will not need changes
  because the new functionality lives in plugin skill files plus template docs,
  not in template copy behavior.

## Planned Tests

- Add failing coverage that proves the new plugin skill directories and
  metadata exist in the expected root `skills/` layout.
- Run `python3 -m unittest discover -s tests`.
- Run the skill validator against each new plugin skill.
- Manually review the updated template docs for routing consistency.

## Planned Observability

- No runtime observability changes expected; keep the change legible through
  clear plan notes and test assertions that name the new root skill paths and
  the template docs that reference them.

## Completion Notes

- Added `skills/plan-small-change/` with explicit instructions to inspect
  context, draft a brief plan in chat, ask for approval, and stop without
  saving that draft to disk during the planning step.
- Added `skills/plan-medium-large-change/` with explicit instructions to
  inspect context, save a change plan file, ask for approval, and stop before
  implementation.
- Updated the root `README.md` to advertise the new plugin skills.
- Updated the shipped template `README.md`, `AGENTS.md`, `docs/index.md`, and
  `docs/core/workflow.md` so generated repos route functionality changes into
  the right planning skill.
- Validation run:
  - `python3 -m unittest discover -s tests`
  - `python3 "$HOME/.codex/skills/.system/skill-creator/scripts/quick_validate.py" skills/plan-small-change`
  - `python3 "$HOME/.codex/skills/.system/skill-creator/scripts/quick_validate.py" skills/plan-medium-large-change`
- Outcome: no helper code changes were needed because the work was limited to
  plugin skill packaging plus documentation routing.
- Follow-up debt: none recorded.
