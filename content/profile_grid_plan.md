# Profile Grid Rebuild Plan

## Problem

The visible account grid currently over-communicates one thing: forward-facing road footage. Even when videos are different, similar road/pavement/tree-line thumbnails make the channel look repetitive.

The objective is not to delete the motorcycle POV identity. It is to surround POV with enough rider, bike, detail, encounter, and environment imagery that each post reads as a distinct piece of content.

## Next 9-post target

| Slot | Editorial mode | Preferred cover family | Purpose |
|---:|---|---|---|
| 1 | humor short | Humor/Graphic | immediate visual break from road grid |
| 2 | rider identity | Rider Hero | establish creator character |
| 3 | route/GPS story | Destination/Environment | sign/fork/location context |
| 4 | machine/detail | Detail | break pavement repetition |
| 5 | encounter | Encounter | real high-curiosity moment |
| 6 | POV payoff | Curve/Road Reveal | retain core riding identity |
| 7 | one-minute original | Rider/Bike or Environment | depth + original watch time |
| 8 | bike mood/detail | Bike Hero or Night/Mood | visual identity |
| 9 | second encounter/experiment | Encounter or Graphic | range + learning |

## Acceptance criteria

The next nine visible posts should:
- use at least four cover families;
- have no run of three road-family covers;
- have at least two covers where the motorcycle or rider is the obvious subject;
- have at least one real encounter/story cover if suitable footage exists;
- have at least one close/detail composition;
- have no repeated text layout across three adjacent covers;
- avoid three consecutive posts sourced from visually indistinguishable stretches of the same ride.

## Existing-grid correction

Do not panic-delete existing posts solely because the covers are repetitive. The first correction is to make upcoming rows materially better.

Only revisit old posts if there is a strategic reason, such as:
- an obviously poor or misleading cover;
- a duplicate upload;
- an upload defect;
- a post that conflicts with later brand/quality decisions.

## Review process

Before scheduling a new batch:
1. list the current top 6 visible covers;
2. append the planned next 3 covers;
3. inspect the resulting 3x3 grid;
4. run `python scripts/lint_content_plan.py`;
5. change any cover that visually collapses into its neighbors;
6. confirm every planned post also passes the release QA gate.

The grid should look intentional even before someone watches a single video.
