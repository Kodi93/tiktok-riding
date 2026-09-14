# KPI Framework

## Purpose

Views alone are not enough to diagnose performance. Track the audience funnel so we can tell whether a post failed at distribution, hook, retention, interaction, profile conversion, or follow conversion.

## Core post KPIs

Where TikTok/Metricool exposes the data, record:

- views
- unique viewers if available
- average watch time
- completion rate
- total play time
- likes
- comments
- shares
- saves/favorites
- profile views attributed to post if available
- new followers attributed to post if available
- traffic source / For You percentage if available

## Derived metrics

Calculate where inputs exist:

- **like rate** = likes / views
- **comment rate** = comments / views
- **share rate** = shares / views
- **save rate** = saves / views
- **follow conversion** = new followers / views
- **profile conversion** = profile views / views
- **watch ratio** = average watch seconds / video length seconds

Do not fabricate missing values. Leave unknowns blank.

## Observation windows

Default checkpoints:
- ~2 hours: initial distribution / early hook signal
- ~24 hours: first-day performance
- ~72 hours: stable comparison point for most routine analysis
- 7 days: long-tail check for unusually durable posts

Record actual observation time, not just `24h`, because platform delivery is not perfectly uniform.

## Comparison rules

Prefer comparisons among similar formats:
- 8–15s humor vs 8–15s humor
- encounter vs encounter
- 60–75s original vs 60–75s original

Do not use a 7-second loop and a 70-second narrative as if completion rate means the same thing.

## Baselines

Maintain rolling medians for the previous eight comparable posts when enough data exists.

Useful relative signals:
- views vs comparable median
- watch ratio vs comparable median
- share rate vs comparable median
- follow conversion vs comparable median

Use medians rather than averages while the sample is small and outliers are common.

## Creative diagnosis matrix

### Low views + weak watch ratio
Likely creative/hook problem. Review first second, opening visual, pacing, and concept.

### Low views + strong watch ratio
Potentially under-distributed or too small a sample. Do not immediately kill the format.

### Good views + weak follows
Reach worked, identity/conversion may not. Ask whether the post gives a reason to visit/follow.

### Good watch + strong shares
High-value format. Protect the core concept and produce new executions without cloning it.

### Strong likes + weak shares/comments/follows
May be pleasant but passive. Improve story, specificity, or social relevance.

### Strong profile visits + weak follows
Profile/grid/positioning may be failing to convert curiosity. Review covers, bio, pinned posts, and visible content mix.

## Weekly dashboard questions

Every weekly review must answer:
1. Which three openings held attention best?
2. Which cover families produced the strongest post opens/profile curiosity?
3. Which posts generated followers rather than only views?
4. Which series earned another execution?
5. Which format is becoming repetitive?
6. What single variable should the next batch test?
7. What should stop immediately?

## Reporting standard

Never report an estimated number as measured. Label values as:
- observed
- calculated
- estimated
- unknown

Keep screenshots or source notes when a metric matters to a strategic decision.
