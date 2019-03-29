

import settings as constants


class Position:

    # Initialize an instance with its attributes
    def __init__(self, x, y):
        self.position = (x, y)

    # Modify the print of the object
    def __repr__(self):
        return str(self.position)

    # Test if 2 positions are the same
    def __eq__(self, pos):
        return self.position == pos.position

    # Methods to modify a position
    def up(self):
        x, y = self.position
        print(x)
        print(y)
        print(y - 1)
        self.position = (x, y - 1)
        return self.position

    def down(self):
        pass

    def right(self):
        pass

    def left(self):
        pass


class Board:

    # Initialize an instance with its attributes
    def __init__(self, filename):
        self.filename = filename

    @property
    def start(self):
        pass

    def is_path_position(self, position):
        pass

    def load_from_file():
        pass


class Hero:

    # Initialize an instance with its attributes
    def __init__(self, board):
        self.board = board


p = Position(1, 1)

def main():
    print(p)
    print(type(p))
    p.up()
    print(p)
    print(type(p))
    return p

main()
