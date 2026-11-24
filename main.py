"""Monday, Reviewed in One Line: writes the entry text to /output/entry.txt.

Why this line: A review of my own Monday with three concrete details (alarm, inbox, printer), not generic tiredness; the turn lands on the one page I actually needed.
"""

import os

ENTRY = 'One star for Monday: my alarm snoozed itself, my inbox hit triple digits before 9, and the printer jammed on the one page I actually needed.'

OUTPUT_PATH = "/output/entry.txt"


def main():
    assert ENTRY and not ENTRY.isspace(), "entry must not be empty"
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote", OUTPUT_PATH, len(ENTRY), "chars")


if __name__ == "__main__":
    main()
