# Zeph Rides TikTok Content Operating System

This repository is the planning and measurement source of truth for `@zeph.rides.wv`.

Read first:
- `BRAND_BIBLE.md`
- `PRODUCTION_STANDARD.md`
- `VISUAL_LANGUAGE.md`
- `QA_RELEASE_CHECKLIST.md`
- `GROWTH_STRATEGY.md`

## Objective

Build a repeatable system that increases reach, followers, repeat viewers, and original-content quality without turning the feed into a high-volume dump of near-identical motorcycle footage.

Professional quality outranks cadence.

## Current correction — 2026-09-14

The early profile is visually too repetitive. Road POV remains a core content type, but it can no longer dominate the visible grid or thumbnail language.

Immediate correction:
- force cover variation;
- introduce rider/bike/detail/encounter imagery;
- prioritize real high-value moments already present in source footage;
- build recognizable recurring series;
- stop using generic reflective/motivational copy as a default content engine;
- track the creative reason behind each post.

## Production pipeline

Every asset moves through:

`SOURCE -> SELECT -> CONCEPT -> SCRIPT -> EDIT -> COVER -> QA -> SCHEDULE -> PUBLISH -> MEASURE -> DECIDE`

### SOURCE
Log source footage or capture requirements in `content/source_inventory.csv` and `content/backlog.md`.

### SELECT
Choose moments with an actual reason to exist: encounter, visual satisfaction, humor, story, rider identity, machine detail, scenery, or useful observation.

### CONCEPT
Assign:
- content series/pillar;
- target length;
- opening visual;
- hook;
- payoff;
- cover family;
- metric/hypothesis if experimental.

### SCRIPT
Use `content/hook_library.md` and `content/voiceover_scripts.md` as pattern references, not copy-paste generators.

### EDIT
Follow `PRODUCTION_STANDARD.md`. Remove anything that does not strengthen the idea.

### COVER
Log in `content/cover_plan.csv`. Follow `content/thumbnail_strategy.md` and `VISUAL_LANGUAGE.md`.

### QA
Score with `QA_RELEASE_CHECKLIST.md`. Default publish threshold: 18/22, with no zero in critical categories.

### SCHEDULE
Schedule only after asset and QA are complete. Do not create an artificial deadline that forces weak content live.

### MEASURE
Record performance in `analytics/metrics.csv` at approximately 2h/24h/72h and 7d where useful.

### DECIDE
Use `analytics/kpi_framework.md`, `analytics/experiments.csv`, and `analytics/weekly-review.md` to keep, revise, or retire the format.

## Daily operating routine

When publishing:
1. confirm the post passed QA;
2. confirm the cover does not worsen grid repetition;
3. publish/schedule with exact caption and audio documented;
4. reply to authentic comments when practical;
5. record performance checkpoints;
6. capture any viewer questions that can become future posts.

## Production block

A normal production block should intentionally create visual range.

Target:
- 2–3 short reach clips with different opening visual types;
- 1 real encounter/story when source footage supports it;
- 1 rider/bike/detail piece;
- 1 longer structured original;
- at least one clean engine/original-audio asset;
- at least one native-TTS asset only when TTS improves the concept.

Do not render an entire backlog simply because it exists.

## Feed architecture gate

Every planned 9-post window should normally contain at least four materially different cover families and four editorial modes.

Run:

```bash
python scripts/lint_content_plan.py
```

If the plan fails, revise it before scheduling.

## Recurring content pillars

| Pillar / series | Typical length | Job | Typical visual |
|---|---:|---|---|
| Ride Encounters | 6–30s | curiosity, shares, comments | real person/animal/event |
| One More Corner | 6–15s | relatable humor | curve + varied humor graphic |
| WV Road Test | 8–25s | regional identity/reach | distinctive road feature |
| Helmet On | 7–20s | rider identity/follows | rider + bike |
| Machine Details | 6–20s | visual variety/curiosity | controls/startup/details |
| The Long Way Home | 10–45s | emotional/cinematic identity | rider/bike/environment |
| Things BikeTok Doesn't Show | 8–60s | authenticity/humor | unglamorous real moments |
| Hybrid Life | 10–45s | bike differentiation/search curiosity | machine + context |
| 60 Seconds of WV | 60–75s | original watch time/story | structured multi-beat ride |

See `content/series_architecture.md`.

## Native TikTok TTS standard

TTS is a tool, not the channel identity.

Use native TikTok TTS when it improves timing, humor, or platform-native feel. Do not apply it automatically to every short.

Workflow:
1. upload finished vertical cut;
2. add concise narration text;
3. apply native text-to-speech;
4. split text blocks when timing requires pauses;
5. set text duration to the visual beat;
6. balance engine audio underneath;
7. add native sound only if it improves the piece.

## Capture standard

Future rides must generate supporting coverage, not only forward POV. Follow `content/shot_list.md` and intentionally capture:
- rider/bike hero shots;
- startup/control details;
- static environment shots;
- signs/location details;
- night/mood material;
- authentic encounter context.

## Rights and integrity

Follow `rights/ASSET_RIGHTS_POLICY.md`.

External or generated images may be used to raise visual quality only when they are relevant, legally usable, and not misleading. Never fabricate real ride events for a cover.

## Measurement rules

Use relative rules until the account has a larger sample:
- compare similar formats;
- use rolling medians where possible;
- distinguish observed from estimated values;
- value retention, shares, profile visits, and follows in addition to raw views;
- do not declare a format dead from one post.

## Decision log

For winners, record **why** they worked. For weak posts, diagnose separately:
- concept;
- first frame;
- hook;
- pacing;
- payoff;
- duration;
- audio;
- cover;
- caption;
- grid context;
- distribution/sample size.

The system succeeds when the feed becomes more visually varied, more recognizable, and more effective over time — not merely when upload count increases.
