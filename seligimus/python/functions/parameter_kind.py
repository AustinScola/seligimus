"""A kind of function parameter."""
from enum import Enum
from inspect import Parameter


class ParameterKind(Enum):
    """A kind of function parameter."""
    POSITIONAL_ONLY = Parameter.POSITIONAL_ONLY.value
    POSITIONAL_OR_KEYWORD = Parameter.POSITIONAL_OR_KEYWORD.value
    VAR_POSITIONAL = Parameter.VAR_POSITIONAL.value
    KEYWORD_ONLY = Parameter.KEYWORD_ONLY.value
    VAR_KEYWORD = Parameter.VAR_KEYWORD.value
