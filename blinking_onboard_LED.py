from machine import Pin
import time

led = Pin(25, Pin.OUT)

count = 0
blink_interval = 1

while True:
    print(count)
    count += 1
    led.on()
    time.sleep(blink_interval)
    led.off()
    time.sleep(blink_interval)