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
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, default=Path("manifest.json"))
    parser.add_argument("--out", type=Path, default=Path("frames"))
    # parse_known_args ignores stray args Jupyter injects (e.g. -f kernel.json)
    args, _ = parser.parse_known_args()
    download_frames(args.manifest, args.out)
