# -*- coding: utf-8 -*-

"""
from GUI.gui_game import main as gui_main
from CLI.cli_game import main as cli_main
"""

from GUI.gui_game import main as gui_main
from CLI.cli_controller import Game as cli_game


def game_factory(appli = True):

    if appli == True:
        factory = gui_main
    else :
        factory = cli_game
    
    game = factory()
    return game.controller.starter()


def main():
    game_factory(False)


if __name__ == "__main__":
    main()

 