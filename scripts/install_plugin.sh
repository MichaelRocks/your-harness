#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
PLUGIN_NAME="your-harness"
CODEX_HOME_DIR="${CODEX_HOME_DIR:-${HOME}/.codex}"
TARGET_PLUGINS_DIR="${CODEX_HOME_DIR}/plugins"
TARGET_PLUGIN_DIR="${TARGET_PLUGINS_DIR}/${PLUGIN_NAME}"
TARGET_MARKETPLACE_PATH="${TARGET_PLUGINS_DIR}/marketplace.json"
REPO_MARKETPLACE_PATH="${REPO_ROOT}/.agents/plugins/marketplace.json"
CACHE_ROOT="${TARGET_PLUGINS_DIR}/cache"

mkdir -p "${TARGET_PLUGINS_DIR}"

rsync -a --delete \
  --exclude ".git" \
  --exclude "__pycache__/" \
  --exclude ".pytest_cache/" \
  --exclude ".mypy_cache/" \
  --exclude ".ruff_cache/" \
  --exclude ".DS_Store" \
  "${REPO_ROOT}/" "${TARGET_PLUGIN_DIR}/"

if [ -d "${CACHE_ROOT}" ]; then
  while IFS= read -r cache_dir; do
    rm -rf "${cache_dir}"
    printf 'Cleared plugin cache: %s\n' "${cache_dir}"
  done < <(
    find "${CACHE_ROOT}" -mindepth 2 -maxdepth 2 -type d -name "${PLUGIN_NAME}" | sort
  )
fi

REPO_MARKETPLACE_PATH="${REPO_MARKETPLACE_PATH}" \
TARGET_MARKETPLACE_PATH="${TARGET_MARKETPLACE_PATH}" \
PLUGIN_NAME="${PLUGIN_NAME}" \
python3 - <<'PY'
import json
import os
from pathlib import Path

repo_marketplace_path = Path(os.environ["REPO_MARKETPLACE_PATH"])
target_marketplace_path = Path(os.environ["TARGET_MARKETPLACE_PATH"])
plugin_name = os.environ["PLUGIN_NAME"]

repo_payload = json.loads(repo_marketplace_path.read_text())
repo_plugins = repo_payload.get("plugins", [])
source_entry = next(
    (plugin for plugin in repo_plugins if plugin.get("name") == plugin_name),
    None,
)
if source_entry is None:
    raise SystemExit(f"Could not find {plugin_name!r} in {repo_marketplace_path}")

if target_marketplace_path.exists():
    target_payload = json.loads(target_marketplace_path.read_text())
else:
    target_payload = {
        "name": repo_payload.get("name", "local-plugins"),
        "interface": repo_payload.get(
            "interface", {"displayName": "Local Plugins"}
        ),
        "plugins": [],
    }

merged_entry = json.loads(json.dumps(source_entry))
merged_entry["source"]["path"] = f"./{plugin_name}"

target_plugins = list(target_payload.get("plugins", []))
for index, plugin in enumerate(target_plugins):
    if plugin.get("name") == plugin_name:
        target_plugins[index] = merged_entry
        break
else:
    target_plugins.append(merged_entry)

target_payload["plugins"] = target_plugins
target_marketplace_path.write_text(json.dumps(target_payload, indent=2) + "\n")
PY

printf 'Installed plugin: %s\n' "${TARGET_PLUGIN_DIR}"
printf 'Updated marketplace: %s\n' "${TARGET_MARKETPLACE_PATH}"
