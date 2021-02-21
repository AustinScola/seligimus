"""Test seligimus.python.functions.parameters."""
from inspect import Parameter
from typing import Any, Callable, Dict

import pytest

from seligimus.python.functions.parameter_kind import ParameterKind
from seligimus.python.functions.parameter_list import ParameterList
from seligimus.python.functions.parameters import get_parameters_by_kind


def f() -> None:  # pylint: disable=missing-function-docstring, invalid-name
    pass


def g(a: Any) -> None:  # pylint: disable=missing-function-docstring, invalid-name, unused-argument
    pass


def h(a: Any, b: Any) -> None:  # pylint: disable=missing-function-docstring, invalid-name, unused-argument
    pass


def i(a: Any, *b: Any, c: Any = None) -> None:  # pylint: disable=missing-function-docstring, invalid-name, unused-argument
    pass


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('function, expected_parameters_by_kind', [
    (f, {}),
    (g, {ParameterKind.POSITIONAL_OR_KEYWORD: [Parameter('a', Parameter.POSITIONAL_OR_KEYWORD, annotation=Any)]}),
    (h, {ParameterKind.POSITIONAL_OR_KEYWORD: [Parameter('a', Parameter.POSITIONAL_OR_KEYWORD, annotation=Any), Parameter('b', Parameter.POSITIONAL_OR_KEYWORD, annotation=Any)]}),
    (i, {ParameterKind.POSITIONAL_OR_KEYWORD: [Parameter('a', Parameter.POSITIONAL_OR_KEYWORD, annotation=Any)], ParameterKind.VAR_POSITIONAL: [Parameter('b', Parameter.VAR_POSITIONAL, annotation=Any)], ParameterKind.KEYWORD_ONLY: [Parameter('c', Parameter.KEYWORD_ONLY, annotation=Any, default=None)]}),
])
# yapf: enable # pylint: enable=line-too-long
def test_get_parameters_by_kind(function: Callable,
                                expected_parameters_by_kind: ParameterKind) -> None:
    """Test seligimus.python.functions.parameters.get_parameters_by_kind."""
    parameters_by_kind: Dict[ParameterKind, ParameterList] = get_parameters_by_kind(function)

    assert parameters_by_kind == expected_parameters_by_kind
