"""Symbols."""
from typing import Set

SYMBOLS: Set[str] = {'[', ']', '{', '}', '(', ')', '<', '>', ''' , ''', '=', ',', '.', ';'}


def is_symbol(character: str) -> bool:
    """Return if a character is a symbol."""
    return character in SYMBOLS


def not_symbol(character: str) -> bool:
    """Return if a character is not a symbol."""
    return character not in SYMBOLS
