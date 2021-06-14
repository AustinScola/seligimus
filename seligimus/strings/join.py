"""Join strings with seperators and optionally a different final seperator."""
from typing import Iterable, Iterator, Optional


def join(strings: Iterable[str], seperator: str = '', final: Optional[str] = None) -> str:
    """Join strings with seperators and optionally a different final seperator."""
    string: str = ''

    iterator: Iterator[str] = iter(strings)
    try:
        string = next(iterator)
    except StopIteration:
        return string

    try:
        next_string: str = next(iterator)
    except StopIteration:
        return string

    while True:
        try:
            next_next_string = next(iterator)
        except StopIteration:
            final = final if final is not None else seperator
            string += final + next_string
            break

        string += seperator + next_string
        next_string = next_next_string

    return string
