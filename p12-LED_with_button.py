from machine import Pin
import time

led = Pin(16, Pin.OUT)
button = Pin(15, Pin.IN, Pin.PULL_UP)

while True:
    if button.value() == 0:
        led.on()
    else:
        led.off()
    time.sleep(0.02)
