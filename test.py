import arcade
import random
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 5
KEY_STATUS= 0000
class MyGame(arcade.Window):
    """ Главный класс приложения. """

    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.AMAZON)
    def on_key_press(self, key, modifiers):
        print('нажата %d' % key)

    def on_key_release(self, key, modifiers):
        print('отпустили %d' % key)


    def setup(self):
        # Настроить игру здесь

        pass

    def on_draw(self):
        """ Отрендерить этот экран. """
        arcade.start_render()

        # Здесь код рисунка

    def update(self, delta_time):
        """ Здесь вся игровая логика и логика перемещения."""


        pass




def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main() 