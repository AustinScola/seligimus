"""Test seligimus.python.classes.attributes."""
from typing import Any, Dict

import pytest

from seligimus.python.classes.attributes import get_instance_attributes, set_attributes
from seligimus.python.classes.empty_class import EmptyClass


# yapf: disable
@pytest.mark.parametrize('attributes', [
    ({}),
    ({'foo': None}),
    ({'foo': 1}),
    ({'foo': 1, 'bar': 42}),
])
# yapf: enable
def test_get_instance_attributes(attributes: Dict[str, Any]) -> None:
    """Test seligimus.python.classes.get_instance_attributes."""
    instance = EmptyClass()

    for attribute_name, attribute_value in attributes.items():
        setattr(instance, attribute_name, attribute_value)

    gotten_attributes = get_instance_attributes(instance)

    assert gotten_attributes == attributes


# yapf: disable
@pytest.mark.parametrize('attributes', [
    ({}),
    ({'foo': None}),
    ({'foo': 1}),
    ({'foo': 1, 'bar': 42}),
])
# yapf: enable
def test_set_attributes(attributes: Dict[str, Any]) -> None:
    """Test seligimus.python.classes.set_attributes."""
    instance = EmptyClass()

    set_attributes(instance, attributes)

    for attribute_name, attribute_value in attributes.items():
        assert getattr(instance, attribute_name) == attribute_value
