import random

class BaseSensor:
    def __init__(self, sensor_id, sensor_type, sensor_location):
        self.sensor_id = sensor_id
        self.sensor_type = sensor_type
        self.sensor_location = [sensor_location[1], sensor_location[0]]

    def new_sensor(self):
        """Método que cada sensor deve implementar"""
        raise NotImplementedError("Subclasses devem implementar este método")