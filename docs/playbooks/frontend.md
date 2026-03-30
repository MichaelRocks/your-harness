# Frontend Playbook

## Common Change Types

- User flows and interaction changes
- Rendering, state, and data-fetch behavior
- Accessibility and input handling
- Performance-sensitive views and asset loading

## Preferred Test Layers

- Start with a failing user-journey or contract test that exercises what the
  user can actually observe.
- Add component or utility tests only when they support diagnosis or stabilize
  important logic.
- Do not swap an end-user behavior test for implementation-detail assertions.

## Observability Expectations

- Client-side error reporting with actionable context
- Journey metrics for key funnels and latency-sensitive interactions
- Network and API failure visibility
- Signals for rendering regressions, accessibility failures, or broken assets

## Failure Modes and Root-Cause Cues

- State desynchronization, race conditions, inaccessible interactions, cache
  invalidation issues, and silent client-side failures
- Look for boundary confusion between UI state, server state, and derived view
  state
- Do not hide bugs by removing UI states that expose the underlying problem

## Validation Patterns

- Exercise the relevant user flow end to end
- Validate visible content, interaction affordances, and accessibility behavior
- Check error reporting and client telemetry for the changed path
- Confirm degraded behavior for slow networks, failed requests, and reloads
