from machine import Pin, Timer

led = Pin(25, Pin.OUT)

led_state = 0

def blink_led(timer):
    global led_state
    if led_state == 0:
        led_state = 1
    else:
        led_state = 0
    led.value(led_state)

timer = Timer()
timer.init(period=500, mode=Timer.PERIODIC, callback=blink_led)

while True:
    pass
