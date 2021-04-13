"""The type of an equality operator."""
from typing import Any, Callable

EqualityOperator = Callable[[Any, Any], bool]
EqualityOperatorDecorator = Callable[[EqualityOperator], EqualityOperator]
