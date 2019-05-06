"""Gere les items à récupérer"""

from random import choice

from position import Position
from board import Board

import settings as constants


# TODO: create the class Equipment
#   - create a superclass (or a class with a class method for the type) to deal with each equipment
#   - introduce the library Random to generate the position of the equipment


class Equipment:

    def __init__(self, board):
        self.board = board
        self.position = None

        self.clustering(self.char)

 
    # Initialize the starting position of the person
    def clustering(self, char):
        cluster = self.random_path()
        print(cluster)
        cluster.toping = char
        self.position = Position(cluster.x, cluster.y)
        return self.position

    def random_path(self):
        if choice(self.board.grid).free is True:
            return choice(self.board.grid)
        else:
            self.random_path()


class Ether(Equipment):
    char = constants.ITEM_1_CHAR

class Needle(Equipment):
    char = constants.ITEM_2_CHAR

class Tube(Equipment):
    char = constants.ITEM_3_CHAR
