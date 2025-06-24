from typing import Optional

from favie_data_common.common.pydantic_utils import PydanticUtils
from pydantic import BaseModel, field_validator

from favie_data_schema.favie.tools.data_mock_read import read_object


class EventItem(BaseModel):
    item_id: Optional[str] = None
    item_name: Optional[str] = None
    item_type: Optional[str] = None
    item_index: Optional[int] = None


class GensmoEvent(BaseModel):
    event_id: Optional[str] = None

    @field_validator("event_id", mode="before")
    def validate_event_id(cls, value):
        return PydanticUtils.deserialize_data(str, value)

    user_id: Optional[str] = None

    @field_validator("user_id", mode="before")
    def validate_user_id(cls, value):
        return PydanticUtils.deserialize_data(str, value)

    device_id: Optional[str] = None

    @field_validator("device_id", mode="before")
    def validate_device_id(cls, value):
        return PydanticUtils.deserialize_data(str, value)

    event_version: Optional[str] = None

    @field_validator("event_version", mode="before")
    def validate_event_version(cls, value):
        return PydanticUtils.deserialize_data(str, value)

    refer: Optional[str] = None

    @field_validator("refer", mode="before")
    def validate_refer(cls, value):
        return PydanticUtils.deserialize_data(str, value)

    ap_name: Optional[str] = None

    @field_validator("ap_name", mode="before")
    def validate_ap_name(cls, value):
        return PydanticUtils.deserialize_data(str, value)

    event_name: Optional[str] = None

    @field_validator("event_name", mode="before")
    def validate_event_name(cls, value):
        return PydanticUtils.deserialize_data(str, value)

    event_method: Optional[str] = None

    @field_validator("event_method", mode="before")
    def validate_event_method(cls, value):
        return PydanticUtils.deserialize_data(str, value)

    event_action_type: Optional[str] = None

    @field_validator("event_action_type", mode="before")
    def validate_event_action_type(cls, value):
        return PydanticUtils.deserialize_data(str, value)

    event_items: Optional[list[EventItem]] = None

    @field_validator("event_items", mode="before")
    def validate_event_items(cls, value):
        return PydanticUtils.deserialize_data(list[EventItem], value)

    event_ab_infos: Optional[list[int]] = None

    @field_validator("event_ab_infos", mode="before")
    def validate_event_ab_infos(cls, value):
        return PydanticUtils.deserialize_data(list[str], value)

    event_timestamp: Optional[int] = None

    @field_validator("event_timestamp", mode="before")
    def validate_event_timestamp(cls, value):
        return PydanticUtils.deserialize_data(int, value)

    user_login_type: Optional[str] = None

    @field_validator("user_login_type", mode="before")
    def validate_user_login_type(cls, value):
        return PydanticUtils.deserialize_data(str, value)

    platform: Optional[str] = None

    @field_validator("platform", mode="before")
    def validate_platform(cls, value):
        return PydanticUtils.deserialize_data(str, value)

    app_version: Optional[str] = None

    @field_validator("app_version", mode="before")
    def validate_app_version(cls, value):
        return PydanticUtils.deserialize_data(str, value)

    appsflyer_id: Optional[str] = None

    @field_validator("appsflyer_id", mode="before")
    def validate_appsflyer_id(cls, value):
        return PydanticUtils.deserialize_data(str, value)

    f_updates_at: Optional[str] = None

    @field_validator("f_updates_at", mode="before")
    def validate_f_updates_at(cls, value):
        return PydanticUtils.deserialize_data(str, value)

    f_creates_at: Optional[str] = None

    @field_validator("f_creates_at", mode="before")
    def validate_f_creates_at(cls, value):
        return PydanticUtils.deserialize_data(str, value)


if __name__ == "__main__":
    event = read_object("./favie_data_schema/favie/resources/gensmo_event.json", GensmoEvent)

    print(event.model_dump_json(exclude_none=True) if event else None)
