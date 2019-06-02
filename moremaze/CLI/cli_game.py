"""Manage the flow of the game"""


from models.board import Board
from models.person import Hero, Guard
from models.equipment import Ether, Needle, Tube
from models.position import Position

from CLI.cli_view import CLIview
from CLI.cli_event import CLIevent

import config.constants as constants


class Game:

    def __init__(self):
        
        self.board = Board.load_blueprint(pick=False)

        self.hero = Hero(self.board)
        self.guard = Guard(self.board)
        
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

