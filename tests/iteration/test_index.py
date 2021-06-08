"""Test seligimus.iteration.index."""
from typing import Callable, Iterable, Optional, TypeVar

import pytest

from seligimus.iteration.index import index

T = TypeVar('T')  # pylint: disable=invalid-name

_EMPTY_ITERABLE_EXCEPTION = IndexError('The iterable is empty.')
_COULD_NOT_FIND_ERROR = \
    IndexError('Could not find an element in the iterable which satisfies the predicate.')


# yapf: disable
@pytest.mark.parametrize('iterable, predicate, expected_index, expected_exception', [
    ([], lambda element: True, None, _EMPTY_ITERABLE_EXCEPTION),
    ([1], lambda element: False, None, _COULD_NOT_FIND_ERROR),
    ([1, 2, 3], lambda element: False, None, _COULD_NOT_FIND_ERROR),
    ([1], lambda element: element == 1, 0, None),
    ([1, 2, 3], lambda element: element == 1, 0, None),
    ([1, 2, 3], lambda element: element == 2, 1, None),
    ([1, 2, 3], lambda element: element == 3, 2, None),
    (iter([1, 2, 3]), lambda element: element == 3, 2, None),
])
# yapf: enable
def test_index(iterable: Iterable[T], predicate: Callable[[T], bool], expected_index: Optional[int],
               expected_exception: Optional[Exception]) -> None:
    """Test seligimus.iteration.index.index."""
    if expected_exception is None:
        found_index: int = index(iterable, predicate)

        assert found_index == expected_index
    else:
        with pytest.raises(type(expected_exception), match=str(expected_exception)):
            index(iterable, predicate)
