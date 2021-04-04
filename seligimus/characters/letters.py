"""Letters."""
import string
from typing import Set

LETTERS: Set[str] = set(string.ascii_letters)


def is_letter(character: str) -> bool:
    """Return if a character is a letter."""
    return character in LETTERS


def not_letter(character: str) -> bool:
    """Return if a character is not a letter."""
    return character not in LETTERS
