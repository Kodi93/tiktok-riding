# Zeph Rides — Creator Operations

Professional content strategy, production, scheduling, quality control, experimentation, and performance measurement for `@zeph.rides.wv`.

This repository is the operating system for the channel. The standard is not `good enough to upload`; the standard is content credible beside established motorcycle creators.

## Mission

Build Zeph Rides into a recognizable motorcycle creator brand with:
- professional editing and art direction;
- strong first-second hooks;
- significant thumbnail/cover variation;
- recurring series with real identity;
- deliberate rider/bike presence;
- authentic West Virginia/Appalachian character;
- disciplined analytics and experimentation;
- a path toward sustainable follower growth and future monetization.

## Start here

### Strategy / brand
- [Brand Bible](BRAND_BIBLE.md)
- [Growth Strategy](GROWTH_STRATEGY.md)
- [30-Day Roadmap](ROADMAP.md)
- [Visual Language & Art Direction](VISUAL_LANGUAGE.md)
- [Professional Production Standard](PRODUCTION_STANDARD.md)
- [Release QA Gate](QA_RELEASE_CHECKLIST.md)
- [Content Operating System](CONTENT_SYSTEM.md)

### Content planning
- [Content Backlog](content/backlog.md)
- [Publishing Calendar](content/calendar.md)
- [Recurring Series Architecture](content/series_architecture.md)
- [Hook Library](content/hook_library.md)
- [Thumbnail / Cover Strategy](content/thumbnail_strategy.md)
- [Cover Plan](content/cover_plan.csv)
- [Capture Shot List](content/shot_list.md)
- [Native TikTok TTS Scripts](content/voiceover_scripts.md)
- [Asset Manifest](content/asset_manifest.csv)
- [Source Inventory](content/source_inventory.csv)

### Analytics / experiments
- [KPI Framework](analytics/kpi_framework.md)
- [Metrics Log](analytics/metrics.csv)
- [Experiment Registry](analytics/experiments.csv)
- [Weekly Review](analytics/weekly-review.md)
- [Progress Dashboard](analytics/dashboard.html)

### Automation / QA
- [Metrics Analyzer](scripts/analyze_metrics.py)
- [Dashboard Builder](scripts/build_dashboard.py)
- [Content Plan Linter](scripts/lint_content_plan.py)

### Rights / integrity
- [Asset Rights & Sourcing Policy](rights/ASSET_RIGHTS_POLICY.md)

## Current strategic correction

The early feed is too road-POV heavy, especially in profile thumbnails. That is now treated as a production defect rather than a cosmetic issue.

Immediate priorities:
1. break up the visible grid with rider/bike/detail/encounter covers;
2. locate and professionally cut the turkey and older-gentleman thumbs-up moments from existing footage;
3. establish the helmet-on rider as a recognizable character;
4. capture a reusable bank of rider, bike, startup, detail, night, and environment shots;
5. stop publishing repetitive filler simply to satisfy cadence;
6. measure retention, shares/comments, profile visits, and follow conversion rather than views alone.

## Release rule

Every new post should:
- pass `QA_RELEASE_CHECKLIST.md`;
- have an intentional cover logged in `content/cover_plan.csv`;
- add something materially new to the channel;
- fit a content pillar/series or be a documented experiment;
- have its key creative variables recorded for later review.

Run before scheduling a planned batch:

```bash
python scripts/lint_content_plan.py
```

A failed linter result means **HOLD and revise the plan**, not `schedule it anyway`.

## Current operating model

- Publishing timezone: `America/New_York`
- Primary scheduler: Metricool
- Native TikTok editor: preferred for native TTS/sounds where required
- Footage: kept outside the repository when files are too large; repo stores source inventory, asset identifiers, editorial decisions, and performance evidence
- Default cadence: up to two posts/day only when quality supports it

## Core principle

**We are building a creator brand, not maximizing upload count.**

If a piece is weak, repetitive, misleading, visually generic, poorly sourced, or below the release threshold, re-cut it, redesign it, source better supporting creative, or do not publish it.
