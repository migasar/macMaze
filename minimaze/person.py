"""Gere les personnages"""


from position import Position
from board import Board

import settings as constants


class Person:

    def __init__(self, board):
        self.board = board
        self.position = None
        self.homing(self.aim, self.char)


    def homing(self, aim, char):
    # Initialize the starting position of the person
        home = self.board.get_case("landing", aim)
        home.toping = char
        self.position = Position(home.x, home.y)
        return self.position


class Hero(Person):

    aim = "start"
    char = constants.HERO_CHAR

    # TODO: creer un attribut toolbox pour gerer la récupération des éléments par le héros

    def move(self, next_step):
    # 4 moves (up, down, left, right)
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

    aim = "goal"
    char = constants.ENEMY_CHAR

