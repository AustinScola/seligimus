"""Function for finding the index of an element in an iterable which satisfies a predicate."""
from typing import Callable, Iterable, Optional, TypeVar

T = TypeVar('T')  # pylint: disable=invalid-name


def index(iterable: Iterable[T], predicate: Callable[[T], bool]) -> int:
    """Return the index of an element in an iterable which satisfies a predicate."""
    index_: Optional[int] = None
    for index_, element in enumerate(iterable):
        if predicate(element):
            return index_

    message: str
    if index_ is None:
        message = 'The iterable is empty.'
    else:
        message = 'Could not find an element in the iterable which satisfies the predicate.'
    raise IndexError(message)
