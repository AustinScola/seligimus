"""A position in the two-dimensional integer lattice."""
from seligimus.maths.vector_2 import Vector2


class IntegerPosition2D(Vector2[int]):
    """A position in the two-dimensional integer lattice."""
    def __init__(self, x: int = 0, y: int = 0):  # pylint: disable=invalid-name, useless-super-delegation
        super().__init__(x, y)

    def __add__(self, other: Vector2[int]) -> 'IntegerPosition2D':
        sum_: Vector2[int] = super().__add__(other)
        return IntegerPosition2D(sum_.x, sum_.y)

    def __sub__(self, other: Vector2[int]) -> 'IntegerPosition2D':
        difference: Vector2[int] = super().__sub__(other)
        return IntegerPosition2D(difference.x, difference.y)

    def __iadd__(self, other: Vector2[int]) -> 'IntegerPosition2D':
        super().__iadd__(other)
        return self

    def __isub__(self, other: Vector2[int]) -> 'IntegerPosition2D':
        super().__isub__(other)
        return self

    def __neg__(self) -> 'IntegerPosition2D':
        negation: Vector2[int] = super().__neg__()
        return IntegerPosition2D(negation.x, negation.y)
