"""Gere les personnages"""


import settings as constants


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
                block.toping = constants.HERO_CHAR
                self.position = Position(block.x, block.y)
            break
        return self.position
    
    # Methods :
    # 4 moves (up, down, left, right)
    def up(self):

        back_step = Position(self.position.x, self.position.y)
        next_step = Position(self.position.x, self.position.y - 1)
        
        #verify that the new position is not a wall
        for i, block in enumerate(self.board.grid):
            if block.x == next_step.x and block.y == next_step.y:
                if block.walk is True:
                    self.board.grid[i].toping = constants.HERO_CHAR
                    for j, back in enumerate(self.board.grid):
                        if back.x == back_step.x and back.y == back_step.y:
                            self.board.grid[j].toping = ""
                            break
                    self.position = next_step
                    return self.position
                else:
                    print(
                        """
                        Mac Gyver ne peut pas aller par là
                        """
                        )

    def down(self):

        back_step = Position(self.position.x, self.position.y)
        next_step = Position(self.position.x, self.position.y + 1)
        
        #verify that the new position is not a wall
        for i, block in enumerate(self.board.grid):
            if block.x == next_step.x and block.y == next_step.y:
                if block.walk is True:
                    self.board.grid[i].toping = constants.HERO_CHAR
                    for j, back in enumerate(self.board.grid):
                        if back.x == back_step.x and back.y == back_step.y:
                            self.board.grid[j].toping = ""
                            break
                    self.position = next_step
                    return self.position
                else:
                    print(
                        """
                        Mac Gyver ne peut pas aller par là
                        """
                        )

    def right(self):
        back_step = Position(self.position.x, self.position.y)
        next_step = Position(self.position.x + 1, self.position.y)
        
        #verify that the new position is not a wall
        for i, block in enumerate(self.board.grid):
            if block.x == next_step.x and block.y == next_step.y:
                if block.walk is True:
                    self.board.grid[i].toping = constants.HERO_CHAR
                    for j, back in enumerate(self.board.grid):
                        if back.x == back_step.x and back.y == back_step.y:
                            self.board.grid[j].toping = ""
                            break
                    self.position = next_step
                    return self.position
                else:
                    print(
                        """
                        Mac Gyver ne peut pas aller par là
                        """
                        )

    def left(self):
        back_step = Position(self.position.x, self.position.y)
        next_step = Position(self.position.x - 1, self.position.y)
        
        #verify that the new position is not a wall
        for i, block in enumerate(self.board.grid):
            if block.x == next_step.x and block.y == next_step.y:
                if block.walk is True:
                    self.board.grid[i].toping = constants.HERO_CHAR
                    for j, back in enumerate(self.board.grid):
                        if back.x == back_step.x and back.y == back_step.y:
                            self.board.grid[j].toping = ""
                            break
                    self.position = next_step
                    return self.position
                else:
                    print(
                        """
                        Mac Gyver ne peut pas aller par là
                        """
                        )

class Enemy:
    #Enemy et Hero pouraient avoir une classe parent (la classe Person)

    # def __init__()

    # Attributes :
    # position (main attribute)
    pass
