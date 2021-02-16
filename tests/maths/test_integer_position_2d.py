"""Test seligimus.maths.integer_position_2d."""
from seligimus.maths.integer_position_2d import IntegerPosition2D
from seligimus.maths.vector_2 import Vector2
from seligimus.python.classes.is_subclass_of_generic import is_subclass_of_generic


def test_inheritance() -> None:
    """Test seligimus.maths.integer_position_2d.IntegerPosition2D inheritance."""
    assert is_subclass_of_generic(IntegerPosition2D, Vector2[int])
