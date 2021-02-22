"""A size in the two-dimensional integer lattice."""
from seligimus.maths.vector_2 import Vector2
from seligimus.python.decorators.standard_representation import standard_representation


class IntegerSize2D(Vector2[int]):
    """A size in the two-dimensional integer lattice."""
    def __init__(self, width: int, height: int):  # pylint: disable=useless-super-delegation
        super().__init__(width, height)

    @property
    def width(self) -> int:
        """Return the width."""
        return self.x

    @width.setter
    def width(self, width: int) -> None:
        self.x = width  # pylint: disable=invalid-name

    @property
    def height(self) -> int:
        """Return the height."""
        return self.y

    @height.setter
    def height(self, height: int) -> None:
        self.y = height  # pylint: disable=invalid-name

    @standard_representation
    def __repr__(self) -> str:
        pass  # pragma: no cover
