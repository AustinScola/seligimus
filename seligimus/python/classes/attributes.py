"""Setters and getters for Python class attributes."""
from typing import Any, Dict


def get_instance_attributes(instance: Any) -> Dict[str, Any]:
    """Return the instance attributes of an instance."""
    attributes: Dict[str, Any] = instance.__dict__.copy()
    return attributes


def set_attributes(instance: Any, attributes: Dict[str, Any]) -> None:
    """Set the instance attributes of an instance."""
    for attribute_name, attribute_value in attributes.items():
        setattr(instance, attribute_name, attribute_value)
