"""
Manage the board of the game
and the interactions between its squares and the other elements of the game
"""

from random import choice

from models.square import Square
from config import constants


class Board:

    def __init__(self, grid):
        self.grid = grid

    @classmethod
    def load_blueprint(cls, pick=True):
        """
        Create a grid of squares that will serve as the maze for the game.
        The maze follows a scheme obtained from a text file.
        """

        if pick is True:
            filename = constants.BLUEPRINT
        else:
            filename = cls.pick_board()

        grid = []

        with open(filename) as infile:
            content = [
                line.strip() for line in infile.readlines() if line.strip()
                ]

            for y, line in enumerate(content):
                grid.append([])

                for x, col in enumerate(line):
                    if col == 'S':
                        block = Square(
                            x, y, walk=True, landing='start', visual=col
                        )
                    elif col == 'G':
                        block = Square(
                            x, y, walk=True, landing='goal', visual=col
                        )
                    elif col == '.':
                        block = Square(x, y, walk=True, visual=col)
                    else:
                        block = Square(x, y, walk=False, visual=col)

                    grid[y].append(block)

        return cls(grid)

    @classmethod
    def pick_board(cls):
        """Select randomly the scheme of the board"""

        return constants.reach_board(
            choice(constants.BOARDS_LIST)
            )

    ######
    # methods related to the size of the board
    @property
    def width(self):
        """Return the width of the board (number of squares as unit)"""

        return self.grid[-1][-1].x_square

    @property
    def height(self):
        """Return the height of the board (number of squares as unit)"""

        return self.grid[-1][-1].y_square

    def inside(self, step):
        """Check if the position is still inside the boundaries of the board"""

        return 0 <= step.x_pos <= self.width and 0 <= step.y_pos <= self.height

    ######
    # methods to get to a specific square of the board
    def pathfinder(self):
        """Return a list with every empty squares of the board"""

        pathway = []
        for y, line in enumerate(self.grid):
            for x, block in enumerate(self.grid[y]):
                if block.free is True:
                    pathway.append((x, y))
        return pathway

    def random_path(self):
        """Select randomly an empty square of the board"""

        pathway = self.pathfinder()
        path_index = choice(pathway)
        free_path = self.grid[path_index[1]][path_index[0]]
        return free_path

    def get_square(self, att, val):
        """Return a square matching a specific attribute"""

        for y, line in enumerate(self.grid):
            for block in self.grid[y]:
                if getattr(block, att) == val:
                    return block

    def get_coordinates(self, attx, atty, valx, valy):
        """Return a square matching a specific position"""

        for y, line in enumerate(self.grid):
            for block in self.grid[y]:
                if (
                    getattr(block, attx) == valx
                    and getattr(block, atty) == valy
                ):
                    return block
