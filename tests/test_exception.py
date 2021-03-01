"""Test seligimus.exception."""
from seligimus.exception import SeligimusException


def test_inheritance() -> None:
    """Test seligimus.exception.SeligimusException inheritance."""
    assert issubclass(SeligimusException, Exception)
