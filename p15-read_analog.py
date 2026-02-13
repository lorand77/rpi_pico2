from machine import Pin, ADC
import utime

adc = ADC(Pin(28))

while True:
    raw = adc.read_u16()   # 16-bit scaled value (0-65535)
    voltage = raw * 3.261 / 65535
    print("Raw:", raw, "Voltage:", voltage)
    utime.sleep(0.5)
