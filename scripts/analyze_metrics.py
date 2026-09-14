#!/usr/bin/env python3
"""Dependency-free analyzer for analytics/metrics.csv.

The analyzer is descriptive, not predictive. Missing values remain missing, and
small samples are explicitly called out.
"""

from __future__ import annotations

import argparse
import csv
import statistics
from collections import defaultdict
from pathlib import Path


def number(row: dict[str, str], key: str) -> float | None:
    value = (row.get(key) or "").strip().replace(",", "")
    if not value:
        return None
    try:
        return float(value)
    except ValueError:
        return None


def label(row: dict[str, str]) -> str:
    return row.get("asset") or row.get("post_id") or "unknown"


def rate(numerator: float | None, denominator: float | None) -> float | None:
    if numerator is None or denominator in (None, 0):
        return None
    return (numerator / denominator) * 100


def watch_ratio(row: dict[str, str]) -> float | None:
    avg_watch = number(row, "avg_watch_s")
    length = number(row, "length_s")
    return rate(avg_watch, length)


def visible_engagement(row: dict[str, str]) -> float | None:
    views = number(row, "views")
    if not views:
        return None
    observed = [number(row, key) for key in ("likes", "comments", "shares", "saves")]
    values = [value for value in observed if value is not None]
    return rate(sum(values), views) if values else None


def share_rate(row: dict[str, str]) -> float | None:
    return rate(number(row, "shares"), number(row, "views"))


def follow_conversion(row: dict[str, str]) -> float | None:
    return rate(number(row, "new_followers"), number(row, "views"))


def profile_conversion(row: dict[str, str]) -> float | None:
    return rate(number(row, "profile_visits"), number(row, "views"))


def median(values: list[float]) -> float | None:
    return statistics.median(values) if values else None


def print_ranked(rows: list[dict[str, str]], title: str, getter, suffix: str = "") -> None:
    ranked = []
    for row in rows:
        value = getter(row)
        if value is not None:
            ranked.append((value, label(row)))
    if not ranked:
        return
    ranked.sort(reverse=True)
    print(f"\n{title}")
    for value, asset in ranked[:5]:
        print(f"- {asset}: {value:.2f}{suffix}")


def group_summary(rows: list[dict[str, str]], key: str) -> None:
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        value = (row.get(key) or "").strip()
        if value:
            grouped[value].append(row)

    if not grouped:
        return

    print(f"\nBy {key}")
    for group, group_rows in sorted(grouped.items()):
        views = [number(row, "views") for row in group_rows]
        views = [value for value in views if value is not None]
        watch = [watch_ratio(row) for row in group_rows]
        watch = [value for value in watch if value is not None]
        follows = [follow_conversion(row) for row in group_rows]
        follows = [value for value in follows if value is not None]

        parts = [f"n={len(group_rows)}"]
        if views:
            parts.append(f"median views={median(views):.0f}")
        if watch:
            parts.append(f"median watch ratio={median(watch):.1f}%")
        if follows:
            parts.append(f"median follow conversion={median(follows):.2f}%")
        print(f"- {group}: " + ", ".join(parts))


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

    print(f"Rows: {len(rows)}")
    print(f"Rows with numeric views: {len(view_values)}")

    if not view_values:
        print("No numeric view data yet.")
        return

    print(f"Total recorded views: {sum(view_values):.0f}")
    print(f"Average views: {statistics.mean(view_values):.1f}")
    print(f"Median views: {statistics.median(view_values):.1f}")

    engagement_values = [visible_engagement(row) for row in rows]
    engagement_values = [value for value in engagement_values if value is not None]
    if engagement_values:
        print(f"Median visible engagement: {statistics.median(engagement_values):.2f}%")

    watch_values = [watch_ratio(row) for row in rows]
    watch_values = [value for value in watch_values if value is not None]
    if watch_values:
        print(f"Median watch ratio: {statistics.median(watch_values):.1f}%")

    follow_values = [follow_conversion(row) for row in rows]
    follow_values = [value for value in follow_values if value is not None]
    if follow_values:
        print(f"Median follow conversion: {statistics.median(follow_values):.2f}%")

    print_ranked(rows, "Top posts by views", lambda row: number(row, "views"))
    print_ranked(rows, "Top posts by watch ratio", watch_ratio, "%")
    print_ranked(rows, "Top posts by share rate", share_rate, "%")
    print_ranked(rows, "Top posts by profile conversion", profile_conversion, "%")
    print_ranked(rows, "Top posts by follow conversion", follow_conversion, "%")

    group_summary(rows, "format")
    group_summary(rows, "series")
    group_summary(rows, "cover_family")
    group_summary(rows, "hook_type")

    comparable = [row for row in rows if number(row, "views") is not None]
    if len(comparable) < 8:
        print("\nWarning: fewer than eight posts have view data; conclusions are directional only.")

    if not any(number(row, "avg_watch_s") is not None for row in rows):
        print("Note: average watch time is not yet populated; retention diagnosis is limited.")
    if not any(number(row, "profile_visits") is not None for row in rows):
        print("Note: profile visits are not yet populated; profile-conversion diagnosis is limited.")
    if not any(number(row, "new_followers") is not None for row in rows):
        print("Note: attributed followers are not yet populated; follow-conversion diagnosis is limited.")


if __name__ == "__main__":
    main()
