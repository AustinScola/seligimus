"""A decorator for equality operators to check that the other object has equal instance
attributes."""
from functools import wraps
from typing import Any, Callable, Dict

from seligimus.python.classes.attributes import get_instance_attributes


def equal_instance_attributes(
        equality_operator: Callable[[Any, Any], bool]) -> Callable[[Any, Any], bool]:
    """Return an equality operator which first checks if the other object has equal instance
    attributes."""
    @wraps(equality_operator)
    def equality_operator_with_equal_instance_attributes(self: Any, other: Any) -> bool:
        self_attributes: Dict[str, Any] = get_instance_attributes(self)
        other_attributes: Dict[str, Any] = get_instance_attributes(other)

        if not self_attributes == other_attributes:
            return False

        return equality_operator(self, other)

    return equality_operator_with_equal_instance_attributes
