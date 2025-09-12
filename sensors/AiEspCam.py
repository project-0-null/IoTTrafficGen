from ultralytics import YOLO


from .BaseSensor import BaseSensor
import random
import time
import cv2

class AiEspCam(BaseSensor):
    def __init__(self, sensor_id, sensor_location):
        super().__init__(sensor_id, "AI ESP Cam", sensor_location)

    def new_sensor(self):
        return {
            "id": "urn:ngsi-ld:AiEspCam:" + self.sensor_id,
            "type": "AiEspCam",
            "name": {
                "type": "Property",
                "value": "Presence Sensor"
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
            }
        }

    def update_peopleCount(self, peopleCount):
        data = {
            "peopleCount": {
            "type": "Property",
            "value": peopleCount
            }
        }
        return data
    
    def detect_person(self, stream_url):
        model = YOLO("yolo11n.pt")  # Certifique-se de usar um modelo YOLO válido
        cap = cv2.VideoCapture(stream_url)

        if not cap.isOpened():
            print("Erro ao abrir o stream")
            return

        ret, frame = cap.read()
        if not ret:
            print("Erro ao capturar frame")
            
        
        results = model(frame, stream=True)  # YOLO inference

        peopleCount = sum(1 for result in results for class_id in result.boxes.cls if int(class_id) == 0)  # Classe 0 é "person" no COCO
        return peopleCount
            

        cap.release()
        cv2.destroyAllWindows()
