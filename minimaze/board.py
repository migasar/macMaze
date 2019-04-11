"""Gere la map des objets"""


import settings as constants

from .position import Position
from .case import Case


class Board:

    def __init__(self, grid, starting, ending):

        self.grid = grid

        self.starting = starting
        self.ending = ending

    @property
    def strating(self):
        return self.starting
    
    @property
    def ending(self):
        return self.ending

    @classmethod
    def load_blueprint(cls, filename):

        grid = []

        starting = None
        ending = None

        with open(filename, 'r') as infile:
            for y, line in enumerate(infile):
                for x, col in enumerate(line):

                    if col == "S":
                        grid.append(Case(x, y, walk=True, landing="start"))
                        starting = Position(x, y)
                    elif col == "G":
                        grid.append(Case(x, y, walk=True, landing="goal"))
                        ending = Position(x, y)
                    elif col == ".":
                        grid.append(Case(x, y, walk=True))
                    else:
                        grid.append(Case(x, y, walk=False))

        return cls(grid, starting, ending)


"""
# TEST
def main():
    board = Board.load_blueprint(constants.blueprint)
    print(board.starting())


if __name__ == "__main__":
    main()
"""
