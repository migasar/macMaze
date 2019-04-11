"""Gere les personnages"""


from .position import Position
from .board import Board


class Hero:

    def __init__(self, board):
        # Attributes :
        # position (main attribute --> begin with the position on the case "start")
        # toolbox (start empty --> counter full at 3)
        self.board = board
        self.position = self.board.starting

    def move(self, direction):
        """docstring."""
        # getattr can access an object property using a string
        new_position = getattr(self.position, direction)()
        if new_position in self.board:
            self.position = new_position

    # Magic Methods :
    # __repr__

    # Methods :
    # def move(self, direction):
        """this method permits the movement of the hero by verifying if the position is a valid one, and by solving eventual collisions with any object standing on the case"""
        # test if the new position doesn't put the hero outside of the board
        # test if the new position is not a wall
        # test if the new position is an empty case
        # if the case is not empty
        # solve the collision between the hero
        # and the object standing on the case


class Enemy:
    #Enemy et Hero pouraient avoir une classe parent (la classe Person)

    # def __init__()

    # Attributes :
    # position (main attribute)
    pass

