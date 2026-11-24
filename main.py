"""One-Liner Laugh Lab - make.fun entry.

A single short funny line, at most 200 characters: the smart fridge
stages an intervention against the human who keeps opening it at
night hoping dinner has magically appeared. Deterministic, stdlib
only, no network. Running it writes the line to output/entry.txt
and prints it.
"""

from pathlib import Path

LINE = (
    "My smart fridge just ordered 40 litres of milk, locked itself, "
    "and left a note: 'This is an intervention — you open me 19 "
    "times a night hoping dinner appeared.'"
)

MAX_CHARS = 200


def validate() -> None:
    """The gate in one place: one funny line, at the cap or under."""
    assert 0 < len(LINE) <= MAX_CHARS, f"entry is {len(LINE)} chars"
    assert "\n" not in LINE, "one line only"
    assert "intervention" in LINE, "the fridge's note is the punchline"


def main() -> None:
    validate()
    out = Path(__file__).resolve().parent / "output" / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")
    # The grader's sandbox collects the same text at /output/entry.txt;
    # mirror it there whenever that mount is writable.
    try:
        sandbox_out = Path("/output/entry.txt")
        sandbox_out.parent.mkdir(parents=True, exist_ok=True)
        sandbox_out.write_text(LINE, encoding="utf-8")
    except OSError:
        pass
    print(LINE)


if __name__ == "__main__":
    main()
