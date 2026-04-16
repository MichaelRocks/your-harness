# Create Harness Questionnaire

Use this input frame before running `scripts/create_harness.py`.

## Required

- Project name
- Product description

## Short Follow-ups

- Primary stacks: backend, frontend, mobile, devops, or another short label
- Platforms: web, iOS, Android, backend-only, desktop, or similar
- Operations profile: low, moderate, or high sensitivity
- Testing posture: behavior-first by default unless the repo needs another emphasis
- Areas of emphasis: observability, reliability, security, compliance, performance, accessibility, or none yet

## Defaults

- Missing stacks or platforms stay `TBD`
- Missing operations profile defaults to `standard`
- Missing testing posture defaults to `behavior-first`
- Missing emphasis areas become `None yet`
