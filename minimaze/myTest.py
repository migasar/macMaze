

import settings as constants


class Position:

    # Initialize an instance with its attributes
    def __init__(self, x, y):
        self.position = (x, y)
        self.x = x
        self.y = y 

    # Modify the print of the object
    def __repr__(self):
        return str(self.position)

    # Test if 2 positions are the same
    def __eq__(self, pos):
        return self.position == pos.position

    # Methods to modify a position
    def up(self):
        x, y = self.position 
        # je ne comprend pas pourquoi j'ai besoin de cette ligne
        self.position = (x, y - 1)
        self.x = x
        self.y = y - 1
        return self.position

    def down(self):
        x, y = self.position
        self.position = (x, y + 1)
        self.x = x
        self.y = y + 1
        return self.position

    def left(self):
        x, y = self.position
        self.position = (x - 1, y)
        self.x = x - 1
        self.y = y
        return self.position

    def right(self):
        x, y = self.position
        self.position = (x + 1, y)
        self.x = x + 1
        self.y = y
        return self.position



class Case:

    kind = ["path", "wall"]
    landing = ["start", "goal", None]
    toping_person = ["hero", "enemy", None]
    toping_item = ["item", "needle", None]

    def __init__(self, position, kind, landing=None, toping_person=None, toping_item=None):
        self.position = position
        self.kind = kind
        self.landing = landing
        self.toping_person = toping_person
        self.toping_item = toping_item

    # Modify the representation of the object
    def __repr__(self):
        return str(self.position)
    
    # Modify the detailed print of the object
    def __str__(self):
        pass

    # Method to deal with collision between objects standing on the case
    def modify_toping(self, top):
        pass


class Board:

    # Initialize an instance with its attributes
    def __init__(self, filename):
        self.filename = filename

        self.cases = []

        self.paths = []
        self.walls = []
        self.start = []
        self.goal = []

        self.load_from_file()
       #  self.load_blueprint()

    @property
    def start(self):
        return list(self.start)[0]

    def is_path_position(self, position):
        # check if a position is valid
        return position in self.paths
    
    def test_path(self, case):
        # check if a position is valid
        return "path" in self.kind

    def load_from_file():
        with open(self.filename) as infile:
            for y, line in enumerate(infile):
                for x, col in enumerate(line):
                    if col == constants.PATH_CHAR:
                        self.paths.add(Position(x, y))
                    elif col == constants.START_CHAR:
                        self.start.add(Position(x, y))
                        self.paths.add(Position(x, y))
                    elif col == constants.GOAL_CHAR:
                        self.goal.add(Position(x, y))
                        self.paths.add(Position(x, y))
                    else:
                        self.walls.add(Position(x, y))

"""
    def load_blueprint():
        with open(self.filename) as infile:
            for line in enumerate(infile):
                for col in enumerate(infile):
                    if col == constants.PATH_CHAR:
                        self.paths.add(Position(col, line))
                        self.cases.append(
                            Case(Position(col, line), kind="path"))
                    elif col == constants.START_CHAR:
                        self.start.add(Position(col, line))
                        self.paths.add(Position(col, line))
                        self.cases.append(
                            Case(Position(col, line), kind="path", landing="start"))
                    elif col == constants.GOAL_CHAR:
                        self.goal.add(Position(col, line))
                        self.paths.add(Position(col, line))
                        self.cases.append(
                            Case(Position(col, line), kind="path", landing="goal"))
                    else:
                        self.walls.add(Position(col, line))
                        self.cases.append(
                            Case(Position(col, line), kind="wall"))
"""




class Hero:

    # Initialize an instance with its attributes
    def __init__(self, board):
        self.board = board
        self.position = self.board.start

    def move(self, direction):
            """docstring."""
            # getattr can access an object property using a string
            new_position = getattr(self.position, direction)()
            if new_position in self.board:
                self.position = new_position


blueprint = constants.blueprint
p = Position(1, 1)
q = Position(1, 1)

def main():
    print("my board is coming")
    my_board = Board(blueprint)
    print("my board is here")

main()

