from machine import ADC, Pin, I2C
import utime
from sh1106 import SH1106_I2C

SCREEN_WIDTH = 128
SCREEN_HEIGHT = 64
CIRCLE_RADIUS = 4

xAxis = ADC(27)
yAxis = ADC(26)
i2c = I2C(1, scl=Pin(19), sda=Pin(18), freq=100000)                                            # Init I2C using I2C0 defaults, SCL=Pin(GP9), SDA=Pin(GP8), freq=400000
oled = SH1106_I2C(SCREEN_WIDTH, SCREEN_HEIGHT, i2c)

x = SCREEN_WIDTH // 2
y = SCREEN_HEIGHT // 2

def fill_circle(display, cx, cy, radius, color):
    for dy in range(-radius, radius + 1):
        dx = int((radius * radius - dy * dy) ** 0.5)
        display.hline(cx - dx, cy + dy, 2 * dx + 1, color)

while True:
    xValue = xAxis.read_u16()
    yValue = yAxis.read_u16()
    vx = (xValue / 2**16 - 0.5) * 16
    vy = (yValue / 2**16 - 0.5) * 8
    x += int(vx)
    y += int(vy)
    if x < CIRCLE_RADIUS:
        x = CIRCLE_RADIUS
    elif x > SCREEN_WIDTH - 1 - CIRCLE_RADIUS:
        x = SCREEN_WIDTH - 1 - CIRCLE_RADIUS
    if y < CIRCLE_RADIUS:
        y = CIRCLE_RADIUS
    elif y > SCREEN_HEIGHT - 1 - CIRCLE_RADIUS:
        y = SCREEN_HEIGHT - 1 - CIRCLE_RADIUS
    #oled.fill(0)
    fill_circle(oled, x, y, CIRCLE_RADIUS, 1)
    oled.show()
    utime.sleep_ms(5)
