"""A decorator for equality operators to check that the other object has the same type and the same
instance attributes."""
from typing import Any, Callable

from seligimus.python.decorators.operators.equality.equal_instance_attributes import \
    equal_instance_attributes
from seligimus.python.decorators.operators.equality.equal_type import equal_type


def standard_equality(_equality_operator: Callable[[Any, Any], bool]) -> Callable[[Any, Any], bool]:
    """A decorator for equality operators to check that the other object has the same type and the
    same instance attributes."""
    standard_equality_operator = equal_type(equal_instance_attributes(lambda self, other: True))

    return standard_equality_operator
