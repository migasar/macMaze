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
                self.position = (block.x, block.y)
            break
        return self.position
    
    def move(self, direction):
        """docstring"""
        # getattr can access an object property using a string
        new_position = getattr(self.position, direction)()
        if new_position in self.board:
            self.position = new_position


class Enemy:
    #Enemy et Hero pouraient avoir une classe parent (la classe Person)

    # def __init__()

    # Attributes :
    # position (main attribute)
    pass
