"""An exception raised when an iterable does not have a first item."""
from seligimus.exception import SeligimusException


class NoHead(SeligimusException):
    """Raised when an iterable does not have a first item."""
    def __init__(self) -> None:
        message: str = 'The iterable does not have a first item.'
        super().__init__(message)
