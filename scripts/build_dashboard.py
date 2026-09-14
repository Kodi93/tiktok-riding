#!/usr/bin/env python3
"""Build a dependency-free HTML/SVG Zeph Rides progress dashboard."""

from __future__ import annotations

import argparse
import csv
import html
import statistics
from pathlib import Path


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def number(value: str | None) -> float | None:
    try:
        cleaned = value.strip().replace(",", "") if value is not None else ""
        return float(cleaned) if cleaned else None
    except (AttributeError, ValueError):
        return None


def metric(row: dict[str, str], name: str) -> float | None:
    return number(row.get(name))


def label_for(row: dict[str, str]) -> str:
    return row.get("asset") or row.get("post_id") or "post"


def date_for(row: dict[str, str]) -> str:
    return row.get("observed_at") or row.get("posted_at") or ""


def rate(numerator: float | None, denominator: float | None) -> float | None:
    if numerator is None or denominator in (None, 0):
        return None
    return (numerator / denominator) * 100


def watch_ratio(row: dict[str, str]) -> float | None:
    return rate(metric(row, "avg_watch_s"), metric(row, "length_s"))


def visible_engagement_rate(row: dict[str, str]) -> float | None:
    views = metric(row, "views")
    if not views:
        return None
    values = [metric(row, field) for field in ("likes", "comments", "shares", "saves")]
    observed = [value for value in values if value is not None]
    return rate(sum(observed), views) if observed else None


def follow_conversion(row: dict[str, str]) -> float | None:
    return rate(metric(row, "new_followers"), metric(row, "views"))


def profile_conversion(row: dict[str, str]) -> float | None:
    return rate(metric(row, "profile_visits"), metric(row, "views"))


def median_present(values: list[float | None]) -> float | None:
    present = [value for value in values if value is not None]
    return statistics.median(present) if present else None


def fmt(value: float | int | None, decimals: int = 0) -> str:
    if value is None:
        return "—"
    return f"{value:,.{decimals}f}"


def pct(value: float | None) -> str:
    return "—" if value is None else f"{value:.2f}%"


def build_chart(rows: list[dict[str, str]]) -> str:
    points = [(label_for(row), metric(row, "views")) for row in rows]
    points = [(label, views) for label, views in points if views is not None]
    if not points:
        return '<p class="empty">No numeric views recorded yet.</p>'

    width = 980
    row_height = 38
    height = max(96, len(points) * row_height + 32)
    maximum = max(view for _, view in points) or 1
    bars: list[str] = []

    for index, (label, views) in enumerate(points):
        y = 16 + index * row_height
        bar_width = max(1, round((views / maximum) * 650))
        bars.append(
            f'<text x="8" y="{y + 16}" class="label">{html.escape(label[:28])}</text>'
            f'<rect x="220" y="{y}" width="{bar_width}" height="22" rx="5" class="bar"/>'
            f'<text x="{230 + bar_width}" y="{y + 16}" class="value">{fmt(views)}</text>'
        )

    return (
        f'<svg viewBox="0 0 {width} {height}" role="img" aria-label="Recorded views by TikTok asset">'
        + "".join(bars)
        + "</svg>"
    )


