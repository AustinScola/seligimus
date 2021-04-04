"""Test seligimus.characters.lowercase_letters."""
import pytest

from seligimus.characters.lowercase_letters import (LOWERCASE_LETTERS, is_lowercase_letter,
                                                    not_lowercase_letter)


def test_lowercase_letters() -> None:
    """Test seligimus.characters.lowercase_letters.LOWERCASE_LETTERS."""
    assert LOWERCASE_LETTERS == {
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
        's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    }


# yapf: disable
@pytest.mark.parametrize('string, expected_membership', [
    ('a', True),
    ('b', True),
    ('z', True),
    ('A', False),
    ('$', False),
])
# yapf: enable
def test_is_lowercase_letter(string: str, expected_membership: bool) -> None:
    """Test seligimus.characters.lowercase_letters.is_lowercase_letter."""
    membership: bool = is_lowercase_letter(string)

    assert membership == expected_membership


# yapf: disable
@pytest.mark.parametrize('string, expected_nonmembership', [
    ('a', False),
    ('b', False),
    ('z', False),
    ('A', True),
    ('$', True),
])
# yapf: enable
def test_not_lowercase_letter(string: str, expected_nonmembership: bool) -> None:
    """Test seligimus.characters.lowercase_letters.not_lowercase_letter."""
    nonmembership: bool = not_lowercase_letter(string)

    assert nonmembership == expected_nonmembership
