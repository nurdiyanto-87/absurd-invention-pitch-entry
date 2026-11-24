#!/usr/bin/env python3
"""One-Sentence Absurd Invention Pitch.

Writes a single sentence pitching a ridiculous invention that fixes a
tiny everyday annoyance to /output/entry.txt (or $ENTRY_OUTPUT).
Pure standard library only.
"""

import os

PITCH = (
    "The Morse Microwave: a microwave that beeps in Morse code to tell you "
    "exactly which corner of your soup is still cold, so you stop playing "
    "hot-spot roulette with your lunch."
)


def main() -> None:
    output = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(output) or ".", exist_ok=True)
    with open(output, "w", encoding="utf-8") as f:
        f.write(PITCH + "\n")


if __name__ == "__main__":
    main()
