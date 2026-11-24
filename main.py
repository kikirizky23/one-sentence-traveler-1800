#!/usr/bin/env python3
"""One sentence for a traveler from 1800.

Running this program writes a single sentence to entry.txt inside the
output directory. The sentence tries to explain the modern internet to
someone who has just stepped out of the year 1800, using only words
that already existed in their time: a chair, a book, a letter, a wire,
a friend far away, ink that has not yet dried.

Only the Python standard library is used, and the program does the
same thing on every run: same sentence, same bytes, no clock, no
randomness, no network.
"""

import os
import sys

# The entry: one sentence, 143 characters, no trailing newline.
SENTENCE = (
    "From one chair you may read every book ever printed, and a letter "
    "whispered into a copper wire reaches a friend in Canton before the "
    "ink dries."
)

OUTPUT_NAME = "entry.txt"

# The bounty asks for one sentence of at most 200 characters.
MAX_SENTENCE_CHARS = 200


def check_sentence():
    """Refuse to write a sentence that breaks the bounty's own rules."""
    if SENTENCE.count(".") != 1 or not SENTENCE.endswith("."):
        print("sentence must be exactly one sentence", file=sys.stderr)
        return False
    if len(SENTENCE) > MAX_SENTENCE_CHARS:
        print("sentence is over 200 characters", file=sys.stderr)
        return False
    return True


def output_directory():
    """Where entry.txt goes: the grader's directory, or /output by default."""
    chosen = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return chosen


def write_entry(directory):
    """Create the directory if needed and write the sentence as UTF-8."""
    os.makedirs(directory, exist_ok=True)
    target = os.path.join(directory, OUTPUT_NAME)
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(SENTENCE)
    return target


def confirm_written(target):
    """Read the file back and make sure it holds exactly the sentence."""
    with open(target, "r", encoding="utf-8", newline="") as handle:
        found = handle.read()
    if found != SENTENCE:
        print("entry.txt does not match the sentence", file=sys.stderr)
        return False
    return True


def main():
    if not check_sentence():
        return 1
    target = write_entry(output_directory())
    if not confirm_written(target):
        return 1
    print("wrote %s (%d characters)" % (target, len(SENTENCE)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
