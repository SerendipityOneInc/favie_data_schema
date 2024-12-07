import json
from typing import Any, get_args

from favie_data_common.common.pydantic_utils import PydanticUtils


def deserialize_data(expected_type: Any, value: Any) -> Any:
    if value is None:
        return None

    # 检查并转换基本类型
    if expected_type in {int, float, str, bool}:
        try:
            return expected_type(value)
        except ValueError:
            raise ValueError(f"Cannot convert value '{value}' to {expected_type.__name__}")

    # 处理字符串形式的复杂结构
    if isinstance(value, str):
        try:
            value = json.loads(value)
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON string for deserializing {expected_type}")

    if PydanticUtils.is_type_of_pydantic_class(expected_type):
        # 对 Pydantic 模型进行处理
        if isinstance(value, dict):
            return expected_type(**value)
        else:
            return value

    # 检查并处理复杂类型
    if PydanticUtils.is_type_of_list(expected_type):
        item_type = get_args(expected_type)[0]
        return [deserialize_data(item_type, item) for item in value]
    elif PydanticUtils.is_type_of_set(expected_type):
        item_type = get_args(expected_type)[0]
        return {deserialize_data(item_type, item) for item in value}
    elif PydanticUtils.is_type_of_tuple(expected_type):
        item_types = get_args(expected_type)
        return tuple(deserialize_data(item_type, item) for item_type, item in zip(item_types, value))
    elif PydanticUtils.is_type_of_dict(expected_type):
        key_type, val_type = get_args(expected_type)
        return {deserialize_data(key_type, k): deserialize_data(val_type, v) for k, v in value.items()}

    # 默认返回原始值
    return value
