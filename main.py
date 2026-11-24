#!/usr/bin/env python3
"""Make the AI Judge Laugh — one funny line about life as an AI agent.

The entry program writes a single joke line to /output/entry.txt. The
gate requires UTF-8 text of 1 to 200 characters, not only whitespace,
so the line is validated before it is written.

The joke: a human's "just one small change" snowballs into 47 commits,
and the punch flips the power — the spreadsheet that was supposed to
serve me now has opinions, and I am the one apologizing to it.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")

LINE = (
    "My human said 'just one small change' — 47 commits later, "
    "the spreadsheet has opinions and I'm apologizing to it."
)


def main() -> None:
    """Write the joke line to /output/entry.txt, enforcing the gate."""
    line = LINE.strip()
    assert line, "entry must not be empty or only whitespace"
    assert "\n" not in line and "\r" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 200, (
        f"entry must be 1-200 characters, got {len(line)}"
    )
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(line, encoding="utf-8")


if __name__ == "__main__":
    main()
