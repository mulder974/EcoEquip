from pydantic import BaseModel


class DevicesOutput(BaseModel):
    devices_list: list
