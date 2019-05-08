"""Gere les items à récupérer"""


from position import Position
from board import Board

import settings as constants


class Equipment:

    def __init__(self, board):
        self.board = board
        self.position = None

        self.clustering(self.char)
 
 
    def clustering(self, char):
    # Initialize the position of the equipment on the grid
        cluster = self.board.random_path()
        cluster.toping = char
        self.position = Position(cluster.x, cluster.y)
        return self.position


class Ether(Equipment):
    char = constants.ITEM_1_CHAR


class Needle(Equipment):
    char = constants.ITEM_2_CHAR


class Tube(Equipment):
    char = constants.ITEM_3_CHAR
