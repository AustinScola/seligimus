"""Methods for handling function parameters."""
import inspect
from collections import defaultdict
from inspect import Parameter, Signature
from typing import Callable, Dict, Mapping

from seligimus.python.functions.parameter_kind import ParameterKind
from seligimus.python.functions.parameter_list import ParameterList


def get_parameters_by_kind(function: Callable) -> Dict[ParameterKind, ParameterList]:
    """Return the parameters of a function by kind."""
    parameters_by_kind: Dict[ParameterKind, ParameterList] = defaultdict(list)

    signature: Signature = inspect.signature(function)
    parameters: Mapping[str, Parameter] = signature.parameters

    for parameter in parameters.values():
        parameter_kind: ParameterKind = ParameterKind(parameter.kind)
        parameters_by_kind[parameter_kind].append(parameter)

    return parameters_by_kind
