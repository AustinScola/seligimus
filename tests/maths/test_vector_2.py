"""Test seligimus.maths.vector_2."""
from typing import Any

import pytest

from seligimus.maths.vector_2 import T, Vector2


# yapf: disable
@pytest.mark.parametrize('x, y', [
    (0, 0),
    (1, 0),
    (0, 1),
    (1, 1),
    (7.2, 5.4),
])  # pylint: disable=invalid-name
# yapf: enable
def test_init(x: T, y: T) -> None:
    """Test seligimus.maths.vector_2.Vector2.__init__."""
    vector_2 = Vector2(x, y)

    assert vector_2.x == x
    assert vector_2.y == y


# yapf: disable
@pytest.mark.parametrize('vector_2, other, expected_equality', [
    (Vector2(0, 0), 'foo', False),
    (Vector2(0, 0), Vector2(0, 1), False),
    (Vector2(0, 0), Vector2(1, 0), False),
    (Vector2(0, 0), Vector2(1, 1), False),
    (Vector2(0, 0), Vector2(0, 0), True),
    (Vector2(0, 1), Vector2(0, 1), True),
    (Vector2(1, 0), Vector2(1, 0), True),
    (Vector2(1, 1), Vector2(1, 1), True),
    (Vector2(1, 2), Vector2(1, 2.0), True),
    (Vector2(7.0, 1.0), Vector2(7.0, 1.0), True),
])
# yapf: enable
def test_eq(vector_2: Vector2, other: Any, expected_equality: bool) -> None:
    """Test seligimus.maths.vector_2.Vector2.__eq__."""
    equality: bool = vector_2 == other

    assert equality == expected_equality


# yapf: disable
@pytest.mark.parametrize('vector_2, expected_truthiness', [
    (Vector2(0, 0), False),
    (Vector2(0, 1), True),
    (Vector2(1, 0), True),
    (Vector2(1, 1), True),
])
# yapf: enable
def test_bool(vector_2: Vector2, expected_truthiness: bool) -> None:
    """Test seligimus.maths.vector_2.Vector2.__bool__."""
    truthy: bool = bool(vector_2)

    assert truthy == expected_truthiness


# yapf: disable
@pytest.mark.parametrize('vector_2, expected_string', [
    (Vector2(0, 0), 'Vector2(0, 0)'),
    (Vector2(0, 1), 'Vector2(0, 1)'),
    (Vector2(1, 0), 'Vector2(1, 0)'),
    (Vector2(1, 1), 'Vector2(1, 1)'),
    (Vector2(7.0, 1.0), 'Vector2(7.0, 1.0)'),
])
# yapf: enable
def test_repr(vector_2: Vector2, expected_string: str) -> None:
    """Test seligimus.maths.vector_2.Vector2.__repr__."""
    string: str = repr(vector_2)

    assert string == expected_string


# yapf: disable
@pytest.mark.parametrize('vector_2, other, expected_sum', [
    (Vector2(0, 0), Vector2(0, 0), Vector2(0, 0)),
    (Vector2(0, 0), Vector2(0, 1), Vector2(0, 1)),
    (Vector2(0, 0), Vector2(1, 0), Vector2(1, 0)),
    (Vector2(0, 0), Vector2(1, 1), Vector2(1, 1)),
    (Vector2(0, 1), Vector2(0, 0), Vector2(0, 1)),
    (Vector2(0, 1), Vector2(0, 1), Vector2(0, 2)),
    (Vector2(0, 1), Vector2(1, 0), Vector2(1, 1)),
    (Vector2(0, 1), Vector2(1, 1), Vector2(1, 2)),
    (Vector2(1, 0), Vector2(0, 0), Vector2(1, 0)),
    (Vector2(1, 0), Vector2(0, 1), Vector2(1, 1)),
    (Vector2(1, 0), Vector2(1, 0), Vector2(2, 0)),
    (Vector2(1, 0), Vector2(1, 1), Vector2(2, 1)),
    (Vector2(1, 1), Vector2(0, 0), Vector2(1, 1)),
    (Vector2(1, 1), Vector2(0, 1), Vector2(1, 2)),
    (Vector2(1, 1), Vector2(0, 0), Vector2(1, 1)),
    (Vector2(1, 1), Vector2(0, 1), Vector2(1, 2)),
])
# yapf: enable
def test_add(vector_2: Vector2, other: Vector2, expected_sum: Vector2) -> None:
    """Test seligimus.maths.vector_2.Vector2.__add__."""
    sum_ = vector_2 + other

    assert sum_ == expected_sum


