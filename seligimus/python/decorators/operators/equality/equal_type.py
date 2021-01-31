"""A decorator for equality operators to check that the other object has the same type."""
from functools import wraps
from typing import Any, Callable


def equal_type(equality_operator: Callable[[Any, Any], bool]) -> Callable[[Any, Any], bool]:
    """Return an equality operator which first checks if the other object has the same type."""
    @wraps(equality_operator)
    def equality_operator_with_equal_type(self: Any, other: Any) -> bool:
        if not isinstance(other, self.__class__):
            return False
        return equality_operator(self, other)

    return equality_operator_with_equal_type
