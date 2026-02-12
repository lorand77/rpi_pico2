from machine import Pin
import time

led = Pin(25, Pin.OUT)

blink_interval = 1

while True:
    led.on()
    time.sleep(blink_interval)
    led.off()
    time.sleep(blink_interval)