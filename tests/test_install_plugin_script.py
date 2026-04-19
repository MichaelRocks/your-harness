import json
import os
import subprocess
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = REPO_ROOT / "scripts" / "install_plugin.sh"


class InstallPluginScriptTests(unittest.TestCase):
    def run_script(self, codex_home: Path) -> subprocess.CompletedProcess[str]:
        env = os.environ.copy()
        env["CODEX_HOME_DIR"] = str(codex_home)
        return subprocess.run(
            ["bash", str(SCRIPT_PATH)],
            cwd=REPO_ROOT,
            env=env,
            text=True,
            capture_output=True,
            check=False,
        )

    def test_installs_plugin_and_creates_marketplace(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            codex_home = Path(tmp) / ".codex"

            result = self.run_script(codex_home)

            self.assertEqual(0, result.returncode, msg=result.stderr)
            plugin_dir = codex_home / "plugins" / "your-harness"
            marketplace_path = codex_home / "plugins" / "marketplace.json"
            self.assertTrue((plugin_dir / ".codex-plugin" / "plugin.json").exists())
            self.assertFalse((plugin_dir / ".git").exists())
            self.assertFalse((plugin_dir / "tests" / "__pycache__").exists())
            payload = json.loads(marketplace_path.read_text())
            self.assertEqual("michaelrocks-plugins", payload["name"])
            self.assertEqual("MichaelRocks Plugins", payload["interface"]["displayName"])
            self.assertEqual(1, len(payload["plugins"]))
            self.assertEqual("your-harness", payload["plugins"][0]["name"])
            self.assertEqual("./your-harness", payload["plugins"][0]["source"]["path"])

    def test_replaces_only_your_harness_in_existing_marketplace(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            codex_home = Path(tmp) / ".codex"
            plugins_dir = codex_home / "plugins"
            plugins_dir.mkdir(parents=True, exist_ok=True)
            marketplace_path = plugins_dir / "marketplace.json"
            marketplace_path.write_text(
                json.dumps(
                    {
                        "name": "custom-marketplace",
                        "interface": {"displayName": "Custom Plugins"},
                        "plugins": [
                            {
                                "name": "other-plugin",
                                "source": {"source": "local", "path": "./other-plugin"},
                                "policy": {
                                    "installation": "AVAILABLE",
                                    "authentication": "ON_INSTALL",
                                },
                                "category": "Coding",
                            },
                            {
                                "name": "your-harness",
                                "source": {"source": "local", "path": "./old-path"},
                                "policy": {
                                    "installation": "NOT_AVAILABLE",
                                    "authentication": "ON_INSTALL",
                                },
                                "category": "Other",
                            },
                        ],
                    },
                    indent=2,
                )
            )

            result = self.run_script(codex_home)

            self.assertEqual(0, result.returncode, msg=result.stderr)
            payload = json.loads(marketplace_path.read_text())
            self.assertEqual("custom-marketplace", payload["name"])
            self.assertEqual("Custom Plugins", payload["interface"]["displayName"])
            self.assertEqual(
                ["other-plugin", "your-harness"],
                [plugin["name"] for plugin in payload["plugins"]],
            )
            your_harness = payload["plugins"][1]
            self.assertEqual("./your-harness", your_harness["source"]["path"])
            self.assertEqual("AVAILABLE", your_harness["policy"]["installation"])
            self.assertEqual("ON_INSTALL", your_harness["policy"]["authentication"])
            self.assertEqual("Coding", your_harness["category"])

    def test_clears_cached_plugin_bundle_for_your_harness(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            codex_home = Path(tmp) / ".codex"
            stale_cache_dir = (
                codex_home
                / "plugins"
                / "cache"
                / "michaelrocks-plugins"
                / "your-harness"
                / "0.0.0"
            )
            stale_cache_dir.mkdir(parents=True, exist_ok=True)
            (stale_cache_dir / "README.md").write_text("stale cache\n")

            result = self.run_script(codex_home)

            self.assertEqual(0, result.returncode, msg=result.stderr)
            self.assertFalse(
                stale_cache_dir.exists(),
                msg="install should remove stale cached plugin bundles",
            )


if __name__ == "__main__":
    unittest.main()
