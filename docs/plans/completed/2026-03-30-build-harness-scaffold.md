# Build reusable Harness-style docs scaffold

This ExecPlan is a living document. Keep `Progress`, `Surprises & Discoveries`,
`Decision Log`, and `Outcomes & Retrospective` current as work proceeds. This
plan follows `docs/plans/PLANS.md`, which is being introduced as part of this
same change.

## Purpose / Big Picture

Create a reusable, copy-paste-friendly repository scaffold centered on a short
root `AGENTS.md` and a structured `docs/` tree. The result should make it easy
for an agent to plan changes before coding, write behavior-first tests, prefer
root-cause fixes, improve observability, and keep durable knowledge in the
right documents.

## Progress

- [x] (2026-03-30 18:58Z) Create the initial ExecPlan for this change before
      editing the rest of the scaffold.
- [x] (2026-03-30 19:07Z) Write the root `AGENTS.md` and the `docs/index.md`
      router.
- [x] (2026-03-30 19:07Z) Add core workflow, principle,
      knowledge-management, and enforcement docs.
- [x] (2026-03-30 19:07Z) Add planning templates and policy docs under
      `docs/plans/`.
- [x] (2026-03-30 19:07Z) Add architecture, specs, quality, decisions,
      references, generated, and stack playbook docs.
- [x] (2026-03-30 19:10Z) Validate link targets, policy coverage, and
      `AGENTS.md` size.
- [x] (2026-03-30 19:12Z) Record outcomes and archive the plan to
      `docs/plans/completed/`.

## Surprises & Discoveries

- Observation: The repository started empty except for `.git`, so the scaffold
  has to provide templates and conventions rather than repo-specific content.
  Evidence: `find . -maxdepth 2 -type f` returned only `.git` internals.

- Observation: Simple path extraction checks need to ignore template placeholder
  names such as `YYYY-MM-DD-short-slug.md`, otherwise the validation step
  reports expected examples as missing files.
  Evidence: the first reference scan flagged template examples until the check
  excluded placeholder names.

## Decision Log

- Decision: Keep durable knowledge under `docs/` and leave only `AGENTS.md` at
  the repo root.
  Rationale: This matches the requested copy-paste-friendly layout while still
  keeping `AGENTS.md` small and usable as a routing layer.
  Date/Author: 2026-03-30 / Codex

- Decision: Use a two-tier planning model where every change creates a saved
  plan file before code, with lightweight and full-plan variants.
  Rationale: It satisfies the "always save a description and a plan" rule
  without forcing a heavy process for trivial edits.
  Date/Author: 2026-03-30 / Codex

- Decision: Keep stack playbooks parallel in structure rather than optimizing
  each one for its domain-specific vocabulary.
  Rationale: Consistent headings make the scaffold easier to copy between repos
  and reduce the cost of orienting an agent in a new codebase.
  Date/Author: 2026-03-30 / Codex

## Outcomes & Retrospective

Completed a reusable harness scaffold with a compact root `AGENTS.md`, a
`docs/index.md` router, repo-wide workflow and principle docs, planning
templates, quality guidance, architecture/spec templates, decision records, and
parallel backend/frontend/mobile/devops playbooks. Added marker docs in
`docs/plans/active/` and `docs/plans/completed/` so both workflow folders stay
present in fresh copies of the scaffold.

Validation completed with:

- a file-structure review via `find . -maxdepth 4 -type f | sort`
- an `AGENTS.md` size check via `wc -l AGENTS.md`, which returned 105 lines
- a reference scan over `AGENTS.md` and `docs/` that confirmed all actual
  `docs/*.md` targets exist after excluding placeholder example paths
- a policy coverage scan for the core requirements around planning, testing,
  root-cause fixes, observability, and living plans

No unresolved blockers were found. Follow-up work, if desired later, is to add
actual CI or lint automation for the policies described in
`docs/core/enforcement.md`.

## Context and Orientation

The scaffold is based on OpenAI's Harness engineering guidance, the cookbook
guidance for living ExecPlans, and the wider `AGENTS.md` convention. This repo
is intentionally empty, so every document should read as a reusable template or
policy rather than a product-specific manual.

## Plan of Work

1. Create the routing layer in `AGENTS.md` and `docs/index.md`.
2. Write repo-wide principles and workflow rules under `docs/core/`.
3. Write planning templates and change-record rules under `docs/plans/`.
4. Add reusable templates/guidance for architecture, specs, quality,
   decisions, references, generated artifacts, and stack playbooks.
5. Validate the resulting scaffold with simple mechanical checks and a manual
   navigation pass.

## Validation

- Confirmed all referenced concrete docs exist.
- Confirmed `AGENTS.md` stays within the intended compact size at 105 lines.
- Confirmed the non-negotiables appear in both the routing layer and the
  detailed docs where appropriate.
