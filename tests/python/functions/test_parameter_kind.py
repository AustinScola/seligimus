"""Test seligimus.python.functions.parameter_kind."""
from enum import Enum
from inspect import Parameter

from seligimus.python.functions.parameter_kind import ParameterKind


def test_parameter_kind_inheritance() -> None:
    """Test seligimus.python.functions.parameter_kind.parameter_kind inheritance."""
    assert issubclass(ParameterKind, Enum)


def test_parameter_kind() -> None:
    """Test seligimus.python.functions.parameter_kind.parameter_kind."""
    assert ParameterKind.POSITIONAL_ONLY.value == Parameter.POSITIONAL_ONLY.value
    assert ParameterKind.POSITIONAL_OR_KEYWORD.value == Parameter.POSITIONAL_OR_KEYWORD.value
    assert ParameterKind.VAR_POSITIONAL.value == Parameter.VAR_POSITIONAL.value
    assert ParameterKind.KEYWORD_ONLY.value == Parameter.KEYWORD_ONLY.value
    assert ParameterKind.VAR_KEYWORD.value == Parameter.VAR_KEYWORD.value
