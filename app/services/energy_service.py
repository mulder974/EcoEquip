import csv
from app.db.crud import get_energy_consumption

class EnergyService:
    @staticmethod
    def calculate_energy(input_data):
        energy_consumed = 0
        for device, number in input_data.device_type_conso.items():
            try:
                energy_data = get_energy_consumption(device)
                if energy_data:
                    energy_consumed += (energy_data[0] * number)  # Assuming energy_data[0] corresponds to consumption_1
                else:
                    # Log that no energy data was found for the device
                    print(f"No energy data found for device: {device}")
            except Exception as e:
                # Log any exceptions that occur
                print(f"An error occurred while processing device: {device}, Error: {str(e)}")
        return energy_consumed





