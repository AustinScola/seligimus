"""Test seligimus.python.decorators.operators.equality.equal_instance_attributes."""
from typing import Any, Dict, Optional, Set

import pytest

from seligimus.python.classes.attributes import set_attributes
from seligimus.python.classes.empty_class import EmptyClass
from seligimus.python.decorators.operators.equality.equal_instance_attributes import \
    equal_instance_attributes
from seligimus.python.decorators.operators.equality.equality_operator import (
    EqualityOperator, EqualityOperatorDecorator)


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('equality_operator, excludes, self_attributes, other_attributes, expected_equality', [
    (lambda self, other: False, None, {}, {}, False),
    (lambda self, other: True, None, {'foo': 1}, {}, False),
    (lambda self, other: True, None, {'foo': 1}, {'foo': 2}, False),
    (lambda self, other: True, None, {'foo': 1}, {'bar': 1}, False),
    (lambda self, other: True, None, {'foo': 1}, {'bar': 2}, False),
    (lambda self, other: True, None, {'foo': 1, 'bar': 2}, {'bar': 2}, False),
    (lambda self, other: True, None, {}, {}, True),
    (lambda self, other: True, None, {'foo': 1}, {'foo': 1}, True),
    (lambda self, other: True, None, {'foo': 1, 'bar': 2}, {'foo': 1, 'bar': 2}, True),
    (lambda self, other: True, set(), {}, {}, True),
    (lambda self, other: True, {'foo'}, {'foo': 1}, {'foo': 2}, True),
    (lambda self, other: True, {'bar'}, {'foo': 1, 'bar': 2}, {'foo': 1, 'bar': 7}, True),
])
# yapf: enable # pylint: enable=line-too-long
def test_equal_instance_attributes(equality_operator: EqualityOperator,
                                   excludes: Optional[Set[str]], self_attributes: Dict[str, Any],
                                   other_attributes: Dict[str,
                                                          Any], expected_equality: bool) -> None:
    """Test seligimus.python.decorators.operators.equality.equal_instance_attributes.equal_instance_attributes."""  # pylint: disable=line-too-long, useless-suppression
    self = EmptyClass()
    set_attributes(self, self_attributes)

    other = EmptyClass()
    set_attributes(other, other_attributes)

    equality_operator_decorator: EqualityOperatorDecorator
    if excludes is not None:
        equality_operator_decorator = equal_instance_attributes(excludes=excludes)
    else:
        equality_operator_decorator = equal_instance_attributes

    decorated_equality_operator = equality_operator_decorator(equality_operator)
    equality: bool = decorated_equality_operator(self, other)

    assert equality == expected_equality
