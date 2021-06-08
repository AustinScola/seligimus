"""A decorator for the repr dunder to return a standard representation."""
from inspect import Parameter
from typing import Any, Callable, Dict, List, Optional, Union, overload

from seligimus.python.functions.parameter_kind import ParameterKind
from seligimus.python.functions.parameter_list import ParameterList
from seligimus.python.functions.parameters import get_parameters_by_kind

Repr = Callable[[Any], str]
ReprDecorator = Callable[[Repr], Repr]


@overload
def standard_representation(representation_function: Repr,
                            parameter_to_attribute_name: None = None) -> Repr:
    ...  # pragma: no cover


@overload
def standard_representation(representation_function: None = None,
                            parameter_to_attribute_name: Dict[str, str] = ...) -> ReprDecorator:
    ...  # pragma: no cover


def standard_representation(
        representation_function: Optional[Repr] = None,
        parameter_to_attribute_name: Optional[Dict[str, str]] = None) -> Union[Repr, ReprDecorator]:
    """Return either a decorator or a standard representation function.

    If passed a parameter name to attribute name mapping, then act as a decorator factory, and
    return a standard representation decorator.

    If passed a representation function, then act as a decorator, and return a representation
    function that returns a standard representation.
    """
    _parameter_to_attribute_name: Dict[str, str]
    if parameter_to_attribute_name is None:
        _parameter_to_attribute_name = {}
    else:
        _parameter_to_attribute_name = parameter_to_attribute_name

    def standard_representation_decorator(representation_function: Repr) -> Repr:
        del representation_function

        def standard_representation_function(self: Any) -> str:
            class_name: str = self.__class__.__name__

            parameters_by_kind: Dict[ParameterKind, ParameterList] = \
                get_parameters_by_kind(self.__init__)

            positional_parameters: ParameterList = \
                parameters_by_kind[ParameterKind.POSITIONAL_OR_KEYWORD]

            arguments: List[str] = []
            for positional_parameter in positional_parameters:
                parameter_name: str = positional_parameter.name

                attribute_name: str = _parameter_to_attribute_name.get(
                    parameter_name, parameter_name)
                parameter_value = getattr(self, attribute_name)
                parameter_default_value: Any = positional_parameter.default

                parameter_representation: str
                if parameter_default_value == Parameter.empty:
                    parameter_representation = repr(parameter_value)
                elif parameter_value != parameter_default_value:
                    parameter_representation = f'{parameter_name}={repr(parameter_value)}'
                else:
                    continue  # pragma: no cover (https://github.com/nedbat/coveragepy/issues/198)

                arguments.append(parameter_representation)

            arguments_string: str = ', '.join(arguments)

            return f'{class_name}({arguments_string})'

        return standard_representation_function

    if representation_function is not None:
        return standard_representation_decorator(representation_function)

    return standard_representation_decorator
