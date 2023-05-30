from microbit import *
import random

class LedSprite:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.light()
        
    def light(self):
        display.set_pixel(self.x, self.y, 9)

    def get(self, direction):
        return self.x if direction == 'x' else self.y

    def is_touching(self, sprite):
        return self.x == sprite.x and self.y == sprite.y

    def change(self, direction, value):
        display.set_pixel(self.x, self.y, 0)
        if direction == 'x':
            self.x += value
            if self.x < 0:
                self.x = 0
            elif self.x > 4:
                self.x = 4
        else:
            self.y += value
            if self.y < 0:
                self.y = 0
            elif self.y > 4:
                self.y = 4
        self.light()

ball = LedSprite(2, 0)
paddle = LedSprite(2, 4)
ballDirX = 1
ballDirY = 1

while True:
    sleep(500)
    if ball.get('x') == 0 or ball.get('x') == 4:
        ballDirX = -ballDirX
    if ballDirY == -1 and ball.get('y') == 1 and random.randint(-1, 1) == 0:
        ballDirY = -ballDirY
    if ball.get('y') == 0:
        ballDirY = -ballDirY
    ball.change('x', ballDirX)
    ball.change('y', ballDirY)

    paddle.light()  # Ensure paddle is lit after ball moves

    if ball.is_touching(paddle):
        ballDirY = -ballDirY
        ballDirX = random.randint(-1, 1)

    if ball.get('y') == 4 and not ball.is_touching(paddle):
        display.clear()
        display.scroll('Game Over!')
        break

    if button_a.is_pressed():
        paddle.change('x', -1)
    if button_b.is_pressed():
        paddle.change('x', 1)
