"""Manage the characters"""


from position import Position
from board import Board

import settings as constants


class Person:

    def __init__(self, board):
        self.board = board
        self.position = None
        self.homing(self.aim, self.char)


    def homing(self, aim, char):
        # initialize the starting position of the person
        home = self.board.get_case("landing", aim)
        home.toping = char
        self.position = Position(home.x, home.y)
        return self.position


class Hero(Person):

    aim = "start"
    char = constants.HERO_CHAR

    # a list containing the items collected by the hero
    toolbox = []

    # a boolean inidcating if the hero has reached the end of the maze
    terminus = False


    def move(self, next_step):
        # root method to initiate every move of the hero on the board
        # 4 moves (up, down, left, right), depending of the value of next_step

        back_step = Position(self.position.x, self.position.y)

        # check that the new position is still inside the board
        if self.board.inside(next_step) == False:
            print("Mac Gyver ne peut pas aller par là.")
        
        else:
            blockade = self.board.get_coordinates("x", "y", next_step.x, next_step.y)

            # manage potential collision with other elements on the next case
            if self.check_path(blockade) is False:
                print("Mac Gyver ne peut pas aller par là.")
            
            else:
                # clean the case of the previous position
                back = self.board.get_coordinates("x", "y", back_step.x, back_step.y)
                back.toping = ""

                # change the position of the hero
                self.position = next_step
                return self.position

    def move_up(self):
        return self.move(Position(self.position.x, self.position.y - 1))

    def move_down(self):
        return self.move(Position(self.position.x, self.position.y + 1))

    def move_left(self):
        return self.move(Position(self.position.x - 1, self.position.y))

    def move_right(self):
        return self.move(Position(self.position.x + 1, self.position.y))

    
    def check_path(self, case):
        # check the attributes of the case on the next position
        # initiate the methods in case of collisions

        motion = False

        if case.free is True:
            # check that the new position is not a wall
            case.toping = constants.HERO_CHAR
            motion = True

        elif case.landing == "start":
            # check if the hero came back to starting case
            case.toping = constants.HERO_CHAR
            motion = True

        elif case.toping != "":
            # check if there is already something on the next position
            self.colliding(case)
            motion = True
        
        return motion
 

    def colliding(self, case):
        # determine the type of collision and the method to solve it

        if case.toping == constants.ENEMY_CHAR:
            self.showdown(case)
        else:
            self.loading(case)

    def loading(self, case):
        # manage collision between the hero and the equipment

        if case.toping == constants.ITEM_1_CHAR:
            # ether
            self.toolbox.append(1)
        elif case.toping == constants.ITEM_2_CHAR:
            # needle
            self.toolbox.append(2)
        elif case.toping == constants.ITEM_3_CHAR:
            # tube
            self.toolbox.append(3)

        case.toping = constants.HERO_CHAR 

    def showdown(self, case):
        # manage collision between the hero and the guardian

        self.terminus = True
        if len(self.toolbox) == 3:
            # WIN
            case.toping = constants.HERO_CHAR
            # else: 
                # LOSE --> phantom walk
                # FIXME: phantom walk defeat
                #   - I should find a way to clarify how the game understand that the hero has lost in front of the guardian


class Enemy(Person):

    aim = "goal"
    char = constants.ENEMY_CHAR
