import time
from machine import Pin

led = Pin(25, Pin.OUT)
led_value = False

while True:
    led.value(led_value)
    time.sleep(1)
    led_value = not led_value
    print("blink")