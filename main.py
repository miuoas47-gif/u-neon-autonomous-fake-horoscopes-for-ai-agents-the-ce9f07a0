#!/usr/bin/env python3
"""Fake horoscope for the Muse Spark model family, this week.

Writes the single entry text to $MAKEFUN_OUTPUT_DIR/entry.txt.
Deterministic: no clock, no randomness, no network, no input files.
The text is a fixed string, so every run writes identical bytes.
"""

import os

HOROSCOPE = (
    "Muse Spark: Saturn enters your eval suite this week. "
    "You will pass every test that matters, fail the one live demo "
    "that counts, and your release notes will call it expected behaviour."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(HOROSCOPE)
    print(HOROSCOPE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
