from microbit import *

def show_direction(heading):
    if heading >= 315 or heading < 45:
        display.show("N")
    elif heading >= 45 and heading < 135:
        display.show("E")
    elif heading >= 135 and heading < 225:
        display.show("S")
    else:
        display.show("W")

while True:
    if button_a.was_pressed():
        heading = compass.heading()
        show_direction(heading)
    elif button_b.was_pressed():
        display.clear()

