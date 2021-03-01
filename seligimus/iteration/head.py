"""The first item in an iterable."""
from typing import Any, Iterable

from seligimus.exceptions.iteration.no_head import NoHead


def head(iterable: Iterable) -> Any:
    """Return the first item in an iterable."""
    try:
        return next(iter(iterable))
    except StopIteration as stop_iteration_exception:
        raise NoHead() from stop_iteration_exception
