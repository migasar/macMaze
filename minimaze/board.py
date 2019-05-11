"""
Manage the board of the game 
and the interactions between its cases and the other elements of the game
"""


from random import choice

from position import Position
from case import Case

import settings as constants


class Board:

    def __init__(self, grid):
        self.grid = grid


    @classmethod
    def load_blueprint(cls, filename):
        grid = []

        with open(filename, 'r') as infile:

            content = [
                line.strip() for line in infile.readlines() if line.strip()
                ]

            for y, line in enumerate(content):
                for x, col in enumerate(line):
                    if col == "S":
                        grid.append(
                            Case(x+1, y+1, walk=True, landing="start", visual=col)
                            )
                    elif col == "G":
                        grid.append(
                            Case(x+1, y+1, walk=True, landing="goal", visual=col)
                            )
                    elif col == ".":
                        grid.append(
                            Case(x+1, y+1, walk=True, visual=col)
                            )
                    else:
                        grid.append(
                            Case(x+1, y+1, walk=False, visual=col)
                            )

        return cls(grid)


    @property
    def width(self):
        return self.grid[-1].x

    @property
    def height(self):
        return self.grid[-1].y

    def inside(self,step):
        # check if the position is still inside the boundaries of the board 
        return 1 <= step.x <= self.width and 1 <= step.y <= self.height


    def pathfinder(self):
        # return a list with every empty cases of the board
        pathway = []
        for i, block in enumerate(self.grid):
            if block.free == True:
                pathway.append(i)
        return pathway

    def random_path(self):
        # select randomly an empty case of the board
        pathway = self.pathfinder()
        path_index = choice(pathway)
        free_path = self.grid[path_index]
        return free_path


    def get_case(self, att, val):
        # return a case with a specific attribute
        for i, block in enumerate(self.grid):
            if getattr(block, att) == val:
                return block

    def get_case_index(self, att, val):
        # return the index of a case with a specific attribute
        for i, block in enumerate(self.grid):
            if getattr(block, att) == val:
                return i

    def get_coordinates(self, attx, atty, valx, valy):
        # return a case matching a specific position
        for i, block in enumerate(self.grid):
            if getattr(block, attx) == valx and getattr(block, atty) == valy:
                return block
   

    def game_over(self):
        # check if the hero has won the game
        end = self.get_case("landing", "goal")
        return end.toping == constants.HERO_CHAR
