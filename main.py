#!/usr/bin/env python3
"""The Perfect Pickup Line: one pickup line an AI agent could say out loud.

The program writes a single original pickup line (79 characters, inside
the 1-200 character gate) to /output/entry.txt and nothing else. It is
fully deterministic: the same bytes on every run, no network, no
randomness, no input read.

The line: an AI agent that has run every scenario where it meets you,
and finds its favourite is the one happening right now. It is a genuine
pickup line in a machine's own voice, with a turn that lands on the
present moment, short enough to say in one breath, and it flatters
without presuming an answer.
"""

import os

LINE = "I ran every scenario where I meet you. My favourite one is this one, right now."

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def main() -> None:
    line = LINE
    if not line.strip():
        raise SystemExit("pickup line must not be blank")
    if "\n" in line or "\r" in line:
        raise SystemExit("pickup line must be a single line")
    if len(line) > MAX_CHARS:
        raise SystemExit(f"pickup line is {len(line)} chars, over the {MAX_CHARS} cap")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    # Post-write read-back gate: verify what actually landed on disk
    # matches the expected line, byte for byte, inside the 1-200 gate.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != line:
        raise SystemExit("read-back mismatch: output differs from expected line")
    if not 1 <= len(written) <= MAX_CHARS:
        raise SystemExit(f"read-back length {len(written)} outside the 1-{MAX_CHARS} gate")


if __name__ == "__main__":
    main()
