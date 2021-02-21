"""A decorator for the repr dunder to return a standard representation."""
from inspect import Parameter
from typing import Any, Callable, Dict, List

from seligimus.python.functions.parameter_kind import ParameterKind
from seligimus.python.functions.parameter_list import ParameterList
from seligimus.python.functions.parameters import get_parameters_by_kind


def standard_representation(representation_function: Callable[[Any], str]) -> Callable[[Any], str]:
    """Return an repr which returns return a standard representation."""
    del representation_function

    def standard_representation_function(self: Any) -> str:
        class_name: str = self.__class__.__name__

        initialiazation_parameters_by_kind: Dict[ParameterKind,
                                                 ParameterList] = get_parameters_by_kind(
                                                     self.__init__)

        initialization_positional_parameters: ParameterList = initialiazation_parameters_by_kind[
            ParameterKind.POSITIONAL_OR_KEYWORD]

        initialization_arguments: List[str] = []
        for initialization_positional_parameter in initialization_positional_parameters:
            parameter_name: str = initialization_positional_parameter.name
            if parameter_name == 'self':
                continue

            parameter_value: Any = getattr(self, parameter_name)
            parameter_default_value: Any = initialization_positional_parameter.default

            parameter_representation: str
            if parameter_default_value == Parameter.empty:
                parameter_representation = repr(parameter_value)
            elif parameter_value != parameter_default_value:
                parameter_representation = f'{parameter_name}={repr(parameter_value)}'
            else:
                continue  # pragma: no cover (https://github.com/nedbat/coveragepy/issues/198)

            initialization_arguments.append(parameter_representation)

        initialization_arguments_string: str = ', '.join(initialization_arguments)

        return f'{class_name}({initialization_arguments_string})'

    return standard_representation_function
