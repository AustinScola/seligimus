"""A two-dimensional vector."""
from typing import Any, Generic, TypeVar

from seligimus.python.decorators.operators.equality.equal_instance_attributes import \
    equal_instance_attributes
from seligimus.python.decorators.operators.equality.equal_type import equal_type
from seligimus.python.decorators.standard_representation import standard_representation

T = TypeVar('T', int, float, complex)  # pylint: disable=invalid-name


class Vector2(Generic[T]):
    """A two-dimensional vector."""
    def __init__(self, x: T, y: T):  # pylint: disable=invalid-name
        self.x: T = x  # pylint: disable=invalid-name
        self.y: T = y  # pylint: disable=invalid-name

    @equal_type
    @equal_instance_attributes
    def __eq__(self, other: Any) -> bool:
        return True

    def __bool__(self) -> bool:
        return bool(self.x) or bool(self.y)

    @standard_representation
    def __repr__(self) -> str:
        pass  # pragma: no cover

    def __add__(self, other_position: 'Vector2') -> 'Vector2':
        x: T = self.x + other_position.x  # pylint: disable=invalid-name
        y: T = self.y + other_position.y  # pylint: disable=invalid-name
        sum_ = Vector2(x, y)
        return sum_
