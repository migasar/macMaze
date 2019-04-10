# gere la map des objets
"""DOCSTRING"""


import settings as constants

from position import Position
from case import Case


class Board:

    def __init__(self, grid, pathway, starting, ending, width, height):

        self.grid = grid

        self.pathway = pathway
        self.starting = starting
        self.ending = ending

        self.width = width
        self.height = height

    # Methods:
    # create an empty grid (a list of list --> 15 * 15)
    # load the structure of the board from a file
    # the data fetched from the file will be used as a blueprint
    # with each element from the file,
    # #we will create an object case per element of the list to populate the grid
    @classmethod
    def load_blueprint(cls, filename):
        #grid = {}
        grid = []
        pathway = []
        starting = None
        ending = None
        width = 0
        height = 0

        with open(filename, 'r') as infile:
            #k = 0
            for y, line in enumerate(infile):
                for x, col in enumerate(line):
                    #k += 1

                    if col == "S":
                        #f"case_{k}" = Case(x, y, walk=True, landing="start")
                        #grid[Position(x, y)] = f"case_{k}"
                        grid.append(Case(x, y, walk=True, landing="start"))
                        pathway.append(Position(x, y))
                        starting = Position(x, y)

                    elif col == "G":
                        #f"case_{k}" = Case(x, y, walk=True, landing="goal")
                        #grid[Position(x, y)] = f"case_{k}"
                        grid.append(Case(x, y, walk=True, landing="goal"))
                        pathway.append(Position(x, y))
                        ending = Position(x, y)

                    elif col == ".":
                        #f"case_{k}" = Case(x, y, walk=True)
                        #grid[Position(x, y)] = f"case_{k}"
                        grid.append(Case(x, y, walk=True))
                        pathway.append(Position(x, y))

                    else:
                        #f"case_{k}" = Case(x, y, walk=False)
                        #grid[Position(x, y)] = f"case_{k}"
                        grid.append(Case(x, y, walk=False))

        return cls(grid, pathway, starting, ending, x+1, y+1)

    #pass



"""
# TEST
def main():
    board = Board.load_blueprint(constants.blueprint)
    print(board.starting())
    

if __name__ == "__main__":
    main()
"""

board = Board.load_blueprint(constants.blueprint)
print(board.starting())
