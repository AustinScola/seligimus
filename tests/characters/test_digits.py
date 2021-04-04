"""Test seligimus.characters.digits."""
import pytest

from seligimus.characters.digits import DIGITS, is_digit, not_digit


def test_digits() -> None:
    """Test seligimus.characters.digits.DIGITS."""
    assert DIGITS == {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}


# yapf: disable
@pytest.mark.parametrize('string, expected_membership', [
    ('0', True),
    ('1', True),
    ('9', True),
    ('a', False),
    ('A', False),
    ('$', False),
])
# yapf: enable
def test_is_digit(string: str, expected_membership: bool) -> None:
    """Test seligimus.characters.digits.is_digit."""
    membership: bool = is_digit(string)

    assert membership == expected_membership


# yapf: disable
@pytest.mark.parametrize('string, expected_nonmembership', [
    ('0', False),
    ('1', False),
    ('9', False),
    ('a', True),
    ('A', True),
    ('$', True),
])
# yapf: enable
def test_not_digit(string: str, expected_nonmembership: bool) -> None:
    """Test seligimus.characters.digits.not_digit."""
    nonmembership: bool = not_digit(string)

    assert nonmembership == expected_nonmembership
