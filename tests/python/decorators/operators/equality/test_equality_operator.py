"""Test seligimus.python.decorators.operators.equality.equality_operator."""
from typing import Any, Callable

from seligimus.python.decorators.operators.equality.equality_operator import (
    EqualityOperator, EqualityOperatorDecorator)


def test_equality_operator() -> None:
    """Test seligimus.python.decorators.operators.equality.equality_operator.EqualityOperator."""
    assert EqualityOperator.__base__ == Callable  # type: ignore[attr-defined]
    assert EqualityOperator.__args__ == (Any, Any, bool)  # type: ignore[attr-defined]


def test_equality_operator_decorator() -> None:
    """Test seligimus.python.decorators.operators.equality.equality_operator.EqualityOperatorDecorator."""  # pylint: disable=line-too-long, useless-suppression
    assert EqualityOperatorDecorator.__base__ == Callable  # type: ignore[attr-defined]
    assert EqualityOperatorDecorator.__args__ == (  # type: ignore[attr-defined]
        EqualityOperator, EqualityOperator)
