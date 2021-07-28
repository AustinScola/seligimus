"""Test seligimus.characters.symbols."""
import pytest

from seligimus.characters.symbols import SYMBOLS, is_symbol, not_symbol


def test_symbols() -> None:
    """Test seligimus.characters.symbols.SYMBOLS."""
    assert SYMBOLS == {'[', ']', '{', '}', '(', ')', '<', '>', "'", '"', '=', ',', '.', ';'}


# yapf: disable
@pytest.mark.parametrize('string, expected_membership', [
    ('[', True),
    (']', True),
    (';', True),
    ('a', False),
    ('A', False),
])
# yapf: enable
def test_is_symbol(string: str, expected_membership: bool) -> None:
    """Test seligimus.characters.symbols.is_symbol."""
    membership: bool = is_symbol(string)

    assert membership == expected_membership


# yapf: disable
@pytest.mark.parametrize('string, expected_nonmembership', [
    ('[', False),
    (']', False),
    (';', False),
    ('a', True),
    ('A', True),
])
# yapf: enable
def test_not_symbol(string: str, expected_nonmembership: bool) -> None:
    """Test seligimus.characters.symbols.not_symbol."""
    nonmembership: bool = not_symbol(string)

    assert nonmembership == expected_nonmembership
