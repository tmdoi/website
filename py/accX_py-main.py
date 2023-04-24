from microbit import *

while True:
    acceleration_x = accelerometer.get_x()
    abs_acceleration_x = abs(acceleration_x)

    if abs_acceleration_x > 300:
        display.show(Image.HAPPY)
    elif abs_acceleration_x > 100:
        display.show(Image.SQUARE)
    else:
        display.show(Image.SAD)

    sleep(100)
