import network
import time
import dht
from machine import Pin, I2C
import ssd1306
from framebuf import FrameBuffer, MONO_HLSB
from umqtt.simple import MQTTClient
import ujson

# -------------------------------
# Wi-Fi credentials
# -------------------------------
SSID = "Prime"
PASSWORD = "presentgift"

# -------------------------------
# MQTT setup
# -------------------------------
BROKER = "test.mosquitto.org"
CLIENT_ID = "pico_automaid"
TOPIC = b"automaid/sensors"

# -------------------------------
# Initialize Wi-Fi
# -------------------------------
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PASSWORD)
print("Connecting to Wi-Fi...")
while not wlan.isconnected():
    time.sleep(0.5)
print("Wi-Fi connected. IP:", wlan.ifconfig()[0])

# -------------------------------
# Connect MQTT
# -------------------------------
client = MQTTClient(CLIENT_ID, BROKER)
client.connect()
print("MQTT connected")

# -------------------------------
# Onboard LED
# -------------------------------
led = Pin("LED", Pin.OUT)
led.off()

# -------------------------------
# PIR Sensor + Buzzer
# -------------------------------
pir = Pin(12, Pin.IN)
buzzer = Pin(15, Pin.OUT)
buzzer.off()

# -------------------------------
# DHT22
# -------------------------------
sensor = dht.DHT22(Pin(13))

# -------------------------------
# I2C OLED
# -------------------------------
i2c = I2C(0, scl=Pin(17), sda=Pin(16))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# -------------------------------
# Icons
# -------------------------------
temperature_icon = bytearray([
    0b00011000,0b00111100,0b00111100,0b00111100,
    0b00111100,0b00111100,0b00011000,0b00011000,
    0b00011000,0b00011000,0b00111100,0b01111110,
    0b01111110,0b01111110,0b00111100,0b00000000
])
humidity_icon = bytearray([
    0b00001000,0b00011100,0b00111110,0b01111111,
    0b01111111,0b01111111,0b00111110,0b00011100,
    0b00011100,0b00111110,0b00111110,0b00011100,
    0b00001000,0b00000000,0b00000000,0b00000000
])
temp_icon_fb = FrameBuffer(temperature_icon, 8, 16, MONO_HLSB)
humid_icon_fb = FrameBuffer(humidity_icon, 8, 16, MONO_HLSB)

# -------------------------------
# Startup OLED message
# -------------------------------
oled.fill(0)
oled.text("Automaid v1.0", 0, 0)
oled.text("Sensors active", 0, 12)
oled.text("Wi-Fi & MQTT", 0, 24)
oled.show()

print("System ready: DHT22 + PIR + Buzzer + OLED + MQTT")
