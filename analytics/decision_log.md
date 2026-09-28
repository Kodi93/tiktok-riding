# Editorial Decision Log

Use this file for decisions that materially change the content system. Keep entries short and evidence-based.

## 2026-09-14 — Thumbnail repetition is a production defect

**Observation:** visible profile covers are dominated by similar road/pavement/tree-line compositions.  
**Decision:** significant cover variation is mandatory. Upcoming batches must use multiple cover families and pass the cover-plan linter.  
**Reason:** different videos can still look identical in the profile grid when cover composition repeats.  
**Follow-up:** `content/thumbnail_strategy.md`, `VISUAL_LANGUAGE.md`, `content/cover_plan.csv`, `scripts/lint_content_plan.py`.

## 2026-09-14 — Professional quality outranks cadence

**Decision:** do not publish weak filler merely to maintain two posts per day.  
**Reason:** repetitive low-value output can weaken profile presentation and makes it harder to learn which ideas actually work.  
**Follow-up:** every post should pass `QA_RELEASE_CHECKLIST.md` or be documented as an explicit experiment.

## 2026-09-14 — Build creator identity beyond POV

**Decision:** deliberately add helmet-on rider presence, bike hero shots, machine details, encounters, environment, and recurring series.  
**Reason:** forward POV alone does not create enough visual/personality differentiation.  
**Follow-up:** `BRAND_BIBLE.md`, `content/shot_list.md`, `content/series_architecture.md`.

## 2026-09-14 — Prioritize authentic encounter footage

**Decision:** the turkey crossing and older gentleman thumbs-up moments are P0 source-retrieval targets.  
**Reason:** authentic unscripted moments are more distinctive than another generic scenic clip and can support story, humor, shares, and comments.  
**Follow-up:** log exact source clips/time ranges when found and create dedicated briefs before editing.

## Entry template

### YYYY-MM-DD — Decision title
**Observation:**  
**Decision:**  
**Reason/evidence:**  
**Follow-up:**

## 2026-09-28 — Optimize for shares, repeat viewers, and organic compounding

**Observation:** the latest 28-day account snapshot shows 12.1K post views, 506 likes, 23 comments, 4 shares, and 89 profile views. Promote produced 2.44K views and 157 followers on $43 spend, but organic sharing remains the weakest visible downstream signal.

**Decision:** shift the next growth sprint away from generic scenic POV volume and toward scenario-driven biker comedy, animated/motion-graphic jokes, recurring character/series identity, and strong riding clips that contain a clear premise or payoff. Every P0 concept must contain at least one explicit share/reply/repeat-view reason.

**Reason/evidence:** paid follower conversion is encouraging (~6.43% of promoted views; ~$0.274/follower), but meaningful scale requires organic distribution to grow faster than paid spend. Shares are currently only ~0.03% of the 12.1K overall view snapshot, so shareability is the clearest creative bottleneck.

**Follow-up:** `content/batches/2026-09-28-share-sprint.md`, `content/ANIMATED_MEME_QUEUE.csv`, `GROWTH_STRATEGY.md`, and the Sep 28 rows in `analytics/metrics.csv`.

## 2026-09-28 — Promote is a test accelerator, not the growth engine

**Observation:** $43 of Promote generated 157 followers and 2.44K views.

**Decision:** continue Promote only on creative that already demonstrates strong audience response or as a tightly bounded test. Do not scale spend simply to inflate top-line views. Judge success by post-Promote organic views, repeat viewers, shares, comments, profile visits, and subsequent follower activity.

**Reason/evidence:** the acquisition cost is usable, but a channel that requires proportionally increasing spend to increase reach will not compound into the intended media asset.

**Follow-up:** tag promoted tests separately in analytics and compare their next-post organic lift against non-promoted baselines.

## 2026-09-28 — No additional paid budget

**Observation:** the user does not want to add any more budget to TikTok growth or external video-generation services.

**Decision:** all growth work proceeds on a zero-new-spend basis until the user explicitly changes that constraint. Pause new Promote spend and do not depend on paid third-party generation credits. Use existing footage, original graphics, native TikTok tools, repository automation, and no-cost editing/generation paths already available.

**Reason/evidence:** the account now needs to prove that organic reach can compound from the audience already acquired. Additional paid reach would obscure that test and violate the current budget constraint.

**Follow-up:** measure organic-only performance for the Sep 28 shareability sprint and keep paid historical metrics separated from new organic results.
