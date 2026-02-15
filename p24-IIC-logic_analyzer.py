from machine import Pin, I2C

DS3231_ADDR = 0x68

i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=100000)

i2c.writeto(DS3231_ADDR, bytearray([0b11111111]))
# marker 0:   device address 1101000 (7 bits)
# marker 1:   write bit 0
# marker 2:   ack (0)
# marker 3:   data 8 bits (0b11111111)
# marker 4:   ack (0)

x = i2c.readfrom(DS3231_ADDR, 1)
[bin(y) for y in list(x)]
# ['0b1010000']
# marker 0:   device address 1101000 (7 bits)
# marker 1:   read bit 1
# marker 2:   ack (0)
# marker 3:   data 8 bits (0b01010000)
# marker 4:   nack (1)

x = i2c.readfrom_mem(DS3231_ADDR, 0x00, 1)
[bin(y) for y in list(x)]
#['0b1011001']
# marker 0:   device address 1101000 (7 bits)
# marker 1:   write bit 0
# marker 2:   ack (0)
# marker 3:   register address 0x00 (8 bits)
# marker 4:   ack (0)
# stop + start 
# marker 5:   device address 1101000 (7 bits)
# marker 6:   read bit 1
# marker 7:   ack (0)
# marker 8:   data 8 bits (0b01011001)
# marker 9:   nack (1)