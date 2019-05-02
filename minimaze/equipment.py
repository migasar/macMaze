"""Gere les items à récupérer"""


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
