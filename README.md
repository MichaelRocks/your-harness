# your-harness

`your-harness` is a local Codex plugin that helps teams standardize a durable
engineering workflow around saved plans, behavior-first validation, root-cause
fixes, and long-lived docs.

It ships two explicit-use skills:

- `create-harness`: bootstrap the harness into an empty repository from a short
  product brief
- `adopt-harness`: add the harness to an existing repository without
  overwriting existing files

## Repo Layout

- `.codex-plugin/plugin.json`: plugin manifest
- `skills/`: skill instructions and UI metadata
- `scripts/`: thin CLIs used by the skills
- `shared/`: shared Python implementation
- `assets/harness-template/`: canonical scaffold copied into user repositories
- `references/`: shared input defaults and conflict policy

## Local Use

This checkout includes repo-local marketplace metadata for `MichaelRocks
Plugins` at [`./.agents/plugins/marketplace.json`](./.agents/plugins/marketplace.json).
That entry points back to the repository root so the plugin can be tested from
this checkout.

To install the plugin into a local Codex home, run:

```bash
bash scripts/install_plugin.sh
```

The script copies the current repository into `~/.codex/plugins/your-harness`
without `.git` and common cache directories, then creates or updates
`~/.codex/plugins/marketplace.json` by replacing only the `your-harness` entry
from the repo-local marketplace file.

Skill helpers are simple Python CLIs:

```bash
python3 scripts/create_harness.py \
  --target /path/to/empty-repo \
  --project-name "Acme Radar" \
  --product-description "Track product signals and incident risk." \
  --primary-stacks backend,frontend \
  --platforms web \
  --ops-profile moderate \
  --testing-posture behavior-first \
  --emphasis-areas observability
```

```bash
python3 scripts/adopt_harness.py \
  --target /path/to/existing-repo
```

Use `--apply` with `scripts/adopt_harness.py` to copy missing files after
reviewing the dry-run conflict report.

## Maintenance

- Update `assets/harness-template/` when the shipped scaffold changes.
- Keep skill instructions, shared references, and Python helpers aligned.
- Run `python3 -m unittest discover -s tests` after helper changes.
- Run the skill validator against each skill after editing `SKILL.md` or
  `agents/openai.yaml`.