# yapf: disable
@pytest.mark.parametrize('vector_2, other, expected_difference', [
    (Vector2(0, 0), Vector2(0, 0), Vector2(0, 0)),
    (Vector2(0, 0), Vector2(0, 1), Vector2(0, -1)),
    (Vector2(0, 0), Vector2(1, 0), Vector2(-1, 0)),
    (Vector2(0, 0), Vector2(1, 1), Vector2(-1, -1)),
    (Vector2(0, 1), Vector2(0, 0), Vector2(0, 1)),
    (Vector2(0, 1), Vector2(0, 1), Vector2(0, 0)),
    (Vector2(0, 1), Vector2(1, 0), Vector2(-1, 1)),
    (Vector2(0, 1), Vector2(1, 1), Vector2(-1, 0)),
    (Vector2(1, 0), Vector2(0, 0), Vector2(1, 0)),
    (Vector2(1, 0), Vector2(0, 1), Vector2(1, -1)),
    (Vector2(1, 0), Vector2(1, 0), Vector2(0, 0)),
    (Vector2(1, 0), Vector2(1, 1), Vector2(0, -1)),
    (Vector2(1, 1), Vector2(0, 0), Vector2(1, 1)),
    (Vector2(1, 1), Vector2(0, 1), Vector2(1, 0)),
    (Vector2(1, 1), Vector2(1, 0), Vector2(0, 1)),
    (Vector2(1, 1), Vector2(1, 1), Vector2(0, 0)),
])
# yapf: enable
def test_sub(vector_2: Vector2, other: Vector2, expected_difference: Vector2) -> None:
    """Test seligimus.maths.vector_2.Vector2.__sub__."""
    difference = vector_2 - other

    assert difference == expected_difference


# yapf: disable
@pytest.mark.parametrize('vector_2, other, expected_sum', [
    (Vector2(0, 0), Vector2(0, 0), Vector2(0, 0)),
    (Vector2(0, 0), Vector2(0, 1), Vector2(0, 1)),
    (Vector2(0, 0), Vector2(1, 0), Vector2(1, 0)),
    (Vector2(0, 0), Vector2(1, 1), Vector2(1, 1)),
    (Vector2(0, 1), Vector2(0, 0), Vector2(0, 1)),
    (Vector2(0, 1), Vector2(0, 1), Vector2(0, 2)),
    (Vector2(0, 1), Vector2(1, 0), Vector2(1, 1)),
    (Vector2(0, 1), Vector2(1, 1), Vector2(1, 2)),
    (Vector2(1, 0), Vector2(0, 0), Vector2(1, 0)),
    (Vector2(1, 0), Vector2(0, 1), Vector2(1, 1)),
    (Vector2(1, 0), Vector2(1, 0), Vector2(2, 0)),
    (Vector2(1, 0), Vector2(1, 1), Vector2(2, 1)),
    (Vector2(1, 1), Vector2(0, 0), Vector2(1, 1)),
    (Vector2(1, 1), Vector2(0, 1), Vector2(1, 2)),
    (Vector2(1, 1), Vector2(0, 0), Vector2(1, 1)),
    (Vector2(1, 1), Vector2(0, 1), Vector2(1, 2)),
])
# yapf: enable
def test_iadd(vector_2: Vector2, other: Vector2, expected_sum: Vector2) -> None:
    """Test seligimus.maths.vector_2.Vector2.__iadd__."""
    vector_2 += other

    assert vector_2 == expected_sum


# yapf: disable
@pytest.mark.parametrize('vector_2, other, expected_difference', [
    (Vector2(0, 0), Vector2(0, 0), Vector2(0, 0)),
    (Vector2(0, 0), Vector2(0, 1), Vector2(0, -1)),
    (Vector2(0, 0), Vector2(1, 0), Vector2(-1, 0)),
    (Vector2(0, 0), Vector2(1, 1), Vector2(-1, -1)),
    (Vector2(0, 1), Vector2(0, 0), Vector2(0, 1)),
    (Vector2(0, 1), Vector2(0, 1), Vector2(0, 0)),
    (Vector2(0, 1), Vector2(1, 0), Vector2(-1, 1)),
    (Vector2(0, 1), Vector2(1, 1), Vector2(-1, 0)),
    (Vector2(1, 0), Vector2(0, 0), Vector2(1, 0)),
    (Vector2(1, 0), Vector2(0, 1), Vector2(1, -1)),
    (Vector2(1, 0), Vector2(1, 0), Vector2(0, 0)),
    (Vector2(1, 0), Vector2(1, 1), Vector2(0, -1)),
    (Vector2(1, 1), Vector2(0, 0), Vector2(1, 1)),
    (Vector2(1, 1), Vector2(0, 1), Vector2(1, 0)),
    (Vector2(1, 1), Vector2(1, 0), Vector2(0, 1)),
    (Vector2(1, 1), Vector2(1, 1), Vector2(0, 0)),
])
# yapf: enable
def test_isub(vector_2: Vector2, other: Vector2, expected_difference: Vector2) -> None:
    """Test seligimus.maths.vector_2.Vector2.__isub__."""
    vector_2 -= other

    assert vector_2 == expected_difference


# yapf: disable
@pytest.mark.parametrize('vector_2, expected_negation', [
    (Vector2(0, 0), Vector2(0, 0)),
    (Vector2(0, 1), Vector2(0, -1)),
    (Vector2(0, -1), Vector2(0, 1)),
    (Vector2(1, 0), Vector2(-1, 0)),
    (Vector2(-1, 0), Vector2(1, 0)),
    (Vector2(1, 1), Vector2(-1, -1)),
    (Vector2(-1, -1), Vector2(1, 1)),
])
# yapf: enable
def test_neg(vector_2: Vector2, expected_negation: Vector2) -> None:
    """Test seligimus.maths.vector_2.Vector2.__neg__."""
    negation: Vector2 = -vector_2

    assert negation == expected_negation
