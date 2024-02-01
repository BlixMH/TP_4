# Par Blix
# En 2023
# TP4

import arcade
import random

width = 800
height = 600


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(width, height, "TP 4")

        self.circles = []
        self.rectangles = []

    def setup(self):
        pass

    def on_draw(self):
        arcade.set_background_color(arcade.color.BLACK)
        arcade.start_render()

    def on_mouse_press(self, x: int, y: int, button, modifiers: None):
        if button == arcade.MOUSE_BUTTON_LEFT:
            ball = Ball()
            ball.draw(x, y)

            self.circles.append(ball)

        elif button == arcade.MOUSE_BUTTON_RIGHT:
            rect = Rectangle()
            rect.draw(x, y)

            self.rectangles.append(rect)


class Ball:
    def __init__(self):
        self.x = None
        self.y = None
        self.changex = None
        self.changey = None

        self.rayon = random.randint(10, 30)
        self.color = arcade.color

    def update(self):
        self.x += self.changex
        self.y += self.changey

        if self.x > width - self.rayon:
            self.x = width - self.rayon
            self.changex = 0

        if self.x < self.rayon:
            self.x = self.rayon
            self.changey = 0

        if self.y > height - self.rayon:
            self.y = height - self.rayon
            self.changey = 0

        if self.y < self.rayon:
            self.y = self.rayon
            self.changey = 0

        arcade.finish_render()

    def draw(self, x, y):
        self.x = x
        self.y = y

        arcade.draw_circle_filled(self.x, self.y, self.rayon, self.color.WHITE)


class Rectangle:
    def __init__(self):
        self.x = None
        self.y = None
        self.changex = None
        self.changey = None

        self.width = random.randint(10, 30)
        self.height = random.randint(10, 30)
        self.angle = random.randint(0, 359)

        self.color = arcade.color

    def update(self):
        if self.x > width - self.width:
            self.x = width - self.width
            self.changex = 0

        if self.x < self.width:
            self.x = self.width
            self.changey = 0

        if self.y > height - self.height:
            self.y = height - self.height
            self.changey = 0

        if self.y < self.height:
            self.y = self.height
            self.changey = 0

        arcade.finish_render()

    def draw(self, x, y):
        self.x = x
        self.y = y

        arcade.draw_rectangle_filled(self.x, self.y, self.width, self.height, self.color.WHITE, self.angle)


def main():
    global rect, circles
    my_game = MyGame()
    my_game.setup()

    arcade.draw_circle_filled(400, 300, 30, arcade.color.WHITE)
    for circles in my_game.circles:
        my_game.circles[circles].update()

    for rect in my_game.rectangles:
        my_game.rectangles[rect].update()

    arcade.run()




main()
