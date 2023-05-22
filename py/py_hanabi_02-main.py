from microbit import *
import math

centerX = 2
centerY = 2
radius = 0

while True:
    while radius <= 4:
        for x in range(centerX - radius, centerX + radius + 1):
            for y in range(centerY - radius, centerY + radius + 1):
                if 0 <= x < 5 and 0 <= y < 5 and math.sqrt((x - centerX) ** 2 + (y - centerY) ** 2) <= radius:
                    display.set_pixel(x, y, 9)
        sleep(200)
        radius += 1
        display.clear()
    radius = 0
