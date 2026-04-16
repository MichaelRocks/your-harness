# Name repo marketplace MichaelRocks Plugins

## Change Summary

Normalize the repo-local marketplace metadata so this plugin is offered through
the dedicated `MichaelRocks Plugins` marketplace with a matching top-level
slug, and make that marketplace name explicit in the README.

## Expected Behavior

- `.agents/plugins/marketplace.json` advertises the plugin through a
  `MichaelRocks Plugins` marketplace.
- The marketplace root name is a clean normalized slug.
- The README identifies the repo-local marketplace by name.

## Hypotheses / Findings

- Finding: the repo-local marketplace already has the intended display name.
- Finding: the top-level marketplace name is currently misspelled as
  `micahelrocks-plugins`.

## Planned Tests

- Validate `.agents/plugins/marketplace.json` as JSON after the edit.
- Review the updated README wording for consistency.

## Planned Observability

- No new observability; this is metadata and docs cleanup.

## Completion Notes

- Updated `.agents/plugins/marketplace.json` to use the normalized marketplace
  slug `michaelrocks-plugins` while keeping the display name `MichaelRocks Plugins`.
- Updated `README.md` to identify the repo-local marketplace by name.
- Validation:
  - `python3 -m json.tool .agents/plugins/marketplace.json`
