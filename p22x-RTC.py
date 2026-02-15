from machine import Pin, I2C
import time

DS3231_ADDR = 0x68

i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=100000)

def bcd2dec(bcd):
    return (bcd >> 4) * 10 + (bcd & 0x0F)

def dec2bcd(dec):
    return ((dec // 10) << 4) + (dec % 10)

def set_time(year, month, day, hour, minute, second):
    data = bytearray(7)
    data[0] = dec2bcd(second)
    data[1] = dec2bcd(minute)
    data[2] = dec2bcd(hour)
    data[3] = dec2bcd(0)  # weekday (not used here)
    data[4] = dec2bcd(day)
    data[5] = dec2bcd(month)
    data[6] = dec2bcd(year - 2000)
    i2c.writeto_mem(DS3231_ADDR, 0x00, data)

def read_time():
    data = i2c.readfrom_mem(DS3231_ADDR, 0x00, 7)
    second = bcd2dec(data[0])
    minute = bcd2dec(data[1])
    hour   = bcd2dec(data[2])
    day    = bcd2dec(data[4])
    month  = bcd2dec(data[5])
    year   = bcd2dec(data[6]) + 2000
    return (year, month, day, hour, minute, second)

# Example: Set time once
#set_time(2026, 2, 15, 9, 17, 0)

# Read time loop
while True:
    t = read_time()
    print("{:04d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}".format(*t))
    time.sleep(1)
