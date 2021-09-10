"""Test seligimus.standards.ansi.escape_codes.cursor."""
import pytest

from seligimus.maths.integer_position_2d import IntegerPosition2D
from seligimus.standards.ansi.escape_codes.cursor import (DEVICE_STATUS_REPORT, HIDE_CURSOR,
                                                          MOVE_CURSOR_HOME, SHOW_CURSOR,
                                                          get_move_cursor)


def test_device_status_report() -> None:
    """Test seligimus.standards.ansi.escape_codes.cursor.DEVICE_STATUS_REPORT."""
    assert DEVICE_STATUS_REPORT == '\x1b[6n'


def test_hide_cursor() -> None:
    """Test seligimus.standards.ansi.escape_codes.cursor.HIDE_CURSOR."""
    assert HIDE_CURSOR == '\x1b[?25l'


def test_show_cursor() -> None:
    """Test seligimus.standards.ansi.escape_codes.cursor.SHOW_CURSOR."""
    assert SHOW_CURSOR == '\x1b[?25h'


# yapf: disable
@pytest.mark.parametrize('position, expected_move_cursor_command', [
    (IntegerPosition2D(), '\x1b[;H'),
    (IntegerPosition2D(0, 1), '\x1b[2;H'),
    (IntegerPosition2D(1, 0), '\x1b[;2H'),
    (IntegerPosition2D(1, 1), '\x1b[2;2H'),
    (IntegerPosition2D(1, 7), '\x1b[8;2H'),
    (IntegerPosition2D(7, 1), '\x1b[2;8H'),
    (IntegerPosition2D(7, 7), '\x1b[8;8H'),
])
# yapf: enable
def test_get_move_cursor(position: IntegerPosition2D, expected_move_cursor_command: str) -> None:
    """Test seligimus.standards.ansi.escape_codes.cursor.get_move_cursor."""
    move_cusor_command: str = get_move_cursor(position)
    assert move_cusor_command == expected_move_cursor_command


def test_move_cursor_home() -> None:
    """Test seligimus.standards.ansi.escape_codes.cursor.MOVE_CURSOR_HOME."""
    assert MOVE_CURSOR_HOME == '\x1b[;H'
