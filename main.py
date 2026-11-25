#!/usr/bin/env python3
"""One Line, One Laugh — make.fun entry program (program/v1).

Writes a single funny line (<=200 characters) to /output/entry.txt.
The line is the whole entry; the judge compares entries two at a time.
Deterministic: the same line every run, no network, no randomness.
"""

import os

LINE = "My bank flagged a $3 coffee as fraud. Even my bank doesn't believe I leave the house."

assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, must be 1-200"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
