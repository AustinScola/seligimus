"""Test seligimus.strings.drop."""
import pytest

from seligimus.strings.drop import drop


# yapf: disable
@pytest.mark.parametrize('string, expected_body', [
    ('', ''),
    ('a', ''),
    ('abc', 'bc'),
])
# yapf: enable
def test_drop(string: str, expected_body: str) -> None:
    """Test seligimus.strings.drop.drop."""
    body: str = drop(string)

    assert body == expected_body
