#!/usr/bin/env python3
"""One Word From Grandma: the single word grandma would text about AI.

Writes the word to /output/entry.txt. Stdlib only, deterministic, no
network. The output directory itself is never removed; this program only
writes its own file into it.
"""

import os

WORD = "Alexa"

if not WORD or any(ch.isspace() for ch in WORD):
    raise ValueError("entry must be exactly one word")

OUT_DIR = "/output"
OUT_FILE = os.path.join(OUT_DIR, "entry.txt")


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(OUT_FILE, "w", encoding="utf-8", newline="") as handle:
        handle.write(WORD)


if __name__ == "__main__":
    main()
