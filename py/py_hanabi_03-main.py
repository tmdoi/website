from microbit import *
import random

# LEDの明るさのレベルを格納する配列
brightness_levels = [[0]*5 for _ in range(5)]

# LEDの明るさのレベルをランダムに設定する関数
def set_random_brightness():
    initial_brightness = random.randint(8, 10)  # 8, 9, 10のいずれかをランダムに選択
    for x in range(5):
        for y in range(5):
            distance = abs(x - 2) + abs(y - 2)  # (2,2)からの距離
            if distance <= initial_brightness - 6:
                brightness_levels[x][y] = initial_brightness - distance

# LEDの明るさのレベルを更新する関数
def update_brightness():
    all_zero = True
    for x in range(5):
        for y in range(5):
            if brightness_levels[x][y] > 0:
                brightness_levels[x][y] -= 1
                display.set_pixel(x, y, brightness_levels[x][y])  # 明るさのレベルを0-9の範囲にスケーリング
                all_zero = False
            else:
                display.set_pixel(x, y, 0)
    return all_zero

# メインループ
while True:
    set_random_brightness()
    while not update_brightness():
        sleep(250)  # 0.25秒待つ
