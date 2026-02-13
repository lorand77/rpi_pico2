from machine import Pin, PWM
import time

led = PWM(Pin(16))
led.freq(1000)

while True:
    for duty in range(0, 65535, 1000):
        led.duty_u16(duty)
        time.sleep(0.01)
    for duty in range(65535, 0, -1000):
        led.duty_u16(duty)
        time.sleep(0.01)
