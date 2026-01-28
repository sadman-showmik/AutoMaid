import paho.mqtt.client as mqtt
from datetime import datetime

BROKER = "test.mosquitto.org"
TOPIC = "automaid/sensors"
FILENAME = "automaid_data.json"

def on_connect(client, userdata, flags, rc):
    print("Connected! Code:", rc)
    client.subscribe(TOPIC)

def on_message(client, userdata, msg):
    data = msg.payload.decode()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Append JSON with timestamp to file
    with open(FILENAME, "a") as f:
        f.write(f"{timestamp} {data}\n")
    print(f"{timestamp} | Received JSON: {data}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, 1883, 60)
client.loop_forever()

