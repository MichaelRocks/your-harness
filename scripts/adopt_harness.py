#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from shared.adopt_harness import AdoptHarnessOptions, adopt_harness


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Add the your-harness scaffold to an existing repository."
    )
    parser.add_argument("--target", required=True, help="Target repository path")
    parser.add_argument("--project-name", help="Optional display name")
    parser.add_argument("--product-description", help="Optional project description")
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Copy missing files and create the adoption plan. Omit for dry-run.",
    )
    args = parser.parse_args()

    try:
        result = adopt_harness(
            AdoptHarnessOptions(
                target_dir=Path(args.target),
                template_dir=Path(__file__).resolve().parents[1] / "assets" / "harness-template",
                project_name=args.project_name,
                product_description=args.product_description,
                dry_run=not args.apply,
            )
        )
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 1
    print(result.to_json())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
