from microbit import *
import random

is_rotating = False
direction = 1
current_position = 0
current_speed = 25
is_slowing_down = False
positions = [
    (0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
    (4, 1), (4, 2), (4, 3), (4, 4),
    (3, 4), (2, 4), (1, 4), (0, 4),
    (0, 3), (0, 2), (0, 1)
]

def on_button_a_pressed():
    global is_rotating, direction, current_speed, is_slowing_down
    if not is_rotating:
        display.show("!", delay=200, clear=True)
        is_rotating = True
        is_slowing_down = False
        current_speed = 25
        if random.choice([True, False]):
            direction = 1
        else:
            direction = -1

def on_button_b_pressed():
    global is_slowing_down
    is_slowing_down = True

display.scroll("Roulette")

while True:
    if button_a.was_pressed():
        on_button_a_pressed()
    if button_b.was_pressed():
        on_button_b_pressed()

    if is_rotating:
        display.clear()
        x, y = positions[current_position]
        display.set_pixel(x, y, 9)
        current_position = (current_position + direction) % 16
        sleep(current_speed)

        if is_slowing_down:
            if current_speed < 300:
                current_speed += 25
            else:
                is_rotating = False
