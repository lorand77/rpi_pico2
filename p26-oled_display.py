from machine import I2C, Pin
from sh1106 import SH1106_I2C
#import framebuf

i2c = I2C(1, scl=Pin(19), sda=Pin(18), freq=100000)                                            # Init I2C using I2C0 defaults, SCL=Pin(GP9), SDA=Pin(GP8), freq=400000
oled = SH1106_I2C(128, 64, i2c)             


oled.fill(0)

oled.text("Raspberry Pi Pico 2 is awesome!",0,0)

#oled.text("Pico",0,10)

oled.show()


