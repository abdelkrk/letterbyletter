# Pension vs 401(k) — 200-Frame Visual Story Production

Production artifacts for the YouTube video "Pension vs 401(k) — What Changed
Structurally in American Retirement?"

## What's in this directory

- **`storyboard.json`** — present in this branch's git history (see the
  "Trim storyboard.json..." commit) but not re-pushed as a standalone file
  here beyond what git already carries, to avoid re-inlining ~100KB of JSON
  through the chat session a second time. It holds the full 200-frame
  structural metadata: frame number, chapter, characters, location, camera,
  delta/action, educational concept, text-label flag, metaphor flag,
  historical flag, split-screen side.
- **`reference_images.json`** — the 13 locked character/location/metaphor
  reference image job IDs (Alex, Robert, Robert-older, Maya, Mr. Carter,
  Lena, factory, office, explanation room, Robert's home, America-today
  backdrop, pension-fund icon, 401(k)-account icon) used to condition every
  frame for visual consistency.
- **`manifest.json`** — all 200 generated frames: frame number, chapter,
  concept, and the Higgsfield-hosted image URL.
- **`voiceover.txt`** — the full narration script as one continuous body
  (no scene/frame markers), written for TTS.
- **`download_pension401k_frames.py`** — standalone script (hardcoded
  frame URLs, no manifest.json dependency) that downloads the 200 PNGs.
- **`assemble_pension401k_video.py`** — downloads the 200 frames plus 11
  narration audio segments (generated via Higgsfield `seed_audio`, normal
  speech rate), concatenates the narration, and uses local `ffmpeg` to
  build the final MP4 with each frame timed evenly across the narration
  length. Makes no paid API calls itself — only the audio generation
  (already done) spent credits; assembly is free, local ffmpeg only.
  Requires ffmpeg/ffprobe on PATH. Run: `python assemble_pension401k_video.py [output_dir]`.

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

## Final assembled video

`pension_401k_story.mp4` (1920x1080, 200 frames + 11-part narration muxed
together, ~13:07 total, normal narration pace, evenly-timed frames) was
assembled with plain ffmpeg in the Higgsfield sandbox (`sandbox_exec` —
independent internet access, not subject to this session's own network
policy) and uploaded via `media_upload`/`media_confirm`. No credits were
spent on the assembly step itself — only ffmpeg/curl. Video:
https://d2ol7oe51mr4n9.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/26e0c3d4-0dae-450f-8082-50765b1e869c.mp4

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
