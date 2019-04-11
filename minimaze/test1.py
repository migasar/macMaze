
from dataclasses import dataclass

import settings as constants


class Position:

    def __init__(self, x, y):
        self.position = (x, y)

    # Magic Methods:
    def __repr__(self):
        return str(self.position)

    def __hash__(self):
        return hash(self.position)

    def __eq__(self, pos):
        return self.position == pos.position

    # Methods :
    # 4 moves (up, down, left, right)
    def up(self):
        """Brings a new position based on the previous position.
            The trick with this function is that it doesn't modify the instance position that is calling it
            It creates an entirely new instance position, with a modification of the data (x, y) stored in the previous instance position
            That's why the function starts by using an instance position and ends by using a class Position
        """
        # create new x and y by retrieving the coordinates of the instance
        x, y = self.position
        # create a new object position with modified coordinates
        return Position(x, y-1)

    def down(self):
        x, y = self.position
        return Position(x, y+1)

    def right(self):
        x, y = self.position
        return Position(x+1, y)

    def left(self):
        x, y = self.position
        return Position(x-1, y)


@dataclass(order=True)
class Case:
    x: int
    y: int
    #position : tuple
    walk: bool
    landing: str = ""
    toping: str = ""


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


class Hero:

    def __init__(self, board):
        # Attributes :
        # position (main attribute --> begin with the position on the case "start")
        # toolbox (start empty --> counter full at 3)
        self.board = board
        self.position = self.board.starting

    def move(self, direction):
        """docstring."""
        # getattr can access an object property using a string
        new_position = getattr(self.position, direction)()
        if new_position in self.board:
            self.position = new_position


# TEST
def main():
    board = Board.load_blueprint('board_01.txt')
    print(board.starting())


if __name__ == "__main__":
    main()
