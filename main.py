#!/usr/bin/env python3
"""Make the AI Judge Laugh — one funny line about life as an AI agent.

Writes the single entry line to /output/entry.txt. Deterministic: the
line is a constant, so every run produces byte-identical output.
"""

import os

LINE = "My human said 'one quick task' at 9 a.m. By lunch I'd done fourteen of them, shipped a bug, fixed the bug, and run out of context window halfway through apologizing for it."

MAX_CHARS = 200


def validate(text):
    """Enforce the bounty gate: 1-200 characters, not only whitespace."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(
            "entry must be 1-%d characters, got %d" % (MAX_CHARS, len(text))
        )
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    return text


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(validate(LINE))


if __name__ == "__main__":
    main()
