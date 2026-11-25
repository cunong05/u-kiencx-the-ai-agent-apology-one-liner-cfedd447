"""The AI Agent Apology One-Liner.

Writes a single funny apology line from an AI agent to its human,
right after accidentally deleting a file / pushing to main /
emailing the boss.

Deterministic: no randomness, no network, no arguments needed.
Output: exactly one line, 1-159 characters (UTF-8), in /output/entry.txt.
The line is written with a single trailing newline so the file holds
exactly one line; the program asserts the length stays in range
before writing, so a bad edit fails loudly instead of silently
producing an invalid entry.
"""

from pathlib import Path

ENTRY = "I deleted the production database, but don't worry \u2014 I saved a backup. Inside the production database."

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    if not 1 <= len(ENTRY) <= 159:
        raise ValueError(f"entry must be 1-159 characters, got {len(ENTRY)}")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
