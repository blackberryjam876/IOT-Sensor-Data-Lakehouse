import json, time, random
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

CLIENT_ID = "sensor-sim"
ENDPOINT = "<your-iot-endpoint>.iot.us-east-1.amazonaws.com"
ROOT_CA = "certs/root-CA.crt"
PRIVATE_KEY = "certs/private.pem.key"
CERT_FILE = "certs/certificate.pem.crt"

client = AWSIoTMQTTClient(CLIENT_ID)
client.configureEndpoint(ENDPOINT, 8883)
client.configureCredentials(ROOT_CA, PRIVATE_KEY, CERT_FILE)
client.connect()

while True:
    payload = {
        "sensorId": "sensor-1",
        "timestamp": int(time.time()),
        "temperature": round(random.uniform(20.0, 30.0), 2),
        "humidity": round(random.uniform(30.0, 50.0), 2)
    }
    client.publish("sensors/data", json.dumps(payload), 1)
    print(f"Published: {payload}")
    time.sleep(5)
