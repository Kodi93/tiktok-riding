# Zeph Creator OS — Platform Architecture

## Purpose

Turn the Zeph Rides project from a collection of content plans into a practical creator operating platform that connects ChatGPT strategy, the local editing workstation, TikTok, Metricool, and GitHub.

The objective is **not to guarantee virality**. Virality is probabilistic. The objective is to build a system that materially improves the odds by making content discovery, production, testing, publishing, analytics, and iteration faster and more disciplined.

## Core system

```text
ChatGPT
  |
  v
GitHub command/result queue
  |
  v
Local Zeph Worker on Windows
  |----> Dedicated Chrome/TikTok session
  |----> Local footage library
  |----> Render/edit utilities
  |----> Screenshot/metadata collector
  |
  +----> Metricool / official APIs where available
```

## Responsibilities

### ChatGPT — strategy / decision layer

ChatGPT should be able to:

- create scouting jobs;
- review returned TikTok candidates;
- rank REPOST / STITCH / DUET / INSPIRED ORIGINAL / SKIP opportunities;
- write hooks, captions, remix concepts, content briefs, and cover plans;
- choose experiments;
- interpret post analytics;
- update the content backlog and production priorities;
- prepare jobs for the local worker;
- never require the TikTok password.

### GitHub — durable control plane

GitHub stores:

- jobs;
- results;
- content plans;
- candidate URLs;
- source/rights status;
- edit instructions;
- release QA;
- analytics;
- worker logs;
- system configuration that is safe to commit.

Secrets, login cookies, browser profiles, and access tokens do **not** belong in GitHub.

### Local Zeph Worker — execution layer

The worker runs on the user's Windows PC and should:

- poll the GitHub job queue at a conservative interval;
- launch/reuse a dedicated Chrome profile;
- preserve the user's local TikTok login session;
- browse TikTok at human-scale rates;
- collect public/visible candidate metadata;
- capture screenshots where useful;
- identify likely Stitch/Duet availability when visible;
- inspect our own profile/posts;
- scan local footage when requested;
- render prepared drafts using local tools;
- return structured results to GitHub;
- stop for human intervention on CAPTCHA, login challenge, or unexpected security prompts.

### TikTok — discovery / publishing surface

Use TikTok for:

- trend and creator discovery;
- native Repost/Stitch/Duet workflows where available;
- native sounds/TTS when useful;
- direct creator/community interaction;
- profile and post review.

Prefer official APIs or native platform functions for publishing when they provide the required capability.

### Metricool — scheduling / analytics lane

Continue using Metricool for:

- scheduling where supported;
- post-performance retrieval;
- recommended posting times when available;
- maintaining a stable publishing calendar.

## Job model

Every worker job receives a unique ID and one of these initial types:

- `SCOUT_TIKTOK`
- `ANALYZE_TIKTOK_URL`
- `SCAN_OWN_PROFILE`
- `SCAN_LOCAL_FOOTAGE`
- `RENDER_DRAFT`
- `CAPTURE_SCREENSHOT`
- `PREPARE_UPLOAD`

Future write-capable job types may include:

- `UPLOAD_DRAFT`
- `PUBLISH_POST`
- `POST_COMMENT`
- `FOLLOW_CREATOR`

Write actions must be disabled by default until explicitly enabled and approved.

## Example: scouting job

```json
{
  "job_id": "20260914-001",
  "type": "SCOUT_TIKTOK",
  "status": "queued",
  "query": "funny motorcycle rider moments animals biker memes hybrid motorcycles",
  "max_results": 20,
  "created_by": "chatgpt",
  "risk": "read_only"
}
```

Expected result fields:

```json
{
  "job_id": "20260914-001",
  "status": "complete",
  "results": [
    {
      "url": "...",
      "creator": "...",
      "caption": "...",
      "visible_views": null,
      "visible_likes": null,
      "stitch_visible": null,
      "duet_visible": null,
      "screenshot": "...",
      "notes": "..."
    }
  ]
}
```

## Approval model

### Automatic

- read-only browsing;
- search;
- candidate collection;
- screenshots;
- metadata extraction;
- local analysis;
- rendering drafts;
- GitHub logging.

### Human approval required

Initially require approval for:

- publishing;
- commenting;
- following/unfollowing;
- deleting;
- changing profile settings;
- sending DMs;
- any unexpected account/security action.

The worker should fail closed: if the action type is not explicitly allowed, it does not execute.

## Security rules

- TikTok password never enters ChatGPT, GitHub, source code, logs, or config files.
- Browser cookies stay in the local dedicated browser profile.
- Store API secrets only in local environment variables or OS credential storage.
- `.gitignore` must exclude browser profiles, tokens, logs containing session data, and local render caches.
- Never attempt to bypass CAPTCHA, anti-bot challenges, 2FA, or platform security controls.
- Never implement mass-follow, mass-comment, mass-like, or spam behavior.
- Rate-limit browsing and prefer explicit jobs over continuous scraping.

## Virality engine

The platform cannot manufacture virality. It can improve the probability by enforcing a fast learning loop:

```text
Scout -> Select -> Brief -> Produce -> QA -> Publish -> Measure -> Diagnose -> Iterate
```

Every post should contribute evidence about:

- hook type;
- first-frame visual;
- duration;
- series;
- rider presence;
- cover family;
- TTS vs engine/voice;
- original vs remix/community;
- shares;
- profile visits;
- follower conversion;
- retention/completion where available.

The system should prefer formats that repeatedly outperform comparable posts rather than chasing one-off vanity views.

## MVP

The first usable version should do only four things well:

1. run locally on Windows;
2. reuse a dedicated logged-in TikTok browser profile;
3. accept a GitHub `SCOUT_TIKTOK` job and return 10–20 candidate URLs with metadata/screenshots;
4. accept `ANALYZE_TIKTOK_URL` and return enough information for ChatGPT to classify the candidate as REPOST / STITCH / DUET / INSPIRED ORIGINAL / SKIP.

No publishing automation is required for MVP.

## Phase 2

After read-only reliability is proven:

- local footage search and clip extraction;
- automatic remix brief generation inputs;
- local draft rendering;
- upload-to-draft where supported;
- analytics sync and experiment correlation;
- thumbnail/contact-sheet generation;
- worker health/status dashboard.

## Definition of success

The platform is successful when the user can say in normal ChatGPT:

> Find good BikeTok content for us to react to.

and, without Work mode, the local worker returns a usable ranked candidate set from the user's TikTok environment for strategic review.

The larger creator system is successful when Zeph Rides can repeatedly discover, produce, publish, and learn from stronger content with less manual friction and measurably better follower/reach outcomes over time.
