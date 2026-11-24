#!/usr/bin/env python3
"""Weirdest Job Title entry: write one job title to /output/entry.txt.

The title is a fixed, hand-picked string. The program does no I/O besides
writing that string, takes no input, and uses no randomness, clock, network,
or environment, so two runs produce byte-identical output.
"""

import os

TITLE = "Professional Mourner for Strangers' Goldfish"

OUTPUT_PATH = "/output/entry.txt"


def validate(title: str) -> None:
    """Enforce the competition gate before writing anything.

    The sealed scorer accepts only UTF-8 text of 1 to 60 characters that is
    not only whitespace; an invalid entry is never judged and takes no prize.
    Fail loudly here instead of shipping a bad file.
    """
    if not (1 <= len(title) <= 60):
        raise ValueError(f"title is {len(title)} chars, gate needs 1-60")
    if not title.strip():
        raise ValueError("title is only whitespace")
    title.encode("ascii")  # keep the file plain ASCII: no encoding surprises


def main() -> None:
    validate(TITLE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(TITLE)


if __name__ == "__main__":
    main()
