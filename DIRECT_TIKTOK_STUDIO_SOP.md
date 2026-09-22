# Direct TikTok Studio Publishing SOP

**Status:** Active primary publishing path as of 2026-09-22  
**Account:** `@zeph.rides.wv`  
**Publishing timezone:** `America/New_York`

This workflow removes third-party scheduler plans from the critical path. Masters are rendered and validated by us, then uploaded and scheduled in authenticated TikTok Studio.

## Non-negotiables

- Never show the house, garage, driveway, porch, residential yard, or recognizable home surroundings.
- Keep the creator faceless/visor-down unless the owner explicitly changes that rule.
- Use owned graphics/footage, native TikTok Stitch/Duet/Repost, or permission-cleared sources. Downloaded reuploads are not a growth strategy.
- TikTok and Facebook remain separate editorial lanes.
- Do not put credentials, cookies, session data, or one-time codes in this repository.
- Metricool is legacy queue history only. Do not add new scheduled posts there.
- The owned production path must work with local editing and approved source footage. External generators/editors are optional, never required.

## Owned pipeline

1. **Produce the master.** Build original 9:16 motion graphics or edit approved riding footage. Default target: 1080×1920, H.264 High, 30 fps, `yuv420p`, AAC-LC 48 kHz stereo, `+faststart`.
2. **Validate locally.** Run:

   ```bash
   scripts/validate_tiktok_master.sh path/to/master.mp4
   ```

3. **Record the release.** Add the filename, caption, rights status, and intended Eastern time to `content/DIRECT_UPLOAD_QUEUE.csv` before the upload.
4. **Open the authenticated account.** Use TikTok Studio directly at the upload page. If sign-in is required, use the secure browser authentication handoff; never type or expose secrets through automation.
5. **Use the cloud file bridge correctly.** A generated file under `/workspace/scratch/<relative-path>` is visible to the browser at `/home/oai/share/<relative-path>`. The browser-side path must be passed to the file chooser. Passing the main-container path caused the prior false `DataView`/media-parser failures.
6. **Upload and stage.** Set the caption, cover, audience, native sound/TTS where appropriate, and TikTok's own schedule controls. Keep HD upload, music copyright check, and Content Check Lite enabled.
7. **Convert the schedule clock.** TikTok Studio uses the browser's local timezone. Read that timezone from the active browser, convert from the queue's authoritative `America/New_York` time, and record both values. Never guess.
8. **Quality decision.** If the owner rejects an asset, mark it `REJECTED_QUALITY_HOLD` even if the upload and platform checks succeeded. Do not schedule or post it.
9. **Final action.** Immediately before clicking **Schedule** or **Post**, obtain action-time approval because the click publishes representational content. One approval may cover a clearly listed batch with exact files, captions, account, and times.
10. **Verify.** Confirm TikTok shows the scheduled/published state, capture evidence, and update the queue from `STAGED_NATIVE_STUDIO` to `SCHEDULED_NATIVE` or `PUBLISHED`.
11. **Measure.** Log 2h, 24h, and 72h performance in `analytics/metrics.csv`; use shares, rewatches, profile visits, and follows to select variants.

## Failure handling

- If TikTok rejects a file, first verify the browser-side `/home/oai/share/...` path, then run the validator and a full decode test.
- Retry once only after correcting a concrete cause. Do not loop uploads.
- Do not fall back to a third-party free scheduler. Keep the validated master and retry TikTok Studio directly.
- Do not use a photo carousel as a substitute for a failed video unless that carousel was intentionally designed as its own post.

## Cadence

- Baseline: up to two quality posts per day with at least four hours between them.
- Maintain a rolling seven-day native TikTok queue.
- Favor strong Z7 Hybrid identity, public-road stories, rider/bike detail, and clean cinematic edits. Use comedy/animation selectively when the premise and execution warrant it.

## Current proof

The browser/file bridge was proven on 2026-09-22 when three masters passed TikTok's upload checks. That proved transport only, not creative quality. The owner rejected those three drafts, so they are now `REJECTED_QUALITY_HOLD` and must not be scheduled or posted.

The first replacement flagship is `zeph-rides-z7-flagship-v1.mp4`: an owned public-road, locally rendered Z7 Hybrid identity cut. It remains `READY_FOR_OWNER_REVIEW`; no post or schedule action is authorized by that status.
