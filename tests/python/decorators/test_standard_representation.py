"""Test seligimus.python.decorators.standard_representation."""
import types
from typing import Any, Callable, Dict

import pytest

from seligimus.python.classes.attributes import set_attributes
from seligimus.python.decorators.standard_representation import Repr, standard_representation


def test_repr() -> None:
    """Test seligimus.python.decorators.standard_representation.Repr."""
    assert Repr.__base__ == Callable  # type: ignore[attr-defined]
    assert Repr.__args__ == (Any, str)  # type: ignore[attr-defined]


def init_1(self: Any) -> None:  # pylint: disable=missing-function-docstring, unused-argument
    pass


def init_2(self: Any, bar: int) -> None:  # pylint: disable=missing-function-docstring, blacklisted-name, unused-argument
    pass


def init_3(self: Any, bar: int, baz: str) -> None:  # pylint: disable=missing-function-docstring, blacklisted-name, unused-argument
    pass


def init_4(self: Any, bar: int = 0) -> None:  # pylint: disable=missing-function-docstring, blacklisted-name, unused-argument
    pass


def init_5(self: Any, bar: int, baz: str = 'spam') -> None:  # pylint: disable=missing-function-docstring, blacklisted-name, unused-argument
    pass


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('class_name, initialization_method, instance_attributes, parameter_to_attribute_name, expected_representation', [
    ('Foo', init_1, {}, None, 'Foo()'),
    ('Foo', init_2, {'bar': 1}, None, 'Foo(1)'),
    ('Foo', init_2, {'baz': 1}, {'bar': 'baz'}, 'Foo(1)'),
    ('Foo', init_3, {'bar': 1, 'baz': 'spam'}, None, "Foo(1, 'spam')"),
    ('Foo', init_4, {'bar': 1}, None, 'Foo(bar=1)'),
    ('Foo', init_4, {'wibble': 1}, {'bar': 'wibble'}, 'Foo(bar=1)'),
    ('Foo', init_5, {'bar': 1, 'baz': 'spam'}, None, 'Foo(1)'),
])
# yapf: enable # pylint: enable=line-too-long
def test_standard_reprsentation(class_name: str, initialization_method: Callable[[], None],
                                instance_attributes: Dict[str, Any],
                                parameter_to_attribute_name: Dict[str, str],
                                expected_representation: str) -> None:
    """Test seligimus.python.decorators.standard_representation."""
    class_ = types.new_class(class_name)
    instance = class_()
    instance.__init__ = initialization_method
    set_attributes(instance, instance_attributes)

    representation_function: Callable[[Any],
                                      str] = standard_representation(instance.__repr__,
                                                                     parameter_to_attribute_name)

    representation = representation_function(instance)

    assert representation == expected_representation
