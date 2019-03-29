

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
        self.position = (x, y - 1)
        return self.position

    def down(self):
        x, y = self.position
        self.position = (x, y + 1)
        return self.position

    def left(self):
        x, y = self.position
        self.position = (x - 1, y)
        return self.position

    def right(self):
        x, y = self.position
        self.position = (x + 1, y)
        return self.position


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


"""
p = Position(1, 1)

def main():
    print(p)
    p.up()
    print(p)
    return p

main()
"""
