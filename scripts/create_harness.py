#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from shared.create_harness import CreateHarnessOptions, create_harness


def parse_csv(value: str) -> list[str]:
    return [item.strip() for item in value.split(",") if item.strip()]


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Bootstrap an empty repository with the your-harness scaffold."
    )
    parser.add_argument("--target", required=True, help="Target repository path")
    parser.add_argument("--project-name", required=True, help="Product or repo name")
    parser.add_argument(
        "--product-description",
        required=True,
        help="Short description of the product or repository",
    )
    parser.add_argument("--project-slug", help="Optional explicit slug")
    parser.add_argument("--primary-stacks", default="", help="Comma-separated stacks")
    parser.add_argument("--platforms", default="", help="Comma-separated platforms")
    parser.add_argument("--ops-profile", default="standard")
    parser.add_argument("--testing-posture", default="behavior-first")
    parser.add_argument("--emphasis-areas", default="", help="Comma-separated areas")
    args = parser.parse_args()

    try:
        result = create_harness(
            CreateHarnessOptions(
                target_dir=Path(args.target),
                template_dir=Path(__file__).resolve().parents[1] / "assets" / "harness-template",
                project_name=args.project_name,
                product_description=args.product_description,
                project_slug=args.project_slug,
                primary_stacks=parse_csv(args.primary_stacks),
                platforms=parse_csv(args.platforms),
                ops_profile=args.ops_profile,
                testing_posture=args.testing_posture,
                emphasis_areas=parse_csv(args.emphasis_areas),
            )
        )
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 1
    print(result.to_json())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
