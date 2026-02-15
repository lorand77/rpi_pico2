from machine import Pin, I2C
import utime
import tm1637

DS3231_ADDR = 0x68

i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=100000)
display = tm1637.TM1637(clk=Pin(18), dio=Pin(19))

def bcd2dec(bcd):
    return (bcd >> 4) * 10 + (bcd & 0x0F)

def dec2bcd(dec):
    return ((dec // 10) << 4) + (dec % 10)

def read_time():
    data = i2c.readfrom_mem(DS3231_ADDR, 0x00, 2)
    second = bcd2dec(data[0])
    minute = bcd2dec(data[1])
    return (minute, second)

while True:
    t = read_time()
    display.numbers(t[0], t[1])
    utime.sleep_ms(100)
