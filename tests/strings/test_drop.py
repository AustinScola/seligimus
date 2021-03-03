"""Test seligimus.strings.drop."""
import pytest

from seligimus.strings.drop import drop


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('string, expected_body', [
    ('', ''),
    ('a', ''),
    ('abc', 'bc'),
])
# yapf: enable # pylint: enable=line-too-long
def test_drop(string: str, expected_body: str) -> None:
    """Test seligimus.strings.drop.drop."""
    body: str = drop(string)

    assert body == expected_body
