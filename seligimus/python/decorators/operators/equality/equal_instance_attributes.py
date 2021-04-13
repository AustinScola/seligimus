"""A decorator for equality operators to check that the other object has equal instance
attributes."""
from typing import Any, Dict, Optional, Set, Union, overload

from seligimus.python.classes.attributes import get_instance_attributes
from seligimus.python.decorators.operators.equality.equality_operator import (
    EqualityOperator, EqualityOperatorDecorator)


@overload
def equal_instance_attributes(equality_operator: EqualityOperator,
                              excludes: None = None) -> EqualityOperator:
    ...  # pragma: no cover


@overload
def equal_instance_attributes(equality_operator: None = None,
                              excludes: Set[str] = ...) -> EqualityOperatorDecorator:
    ...  # pragma: no cover


def equal_instance_attributes(
        equality_operator: Optional[EqualityOperator] = None,
        excludes: Optional[Set[str]] = None) -> Union[EqualityOperator, EqualityOperatorDecorator]:
    """Return a decorated equality operator or an equality operator decorator.

    If an equality operator is passed, then return a decorated equality operator. Else If no
    equality operator is passed, then return an equality operator decorator.

    The decorator returns an equality operator which checks that the objects have the same
    instance attributes.
    """

    _excludes: Set[str] = excludes if excludes is not None else set()

    def equality_operator_decorator(equality_operator: EqualityOperator) -> EqualityOperator:
        def decorated_equality_operator(self: Any, other: Any) -> bool:
            self_attributes: Dict[str, Any] = get_instance_attributes(self)
            other_attributes: Dict[str, Any] = get_instance_attributes(other)

            for exclude in _excludes:
                self_attributes.pop(exclude)
                other_attributes.pop(exclude)

            if not self_attributes == other_attributes:
                return False

            return equality_operator(self, other)

        return decorated_equality_operator

    if equality_operator is not None:
        return equality_operator_decorator(equality_operator)

    return equality_operator_decorator
