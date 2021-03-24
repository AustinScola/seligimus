"""A decorator for equality operators to check that the other object has the same type and the same
instance attributes."""
from typing import Optional

from seligimus.python.decorators.operators.equality.equal_instance_attributes import \
    equal_instance_attributes
from seligimus.python.decorators.operators.equality.equal_type import equal_type
from seligimus.python.decorators.operators.equality.equality_operator import EqualityOperator


def standard_equality(_equality_operator: Optional[EqualityOperator] = None) -> EqualityOperator:
    """A decorator for equality operators to check that the other object has the same type and the
    same instance attributes."""
    standard_equality_operator = equal_type(equal_instance_attributes(lambda self, other: True))

    return standard_equality_operator
