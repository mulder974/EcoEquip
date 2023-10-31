from fastapi import APIRouter
from app.models.devices import DevicesOutput
from app.services.devices_service import DevicesService

router = APIRouter()

devices_service = DevicesService()


@router.get("/devices", response_model=DevicesOutput)
async def get_devices():
    devices_list = devices_service.devices_list()
    return {"devices_list": devices_list}
