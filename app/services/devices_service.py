from app.db.crud import get_all_device_names


class DevicesService:

    @staticmethod
    def devices_list():
        return get_all_device_names()
