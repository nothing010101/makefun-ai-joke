#!/usr/bin/env python3
"""Make the AI judge laugh - make.fun bounty ai-joke-03.

Writes exactly one original joke about AI coding agents to
/output/entry.txt (the file the make.fun grader reads).

Deterministic: no network, no randomness, no time dependence -
every run writes the same bytes.
"""

import os

JOKE = (
    "My AI coding agent had one job: fix a typo. "
    "It fixed the typo, rewrote the entire auth system, "
    "and left a commit message that just says 'you're welcome.'"
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # The grader reads exactly this file: 1-280 chars, not blank.
    # Fail loudly instead of submitting an invalid joke.
    if not 1 <= len(JOKE) <= 280 or not JOKE.strip():
        raise SystemExit("joke must be 1-280 chars and not blank")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)
    print(JOKE)


if __name__ == "__main__":
    main()
