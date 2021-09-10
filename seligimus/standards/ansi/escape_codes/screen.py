"""ANSI escape codes for the controlling the screen."""
from seligimus.standards.ansi.escape_codes.control import CONTROL_SEQUENCE_INTRODUCER

ENABLE_ALTERNATIVE_SCREEN = CONTROL_SEQUENCE_INTRODUCER + '?1049h'
DISABLE_ALTERNATIVE_SCREEN = CONTROL_SEQUENCE_INTRODUCER + '?1049l'
