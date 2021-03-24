"""Test seligimus.python.decorators.operators.equality.equality_operator."""
from typing import Any, Callable

from seligimus.python.decorators.operators.equality.equality_operator import EqualityOperator


def test_equality_operator() -> None:
    """Test seligimus.python.decorators.operators.equality.equality_operator.EqualityOperator."""
    assert EqualityOperator.__base__ == Callable  # type: ignore[attr-defined]
    assert EqualityOperator.__args__ == (Any, Any, bool)  # type: ignore[attr-defined]
