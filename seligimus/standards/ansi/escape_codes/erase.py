"""ANSI escape codes for erasing text."""
from seligimus.standards.ansi.escape_codes.control import CONTROL_SEQUENCE_INTRODUCER

CLEAR_SCREEN = CONTROL_SEQUENCE_INTRODUCER + '2J'
