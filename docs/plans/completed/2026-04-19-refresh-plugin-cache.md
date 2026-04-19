# Refresh stale plugin cache

## Change Summary

Fix local plugin installation so Codex does not keep serving a stale cached
bundle after plugin skills or metadata change. The scope is the install flow
and its regression tests, plus any version metadata needed to force a refresh
of already-cached plugin bundles.

## Expected Behavior

- Reinstalling `your-harness` refreshes or invalidates Codex's cached plugin
  bundle for this plugin.
- Newly added skills become discoverable after reinstall instead of being
  hidden behind an old cached snapshot.
- The shipped plugin version reflects the new bundle revision.

## Hypotheses / Findings

- Finding: Codex is loading `/Users/mr/.codex/plugins/cache/michaelrocks-plugins/your-harness/0.1.0/`,
  which still contains only the original two skills.
- Finding: `scripts/install_plugin.sh` updates `~/.codex/plugins/your-harness`
  and `marketplace.json` but does not clear the plugin cache.
- Hypothesis: clearing the cached plugin bundle during install and bumping the
  plugin version will make the new planning skills discoverable.

## Planned Tests

- Add a failing regression test showing that install leaves a stale cached
  plugin bundle behind today.
- Run `python3 -m unittest tests.test_install_plugin_script`.
- Run `python3 -m unittest discover -s tests`.
- Real behavior validation: inspect the installed plugin cache paths after
  reinstall and confirm the stale bundle is removed.

## Planned Observability

- Use the on-disk installed plugin directory and cache directory as the direct
  behavior signal for this workflow.

## Completion Notes

- Added a regression test covering stale cached plugin bundles left under
  `~/.codex/plugins/cache/*/your-harness/`.
- Updated `scripts/install_plugin.sh` to remove cached `your-harness` plugin
  bundles during reinstall and print each cleared cache path.
- Bumped `.codex-plugin/plugin.json` from `0.1.0` to `0.1.1` so the updated
  bundle revision is explicit.
- Validation:
  - `python3 -m unittest tests.test_install_plugin_script`
  - `python3 -m unittest discover -s tests`
  - `bash scripts/install_plugin.sh`
  - Confirmed the installer removed
    `/Users/mr/.codex/plugins/cache/michaelrocks-plugins/your-harness`
    and refreshed `/Users/mr/.codex/plugins/your-harness/.codex-plugin/plugin.json`
    to version `0.1.1`.
- Follow-up debt: Codex may still need an app restart before the current UI
  session reloads the refreshed plugin skill catalog.
