from microbit import *
import random

# 初期化
position = 0

while True:
    # 位置をランダムに決める
    position = random.randint(0, 4)
    
    # 花火が上昇
    for index in range(5):
        display.clear()
        display.set_pixel(position, 4 - index, 9)
        sleep(200)

    for index in range(3):
        display.clear()
        display.set_pixel(position, 4 - index, 9)
        sleep(200)

    # 花火が爆発
    display.clear()
    display.set_pixel(position, 2, 9)
    sleep(25)
    if position - 1 >= 0:
        display.set_pixel(position - 1, 1, 9)
    if position + 1 < 5:
        display.set_pixel(position + 1, 1, 9)
    if position - 1 >= 0:
        display.set_pixel(position - 1, 3, 9)
    if position + 1 < 5:
        display.set_pixel(position + 1, 3, 9)
    sleep(25)
    if position - 2 >= 0:
        display.set_pixel(position - 2, 2, 9)
    if position + 2 < 5:
        display.set_pixel(position + 2, 2, 9)
    display.set_pixel(position, 0, 9)
    display.set_pixel(position, 4, 9)
    sleep(200)

    # 爆発の後、花火が消える
    display.clear()
    sleep(200)
