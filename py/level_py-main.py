from microbit import *
import math

def get_angle(x, y):
    angle = int((-(180 / math.pi) * math.atan2(y, x)) + 180)
    return angle

def map_value(value, in_min, in_max, out_min, out_max):
    return int((value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

while True:
    x = accelerometer.get_x()
    y = accelerometer.get_y()
    z = accelerometer.get_z()

    angle = get_angle(x, y)
    mapped_angle = map_value(angle, 0, 360, 0, 9)

    display.clear()

    if 80 <= angle <= 100:
        display.show(Image.YES)
    else:
        display.set_pixel(mapped_angle % 5, int(mapped_angle / 5), 9)

    sleep(100)
