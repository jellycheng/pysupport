import json
from typing import Any

def toJson(data: Any, is_default_list_str: bool = False) -> str:
    """序列化JSON数据,对象转字符串"""
    if data is None or not data:
        return "[]" if is_default_list_str else "{}"
    try:
        return json.dumps(data, ensure_ascii=False)
    except (TypeError, ValueError):
        return "[]" if is_default_list_str else "{}"

def unJson(data: str, is_default_list: bool = False) -> Any:
    """反序列化JSON数据,字符串转对象"""
    if data is None or not data:
        return [] if is_default_list else {}
    try:
        return json.loads(data)
    except json.JSONDecodeError:
        return [] if is_default_list else {}

