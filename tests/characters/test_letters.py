"""Test seligimus.characters.letters."""
import pytest

from seligimus.characters.letters import LETTERS, is_letter, not_letter


def test_letters() -> None:
    """Test seligimus.characters.letters.LETTERS."""
    assert LETTERS == {
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
        's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
        'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    }


# yapf: disable
@pytest.mark.parametrize('string, expected_membership', [
    ('a', True),
    ('b', True),
    ('z', True),
    ('A', True),
    ('$', False),
])
# yapf: enable
def test_is_letter(string: str, expected_membership: bool) -> None:
    """Test seligimus.characters.letters.is_letter."""
    membership: bool = is_letter(string)

    assert membership == expected_membership


# yapf: disable
@pytest.mark.parametrize('string, expected_nonmembership', [
    ('a', False),
    ('b', False),
    ('z', False),
    ('A', False),
    ('$', True),
])
# yapf: enable
def test_not_letter(string: str, expected_nonmembership: bool) -> None:
    """Test seligimus.characters.letters.not_letter."""
    nonmembership: bool = not_letter(string)

    assert nonmembership == expected_nonmembership
