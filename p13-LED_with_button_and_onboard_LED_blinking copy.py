from machine import Pin, Timer
import time


led_onboard = Pin(25, Pin.OUT)

led_state = 0

def blink_led(timer):
    global led_state
    if led_state == 0:
        led_state = 1
    else:
        led_state = 0
    led_onboard.value(led_state)

timer = Timer()
timer.init(period=500, mode=Timer.PERIODIC, callback=blink_led)


led = Pin(16, Pin.OUT)
button = Pin(15, Pin.IN, Pin.PULL_UP)

while True:
    if button.value() == 0:
        led.on()
    else:
        led.off()
    time.sleep(0.02)
