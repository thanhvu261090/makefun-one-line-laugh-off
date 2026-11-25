"""Write one funny line for the One-Line Laugh-Off bounty.

Writes the line to /output/entry.txt. Stdlib only, no network.
The joke: a smart speaker takes "I'm fine" literally and escalates —
pizza, therapist, divorce lawyer — a triple escalation that lands
suddenly on a cold read, with every word earning its place.
"""

import os

ENTRY = (
    'My smart speaker heard me say "I\'m fine" and ordered a pizza, '
    "a therapist, and a divorce lawyer \u2014 just in case."
)


def validate_utf8(text):
    """Confirm the entry encodes cleanly as UTF-8.

    Returns the encoded bytes so callers can also check the byte length.
    Raises UnicodeEncodeError if the text is not encodable.
    """
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    return text.encode("utf-8")


def validate_length(text):
    """Enforce the kit gate: 1-200 characters, single line, non-whitespace.

    Raises ValueError with a specific message naming the failed rule, so a
    bad entry is easy to diagnose instead of failing silently.
    """
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    return True


def gate_check(text):
    """Run every kit-gate validation on the entry text before it is written."""
    validate_utf8(text)
    return validate_length(text)


def self_test():
    """Small self-test: the real entry passes, and each bad input is refused.

    Checks the happy path plus one failure per gate rule, so a future edit
    that breaks validation is caught immediately instead of at submit time.
    Does not write any output file.
    """
    assert gate_check(ENTRY) is True
    assert len(ENTRY) == 111, f"entry length changed: {len(ENTRY)}"
    bad_cases = [
        ("", "empty entry"),
        (" " * 10, "whitespace-only entry"),
        ("x" * 201, "entry over 200 characters"),
        ("two\nlines", "multi-line entry"),
        (" padded ", "entry with surrounding whitespace"),
        (123, "non-string entry"),
    ]
    for bad_text, label in bad_cases:
        try:
            gate_check(bad_text)
        except (ValueError, TypeError, UnicodeEncodeError):
            continue
        raise AssertionError(f"self-test failed: gate accepted {label}")
    return True


def main():
    gate_check(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    self_test()
    main()
