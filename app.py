# -*- coding: utf-8 -*-
"""
Launch the game and set its interface (CLI or GUI)
"""

from macmaze.controllers.cli_controller import CLIgame
from macmaze.controllers.gui_controller import GUIgame


def game_factory(graphical=True):
    """Set the type of interface of the game"""

    if graphical is True:
        factory = GUIgame
    else:
        factory = CLIgame

    game = factory()
    return game.controller.start()


def main():
    """Launch the game"""

    game_factory(graphical=True)


if __name__ == "__main__":
    main()
