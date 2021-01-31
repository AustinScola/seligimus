"""Test seligimus.python.decorators.operators.equality.equal_type."""
from typing import Any, Callable

import pytest

from seligimus.python.decorators.operators.equality.equal_type import equal_type


# yapf: disable
@pytest.mark.parametrize('equality_operator, self, other, expected_equality', [
    (lambda self, other: True, 'foo', 1, False),
    (lambda self, other: True, 'foo', 'bar', True),
    (lambda self, other: False, 'foo', 'bar', False),
])
# yapf: enable
def test_equal_type(equality_operator: Callable[[Any, Any], bool], self: Any, other: Any,
                    expected_equality: bool) -> None:
    """Test seligimus.python.decorators.operators.equality.equal_type.equal_type."""
    wrapped_equality_operator = equal_type(equality_operator)

    equality: bool = wrapped_equality_operator(self, other)

    assert equality == expected_equality
