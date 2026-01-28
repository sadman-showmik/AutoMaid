import network
import time
from umqtt.simple import MQTTClient

# Wi-Fi credentials
SSID = "Prime"
PASSWORD = "presentgift"

# Connect Wi-Fi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PASSWORD)
while not wlan.isconnected():
    time.sleep(0.5)
print("Wi-Fi connected. IP:", wlan.ifconfig()[0])

# MQTT setup
BROKER = "test.mosquitto.org"
CLIENT_ID = "pico_test"

client = MQTTClient(CLIENT_ID, BROKER)
client.connect()
print("MQTT connected to broker")

# Publish a test message
TOPIC = b"automaid/test"
client.publish(TOPIC, b"Hello from Pico W!")
print("Test message sent")
client.disconnect()
print("MQTT disconnected")
