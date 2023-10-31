from fastapi import FastAPI

from app.controllers.energy_controller import router as energy_router
from app.controllers.device_controller import router as device_router

app = FastAPI()

app.include_router(energy_router, tags=["Energy"])
app.include_router(device_router, tags=["Device"])
