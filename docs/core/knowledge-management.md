# Knowledge Management

Use this document to decide where information should live.

## What To Record During Work

- Hypotheses: what you think may be true before verification
- Findings: confirmed facts discovered during exploration or validation
- Decisions: tradeoffs you intentionally chose
- Ideas: useful follow-ups that are not part of the current change
- Takeaways: lessons that should change future work

Record these first in the active plan so they are not lost.
During incident response, record them in the active incident report instead of
leaving them in chat or memory.

## Promotion Rules

- Put it in `AGENTS.md` if it changes how the agent should approach most tasks
  in the repository.
- Put it in `docs/core/` if it is a repo-wide workflow or policy detail.
- Put it in `docs/architecture/` if it describes boundaries, dependencies,
  topology, ownership, or structure.
- Put it in `docs/specs/` if it defines expected behavior, journeys, contracts,
  or acceptance criteria.
- Put it in `docs/quality/` if it changes testing, observability, reliability,
  or security practice.
- Put it in `docs/operations/` if it is incident history, operator-facing
  recovery guidance, or a runbook that should be available during response.
- Put it in `docs/playbooks/` if it is stack-specific guidance.
- Put it in `docs/decisions/` if it is a durable cross-cutting decision with
  tradeoffs.
- Put it in `docs/plans/tech-debt.md` if it is important but intentionally
  deferred.

## What Should Stay In the Plan or Incident Report

- Temporary investigation trails
- Dead-end hypotheses
- Task-specific implementation notes
- Validation details for a single change or incident
- Work that matters historically but does not change future default behavior

## Update Cadence

- Add hypotheses before implementation starts or as soon as they appear during
  incident response.
- Replace hypotheses with findings as they are confirmed or disproved.
- Record decisions when they are made, not at the end from memory.
- Promote durable takeaways before marking the change complete.
