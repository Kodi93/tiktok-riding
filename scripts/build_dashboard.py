#!/usr/bin/env python3
"""Build a dependency-free HTML/SVG TikTok progress dashboard."""

from __future__ import annotations

import argparse
import csv
import html
import statistics
from pathlib import Path


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def number(value: str) -> float | None:
    try:
        cleaned = value.strip().replace(",", "")
        return float(cleaned) if cleaned else None
    except (AttributeError, ValueError):
        return None


def fmt(value: float | int | None) -> str:
    if value is None:
        return "—"
    if isinstance(value, float) and value.is_integer():
        value = int(value)
    return f"{value:,}"


def build_chart(rows: list[dict[str, str]]) -> str:
    points = []
    for row in rows:
        views = number(row.get("views", ""))
        if views is not None:
            label = row.get("asset_id") or row.get("post_id") or "post"
            points.append((label, views))

    if not points:
        return '<p class="empty">No numeric views recorded yet.</p>'

    width = 920
    row_height = 38
    height = max(96, len(points) * row_height + 32)
    maximum = max(view for _, view in points) or 1
    bars = []
    for index, (label, views) in enumerate(points):
        y = 16 + index * row_height
        bar_width = round((views / maximum) * 660)
        safe_label = html.escape(label)
        bars.append(
            f'<text x="8" y="{y + 16}" class="label">{safe_label}</text>'
            f'<rect x="190" y="{y}" width="{bar_width}" height="22" rx="5" class="bar"/>'
            f'<text x="{200 + bar_width}" y="{y + 16}" class="value">{fmt(views)}</text>'
        )

    return (
        f'<svg viewBox="0 0 {width} {height}" role="img" '
        'aria-label="Recorded views by TikTok asset">'
        + "".join(bars)
        + "</svg>"
    )


def render(rows: list[dict[str, str]]) -> str:
    view_values = [value for row in rows if (value := number(row.get("views", ""))) is not None]
    engagement_values = [
        value
        for row in rows
        if (value := number(row.get("visible_engagement_rate", ""))) is not None
    ]
    total_views = sum(view_values)
    median_views = statistics.median(view_values) if view_values else None
    average_engagement = (
        statistics.mean(engagement_values) if engagement_values else None
    )

    cards = [
        ("Rows", fmt(len(rows))),
        ("Posts with views", fmt(len(view_values))),
        ("Total views", fmt(total_views)),
        ("Median views", fmt(median_views)),
        (
            "Avg. visible engagement",
            f"{average_engagement:.2f}%"
            if average_engagement is not None
            else "—",
        ),
    ]
    card_html = "".join(
        f'<div class="card"><span>{html.escape(label)}</span><strong>{value}</strong></div>'
        for label, value in cards
    )

    table_rows = []
    for row in rows:
        views = number(row.get("views", ""))
        engagement = number(row.get("visible_engagement_rate", ""))
        table_rows.append(
            "<tr>"
            f"<td>{html.escape(row.get('asset_id', ''))}</td>"
            f"<td>{html.escape(row.get('posted_at', ''))}</td>"
            f"<td>{fmt(views)}</td>"
            f"<td>{f'{engagement:.2f}% ' if engagement is not None else '—'}</td>"
            f"<td>{html.escape(row.get('notes', ''))}</td>"
            "</tr>"
        )

    table = (
        "<table><thead><tr><th>Asset</th><th>Posted</th><th>Views</th>"
        "<th>Visible engagement</th><th>Notes</th></tr></thead><tbody>"
        + "".join(table_rows)
        + "</tbody></table>"
        if table_rows
        else '<p class="empty">Add a row to analytics/metrics.csv to begin tracking.</p>'
    )

    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Zeph Rides TikTok progress</title>
<style>
:root {{ color-scheme: dark; font-family: Inter, ui-sans-serif, system-ui, sans-serif; }}
body {{ margin: 0; background: #10131a; color: #edf2f7; }}
main {{ max-width: 1100px; margin: 0 auto; padding: 32px 20px 56px; }}
h1 {{ margin-bottom: 6px; }}
p {{ color: #aab5c4; }}
.cards {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 12px; margin: 24px 0; }}
.card {{ background: #1b2230; border: 1px solid #2e3a4d; border-radius: 12px; padding: 16px; }}
.card span {{ display: block; color: #aab5c4; font-size: 0.85rem; }}
.card strong {{ display: block; margin-top: 6px; font-size: 1.45rem; }}
section {{ background: #151b26; border: 1px solid #2e3a4d; border-radius: 12px; padding: 18px; margin-top: 18px; overflow-x: auto; }}
svg {{ width: 100%; min-height: 96px; }}
.label, .value {{ fill: #edf2f7; font-size: 13px; dominant-baseline: middle; }}
.bar {{ fill: #25d0a5; }}
table {{ border-collapse: collapse; width: 100%; min-width: 680px; }}
th, td {{ border-bottom: 1px solid #2e3a4d; text-align: left; padding: 10px 8px; vertical-align: top; }}
th {{ color: #aab5c4; font-size: 0.82rem; text-transform: uppercase; letter-spacing: .04em; }}
.empty {{ padding: 18px 0; }}
code {{ color: #8de8cf; }}
</style>
</head>
<body>
<main>
<h1>Zeph Rides TikTok progress</h1>
<p>Descriptive snapshot generated from <code>analytics/metrics.csv</code>; blank metrics stay blank.</p>
<div class="cards">{card_html}</div>
<section><h2>Recorded views</h2>{build_chart(rows)}</section>
<section><h2>Metric log</h2>{table}</section>
</main>
</body>
</html>
"""


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "input",
        nargs="?",
        type=Path,
        default=Path("analytics/metrics.csv"),
        help="CSV metrics file (default: analytics/metrics.csv)",
    )
    parser.add_argument(
        "output",
        nargs="?",
        type=Path,
        default=Path("analytics/dashboard.html"),
        help="HTML output path (default: analytics/dashboard.html)",
    )
    args = parser.parse_args()

    rows = read_rows(args.input)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(render(rows), encoding="utf-8")
    print(f"Wrote {args.output} from {args.input} ({len(rows)} rows)")


if __name__ == "__main__":
    main()
