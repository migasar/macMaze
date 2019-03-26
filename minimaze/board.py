# gere la map des objets

import settings as constants
from position import Position

class Board:

    def __init__(self, filename):
        self.filename = filename

        self.path = list()
        self.wall = list()
        self.start = list()
        self.goal = list()

        self.load_from_file()

    @property
    def start(self):
        return list(self.start)[0]

    def is_path_position(self, position):
        # check if a position is valid
        return position in self.path

    def load_from_file():
            with open(self.filename) as infile:
                for y, line in enumerate(infile):
                    for x, col in enumerate(line):
                        if col == constants.PATH_CHAR:
                            self.path.add(Position(x, y))
                        elif col == constants.START_CHAR:
                            self.start.add(Position(x, y))
                            self.path.add(Position(x, y))
                        elif col == constants.GOAL_CHAR:
                            self.goal.add(Position(x, y))
                            self.path.add(Position(x, y))
                        else :
                            self.wall.add(Position(x, y))


""" 
# TEST
def main():
    board = Board('board-01.txt')
    p = Position(1, 1)
    print(board.is_path_position(p))

if __name__ == "__main__":
    main()
"""
