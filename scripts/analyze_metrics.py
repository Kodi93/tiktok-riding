#!/usr/bin/env python3
"""Small, dependency-free analyzer for analytics/metrics.csv."""

from __future__ import annotations

import argparse
import csv
import statistics
from pathlib import Path


def number(row: dict[str, str], key: str) -> float | None:
    value = (row.get(key) or "").strip()
    if not value:
        return None
    try:
        return float(value)
    except ValueError:
        return None


def pct(value: float | None) -> str:
    return "n/a" if value is None else f"{value:.2f}%"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "csv_path",
        nargs="?",
        default="analytics/metrics.csv",
        help="Path to the metrics CSV",
    )
    args = parser.parse_args()

    path = Path(args.csv_path)
    if not path.exists():
        raise SystemExit(f"Missing metrics file: {path}")

    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))

    view_values = [number(row, "views") for row in rows]
    view_values = [value for value in view_values if value is not None]
    engagement_values = []

    for row in rows:
        views = number(row, "views")
        if not views:
            continue
        interactions = sum(
            number(row, field) or 0
            for field in ("likes", "comments", "shares")
        )
        engagement_values.append((interactions / views) * 100)

    print(f"Rows: {len(rows)}")
    if not view_values:
        print("No numeric view data yet.")
        return

    print(f"Posts with views: {len(view_values)}")
    print(f"Total views: {sum(view_values):.0f}")
    print(f"Average views: {statistics.mean(view_values):.1f}")
    print(f"Median views: {statistics.median(view_values):.1f}")

    if engagement_values:
        print(
            "Average visible engagement rate: "
            f"{statistics.mean(engagement_values):.2f}%"
        )

    ranked = sorted(
        (
            (number(row, "views") or 0, row.get("asset") or row.get("post_id") or "unknown")
            for row in rows
        ),
        reverse=True,
    )
    print("Top posts by recorded views:")
    for views, asset in ranked[:5]:
        print(f"- {asset}: {views:.0f}")

    if len(view_values) < 8:
        print("Warning: sample is small; use the result directionally only.")


if __name__ == "__main__":
    main()
