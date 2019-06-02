"""
Manage the board of the game 
and the interactions between its squares and the other elements of the game
"""


from random import choice

from models.position import Position
from models.square import Square

import config.constants as constants


class Board:

    def __init__(self, grid):
        self.grid = grid

    @classmethod
    def load_blueprint(cls, pick = True):

        if pick == True:
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
                        block = Square(x, y, walk=True, landing='start', visual=col)
                    elif col == 'G':
                        block = Square(x, y, walk=True, landing='goal', visual=col)
                    elif col == '.':
                        block = Square(x, y, walk=True, visual=col)
                    else:
                        block = Square(x, y, walk=False, visual=col)

                    grid[y].append(block)

        return cls(grid)

    @classmethod
    def pick_board(cls):
        return constants.reach_board(
            choice(constants.BOARDS_LIST)
            )


    ## methods related to the size of the board
    ######
    @property
    def width(self):
        return self.grid[-1][-1].x_square

    @property
    def height(self):
        return self.grid[-1][-1].y_square

    def inside(self,step):
        # check if the position is still inside the boundaries of the board 
        return 0 <= step.x_pos <= self.width and 0 <= step.y_pos <= self.height
    ######


    ## methods to get to a specific square of the board
    ######
    def pathfinder(self):
        # return a list with every empty squares of the board
        pathway = []
        for y, line in enumerate(self.grid):
            for x, block in enumerate(self.grid[y]):
                if block.free == True:
                    pathway.append((x, y))
        return pathway

    def random_path(self):
        # select randomly an empty square of the board
        pathway = self.pathfinder()
        path_index = choice(pathway)
        free_path = self.grid[path_index[1]][path_index[0]]
        return free_path

    def get_square(self, att, val):
        # return a square with a specific attribute
        for y, line in enumerate(self.grid):
            for block in self.grid[y]:
                if getattr(block, att) == val:
                    return block 
    
    def get_coordinates(self, attx, atty, valx, valy):
        # return a square matching a specific position
        for y, line in enumerate(self.grid):
            for block in self.grid[y]:
                if (
                    getattr(block, attx) == valx 
                    and getattr(block, atty) == valy
                    ):
                        return block
    ######


    ## method to know how the game ends
    ######
    def game_over(self):
        # check if the hero has won the game
        end = self.get_square('landing', 'goal')
        return end.toping == constants.HERO_CHAR
    ######
