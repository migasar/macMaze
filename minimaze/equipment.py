"""Gere les items à récupérer"""


from position import Position
from board import Board

import settings as constants


class Equipment:

    def __init__(self, board):
        self.board = board
        self.position = None

        self.homing()

    def homing(self):
        home = self.board.get_case("landing", "start")
        home.toping = constants.HERO_CHAR
        self.position = Position(home.x, home.y)
        return self.position
