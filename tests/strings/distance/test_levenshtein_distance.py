"""Test seligimus.strings.distance.levenshtein_distance."""
import pytest

from seligimus.strings.distance.levenshtein_distance import levenshtein_distance


# yapf: disable
@pytest.mark.parametrize('string_a, string_b, expected_distance', [
    ('', '', 0),
    ('wibble', 'wobble', 1),
    ('spam', 'ham', 2),
    ('foo', 'bar', 3),
])
# yapf: enable
def test_levenshtein_distance(string_a: str, string_b: str, expected_distance: int) -> None:
    """Test seligimus.strings.distance.levenshtein_distance.levenshtein_distance."""
    distance: int = levenshtein_distance(string_a, string_b)

    assert distance == expected_distance
