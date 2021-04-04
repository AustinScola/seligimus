"""Test seligimus.characters.uppercase_letters."""
import pytest

from seligimus.characters.uppercase_letters import (UPPERCASE_LETTERS, is_uppercase_letter,
                                                    not_uppercase_letter)


def test_uppercase_letters() -> None:
    """Test seligimus.characters.uppercase_letters.UPPERCASE_LETTERS."""
    assert UPPERCASE_LETTERS == {
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
        'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    }


# yapf: disable
@pytest.mark.parametrize('string, expected_membership', [
    ('A', True),
    ('B', True),
    ('Z', True),
    ('a', False),
    ('$', False),
])
# yapf: enable
def test_is_uppercase_letter(string: str, expected_membership: bool) -> None:
    """Test seligimus.characters.uppercase_letters.is_uppercase_letter."""
    membership: bool = is_uppercase_letter(string)

    assert membership == expected_membership


# yapf: disable
@pytest.mark.parametrize('string, expected_nonmembership', [
    ('A', False),
    ('B', False),
    ('Z', False),
    ('a', True),
    ('$', True),
])
# yapf: enable
def test_not_uppercase_letter(string: str, expected_nonmembership: bool) -> None:
    """Test seligimus.characters.uppercase_letters.not_uppercase_letter."""
    nonmembership: bool = not_uppercase_letter(string)

    assert nonmembership == expected_nonmembership
