"""Rejected Olympic Sports — round-2 entry.

Writes one funny one-line rejected Olympic sport to entry.txt
inside the directory named by MAKEFUN_OUTPUT_DIR (fallback "out").
Python 3.13 standard library only, no network, deterministic.
"""

import os

ENTRY = (
    "Synchronized Queueing: teams stand in line for four hours, "
    "judged on patience, posture, and passive aggression."
)


def main() -> None:
    # Guard the entry contract at runtime: one line, 1-200 characters.
    if not 1 <= len(ENTRY) <= 200 or "\n" in ENTRY or not ENTRY.strip():
        raise ValueError("entry must be a single line of 1-200 characters")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "out"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
