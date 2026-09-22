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
- intelligent participation in BikeTok culture through native Repost/Stitch/Duet where appropriate;
- a path toward sustainable follower growth and future monetization.

## Start here

### Strategy / brand
- [Brand Bible](BRAND_BIBLE.md)
- [Brand Voice](BRAND_VOICE.md)
- [Growth Strategy](GROWTH_STRATEGY.md)
- [Monetization Roadmap](MONETIZATION_ROADMAP.md)
- [30-Day Roadmap](ROADMAP.md)
- [Visual Language & Art Direction](VISUAL_LANGUAGE.md)
- [Professional Production Standard](PRODUCTION_STANDARD.md)
- [Editing Playbook](EDITING_PLAYBOOK.md)
- [Shoot Day SOP](SHOOT_DAY_SOP.md)
- [Release QA Gate](QA_RELEASE_CHECKLIST.md)
- [Content Operating System](CONTENT_SYSTEM.md)

### Content planning
- [Content Backlog](content/backlog.md)
- [100-Idea Content Reservoir](content/CONTENT_IDEAS_100.md)
- [Publishing Calendar](content/calendar.md)
- [Recurring Series Architecture](content/series_architecture.md)
- [Remix / Community Strategy](content/remix_strategy.md)
- [Remix Source Queue](content/remix_source_queue.csv)
- [Remix Brief Template](content/remix_brief_template.md)
- [Hook Library](content/hook_library.md)
- [Thumbnail / Cover Strategy](content/thumbnail_strategy.md)
- [Cover Plan](content/cover_plan.csv)
- [Capture Shot List](content/shot_list.md)
- [Native TikTok TTS Scripts](content/voiceover_scripts.md)
- [Comment & Reply-Video Strategy](COMMENT_STRATEGY.md)
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
- [Direct TikTok Studio SOP](DIRECT_TIKTOK_STUDIO_SOP.md)
- [Direct Native Upload Queue](content/DIRECT_UPLOAD_QUEUE.csv)
- [TikTok Master Validator](scripts/validate_tiktok_master.sh)

### Rights / integrity
- [Asset Rights & Sourcing Policy](rights/ASSET_RIGHTS_POLICY.md)
- [Remix Rights / Platform Reuse Matrix](rights/REMIX_RIGHTS_MATRIX.md)

## Current strategic correction

The early feed is too road-POV heavy, especially in profile thumbnails. That is now treated as a production defect rather than a cosmetic issue.

Immediate priorities:
1. break up the visible grid with rider/bike/detail/encounter covers;
2. locate and professionally cut the turkey and older-gentleman thumbs-up moments from existing footage;
3. establish the helmet-on rider as a recognizable character;
4. capture a reusable bank of rider, bike, startup, detail, night, and environment shots;
5. stop publishing repetitive filler simply to satisfy cadence;
6. pilot a controlled community/remix lane using native TikTok reuse features rather than copied reuploads;
7. measure retention, shares/comments, profile visits, and follow conversion rather than views alone;
8. use meme-reaction inserts as punctuation around authentic Zeph footage, not as a substitute for original identity;
9. turn useful comments into reply-video candidates instead of treating engagement as a dead end;
10. capture each ride according to `SHOOT_DAY_SOP.md` so future edits are not constrained by POV-only footage.

## Content portfolio

Default working mix while the account is young:
- **70–80% original Zeph Rides** — the core brand, identity, and future monetization library.
- **20–30% community/remix experiments** — native Reposts, Stitches, Duets, or permission-cleared reactions that add a real Zeph Rides joke, story, comparison, or point of view.

The remix lane exists to introduce people to Zeph Rides, not to replace original production or turn the profile into an aggregator page.

## Release rule

Every new owned/remix post should:
- pass `QA_RELEASE_CHECKLIST.md`;
- have an intentional cover logged where applicable;
- add something materially new to the channel;
- fit a content pillar/series or be a documented experiment;
- have its key creative variables recorded for later review;
- have clear source/reuse status when third-party material is involved.

Run before scheduling a planned batch:

```bash
python scripts/lint_content_plan.py
```

A failed linter result means **HOLD and revise the plan**, not `schedule it anyway`.

## Current operating model

- Publishing timezone: `America/New_York`
- Primary publisher/scheduler: authenticated TikTok Studio using the [direct native workflow](DIRECT_TIKTOK_STUDIO_SOP.md); no third-party plan is in the critical path
- Metricool: legacy queue history only until the already-scheduled items expire; do not add new posts
- Native TikTok editor: preferred for native TTS/sounds and required for authentic native Stitch/Duet workflows
- Footage: kept outside the repository when files are too large; repo stores source inventory, asset identifiers, editorial decisions, and performance evidence
- Default cadence: up to two posts/day only when quality supports it
- Community/remix material: primarily discovery/follower-growth content; original one-minute content remains the monetization-prep lane

## Core principle

**We are building a creator brand, not maximizing upload count.**

If a piece is weak, repetitive, misleading, visually generic, poorly sourced, below the release threshold, or depends on somebody else's content without enough new value, re-cut it, redesign it, source better supporting creative, or do not publish it.

## Active direction — 2026-09-22

The channel is now **Z7 Hybrid and public-road identity first**. Memes remain useful, but they are punctuation—not the whole feed and not a substitute for strong footage.

The working priority is:

- **Z7 Hybrid identity** — make the unusual Kawasaki platform recognizable through attitude, sound, cockpit detail, and honest road use.
- **Cinematic public-road edits** — fast hooks, purposeful cuts, clean engine audio, restrained graphics, and a real visual payoff.
- **WV ride stories and encounters** — distinct roads, moments, and observations rather than interchangeable centerline footage.
- **Machine detail and hybrid curiosity** — accurate, specific pieces that answer what viewers actually want to know.
- **Occasional comedy / animated memes** — only when the joke is sharp enough to share and the execution clears the same quality bar as a flagship edit.
- **Native community experiments** — Repost, Stitch, Duet, or permission-cleared remix when Zeph adds a real point of view.

The production path must work from owned footage, local editing, and direct TikTok Studio publishing. Third-party generators and editors are optional tools, never a dependency for cadence or quality.

The hard visual exclusion remains explicit: no house, garage, driveway, residential yard, porch, or recognizable home surroundings in any TikTok or Facebook asset.

The Facebook lane remains separate. It can lean somewhat more general and humorous, but it does not receive personal TikTok footage by default and should not become a mirror feed.

## Current working release mix

- 40% cinematic Z7 Hybrid / public-road identity.
- 25% ride stories, encounters, and distinctive West Virginia road moments.
- 15% machine detail, hybrid explainers, or cockpit-focused curiosity.
- 15% comedy, animation, or meme-led originals.
- 5% native community/remix experiments.

This is a directional portfolio, not a quota that justifies filler. A weak meme is held. A generic road clip is held. Every release still passes the QA gate and must add something materially new.
