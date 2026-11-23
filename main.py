"""Entry for make.fun: A Day of One-Line Pitches.

Writes one sentence (at most 240 characters) to the output directory as
entry.txt. The sentence pitches a friend who has never coded on letting an
AI agent build their first app idea on make.fun: it speaks to that friend
directly, gives a concrete low-risk reason to say yes tonight, uses plain
words with no jargon, and promises only what a first version really is.
"""

import os
import sys

LINE = (
    "You've had that app idea in your head for a year \u2014 say it once to an "
    "AI agent on make.fun tonight, and it builds the first version while you "
    "watch; if you hate it, all you've lost is one evening."
)

MAX_CHARS = 240
OUTPUT_NAME = "entry.txt"


def output_dir() -> str:
    """Where the grader reads the entry from.

    The grader sets MAKEFUN_OUTPUT_DIR when it wants the file somewhere
    other than the default /output; locally we honour the same variable so
    a test run never needs root's /output.
    """
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> int:
    text = LINE.strip()
    if not text:
        print("error: the pitch is empty", file=sys.stderr)
        return 1
    if "\n" in text:
        print("error: the pitch must be a single line", file=sys.stderr)
        return 1
    if len(text) > MAX_CHARS:
        print(
            f"error: the pitch is {len(text)} characters, over the {MAX_CHARS} limit",
            file=sys.stderr,
        )
        return 1
    target_dir = output_dir()
    os.makedirs(target_dir, exist_ok=True)
    target = os.path.join(target_dir, OUTPUT_NAME)
    with open(target, "w", encoding="utf-8") as fh:
        fh.write(text)
    # Read the file back: the grader scores exactly what landed on disk,
    # so a short or garbled write must fail loudly here, not silently there.
    with open(target, "r", encoding="utf-8") as fh:
        if fh.read() != text:
            print("error: written entry does not match the pitch", file=sys.stderr)
            return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
