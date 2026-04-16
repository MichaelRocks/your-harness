# Backend Playbook

## Common Change Types

- API or RPC behavior
- Background jobs and scheduled tasks
- Data model and persistence behavior
- Event processing and integrations

## Preferred Test Layers

- Start with a failing API, integration, or job-level test that exercises the
  observable contract.
- Add lower-level tests only where they improve diagnosis or cover important
  edge logic.
- Do not replace behavior tests with repository or helper-only tests when the
  actual risk is at the boundary.

## Observability Expectations

- Structured logs for requests, jobs, retries, and failures
- Metrics for throughput, latency, error rate, queue depth, and saturation
- Traces for multi-service or asynchronous flows
- Alerts or dashboards for high-impact endpoints and background pipelines

## Failure Modes and Root-Cause Cues

- Partial writes, duplicate processing, stale reads, timeout cascades, retry
  storms, and schema drift
- Look for ownership confusion at boundaries, missing idempotency, or hidden
  dependency coupling
- Do not hide failures by swallowing exceptions or muting error paths

## Validation Patterns

- Exercise the API or job from the caller side
- Validate persisted state, emitted events, or downstream effects
- Check logs, metrics, and traces for the changed path
- Confirm degraded-path behavior such as retries, timeouts, or validation
  errors
