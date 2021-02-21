"""Test seligimus.python.functions.parameter_list."""
from inspect import Parameter
from typing import List

from seligimus.python.functions.parameter_list import ParameterList


def test_parameter_list() -> None:
    """Test seligimus.python.functions.parameter_list.ParameterList."""
    assert issubclass(ParameterList, List)
    assert ParameterList.__args__ == (Parameter, )  # type: ignore[attr-defined]
