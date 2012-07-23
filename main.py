#!/usr/bin/env python
from direct.showbase.ShowBase import ShowBase

from redgravel.menu import MainMenu


class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # Start the main menu,
        # which can start a game
        menu = MainMenu(self)


if __name__ == '__main__':
    gameApp = Game()
    gameApp.run()
