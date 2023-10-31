from fastapi import APIRouter
from app.models.energy import EnergyCalculationInput, EnergyCalculationOutput
from app.services.energy_service import EnergyService

router = APIRouter()

energy_service = EnergyService()

@router.post("/calculate_energy/", response_model=EnergyCalculationOutput)
async def calculate_energy(input_data: EnergyCalculationInput):
    energy_consumed = energy_service.calculate_energy(input_data=input_data)
    return {"energy_consumed": energy_consumed}
