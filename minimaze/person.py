"""Gere les personnages"""


from position import Position
from board import Board


class Hero:

    def __init__(self, board):

        # toolbox (start empty --> counter full at 3)
        self.board = board
        self.position = None

        self.localize()
    
    def localize(self):
        for block in self.board.grid:
            if block.landing == "start":
                self.position = Position(block.x, block.y)
            break
        return self.position
    
    # Methods :
    # 4 moves (up, down, left, right)
    def up(self):
        """Brings a new position based on the previous position.
            The trick with this function is that it doesn't modify the instance position that is calling it
            It creates an entirely new instance position, with a modification of the data (x, y) stored in the previous instance position
            That's why the function starts by using an instance position and ends by using a class Position
        """
        # create new x and y by retrieving the coordinates of the instance
        #x, y = self.position.x, self.position.y
        # create a new object position with modified coordinates
        new_position = Position(self.position.x, self.position.y + 1)
        
        #verify that the new position is not a wall
        new_case = None
        for block in self.board.grid:
            if block.x == new_position.x and block.y == new_position.y:
                new_case = block
            break
        if new_case.walk is True:
            self.position = new_position
            return self.position
        else:
            print(
                """
                Mac Gyver ne peut pas aller par là
                """
                )

    def down(self):
        x, y = self.position
        return Position(x, y-1)

    def right(self):
        x, y = self.position
        return Position(x+1, y)

    def left(self):
        x, y = self.position
        return Position(x-1, y)

    """
    def move(self, direction):
        # getattr can access an object property using a string
        new_position = getattr(self.position, direction)()

        new_case = None
        for block in self.board.grid:
            if block.x == new_position.x and block.y == new_position.y:
                new_case = block
            break

        if new_case.walk is True:
            self.position = new_position
    """

class Enemy:
    #Enemy et Hero pouraient avoir une classe parent (la classe Person)

    # def __init__()

    # Attributes :
    # position (main attribute)
    pass
