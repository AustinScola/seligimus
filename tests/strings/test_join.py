"""Test seligimus.strings.join."""
from typing import Any, Dict, List

import pytest

from seligimus.strings.join import join


# yapf: disable
@pytest.mark.parametrize('arguments, keyword_arguments, expected_string', [
    ([[], ''], {}, ''),
    ([['foo'], ', '], {}, 'foo'),
    ([['foo', 'bar'], ', '], {}, 'foo, bar'),
    ([['foo', 'bar', 'baz'], ', '], {}, 'foo, bar, baz'),
    ([['foo', 'bar', 'baz'], ' + '], {}, 'foo + bar + baz'),
    ([[], ', '], {'final': ' and '}, ''),
    ([['foo'], ', '], {'final': ' and '}, 'foo'),
    ([['foo', 'bar'], ', '], {'final': ' and '}, 'foo and bar'),
    ([['foo', 'bar', 'baz'], ', '], {'final': ' and '}, 'foo, bar and baz'),
    ([['foo', 'bar', 'baz', 'wibble'], ', '], {'final': ' and '}, 'foo, bar, baz and wibble'),
])
# yapf: enable
def test_join(arguments: List[str], keyword_arguments: Dict[str, Any],
              expected_string: str) -> None:
    """Test seligimus.strings.join.join."""
    string: str = join(*arguments, **keyword_arguments)

    assert string == expected_string
