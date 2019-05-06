"""Gere les personnages"""


from position import Position
from board import Board

import settings as constants


# TODO: rework the class Hero 
#   - introduce a superclass Person
#   - takes in charge the method homing() for the subclass Hero and Enemy


class Person:
    def __init__(self, board):
        self.board = board
        self.position = None

        self.homing(self.aim, self.char)

    # Initialize the starting position of the person
    def homing(self, aim, char):
        home = self.board.get_case("landing", aim)
        home.toping = char
        self.position = Position(home.x, home.y)
        return self.position


class Hero(Person):

    aim = "start"
    char = constants.HERO_CHAR

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


class Enemy(Person):
    #Enemy et Hero pouraient avoir une classe parent (la classe Person)

    aim = "goal"
    char = constants.ENEMY_CHAR

