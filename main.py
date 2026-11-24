"""Alien Field Notes: The Two Day Earth Review -- make.fun entry.

One line, at most 200 characters: a review of planet Earth left by an
alien tourist -- a beautiful blue planet with friendly locals, marred
only by cashiers who ask how your day is going and then wait for an
answer. The program validates the line, prints it, and writes it to
/output/entry.txt.
Pure Python 3.13 standard library only; deterministic; no network.
SPDX-License-Identifier: MIT
"""

import os

TEXT = (
    "Beautiful blue planet, friendly locals, excellent sunsets — but "
    "every cashier asks how my day is going and then waits for an "
    "answer. 4/5 stars, would visit again."
)

MAX_LENGTH = 200
DESTINATION = "/output/entry.txt"


def validate(text):
    """Require one non-blank line of at most 200 characters."""
    if not isinstance(text, str):
        raise ValueError("review must be text")
    if text != text.strip() or not text:
        raise ValueError("review must be a non-blank line")
    if "\n" in text or "\r" in text:
        raise ValueError("review must be a single line")
    if len(text) > MAX_LENGTH:
        raise ValueError("review is %d characters, over the 200 limit" % len(text))
    return text


def emit(text):
    """Print the review and write it to /output/entry.txt."""
    print(text)
    os.makedirs(os.path.dirname(DESTINATION), exist_ok=True)
    with open(DESTINATION, "w", encoding="utf-8") as out:
        out.write(text + "\n")


def main():
    # Validate first, so only a well-formed review ever reaches the file.
    emit(validate(TEXT))


if __name__ == "__main__":
    main()
