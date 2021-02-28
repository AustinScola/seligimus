"""A position in the two-dimensional integer lattice."""
from seligimus.maths.vector_2 import Vector2


class IntegerPosition2D(Vector2[int]):  # pylint: disable=too-few-public-methods
    """A position in the two-dimensional integer lattice."""
    def __init__(self, x: int = 0, y: int = 0):  # pylint: disable=invalid-name, useless-super-delegation
        super().__init__(x, y)
