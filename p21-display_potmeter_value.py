from machine import Pin, ADC
import utime
import tm1637

potmeter = ADC(Pin(28))
display = tm1637.TM1637(clk=Pin(18), dio=Pin(19))

display_value = 0

while True:
    pot_value = potmeter.read_u16()*100//65535
    if (abs(display_value - pot_value) > 1):
        display_value = pot_value
        display.number(display_value)
    utime.sleep(0.1)

