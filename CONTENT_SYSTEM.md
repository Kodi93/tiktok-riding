# Zeph Rides TikTok Content Operating System

This repository is the planning and measurement source of truth for @zeph.rides.wv.

## Objective

Build a repeatable TikTok system that increases reach and followers first, while deliberately producing original one-minute videos that can support Creator Rewards eligibility later. We are not treating virality as guaranteed; we are running controlled creative experiments and keeping the winners.

## Current snapshot — 2026-09-14

- Account: @zeph.rides.wv
- Latest user-reported account snapshot: 0 followers and 52 likes. Recheck TikTok Studio before treating this as authoritative.
- Visible early post baseline: roughly 99 views on a 42-second post and 45 views on a 12-second post.
- Publishing timezone: America/New_York.
- Current Metricool queue: scheduled through 2026-09-24.
- Direct TikTok queue has one known duplicate 10:00 AM item that still needs cleanup when direct TikTok editing is available.
- Native TikTok text-to-speech is the preferred narrator style for short clips. Metricool cannot add that native voice layer after upload.

## The routine

### Every publishing day

1. Publish one short reach clip (8–15 seconds) with a hook in the first frame.
2. Publish one longer original clip (60–75 seconds) only when the cut has a real narrative beat; do not pad footage to hit a duration.
3. Reply to every real comment within the first hour when possible.
4. Log the post in analytics/metrics.csv at approximately 2 hours, 24 hours, and 72 hours.
5. Record the exact hook, duration, TTS script, sound choice, and post time. If those are unknown, mark them unknown rather than guessing.

### Every production block

Create:

- 4–6 short clips with different hooks and distinct moments.
- 2 one-minute originals with a beginning, turn, payoff, and closing question.
- At least one clean-engine/no-music version.
- At least one native-TTS version.
- No duplicate asset within seven days unless it is a clearly labeled hook test with materially different opening seconds.

### Weekly review

Run scripts/analyze_metrics.py, then complete analytics/weekly-review.md.

The weekly decision is:

- Keep the top three hooks.
- Rewrite or retire the bottom two hooks.
- Choose the next batch from the best-performing content pillar.
- Do not judge a format from one post; wait for at least eight comparable posts when possible.

## Content pillars

| Pillar | Length | Job | Audio |
|---|---:|---|---|
| Humorous POV | 8–15s | Reach, shares, follows | Native TikTok TTS + low engine audio |
| Turn/payoff | 12–25s | Retention and comments | Native TTS or engine audio |
| Narrated ride | 60–75s | Original watch time and creator identity | Own voice/native TTS + cleared/original audio |
| Pure ride sound | 15–60s | Audio identity and watch-time test | Clean engine audio, no added music |

## Measurement rules

Use these relative rules until the account has a larger sample:

- Strong hook: 24-hour views at least 1.5x the median of the previous eight comparable posts.
- Strong retention: completion rate or average watch time materially above the format median.
- Strong conversation: comments or shares per 100 views above the format median.
- Strong conversion: measurable follows from the post; record the number even when it is zero.
- Small-sample warning: fewer than eight comparable posts means the result is directional, not conclusive.

Never buy views, followers, or engagement. Never use paid promotion to manufacture Creator Rewards-qualified views.

## Native TikTok TTS standard

For short clips, apply the voice inside TikTok:

1. Upload the finished vertical video.
2. Add a text block containing the narration.
3. Select the text block and choose Text-to-speech.
4. Use the default/narrator style unless a different native option clearly fits.
5. Split lines into separate text blocks when the joke needs a pause.
6. Set each text block's duration to match the visual beat.
7. Keep engine audio low enough that the narration is intelligible.
8. Add a native sound only after the voice and timing are correct.

Metricool remains the reliable scheduling lane, but native TTS must be applied in TikTok before the final scheduled upload.

## Safety and quality gates

Before scheduling:

- 9:16 vertical, 1080x1920 target.
- No black opening frame.
- Hook readable on the first frame.
- No dangerous riding behavior encouraged by the caption.
- Wind reduced without destroying engine character.
- No unlicensed music baked into one-minute monetization-focused originals.
- Caption has one clear question or interaction prompt.
- The asset has not already been scheduled in the same seven-day window.
- The exact asset path and caption are recorded in content/calendar.md.

## Decision log

When a clip wins or loses, record why. Examples:

- “Hook was understandable before the first turn.”
- “Punchline arrived too late.”
- “Text was too small on mobile.”
- “Native TTS sounded natural but engine audio masked the final word.”
- “Views were high but shares/follows were weak.”

This keeps the project from drifting back to generic motorcycle footage with no learning loop.
