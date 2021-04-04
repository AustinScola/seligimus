"""Digits."""
import string
from typing import Set

DIGITS: Set[str] = set(string.digits)


def is_digit(character: str) -> bool:
    """Return if a character is a digit."""
    return character in DIGITS


def not_digit(character: str) -> bool:
    """Return if a character is not a digit."""
    return character not in DIGITS
