"""Gere les personnages"""


import settings as constants


from position import Position
from board import Board


class Hero:

    def __init__(self, board):
        # toolbox (start empty --> counter full at 3)
        self.board = board
        self.position = None

        self.homing()
    
    
    # Initialize the starting position of the Hero
    def homing(self):
        home = self.board.get_case("landing", "start")
        home.toping = constants.HERO_CHAR
        self.position = Position(home.x, home.y)
        return self.position
    

    # 4 moves (up, down, left, right)
    def move(self, next_step):
        back_step = Position(self.position.x, self.position.y)

        #check that the new position is inside the board
        if self.board.inside(next_step) == True:
            
            #check that the new position is not a wall
            blockade = self.board.get_coordinates("x", "y", next_step.x, next_step.y)

            if blockade.walk is True:
                blockade.toping = constants.HERO_CHAR

                #clean the case of the previous position
                back = self.board.get_coordinates("x", "y", back_step.x, back_step.y)
                back.toping = ""

                #change the position of the hero
                self.position = next_step
                return self.position

            else:
                print("Mac Gyver ne peut pas aller par là.")

            """
            for i, block in enumerate(self.board.grid):
                if block.x == next_step.x and block.y == next_step.y:
                    if block.walk is True:
                        self.board.grid[i].toping = constants.HERO_CHAR

                        #clean the case of the previous position
                        for j, back in enumerate(self.board.grid):
                            if back.x == back_step.x and back.y == back_step.y:
                                self.board.grid[j].toping = ""
                                break

                        self.position = next_step
                        return self.position

                    else:
                        print("Mac Gyver ne peut pas aller par là.")
            """

        else:
            print("Mac Gyver ne peut pas aller par là.")

    def move_up(self):
        return self.move(Position(self.position.x, self.position.y - 1))

    def move_down(self):
        return self.move(Position(self.position.x, self.position.y + 1))

    def move_left(self):
        return self.move(Position(self.position.x - 1, self.position.y))
    
    def move_right(self):
        return self.move(Position(self.position.x + 1, self.position.y))


class Enemy:
    #Enemy et Hero pouraient avoir une classe parent (la classe Person)

    # def __init__()

    # Attributes :
    # position (main attribute)
    pass
