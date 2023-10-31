from pydantic import BaseModel




class EnergyCalculationInput(BaseModel):
    device_type_conso: dict


class EnergyCalculationOutput(BaseModel):
    energy_consumed: float


