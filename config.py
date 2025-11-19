import os

SERVER_URL = os.environ.get('SERVER_URL', 'http://192.168.0.95:31357/ngsi-ld/v1/entities')
SENSOR_INTERVAL = 1
CAMERA_STREAM_URL = os.environ.get('CAMERA_STREAM_URL', 'http://172.16.30.102:81/stream')
