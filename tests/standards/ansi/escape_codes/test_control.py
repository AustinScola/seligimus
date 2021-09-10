"""Test seligimus.standards.ansi.escape_codes.control."""
from seligimus.standards.ansi.escape_codes.control import CONTROL_SEQUENCE_INTRODUCER, ESCAPE


def test_escape() -> None:
    """Test seligimus.standards.ansi.escape_codes.control.escape"""
    assert ESCAPE == '\x1b'


def test_control_sequence_introducer() -> None:
    """Test seligimus.standards.ansi.escape_codes.control.CONTROL_SEQUENCE_INTRODUCER."""
    assert CONTROL_SEQUENCE_INTRODUCER == '\x1b['
