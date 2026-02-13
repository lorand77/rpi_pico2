from machine import Pin, ADC, PWM
import utime

potmeter = ADC(Pin(28))
led = PWM(Pin(16))
led.freq(1000)


while True:
    pot_v = potmeter.read_u16()
    led.duty_u16(pot_v)
    utime.sleep(0.05)
