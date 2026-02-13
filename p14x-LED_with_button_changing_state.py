from machine import Pin, Timer
import utime


## Onboard LED blinking

led_onboard = Pin(25, Pin.OUT)
led_onboard_state = 0

def blink_led_onboard(timer):
    global led_onboard_state
    if led_onboard_state == 0:
        led_onboard_state = 1
    else:
        led_onboard_state = 0
    led_onboard.value(led_onboard_state)

timer = Timer()
timer.init(period=500, mode=Timer.PERIODIC, callback=blink_led_onboard)


## External LED controlled by button

led = Pin(16, Pin.OUT)
button = Pin(15, Pin.IN, Pin.PULL_UP)
led_state = 0
last_time = 0 

def button_pressed(pin):
    global led_state, last_time
    now = utime.ticks_ms()
    if utime.ticks_diff(now, last_time) > 50:  
        utime.sleep_ms(20)  
        if button.value() == 0:  
            if led_state == 0:
                led_state = 1
            else:
                led_state = 0
            led.value(led_state)
            last_time = now

button.irq(trigger=Pin.IRQ_FALLING, handler=button_pressed)


## Main loop

while True:
    pass
