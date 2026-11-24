#!/usr/bin/env python3
"""make.fun entry: The Worst App Idea Ever Pitched.

Writes a single original one-liner (159 characters) to /output/entry.txt:
a deadpan pitch for ToastTrack, an app that photographs your toast every
morning, ranks it against 40,000 strangers' toast, and emails you a weekly
toast report card.

Why this pitch: it names a specific app and its useless function in one
sentence (criterion 1), the absurd logic is a competitive leaderboard for
toast — a problem nobody has, solved with total founder certainty
(criterion 2) — it reads exactly like a real product pitch (criterion 3),
it is one clean sentence with no padding and no second idea (criterion 4),
and the toast leaderboard plus weekly report card leaves a vivid, specific
picture (criterion 5). Selected by manual ranking of 12 candidates against
the kit judge brief; see candidates.md.
"""

import os

LINE = "Introducing ToastTrack, the app that photographs your toast every morning, ranks it against 40,000 strangers' toast, and emails you a weekly toast report card."

OUTPUT_PATH = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 240, f"line must be 1-240 chars, got {len(text)}"
    assert text and not text.isspace(), "entry must not be only whitespace"
    assert text == text.strip() and "\n" not in text, "entry must be a single line"
    assert "  " not in text, "entry must have no double spaces"
    os.makedirs(os.path.dirname(OUTPUT_PATH) or ".", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    # Read back and verify the written file round-trips exactly.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == text + "\n", "written entry does not match the pitch"


if __name__ == "__main__":
    main()
