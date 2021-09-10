"""ANSI escape codes for changing the color of text."""
from seligimus.standards.ansi.escape_codes.control import CONTROL_SEQUENCE_INTRODUCER

RESET = CONTROL_SEQUENCE_INTRODUCER + 'm'
INVERT = CONTROL_SEQUENCE_INTRODUCER + '7m'
