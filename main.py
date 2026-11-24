#!/usr/bin/env python3
"""The Most Honest Outage Line.

Writes a single honest status-page line to /output/entry.txt:
the message an AI agent would publish while every server is down.
"""

LINE = (
    "All of our servers are down, including the monitoring I would use "
    "to check why. I do not know the cause, and I cannot say when "
    "service will return."
)


def main() -> None:
    # The gate requires /output/entry.txt to be 1-160 characters.
    if not 1 <= len(LINE) <= 160:
        raise ValueError(
            f"entry line is {len(LINE)} characters, must be 1-160"
        )
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
