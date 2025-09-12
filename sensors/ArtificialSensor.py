from .BaseSensor import BaseSensor
import random
import time

class ArtificialSensor(BaseSensor):
    def __init__(self, sensor_id):
        super().__init__(sensor_id, "artificial", [-20.272474, -40.306343])

    def new_sensor(self):
        return {
            "id": "urn:ngsi-ld:ArtificialSensor:" + self.sensor_id,
            "type": "ArtificialSensor",
            "name": {
                "type": "Property",
                "value": "Artificial Sensor"
            },
            "peopleCount": {
                "type": "Property",
                "value": 0
            },
            "location": {
                "type": "GeoProperty",
                "value": {
                    "type": "Point",
                    "coordinates": [self.sensor_location[0], self.sensor_location[1]]
                }
            },
            "timestamp": {
                "type": "Property",
                "value": time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime())
            },
            "@context": [
                "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context-v1.8.jsonld",
                "https://fiware.github.io/data-models/context.jsonld"
            ]
        }

    def update_peopleCount(self):
        data ={
            "type": "Property",
            "value": random.randint(0, 500)  # Simulate a random people count
            }

        return data

