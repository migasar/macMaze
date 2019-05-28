"""
Manage the board of the game 
and the interactions between its cases and the other elements of the game
"""


from random import choice

from models.position import Position
from models.case import Case

from config import settings as constants


class Board:

    def __init__(self, grid):
        self.grid = grid

    @classmethod
    def load_blueprint(cls, filename):
        grid = []

        with open(filename) as infile:
            content = [
                line.strip() for line in infile.readlines() if line.strip()
                ]

            for y, line in enumerate(content):
                grid.append([])
                
                for x, col in enumerate(line):
                    if col == 'S':
                        block = Case(x, y, walk=True, landing='start', visual=col)
                    elif col == 'G':
                        block = Case(x, y, walk=True, landing='goal', visual=col)
                    elif col == '.':
                        block = Case(x, y, walk=True, visual=col)
                    else:
                        block = Case(x, y, walk=False, visual=col)

                    grid[y].append(block)

        return cls(grid)


    ## methods related to the size of the board
    ######
    @property
    def width(self):
        return self.grid[-1][-1].x_case

    @property
    def height(self):
        return self.grid[-1][-1].y_case

    def inside(self,step):
        # check if the position is still inside the boundaries of the board 
        return 0 <= step.x_pos <= self.width and 0 <= step.y_pos <= self.height
    ######


    ## methods to get to a specific case of the board
    ######
    def pathfinder(self):
        # return a list with every empty cases of the board
        pathway = []
        for y, line in enumerate(self.grid):
            for x, block in enumerate(self.grid[y]):
                if block.free == True:
                    pathway.append((x, y))
        return pathway

    def random_path(self):
        # select randomly an empty case of the board
        pathway = self.pathfinder()
        path_index = choice(pathway)
        free_path = self.grid[path_index[1]][path_index[0]]
        return free_path

    def get_case(self, att, val):
        # return a case with a specific attribute
        for y, line in enumerate(self.grid):
            for block in self.grid[y]:
                if getattr(block, att) == val:
                    return block 
    
    def get_coordinates(self, attx, atty, valx, valy):
        # return a case matching a specific position
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
        end = self.get_case('landing', 'goal')
        return end.toping == constants.HERO_CHAR
    ######
