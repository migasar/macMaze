# -*- coding: utf-8 -*-
"""
Launch the game and set its interface (CLI or GUI)
"""

from controllers.gui_controller import Game as gui_game
from controllers.cli_controller import Game as cli_game



def game_factory(graphic = True):
    """Set the type of interface of the game"""

    if graphic == True:
        factory = gui_game
    else :
        factory = cli_game
    
    game = factory()
    return game.controller.start()


def main():
    """Launch the game"""
    
    game_factory(graphic = False)


if __name__ == "__main__":
    main()
