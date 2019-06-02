"""Manage the flow of the game"""


from CLI.board import Board
from CLI.person import Hero, Enemy
from CLI.equipment import Ether, Needle, Tube
from CLI.position import Position

from CLI.cli_view import CLIview
from CLI.cli_event import CLIevent

import config.constants as constants


class Game:

    def __init__(self):

        self.board = Board.load_blueprint(constants.BLUEPRINT)
        # TODO: randomize blueprint
            #   - create a method to randomize the choice of the file used as a blueprint
            #   - it will be a way to generate different mazes
            #   - this method could also be in the class Board

        self.hero = Hero(self.board)
        self.enemy = Enemy(self.board)
        
        self.ether = Ether(self.board)
        self.needle = Needle(self.board)
        self.tube = Tube(self.board)

        self.view = CLIview(self.board)
        self.event = CLIevent(self.board, self.hero, self.view)

    """
    def start(self):
        self.event.starter()
    """


def main():

    game = Game()
    #game.start()
    game.event.starter()


if __name__ == "__main__":
    main()

