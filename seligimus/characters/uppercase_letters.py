"""Uppercase letters."""
import string
from typing import Set

UPPERCASE_LETTERS: Set[str] = set(string.ascii_uppercase)


def is_uppercase_letter(character: str) -> bool:
    """Return if a character is an uppercase letter."""
    return character in UPPERCASE_LETTERS


def not_uppercase_letter(character: str) -> bool:
    """Return if a character is not an uppercase letter."""
    return character not in UPPERCASE_LETTERS
