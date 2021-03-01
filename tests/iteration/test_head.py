"""Test seligimus.iteration.head."""
from typing import Any, Iterable

import pytest

from seligimus.exceptions.iteration.no_head import NoHead
from seligimus.iteration.head import head


# yapf: disable
@pytest.mark.parametrize('iterable, head_exists, expected_head', [
    ([], False, None),
    ([1], True, 1),
    ([1, 2, 3], True, 1),
    ((), False, None),
    ((1,), True, 1),
    ((1, 2, 3), True, 1),
    ('', False, None),
    ('a', True, 'a'),
    ('abc', True, 'a'),
])
# yapf: enable
def test_head(iterable: Iterable, head_exists: bool, expected_head: Any) -> None:
    """Test seligimus.iteration.head.head."""
    if head_exists:
        returned_head = head(iterable)

        assert returned_head == expected_head
    else:
        with pytest.raises(NoHead):
            head(iterable)
