"""Test seligimus.exceptions.iteration.no_head."""
from seligimus.exception import SeligimusException
from seligimus.exceptions.iteration.no_head import NoHead


def test_inheritance() -> None:
    """Test seligimus.exceptions.iteration.no_head.NoHead inheritance."""
    assert issubclass(NoHead, SeligimusException)


def test_init() -> None:
    """Test seligimus.exceptions.iteration.no_head.NoHead.__init__."""
    no_head = NoHead()

    assert str(no_head) == 'The iterable does not have a first item.'
