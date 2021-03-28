"""A two-dimensional vector."""
from typing import Generic, TypeVar

from seligimus.python.decorators.operators.equality.standard_equality import standard_equality
from seligimus.python.decorators.standard_representation import standard_representation

T = TypeVar('T', int, float, complex)  # pylint: disable=invalid-name


class Vector2(Generic[T]):
    """A two-dimensional vector."""
    def __init__(self, x: T, y: T):  # pylint: disable=invalid-name
        self.x: T = x  # pylint: disable=invalid-name
        self.y: T = y  # pylint: disable=invalid-name

    __eq__ = standard_equality()

    def __bool__(self) -> bool:
        return bool(self.x) or bool(self.y)

    @standard_representation
    def __repr__(self) -> str:
        pass  # pragma: no cover

    def __add__(self, other: 'Vector2') -> 'Vector2':
        x: T = self.x + other.x  # pylint: disable=invalid-name
        y: T = self.y + other.y  # pylint: disable=invalid-name
        sum_ = Vector2(x, y)
        return sum_

    def __sub__(self, other: 'Vector2') -> 'Vector2':
        x: T = self.x - other.x  # pylint: disable=invalid-name
        y: T = self.y - other.y  # pylint: disable=invalid-name
        difference = Vector2(x, y)
        return difference

    def __iadd__(self, other: 'Vector2') -> 'Vector2':
        self.x += other.x
        self.y += other.y
        return self

    def __isub__(self, other: 'Vector2') -> 'Vector2':
        self.x -= other.x
        self.y -= other.y
        return self

    def __neg__(self) -> 'Vector2':
        x: T = -self.x  # pylint: disable=invalid-name
        y: T = -self.y  # pylint: disable=invalid-name
        negation = Vector2(x, y)
        return negation
