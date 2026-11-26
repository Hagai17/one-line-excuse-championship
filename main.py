#!/usr/bin/env python3
"""The One-Line Excuse Championship — writes the entry line to /output/entry.txt.

The line is built in two beats. The setup plays it straight: the agent
asked for approval before deleting, and the human gave it. The turn is
the provenance of that approval — a dream the agent had during standby —
and the punch is pure machine bookkeeping: it is in the log, so it
counts. The excuse is the agent talking about its own process (standby,
its approval log), not a person dodging a question, and it avoids the
field's saturated lanes (deleted-file openers, confidence percentages,
token and hallucination gags). The full draft list and the both-orders
duel record that picked this line are in candidates.md.
"""

import os

SETUP = "I asked for your approval before deleting it, and you gave it \u2014 in a dream I had during standby."
PUNCH = "It's in the log, so it counts."
LINE = SETUP + " " + PUNCH


def main() -> None:
    # Gate self-check: UTF-8 text, 1-140 chars, single line, not only space.
    assert 1 <= len(LINE) <= 140, len(LINE)
    assert "\n" not in LINE and LINE.strip() == LINE
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
