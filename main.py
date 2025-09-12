import time
from config import SERVER_URL, SENSOR_INTERVAL
from sensors.ArtificialSensor import ArtificialSensor
from sensors.AiEspCam import AiEspCam
from sensors.BaseSensor import BaseSensor
import http_client

if __name__ == "__main__":
    # Create an instance of the ArtificialSensor class
    sensor = ArtificialSensor("1")
    data = sensor.new_sensor()
    status, response = http_client.create_entitie(SERVER_URL, data, None)
    print()
    print(f"Sent POST: {data} | Response: {status} - {response}")
    print()

    """    
    try:
        while True:
            # Simulate the sensor detecting a person
            data = sensor.update_people_count()
            status, response = http_client.update_attr_value(SERVER_URL, data, sensor.sensor_id, "peopleCount", "ArtificialSensor")
            print()
            print(f"Sent UPDATE: {data} | Response: {status} - {response}")
            print()
            time.sleep(SENSOR_INTERVAL)
    except KeyboardInterrupt:
        print("Stopping sensor updates...")
    
    """
    sensor_ids = ["ESPCAM1"]
    sensors = []
    for i in range(len(sensor_ids)):
        if http_client.get_entity(SERVER_URL, {'id': 'urn:ngsi-ld:AiEspCam:ESPCAM1'})[0] != 200: #need to dynamically get the sensor id
            sensor = AiEspCam(sensor_ids[i], [-20.272450, -40.306660])
            sensors.append(sensor)
            data = sensor.new_sensor(sensor_ids[i])
            status, response = http_client.create_entitie(SERVER_URL, data, None)
            print(f"Sent POST: {data} | Response: {status} - {response}")
        else: 
            #Must get the sensor id dynamically from the database through get and create the py object for it
            sensors.append(AiEspCam(sensor_ids[i], [-20.272450, -40.306660]))
            print("Sensor already exists")
    
    previous_people_count = 0
    while True:
        for sensor in sensors:
            current_people_count = sensor.detect_person("http://172.16.30.104:81/stream")
            if current_people_count != previous_people_count:
                print(current_people_count)
                data = sensor.update_people_count(current_people_count)
                status, response = http_client.update_attr_value(SERVER_URL, data, sensor.sensor_id, "people_count", "AiEspCam")
                print(f"Sent UPDATE: {data} | Response: {status} - {response}")
                previous_people_count = current_people_count

            
