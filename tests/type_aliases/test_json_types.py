"""Test seligimus.type_aliases_.json_types."""
from typing import Any, Dict, List, Union

from seligimus.type_aliases.json_types import JSON, JSONObject, JSONObjectList


def test_json() -> None:
    """Test seligimus.type_aliases_.json_types.JSON"""
    assert JSON == Union[None, bool, int, float, str, List[Any], Dict[str, Any]]


def test_json_object() -> None:
    """Test seligimus.type_aliases_.json_types.JSONObject."""
    assert JSONObject == Dict[str, JSON]


def test_json_object_list() -> None:
    """Test seligimus.type_aliases_.json_types.JSONObjectList."""
    assert JSONObjectList == List[JSONObject]
