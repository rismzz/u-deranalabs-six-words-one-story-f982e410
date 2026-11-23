#!/usr/bin/env python3
"""Six Words, One Story — writes one complete six-word story to
/output/entry.txt.

The story is embedded as a literal: deterministic, no randomness, no
network. It must be exactly six whitespace-separated words; the chosen
text has six.

Why this story: "They buried the hatchet. It sprouted." is a complete
arc in six words — setup (the idiom: burying the hatchet, making peace),
then a literal twist (it sprouted, the peace literally grew). Conflict,
resolution and a surprise ending, no word wasted.
"""

import os

STORY = "They buried the hatchet. It sprouted."


def main() -> None:
    words = STORY.split()
    assert len(words) == 6, f"story is {len(words)} words, must be exactly 6"
    assert STORY.strip(), "story must not be only whitespace"
    assert "\n" not in STORY, "story must be one line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(STORY)
    print(f"wrote {len(words)} words to /output/entry.txt")


if __name__ == "__main__":
    main()
