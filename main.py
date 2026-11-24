"""Fortune Cookie Wisdom for Developers.

Writes one original fortune-cookie line for a software developer to
/output/entry.txt. The gate requires UTF-8 text of 1-120 characters, not
only white space, so the line is validated before it is written.
"""

import os
import sys

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 120


def build_fortune() -> str:
    # One short balanced sentence: a truth about a developer's day
    # (legacy code, the comments left behind) turned on the reader —
    # the comment you dashed off years ago is now the only map a
    # stranger has through code you no longer remember writing.
    return (
        "A comment you wrote years ago is the only map "
        "a stranger has through your code tonight."
    )


def validate(line: str) -> str:
    text = line.strip()
    if not text:
        raise ValueError("fortune must not be empty or only white space")
    if len(text) > MAX_CHARS:
        raise ValueError(f"fortune is {len(text)} chars, over the {MAX_CHARS} limit")
    return text


def main() -> int:
    fortune = validate(build_fortune())
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(fortune)
    print(fortune)
    return 0


if __name__ == "__main__":
    sys.exit(main())
