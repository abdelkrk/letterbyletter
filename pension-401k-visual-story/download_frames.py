#!/usr/bin/env python3
"""Bulk-download the 200 pension-401k video frames from manifest.json.

Usage:
    pip install requests
    python download_frames.py [--manifest manifest.json] [--out ./frames]

Saves each frame as pension401k_001.png ... pension401k_200.png in the
output directory, in frame order, skipping files that already exist so the
script can be safely re-run after a partial/failed run.
"""
import argparse
import json
import sys
import time
from pathlib import Path

import requests


def download_frames(manifest_path: Path, out_dir: Path, retries: int = 3, timeout: int = 30) -> None:
    with manifest_path.open() as f:
        frames = json.load(f)

    frames.sort(key=lambda entry: entry["frame"])
    out_dir.mkdir(parents=True, exist_ok=True)

    total = len(frames)
    failed = []

    for entry in frames:
        n = entry["frame"]
        url = entry.get("url")
        dest = out_dir / f"pension401k_{n:03d}.png"

        if dest.exists() and dest.stat().st_size > 0:
            print(f"[{n:3d}/{total}] skip (already downloaded): {dest.name}")
            continue

        if not url:
            print(f"[{n:3d}/{total}] MISSING URL for frame {n} — skipping")
            failed.append(n)
            continue

        for attempt in range(1, retries + 1):
            try:
                resp = requests.get(url, timeout=timeout)
                resp.raise_for_status()
                dest.write_bytes(resp.content)
                print(f"[{n:3d}/{total}] saved {dest.name} ({len(resp.content):,} bytes)")
                break
            except requests.RequestException as exc:
                print(f"[{n:3d}/{total}] attempt {attempt}/{retries} failed: {exc}")
                if attempt == retries:
                    failed.append(n)
                else:
                    time.sleep(2 * attempt)

    print(f"\nDone: {total - len(failed)}/{total} frames saved to {out_dir}")
    if failed:
        print(f"Failed frames: {failed}")
        sys.exit(1)


if __name__ == "__main__":
    # Default to paths next to this script, not the caller's cwd, so it
    # works the same whether run as `python download_frames.py`, from a
    # Jupyter notebook, or from any other directory.
    script_dir = Path(__file__).resolve().parent

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, default=script_dir / "manifest.json")
    parser.add_argument("--out", type=Path, default=script_dir / "frames")
    # parse_known_args ignores stray args Jupyter injects (e.g. -f kernel.json)
    args, _ = parser.parse_known_args()

    manifest_path = args.manifest
    if not manifest_path.exists():
        # fall back to a manifest.json next to the script even if a bare
        # relative name was passed from a different working directory
        fallback = script_dir / manifest_path.name
        if fallback.exists():
            manifest_path = fallback
        else:
            raise SystemExit(
                f"Could not find manifest.json.\n"
                f"  tried: {manifest_path.resolve()}\n"
                f"  tried: {fallback.resolve()}\n"
                f"Put manifest.json next to this script, or pass --manifest <full path>."
            )

    print(f"Manifest: {manifest_path.resolve()}")
    print(f"Output dir: {args.out.resolve()}")
    download_frames(manifest_path, args.out)
