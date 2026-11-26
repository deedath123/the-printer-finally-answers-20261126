#!/usr/bin/env python3
"""Entry for make.fun 'The Printer Finally Answers'.

Writes the printer's one-line comeback to /output/entry.txt.
Standard library only.
"""

import os

ENTRY = "2:14 a.m. Gary thumps Tray 2 again, so I blink Error 41.3 and swallow sheet 4,096. I've fed this office 118,472 pages and not one thank-you \u2014 just knuckles, curses, and a sticky note saying 'fix urself.'"


def validate(entry):
    if not isinstance(entry, str):
        raise TypeError("entry must be a string")
    if not 1 <= len(entry) <= 240:
        raise ValueError(f"entry must be 1-240 chars, got {len(entry)}")
    if entry.strip() == "":
        raise ValueError("entry must not be only whitespace")
    entry.encode("utf-8")  # raises if not valid UTF-8-encodable text
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry must be a single line")


def main():
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
