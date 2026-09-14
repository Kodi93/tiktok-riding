# Zeph Rides — Release QA Gate

No post should publish simply because a slot exists.

## Scorecard

Score each category 0–2:
- **0:** fails / weak
- **1:** acceptable but not strong
- **2:** professional / intentional

A post needs **18/22 or better** to publish by default, and it may not score 0 in Hook, Visual, Audio, Cover, or Truth/Rights.

| Category | 0 | 1 | 2 |
|---|---|---|---|
| Hook | slow/confusing | understandable | immediate curiosity/tension |
| Opening visual | generic/dead | usable | distinctive on frame 0 |
| Pacing | drags | acceptable | tight, no wasted beats |
| Payoff | absent | mild | clear/satisfying |
| Visual quality | distracting issues | clean enough | deliberate/professional |
| Audio | muddy/masked | intelligible | balanced/intentional |
| Text | unreadable/generic | functional | concise/native/strong |
| Cover | random/repetitive | usable | distinct/composed/click-worthy |
| Brand fit | could be anyone | motorcycle-relevant | recognizably Zeph Rides |
| Novelty | duplicate/filler | somewhat fresh | meaningfully new angle |
| Truth / rights | misleading/unclear rights | acceptable | clearly truthful/cleared |

## Mandatory preflight

### File / export
- [ ] 9:16 vertical
- [ ] 1080x1920 target where source quality supports it
- [ ] no accidental black frame
- [ ] no broken orientation
- [ ] no obvious compression artifacts
- [ ] no clipped/corrupted ending

### Hook / edit
- [ ] first 0.5–1.0s earns attention
- [ ] no unnecessary setup
- [ ] every cut has a purpose
- [ ] payoff arrives before patience runs out
- [ ] loop is clean if loopability is part of the concept

### Audio
- [ ] narration/TTS understandable on phone speaker
- [ ] engine audible without masking speech
- [ ] wind/noise managed where practical
- [ ] music/sound usage is appropriate for intended monetization

### Text
- [ ] text is readable on a small phone
- [ ] critical words are not covered by UI
- [ ] wording sounds human
- [ ] no spelling/grammar error
- [ ] no generic filler quote unless the visual makes it specific

### Cover
- [ ] intentional cover chosen
- [ ] visually distinct from neighboring posts
- [ ] not the third consecutive road-heavy composition
- [ ] truthful to the video
- [ ] strong at grid size, not only full screen

### Brand / integrity
- [ ] supports at least one brand pillar
- [ ] no misleading claim
- [ ] no fake event presented as real
- [ ] sourced/generated assets are legally/ethically appropriate
- [ ] no obvious AI artifacts
- [ ] no unsafe-riding encouragement in wording

### Publishing / tracking
- [ ] exact caption logged
- [ ] exact publish time logged
- [ ] sound/TTS choice logged
- [ ] cover concept logged
- [ ] experiment variable identified if applicable
- [ ] metrics collection planned for 2h / 24h / 72h

## Hold rules

Automatically HOLD instead of publish when:
- the cover makes the grid look materially more repetitive;
- the first second is generic and cannot be fixed with a better cut;
- the post duplicates a concept from the last seven days without a defined test;
- the clip has no payoff beyond `road continues`;
- audio makes narration hard to understand;
- generated imagery looks fake enough to hurt trust;
- rights/source status is unclear;
- the only reason to publish is `we need something for the slot`.

## Override

A below-threshold post may only publish as a documented experiment with a specific reason, such as testing an intentionally minimal engine-only format. Record the hypothesis in `analytics/experiments.csv`.
