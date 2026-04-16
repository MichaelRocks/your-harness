# Fix plugin activation metadata

## Change Summary

Adjust the root-level `your-harness` plugin metadata to match the shape of
plugins that Codex already installs successfully. The goal is to eliminate the
activation error that occurs after the plugin appears in the list.

## Expected Behavior

- The plugin keeps appearing in the Codex plugin list after selection.
- Codex can activate the plugin without immediately removing it from the active
  bundle.
- The repo root contains the UI metadata and assets expected by Codex's plugin
  installer.

## Hypotheses / Findings

- Finding: built-in plugins that Codex installs successfully all have a root
  `assets/` directory and icon paths in plugin metadata.
- Finding: built-in plugin manifests consistently include root-level interface
  URLs and icon fields that `your-harness` currently lacks.
- Hypothesis: bringing `your-harness` into line with that metadata shape will
  prevent the installer from rejecting it.

## Planned Tests

- Validate `.codex-plugin/plugin.json` after the metadata update.
- Re-sync the plugin into the installed copies.
- Confirm the plugin remains present after another activation attempt.

## Planned Observability

- Use Codex's on-disk plugin bundle and config state as the activation signal.

## Completion Notes

- Pending implementation.
