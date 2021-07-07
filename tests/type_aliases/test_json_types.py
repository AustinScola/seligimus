"""Test seligimus.type_aliases_.json_types."""
from typing import Any, Dict, List, Union

from seligimus.type_aliases.json_types import JSON


def test_json() -> None:
    """Test seligimus.type_aliases_.json_types.JSON"""
    assert JSON == Union[None, bool, int, float, str, List[Any], Dict[str, Any]]
