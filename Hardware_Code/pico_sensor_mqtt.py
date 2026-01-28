import time
import dht
import network
import ujson
from machine import Pin, I2C, ADC
import ssd1306
from framebuf import FrameBuffer, MONO_HLSB
from umqtt.simple import MQTTClient

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
# Wi-Fi connection
# -------------------------------
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PASSWORD)
print("Connecting to Wi-Fi...")
while not wlan.isconnected():
    time.sleep(0.5)
print("Wi-Fi connected. IP:", wlan.ifconfig()[0])

# -------------------------------
# MQTT connection
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
# DHT22 Sensor
# -------------------------------
sensor = dht.DHT22(Pin(13))

# -------------------------------
# Gas Sensor (MIKROE-1630)
# ADC0 → GPIO26
# -------------------------------
gas_adc = ADC(26)

# -------------------------------
# Dust Sensor (Grove 101020012)
# ADC1 → GPIO27
# -------------------------------
dust_adc = ADC(27)

# -------------------------------
# OLED (I2C)
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
# Startup OLED
# -------------------------------
oled.fill(0)
oled.text("Automaid v1.0", 0, 0)
oled.text("All sensors OK", 0, 12)
oled.text("WiFi + MQTT", 0, 24)
oled.show()

print("System ready: DHT22 + PIR + Gas + Dust + MQTT")

# -------------------------------
# Dust sensor smoothing
dust_buffer = []
DUST_SAMPLES = 5   # number of samples to average
# Main loop
# -------------------------------
while True:
    # ---- DHT22 ----
    try:
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
    except OSError:
        temp = None
        hum = None

    # ---- PIR ----
    motion = pir.value() == 1

    if motion:
        led.on()
        buzzer.on()
        time.sleep(0.3)
        buzzer.off()
    else:
        led.off()

    # ---- Gas sensor ----
    gas_raw = gas_adc.read_u16()        # 0–65535
    gas_percent = int((gas_raw / 65535) * 100)
    # ---- Dust sensor ----
    dust_raw = dust_adc.read_u16()      # 0–65535
    dust_voltage = (dust_raw / 65535) * 3.3  # convert to volts (if needed)
    # ---- Dust smoothing ----
    dust_buffer.append(dust_raw)
    if len(dust_buffer) > DUST_SAMPLES:
        dust_buffer.pop(0)

    dust_avg = sum(dust_buffer) / len(dust_buffer)


    # ---- OLED ----
    oled.fill(0)

    oled.blit(temp_icon_fb, 0, 8)
    oled.text("Temp:", 12, 4)
    oled.text("--" if temp is None else "{:.1f}C".format(temp), 12, 18)

    oled.blit(humid_icon_fb, 0, 40)
    oled.text("Hum:", 12, 36)
    oled.text("--" if hum is None else "{:.1f}%".format(hum), 12, 50)

    oled.text("Gas:", 80, 36)
    oled.text("{}%".format(gas_percent), 80, 50)
    
    oled.text("Dust:", 80, 0)
    oled.text("{:.0f}".format(dust_avg), 80, 10)  # raw u16 average

    if motion:
        oled.text("MOTION!", 100, 0)

    oled.show()

    # ---- MQTT JSON ----
    payload = ujson.dumps({
        "temperature": temp,
        "humidity": hum,
        "motion": motion,
        "gas_raw": gas_raw,
        "gas_percent": gas_percent,
        "dust_raw": dust_raw,
        "dust_avg": dust_avg
    })

    try:
        client.publish(TOPIC, payload)
    except Exception as e:
        print("MQTT error:", e)

    # ---- Console ----
    print(
        "Temp:", "--" if temp is None else "{:.1f}C".format(temp),
        "| Hum:", "--" if hum is None else "{:.1f}%".format(hum),
        "| Motion:", "YES" if motion else "NO",
        "| Dust:", dust_avg, "µg/Cubic m"
        "| Gas:", gas_percent, "%"
    )

    time.sleep(2)
