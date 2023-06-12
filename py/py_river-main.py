from microbit import *
import random

# Initialize a 5x5 list with all zeros
brightness = [[0]*5 for _ in range(5)]

while True:
    # Generate new random brightness for y=0
    brightness[0] = [random.choice(range(10)) for _ in range(5)]
    
    # Display current brightness
    for y in range(5):
        for x in range(5):
            display.set_pixel(x, y, brightness[y][x])
    
    sleep(200)
    
    # Shift brightness down
    brightness = brightness[-1:] + brightness[:-1]
