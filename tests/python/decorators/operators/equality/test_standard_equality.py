"""Test seligimus.python.decorators.operators.equality.standard_equality."""
from typing import Any, Callable, Dict

import pytest

from seligimus.python.classes.attributes import set_attributes
from seligimus.python.decorators.operators.equality.standard_equality import standard_equality


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('equality_operator, self_class_name, other_class_name, self_attributes, other_attributes, expected_equality', [
    (lambda self, other: None, 'Foo', 'Bar', {}, {}, False),
    (lambda self, other: None, 'Foo', 'Foo', {'spam': 1}, {}, False),
    (lambda self, other: None, 'Foo', 'Foo', {}, {}, True),
    (lambda self, other: None, 'Foo', 'Foo', {'spam': 1}, {'spam': 1}, True),
])
# yapf: enable # pylint: enable=line-too-long
# pylint: disable=too-many-arguments
def test_standard_equality(equality_operator: Callable[[Any, Any], bool], self_class_name: str,
                           other_class_name: str, self_attributes: Dict[str, Any],
                           other_attributes: Dict[str, Any], expected_equality: bool) -> None:
    """Test seligimus.python.decorators.operators.equality.standard_equality.standard_equality."""
    self_type = type(self_class_name, tuple(), {})
    self = self_type()
    set_attributes(self, self_attributes)

    if other_class_name == self_class_name:
        other_type = self_type
    else:
        other_type = type(other_class_name, tuple(), {})
    other = other_type()
    set_attributes(other, other_attributes)

    wrapped_equality_operator = standard_equality(equality_operator)

    equality: bool = wrapped_equality_operator(self, other)

    assert equality == expected_equality
