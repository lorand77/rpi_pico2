from machine import Pin, ADC
import utime
import tm1637

potmeter = ADC(Pin(28))
display = tm1637.TM1637(clk=Pin(18), dio=Pin(19))


while True:
    pot_value = round(potmeter.read_u16()*100/65535)
    display.number(pot_value)
    utime.sleep(0.1)

