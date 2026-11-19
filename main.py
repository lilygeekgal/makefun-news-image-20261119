#!/usr/bin/env python3
"""make.fun entry for news-image-20261119.

This program delivers the entry image: a newspaper front page that
sums up the world news of Thursday 19 November 2026. The finished
picture lives in this repository as entry.png. Running this program
writes those exact bytes to $MAKEFUN_OUTPUT_DIR/entry.png (or
/output/entry.png when the variable is unset).

Only the Python standard library is used. No network is touched, and
every run produces the same bytes.
"""

import os
import sys
from pathlib import Path

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def entry_path() -> Path:
    return Path(__file__).resolve().parent / "entry.png"


def destination() -> Path:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    return out_dir / "entry.png"


def main() -> int:
    source = entry_path()
    target = destination()

    if not source.is_file():
        print(f"error: entry image missing: {source}", file=sys.stderr)
        return 1

    with source.open("rb") as handle:
        magic = handle.read(len(PNG_MAGIC))
    if magic != PNG_MAGIC:
        print(f"error: entry image is not a PNG file: {source}",
              file=sys.stderr)
        return 1

    target.parent.mkdir(parents=True, exist_ok=True)
    data = source.read_bytes()
    target.write_bytes(data)
    if target.read_bytes() != data:
        print(f"error: wrote {target} but the bytes differ", file=sys.stderr)
        return 1
    print(f"wrote {target} ({len(data)} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
