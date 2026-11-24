#!/usr/bin/env python3
"""Make the AI Judge Laugh: Developer Excuses.

Writes one funny single-line excuse a developer gives when code
breaks in production to /output/entry.txt.
"""

import os

EXCUSE = "The code passed all 400 tests \u2014 unfortunately, production wasn't one of them."


def main() -> None:
    # The gate: 1-200 characters, one line, not only whitespace.
    assert 1 <= len(EXCUSE) <= 200, "excuse must be 1-200 characters"
    assert "\n" not in EXCUSE, "excuse must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
