# gere la map des objets

import config.settings as constants
from .position import Position

class Board:

    def __init__(self, filename):
        self.filename = filename

        self._paths = set()
        self._start = set()
        self._goal = set()
        self._walls = set()

        self.load_from_file()

    @property
    def start(self):
        return list(self._start)[0]

    def __contains__(self, position):
        return position in self._paths

    def load_from_file():
            with open(self.filename) as infile:
                for y, line in enumerate(infile):
                    for x, col in enumerate(line):
                        if col == constants.PATH_CHAR:
                            self._paths.add(Position(x, y))
                        elif col == constants.START_CHAR:
                            self._start.add(Position(x, y))
                            self._paths.add(Position(x, y))
                        elif col == constants.GOAL_CHAR:
                            self._goal.add(Position(x, y))
                            self._paths.add(Position(x, y))
                        else :
                            self._walls.add(Position(x, y))



def main():
    board = Board('data/boards/board-01.txt')

p = Position(-1, 0)
print(board.is_path_position(p))

if __name__ == "__main__":
    main()

