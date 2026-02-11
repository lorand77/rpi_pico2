from machine import Pin
import time

led = Pin(25, Pin.OUT)

count = 0

while True:
    print(count)
    count += 1
    led.on()
    time.sleep(0.5)
    led.off()
    time.sleep(0.5)