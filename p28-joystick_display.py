from machine import ADC, Pin, I2C
import utime
from sh1106 import SH1106_I2C
#import framebuf

xAxis = ADC(27)
yAxis = ADC(26)

i2c = I2C(1, scl=Pin(19), sda=Pin(18), freq=100000)                                            # Init I2C using I2C0 defaults, SCL=Pin(GP9), SDA=Pin(GP8), freq=400000
oled = SH1106_I2C(128, 64, i2c)

while True:
    xValue = xAxis.read_u16()
    yValue = yAxis.read_u16()
    
    oled.fill(0)
    oled.pixel(xValue // 512, yValue // 1024, 1)
    oled.show()
    utime.sleep(0.2)
