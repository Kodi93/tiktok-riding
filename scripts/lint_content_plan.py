#!/usr/bin/env python3
"""Lint planned Zeph Rides content for obvious editorial repetition.

Standard-library only. This is intentionally conservative: it flags planning risks
for human review rather than pretending to predict TikTok performance.
"""

from __future__ import annotations

import csv
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COVER_PLAN = ROOT / "content" / "cover_plan.csv"


def load_rows(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        raise SystemExit(f"Missing required file: {path}")
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def norm(value: str | None) -> str:
    return (value or "").strip().lower()


def main() -> int:
    rows = load_rows(COVER_PLAN)
    if not rows:
        print("FAIL: cover plan is empty")
        return 1

    warnings: list[str] = []
    failures: list[str] = []

    # Required planning fields.
    required = ["asset", "cover_family", "cover_source", "dominant_subject", "status"]
    for index, row in enumerate(rows, start=2):
        missing = [field for field in required if not norm(row.get(field))]
        if missing:
            failures.append(f"row {index}: missing {', '.join(missing)}")

    # No three adjacent covers from the same family.
    for i in range(len(rows) - 2):
        families = [norm(rows[j].get("cover_family")) for j in range(i, i + 3)]
        if families[0] and len(set(families)) == 1:
            failures.append(
                f"rows {i+2}-{i+4}: three adjacent covers use family '{families[0]}'"
            )

    # Any nine-post window should have at least four cover families.
    if len(rows) >= 9:
        for i in range(len(rows) - 8):
            families = {
                norm(row.get("cover_family"))
                for row in rows[i : i + 9]
                if norm(row.get("cover_family"))
            }
            if len(families) < 4:
                failures.append(
                    f"rows {i+2}-{i+10}: only {len(families)} cover families; minimum target is 4"
                )

    # Warn when a dominant subject takes over the plan.
    subjects = [norm(row.get("dominant_subject")) for row in rows if norm(row.get("dominant_subject"))]
    counts = Counter(subjects)
    for subject, count in counts.items():
        if count >= max(4, round(len(rows) * 0.5)):
            warnings.append(
                f"dominant subject '{subject}' appears {count}/{len(rows)} times; review for visual repetition"
            )

    # Explicit adjacent-distinct field must not say NO.
    for index, row in enumerate(rows, start=2):
        if norm(row.get("adjacent_distinct")) == "no":
            failures.append(f"row {index}: adjacent_distinct is NO")

    print(f"Checked {len(rows)} planned covers")

    if warnings:
        print("\nWARNINGS")
        for warning in warnings:
            print(f"- {warning}")

    if failures:
        print("\nFAILURES")
        for failure in failures:
            print(f"- {failure}")
        print("\nRESULT: HOLD — revise the plan before scheduling.")
        return 1

    print("\nRESULT: PASS — no obvious cover-plan repetition violations found.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
