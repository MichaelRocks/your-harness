# Observability

Observability should make failures understandable without guesswork.

## Required Mindset

- Treat telemetry as part of the design.
- Add the signals you would want during the next incident while the context is
  fresh.
- Never remove or bypass instrumentation to hide a bug.

## Baseline Expectations

- Structured logs around critical state transitions and failures
- Metrics for throughput, latency, errors, saturation, or domain-specific
  health
- Traces for multi-hop flows where causal debugging matters
- Dashboards or alerts for high-impact behaviors and failure modes

## Design Questions

- How will an operator know this path is healthy?
- How will an engineer identify where it failed?
- Which user or business journey does the signal map to?
- Which failures need immediate alerting versus later diagnosis?

## Validation

- Review logs for clarity and actionable fields.
- Confirm metrics and traces line up with the affected behavior.
- Check that alerts or dashboards would make the issue visible without relying
  on luck.

## Domain Notes

- Backend: instrument requests, jobs, queues, and data stores.
- Frontend: instrument critical user journeys, network failures, rendering
  regressions, and client-side errors.
- Mobile: instrument lifecycle transitions, crashes, background work, network
  behavior, and device-specific failure patterns.
- DevOps: instrument deploys, provisioning, drift, rollout health, latency, and
  saturation.
