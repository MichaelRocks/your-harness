# Add plugin install shell script

## Change Summary

Add a shell script that installs `your-harness` into the local Codex plugin
directory by copying the current repository into `~/.codex/plugins/your-harness`
without `.git` and other generated junk, and by merging the repo-local
`your-harness` marketplace entry into `~/.codex/plugins/marketplace.json`.

## Expected Behavior

- Running the script copies the current repository into the target plugin
  directory with cache and VCS junk excluded.
- Running the script creates or updates `~/.codex/plugins/marketplace.json`.
- The target marketplace keeps unrelated plugin entries and replaces only the
  `your-harness` entry from the repo-local marketplace file.

## Hypotheses / Findings

- Finding: the repo-local marketplace file already has the desired
  `./plugins/your-harness` entry shape.
- Hypothesis: the safest implementation is a shell wrapper that uses `rsync`
  for copying and a short Python block for JSON merging.

## Planned Tests

- Add a failing test that runs the install script against a temporary Codex
  home and verifies marketplace creation plus plugin copy.
- Add a failing test that verifies an existing target marketplace keeps other
  plugins while replacing only `your-harness`.
- Run `python3 -m unittest discover -s tests`.

## Planned Observability

- Make the script print the installed plugin path and marketplace path so the
  result is visible without reading the implementation.

## Completion Notes

- Added `scripts/install_plugin.sh` to copy the repo into
  `~/.codex/plugins/your-harness` with VCS and cache junk excluded.
- The script now creates or updates `~/.codex/plugins/marketplace.json` by
  preserving unrelated plugins and replacing only the `your-harness` entry with
  a target-relative `./your-harness` source path.
- Added `tests/test_install_plugin_script.py` with behavior-level coverage for
  fresh install and marketplace merge/update behavior.
- Updated `README.md` with the install command and script behavior.
- Validation:
  - `python3 -m unittest tests.test_install_plugin_script`
  - `python3 -m unittest discover -s tests`
  - Direct install smoke test to `~/.codex` was blocked by sandbox permissions
    in this session.