def render(rows: list[dict[str, str]]) -> str:
    views = [metric(row, "views") for row in rows]
    present_views = [value for value in views if value is not None]

    cards = [
        ("Rows", str(len(rows))),
        ("Posts with views", str(len(present_views))),
        ("Total views", fmt(sum(present_views) if present_views else 0)),
        ("Median views", fmt(median_present(views))),
        ("Median watch ratio", pct(median_present([watch_ratio(row) for row in rows]))),
        ("Median engagement", pct(median_present([visible_engagement_rate(row) for row in rows]))),
        ("Median follow conversion", pct(median_present([follow_conversion(row) for row in rows]))),
    ]

    card_html = "".join(
        f'<div class="card"><span>{html.escape(name)}</span><strong>{value}</strong></div>'
        for name, value in cards
    )

    table_rows: list[str] = []
    for row in rows:
        table_rows.append(
            "<tr>"
            f"<td>{html.escape(label_for(row))}</td>"
            f"<td>{html.escape(date_for(row))}</td>"
            f"<td>{html.escape(row.get('series', ''))}</td>"
            f"<td>{html.escape(row.get('cover_family', ''))}</td>"
            f"<td>{fmt(metric(row, 'views'))}</td>"
            f"<td>{pct(watch_ratio(row))}</td>"
            f"<td>{fmt(metric(row, 'shares'))}</td>"
            f"<td>{fmt(metric(row, 'profile_visits'))}</td>"
            f"<td>{fmt(metric(row, 'new_followers'))}</td>"
            f"<td>{pct(profile_conversion(row))}</td>"
            f"<td>{pct(follow_conversion(row))}</td>"
            f"<td>{html.escape(row.get('experiment_id', ''))}</td>"
            f"<td>{html.escape(row.get('notes', ''))}</td>"
            "</tr>"
        )

    table = (
        "<table><thead><tr>"
        "<th>Asset</th><th>Date</th><th>Series</th><th>Cover</th><th>Views</th>"
        "<th>Watch ratio</th><th>Shares</th><th>Profile visits</th><th>Follows</th>"
        "<th>Profile conv.</th><th>Follow conv.</th><th>Experiment</th><th>Notes</th>"
        "</tr></thead><tbody>"
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
<title>Zeph Rides creator dashboard</title>
<style>
:root {{ color-scheme: dark; font-family: Inter, ui-sans-serif, system-ui, sans-serif; }}
body {{ margin: 0; background: #10131a; color: #edf2f7; }}
main {{ max-width: 1280px; margin: 0 auto; padding: 32px 20px 56px; }}
h1 {{ margin-bottom: 6px; }}
p {{ color: #aab5c4; }}
.cards {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(170px, 1fr)); gap: 12px; margin: 24px 0; }}
.card {{ background: #1b2230; border: 1px solid #2e3a4d; border-radius: 12px; padding: 16px; }}
.card span {{ display: block; color: #aab5c4; font-size: 0.85rem; }}
.card strong {{ display: block; margin-top: 6px; font-size: 1.45rem; }}
section {{ background: #151b26; border: 1px solid #2e3a4d; border-radius: 12px; padding: 18px; margin-top: 18px; overflow-x: auto; }}
svg {{ width: 100%; min-height: 96px; }}
.label, .value {{ fill: #edf2f7; font-size: 13px; dominant-baseline: middle; }}
.bar {{ fill: #25d0a5; }}
table {{ border-collapse: collapse; width: 100%; min-width: 1450px; }}
th, td {{ border-bottom: 1px solid #2e3a4d; text-align: left; padding: 10px 8px; vertical-align: top; }}
th {{ color: #aab5c4; font-size: 0.78rem; text-transform: uppercase; letter-spacing: .04em; }}
.empty {{ padding: 18px 0; }}
code {{ color: #8de8cf; }}
</style>
</head>
<body>
<main>
<h1>Zeph Rides creator dashboard</h1>
<p>Descriptive snapshot generated from <code>analytics/metrics.csv</code>. Missing values remain blank; the dashboard does not invent metrics.</p>
<div class="cards">{card_html}</div>
<section><h2>Recorded views</h2>{build_chart(rows)}</section>
<section><h2>Post diagnostics</h2>{table}</section>
</main>
</body>
</html>
"""


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", nargs="?", type=Path, default=Path("analytics/metrics.csv"))
    parser.add_argument("output", nargs="?", type=Path, default=Path("analytics/dashboard.html"))
    args = parser.parse_args()

    rows = read_rows(args.input)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(render(rows), encoding="utf-8")
    print(f"Wrote {args.output} from {args.input} ({len(rows)} rows)")


if __name__ == "__main__":
    main()
