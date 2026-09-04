# Handover: Lessons from the Granada Project (for the next video)

This documents real mistakes made during the Granada 100-image/TTS/video
project, with the specific fix for each, so the next project starts from
these instead of repeating them.

## 1. Cost discipline — the big one

**Mistake:** Ran `get_cost:true` on a short ~15-word test sentence, got
0.15 credits, then assumed that price was flat and generated 7 long
chapter chunks (60-285 words each) without re-checking. Actual cost:
0.30-4.95 credits per chunk, totaling 22.95 credits instead of the
~1 credit assumed. Nobody was warned before the money was spent.

**Fix, always:**
- Run `get_cost:true` on the **actual full-length content**, not a
  sample snippet, before any production-scale generation.
- After generating, **verify actual spend against the ledger**
  (`mcp__higgs_field__transactions`, paginate with `cursor` if the
  project spans more than ~100 transactions) — don't just trust the
  `get_cost` preview or your own running mental tally. Match by
  `display_name` + `created_at` timestamp to isolate this project's
  charges from any unrelated prior activity on the account.
- Report real, ledger-verified numbers, not estimates presented as fact.

## 2. Never guess model-specific IDs (voice names, etc.)

**Mistake:** When `qwen_audio_tts` needed a voice_id, guessed plausible
English names (Ethan, Cherry, Chelsie, Serena) based on general knowledge
of what Qwen-TTS voices are usually called. All failed with
"Voice not found." Wasted calls, no progress.

**Fix:** There is no tool to list Qwen's own preset voice names. Instead,
use a voice you already know works (e.g. from `list_voices` or a prior
successful generation) and check its **metadata for a `supported_models`
field** — visible in a completed generation's full result (via
`job_display`/`show_generation_by_ids`), not in the plain `list_voices`
listing. Example: the "Marcus" preset voice
(`voice_id: 6f98d3dd-324f-4845-8c28-c1d1647a06cd`) lists
`["elevenlabs","minimax","seed_speech","qwen_audio"]` — so it's usable
directly with `model: "qwen_audio_tts"`. This turned out to be the
actual cheapest working Arabic TTS: **~0.05 credits per short sentence**,
confirmed via the ledger (display_name "Qwen Audio 3.0 TTS Flash"),
vs. ~0.45+ credits for the same sentence on `text2speech_v2`/elevenlabs.
For the next project, **default to `qwen_audio_tts` + Marcus (or another
voice confirmed to list qwen_audio) instead of elevenlabs**, and confirm
with one real `get_cost` + one real generation on the actual full script
length before committing to it for all chunks.

## 3. Cheapest image model can silently fail

**Mistake:** `z_image` priced cheapest (0.15 credits) but all 5 test
generations sat at `status: "queued"` for minutes, then flipped to
`status: "failed"` with **no error message at all** — nothing in
`job_display` to explain why. Net cost ended up 0 (auto-refunded), but
time was lost.

**Fix:** Don't assume the cheapest listed model is reliable. Test with
1 image first. If it queues for more than ~60-90s with no progress,
treat it as broken for this session and fall back immediately (in this
project, `kling_omni_image` at 0.5 credits/image was reliable for all 99
remaining images). Don't burn multiple retries hoping it recovers.

## 4. sandbox_exec / ffmpeg pipeline bugs

This environment cannot reach Higgsfield's CDN directly (org network
policy blocks it) — `sandbox_exec` (separate remote sandbox, own network
path, ffmpeg/curl preinstalled, **zero AI credits**) is the only way to
download generated assets or do local video/audio processing. Bugs hit
along the way:

- **`ffmpeg` reads stdin by default.** Any `ffmpeg` call made *inside* a
  `while read ... < file` loop will silently consume lines from that same
  file as its own stdin, corrupting the loop after the first iteration
  (symptoms: garbled/truncated variable values on later iterations, "file
  not found" for nonsense filenames). **Always add `-nostdin` (and/or
  `< /dev/null`) to every ffmpeg invocation**, not just ones you suspect.
- **Don't string-interpolate shell variables into an `awk` program.**
  `awk "BEGIN{n=int(${dur}*30+0.5)}"` is fragile to quoting/locale
  issues. Pass values in with `-v`: `awk -v d="$dur" 'BEGIN{...}'`.
- **`seq -w` zero-pads to the width of the largest number in *that*
  range**, not a fixed width — `seq -w 1 25` gives `01`..`25` (2 digits),
  which silently mismatched `001.mp4`-style 3-digit filenames used
  elsewhere in the same pipeline. Use `printf "%03d"` in a loop instead
  of relying on `seq -w` when filenames need a fixed digit count.
- **`zoompan` motion looks shaky/jittery**, especially when the source
  image is smaller than the output (e.g. 1344x768 source to 1920x1080
  output). Cause: zoompan crops at whole-pixel positions per frame; tiny
  per-frame zoom increments often round to the same pixel for several
  frames then jump, and the upscale amplifies that jump into visible
  jitter. **Fix for next time: supersample** — run zoompan at 2-3x the
  final target resolution, then downscale the result to final size with
  a high-quality scaler (e.g. lanczos). This wasn't fixed in this
  project's delivered video; do it from the start next time.
- **Long-running background jobs:** use `background:true` for anything
  over ~1-2 minutes, then poll with short (`timeout_seconds` ~20-30)
  calls. Long `sleep N` (~60s) inside a poll call can itself hit the
  tool's timeout — prefer several short polls over one call with a long
  `sleep`. Reading `ps aux` CPU-TIME column is cumulative CPU time, not
  wall-clock elapsed (easy to misread as "it's taking forever" on a
  multi-threaded encode when wall-clock elapsed is actually small).
- Binary media produced in the sandbox (images, audio, final video)
  cannot be pulled into this coding environment's own filesystem/repo —
  only text/CSV deliverables can live in the git repo. Finished videos
  need `media_upload` (get presigned URL) -> `curl PUT` from *inside* the
  same sandbox call that produced the file -> `media_confirm`, then hand
  the resulting CDN URL to the user (same limitation as every other
  asset in this project).

## 5. Batch generation quirks

- `generate_image_batch`/`generate_audio_batch` cap at 12 items per call.
- Batches can partially fail mid-submission with `rate_limit_reached` —
  check `submitted_count`/`failed_count` in the response, and retry only
  the failed indices individually (not the whole batch) rather than
  resubmitting everything.

## 6. What worked well — keep doing this

- Writing a durable frame-by-frame storyboard (`granada_storyboard.txt`)
  with story purpose / visual action / matched sentence / image prompt
  for every frame, kept consistent across many separate generation
  batches over a long session.
- Locking a consistent character description block (face, clothing,
  proportions) and re-pasting it verbatim into every prompt for a given
  character/age, rather than re-describing them each time.
- Deriving final frame timing from **real measured audio durations**
  (via `ffprobe`) rather than estimating narration length in advance.
- Keeping a running written cost tally per phase in the repo
  (`asset_report.txt`, `tts_settings.txt`) — just remember to verify it
  against the transactions ledger before reporting it as final.
