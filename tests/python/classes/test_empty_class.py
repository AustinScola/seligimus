"""Test seligimus.python.classes.empty_class."""
from seligimus.python.classes.empty_class import EmptyClass


def test_empty_class() -> None:
    """Test seligimus.python.classes.empty_class.EmptyClass."""
    assert isinstance(EmptyClass, type)
