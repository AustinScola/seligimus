"""Test seligimus.maths.integer_position_2d."""
from typing import Any, Dict, List, Optional

import pytest

from seligimus.maths.integer_position_2d import IntegerPosition2D
from seligimus.maths.vector_2 import Vector2
from seligimus.python.classes.is_subclass_of_generic import is_subclass_of_generic


def test_inheritance() -> None:
    """Test seligimus.maths.integer_position_2d.IntegerPosition2D inheritance."""
    assert is_subclass_of_generic(IntegerPosition2D, Vector2[int])


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('x, pass_x_as_argument, pass_x_as_keyword_argument, y, pass_y_as_argument, pass_y_as_keyword_argument, expected_x, expected_y', [
    (None, False, False, None, False, False, 0, 0),
    (None, False, False, 0, False, True, 0, 0),
    (None, False, False, 1, False, True, 0, 1),
    (0, False, True, None, False, False, 0, 0),
    (1, False, True, None, False, False, 1, 0),
    (0, False, True, 0, False, True, 0, 0),
    (0, False, True, 1, False, True, 0, 1),
    (1, False, True, 0, False, True, 1, 0),
    (1, False, True, 1, False, True, 1, 1),
    (0, True, False, 0, False, True, 0, 0),
    (0, True, False, 1, False, True, 0, 1),
    (1, True, False, 0, False, True, 1, 0),
    (1, True, False, 1, False, True, 1, 1),
    (0, True, False, 0, True, False, 0, 0),
    (0, True, False, 1, True, False, 0, 1),
    (1, True, False, 0, True, False, 1, 0),
    (1, True, False, 1, True, False, 1, 1),
])  # pylint: disable=invalid-name
# yapf: enable # pylint: enable=line-too-long
# pylint: disable=too-many-arguments
def test_init(x: Optional[int], pass_x_as_argument: bool, pass_x_as_keyword_argument: bool,
              y: Optional[int], pass_y_as_argument: bool, pass_y_as_keyword_argument: bool,
              expected_x: int, expected_y: int) -> None:
    """Test seligimus.maths.integer_position_2d.IntegerPosition2D.__init__."""
    arguments: List[Any] = []
    keyword_arguments: Dict[str, Any] = {}

    if pass_x_as_argument:
        arguments.append(x)

    if pass_y_as_argument:
        arguments.append(y)

    if pass_x_as_keyword_argument:
        keyword_arguments['x'] = x

    if pass_y_as_keyword_argument:
        keyword_arguments['y'] = y

    integer_position_2d: IntegerPosition2D = IntegerPosition2D(*arguments, **keyword_arguments)

    assert integer_position_2d.x == expected_x
    assert integer_position_2d.y == expected_y


# yapf: disable
@pytest.mark.parametrize('integer_position_2d, other, expected_sum', [
    (IntegerPosition2D(0, 0), IntegerPosition2D(0, 0), IntegerPosition2D(0, 0)),
])
# yapf: enable
def test_add(integer_position_2d: IntegerPosition2D, other: IntegerPosition2D,
             expected_sum: IntegerPosition2D) -> None:
    """Test seligimus.maths.integer_position_2d.IntegerPosition2D.__add__."""
    sum_: IntegerPosition2D = integer_position_2d + other

    assert sum_ == expected_sum


# yapf: disable
@pytest.mark.parametrize('integer_position_2d, other, expected_difference', [
    (IntegerPosition2D(0, 0), IntegerPosition2D(0, 0), IntegerPosition2D(0, 0)),
])
# yapf: enable
def test_sub(integer_position_2d: IntegerPosition2D, other: IntegerPosition2D,
             expected_difference: IntegerPosition2D) -> None:
    """Test seligimus.maths.integer_position_2d.IntegerPosition2D.__sub__."""
    difference: IntegerPosition2D = integer_position_2d - other

    assert difference == expected_difference


# yapf: disable
@pytest.mark.parametrize('integer_position_2d, other, expected_sum', [
    (IntegerPosition2D(0, 0), IntegerPosition2D(0, 0), IntegerPosition2D(0, 0)),
])
# yapf: enable
def test_iadd(integer_position_2d: IntegerPosition2D, other: IntegerPosition2D,
              expected_sum: IntegerPosition2D) -> None:
    """Test seligimus.maths.integer_position_2d.IntegerPosition2D.__iadd__."""
    integer_position_2d += other

    assert integer_position_2d == expected_sum
