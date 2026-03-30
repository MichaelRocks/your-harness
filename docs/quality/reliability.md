# Reliability

Reliability work should reduce operational surprise and make recovery explicit.

## Focus Areas

- Timeouts, retries, and backoff
- Idempotency and duplicate handling
- Capacity limits, backpressure, and saturation behavior
- Safe rollout, rollback, and recovery paths
- Clear ownership of health signals and runbooks

## Review Questions

- What happens when dependencies are slow, unavailable, or inconsistent?
- What is the user or operator impact of partial failure?
- Can the system recover automatically, and how is that visible?
- Does the change alter load, latency, or failure domains?

## Validation Ideas

- Failure-injection or degraded-dependency tests
- Rollout and rollback drills
- Queue or load behavior checks
- Dashboard and alert review against the changed path
