"""Test seligimus.python.decorators.standard_representation."""
from typing import Any, Callable, Dict, Optional

import pytest

from seligimus.python.decorators.standard_representation import (Repr, ReprDecorator,
                                                                 standard_representation)


def test_repr() -> None:
    """Test seligimus.python.decorators.standard_representation.Repr."""
    assert Repr.__base__ == Callable  # type: ignore[attr-defined]
    assert Repr.__args__ == (Any, str)  # type: ignore[attr-defined]


def test_repr_decorator() -> None:
    """Test seligimus.python.decorators.standard_representation.ReprDecorator."""
    assert ReprDecorator.__base__ == Callable  # type: ignore[attr-defined]
    assert ReprDecorator.__args__ == (Repr, Repr)  # type: ignore[attr-defined]


# pylint: disable=too-few-public-methods, missing-class-docstring, disallowed-name


class Foo1():
    def __init__(self) -> None:
        pass


class Foo2():
    def __init__(self, bar: int) -> None:
        self.bar: int = bar


class Foo2a():
    def __init__(self, bar: int) -> None:
        self.baz: int = bar


class Foo3():
    def __init__(self, bar: int, baz: str) -> None:
        self.bar: int = bar
        self.baz: str = baz


class Foo4():
    def __init__(self, bar: int = 0) -> None:
        self.bar: int = bar


class Foo4a():
    def __init__(self, bar: int = 0) -> None:
        self.wibble: int = bar


class Foo5():
    def __init__(self, bar: int, baz: str = 'spam') -> None:
        self.bar: int = bar
        self.baz: str = baz


class Foo6():
    def __init__(self, foo: Optional['Foo6'] = None):
        self.foo: Optional['Foo6'] = foo

    @standard_representation
    def __repr__(self) -> str:
        pass  # pragma: no cover


foo6 = Foo6()
foo6.foo = foo6


class Foo7():
    def __init__(self, foo: Optional['Foo7'] = None):
        self.foo: Optional['Foo7'] = foo

    @standard_representation
    def __repr__(self) -> str:
        pass  # pragma: no cover


foo7 = Foo7(Foo7())
foo7.foo = Foo7()
foo7.foo.foo = foo7


class Foo8():
    def __init__(self, bar: 'Bar8'):
        self.bar: 'Bar8' = bar

    @standard_representation
    def __repr__(self) -> str:
        pass  # pragma: no cover


class Bar8():
    def __init__(self, foo: Optional['Foo8'] = None):
        self.foo: Optional['Foo8'] = foo

    @standard_representation
    def __repr__(self) -> str:
        pass  # pragma: no cover


bar8 = Bar8()
foo8 = Foo8(bar8)
bar8.foo = foo8

# pylint: enable=disallowed-name


# yapf: disable
@pytest.mark.parametrize('instance, parameter_to_attribute_name, expected_representation', [
    (Foo1(), None, 'Foo1()'),
    (Foo2(1), None, 'Foo2(1)'),
    (Foo2a(1), {'bar': 'baz'}, 'Foo2a(1)'),
    (Foo3(1, 'spam'), None, "Foo3(1, 'spam')"),
    (Foo4(bar=1), None, 'Foo4(bar=1)'),
    (Foo4a(1), {'bar': 'wibble'}, 'Foo4a(bar=1)'),
    (foo6, None, 'Foo6(foo=<..>)'),
    (foo7, None, 'Foo7(foo=Foo7(foo=<...>))'),
    (foo8, None, 'Foo8(Bar8(foo=<...>))'),
])
# yapf: enable
def test_standard_reprsentation(instance: Any, parameter_to_attribute_name: Dict[str, str],
                                expected_representation: str) -> None:
    """Test seligimus.python.decorators.standard_representation."""
    representation_function: Repr
    if parameter_to_attribute_name:
        representation_decorator: Callable[[Repr], Repr] = \
            standard_representation(parameter_to_attribute_name=parameter_to_attribute_name)
        representation_function = representation_decorator(instance.__repr__)
    else:
        representation_function = standard_representation(instance.__repr__)

    representation = representation_function(instance)

    assert representation == expected_representation
