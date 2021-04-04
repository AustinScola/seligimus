"""Lowercase letters."""
import string
from typing import Set

LOWERCASE_LETTERS: Set[str] = set(string.ascii_lowercase)


def is_lowercase_letter(character: str) -> bool:
    """Return if a character is a lowercase letter."""
    return character in LOWERCASE_LETTERS


def not_lowercase_letter(character: str) -> bool:
    """Return if a character is not a lowercase letter."""
    return character not in LOWERCASE_LETTERS
