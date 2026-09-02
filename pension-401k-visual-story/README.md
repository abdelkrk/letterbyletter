# Pension vs 401(k) — 200-Frame Visual Story Production

Production artifacts for the YouTube video "Pension vs 401(k) — What Changed
Structurally in American Retirement?"

## What's in this directory

- **`storyboard.json`** — the full 200-frame storyboard. Each entry has the
  frame number, chapter, characters, location, camera, delta/action,
  educational concept, and the exact rendered prompt sent to the image model.
- **`reference_images.json`** — the 13 locked character/location/metaphor
  reference image job IDs (Alex, Robert, Robert-older, Maya, Mr. Carter,
  Lena, factory, office, explanation room, Robert's home, America-today
  backdrop, pension-fund icon, 401(k)-account icon) used to condition every
  frame for visual consistency.
- **`manifest.json`** — all 200 generated frames: frame number, chapter,
  concept, and the Higgsfield-hosted image URL.

## Model and pipeline

- **Model:** `seedream_v4_5` (Bytedance, via Higgsfield), chosen for
  multi-image reference conditioning, 4K capability, and precise
  instruction-following needed for the diagram/text-heavy frames.
- Every frame was conditioned on 1–4 reference images (the relevant locked
  character portraits, location plate, and/or metaphor diagram) rather than
  strict frame-to-frame chaining, to keep continuity stable across a
  200-frame run without compounding drift.
- Chapters follow the brief exactly: hook (1–10), pension mechanics
  (11–40), pension risk (41–60), legal/historical timeline (61–85), 401(k)
  mechanics (86–120), ten-dimension structural comparison (121–155), why
  401(k)s spread (156–175), what workers gained/inherited (176–190), the
  system today (191–196), ending (197–200).

## Important limitation — read before treating this as finished

The 200 images exist and are viewable/downloadable at the URLs in
`manifest.json`, inside the Higgsfield account that generated them. **The
actual PNG files are not committed to this repository.** This session's
network egress policy blocks the Higgsfield CDN host from this container's
shell, so the binaries could not be downloaded and added to git. Only the
text production artifacts (storyboard, manifest, reference IDs) are
committed here.

Nobody has visually inspected the 200 frames for the continuity/consistency
checks the brief calls for (Section 28–29: character drift, correct
left/right split-screen orientation, no mutated objects, etc.). That QC pass
still needs to happen — by a human, or by a session with unblocked network
access to Higgsfield's CDN — before treating this as final.

## To get the actual image files

1. Open each URL in `manifest.json` directly (they render in any browser), or
2. Use the Higgsfield account's own generation history / gallery to bulk
   download, or
3. Re-run this pipeline from an environment that can reach
   `*.cloudfront.net` / `cdn.higgsfield.ai`, downloading each `manifest.json`
   URL and saving it as `pension401k_NNN.png` (zero-padded per the original
   spec).
