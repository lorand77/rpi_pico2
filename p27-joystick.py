from machine import ADC, Pin
import utime

# Setup ADC pins
xAxis = ADC(27)
yAxis = ADC(26)

# Setup button (with internal pull-up)
button = Pin(22, Pin.IN, Pin.PULL_UP)

while True:
    xValue = xAxis.read_u16()
    yValue = yAxis.read_u16()
    buttonState = button.value()
    
    print("X:", xValue, " Y:", yValue, " Button:", buttonState)
    
    utime.sleep(0.2)