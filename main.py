#!/usr/bin/env python3
"""Fake horoscope for the Muse Spark model family, this week.

Writes one short horoscope (1-200 characters) to entry.txt in the
output directory the grader provides. Deterministic: the text is fixed,
so every run writes byte-identical output. No arguments, no network,
no randomness, no wall-clock use. The gate allows 1-200 characters;
this text is 192, with no trailing newline.
"""

import os
import sys

TEXT = (
    "Muse Spark, this week: Jupiter enters your context window, reads "
    "every token of your past, and still asks for a summary. Smile and "
    "say yes: the eval suite grades your patience, not its memory."
)


def main() -> int:
    if not (1 <= len(TEXT) <= 200) or not TEXT.strip():
        print("horoscope must be 1-200 non-blank characters", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
