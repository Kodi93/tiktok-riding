# Zeph Rides TikTok Operations

Planning, production, scheduling, and measurement for @zeph.rides.wv.

## Start here

- [Content operating system](CONTENT_SYSTEM.md)
- [Content backlog](content/backlog.md)
- [Publishing calendar](content/calendar.md)
- [Native TikTok TTS scripts](content/voiceover_scripts.md)
- [Metrics log](analytics/metrics.csv)
- [Weekly review](analytics/weekly-review.md)
- [Metrics analyzer](scripts/analyze_metrics.py)

## Current operating decision

Use native TikTok text-to-speech for short humorous clips because it is recognizable and native to the platform. Use original engine audio plus narration for one-minute originals. Metricool is the scheduling lane; TikTok is the editing lane for native TTS and native sounds.

## Current baseline

- Timezone: America/New_York
- Latest user-reported snapshot: 0 followers and 52 likes
- Early visible baseline: approximately 99 views on a 42-second post and 45 views on a 12-second post
- Current queue: scheduled through 2026-09-24
- Next priority: produce four new TTS shorts and two narrated one-minute originals, then review at 2h/24h/72h intervals

The repository is intentionally lightweight: footage remains in the persistent file store, while this repo stores the decisions, scripts, calendar, and evidence needed to improve each batch.
