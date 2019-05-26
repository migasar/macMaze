"""Manage the characters"""


from models.position import Position
from models.board import Board

from config import settings as constants


class Person:

    def __init__(self, board):
        self.board = board
        self.position = None
        self.homing(self.aim, self.char)

    def homing(self, aim, char):
        # initialize the starting position of the person
        home = self.board.get_case("landing", aim)
        home.toping = char
        self.position = Position(home.x_case, home.y_case)
        return self.position


class Hero(Person):

    aim = "start"
    char = constants.HERO_CHAR

    # a list containing the items collected by the hero
    toolbox = []
    # a boolean inidcating if the hero has reached the end of the maze
    terminus = False


    ## methods for every move of the hero on the board
    ## 4 moves (up, down, left, right), depending of the value of next_step
    ######
    def move(self, next_step):
        # method to initiate every move of the hero 
        
        back_step = Position(self.position.x_pos, self.position.y_pos)
        motion = True

        # check that the new position is still inside the board
        if self.board.inside(next_step) == False:
            motion = False
        
        else:
            blockade = self.board.get_coordinates(
                "x_case", "y_case", next_step.x_pos, next_step.y_pos
                )

            # manage potential collision with other elements on the next case
            if self.check_path(blockade) is False:
                motion = False
            
            else:
                # clean the case of the previous position
                back = self.board.get_coordinates("x_case", "y_case", back_step.x_pos, back_step.y_pos)
                back.toping = ""

                # change the position of the hero
                self.position = next_step
                # FIXME: this modify the position silently
                    # - the new position of the hero comes as a side-effect,
                    # - instead of returning directly the new position,
                    # - it might confuse someone reading or modifying this code

        return motion

    def move_up(self):
        return self.move(Position(self.position.x_pos, self.position.y_pos - 1))

    def move_down(self):
        return self.move(Position(self.position.x_pos, self.position.y_pos + 1))

    def move_left(self):
        return self.move(Position(self.position.x_pos - 1, self.position.y_pos))

    def move_right(self):
        return self.move(Position(self.position.x_pos + 1, self.position.y_pos))
    ######


    ## methods to solve the collisions
    ## between the hero and of other elements standing on a case 
    ######
    def check_path(self, case):
        # check the attributes of the case on the next position
        # initiate the methods in case of collisions

        pathway = False

        if case.free is True:
            # check that the new position is not a wall
            case.toping = constants.HERO_CHAR
            pathway = True

        elif case.landing == "start":
            # check if the hero came back to starting case
            case.toping = constants.HERO_CHAR
            pathway = True

        elif case.toping != "":
            # check if there is already something on the next position
            self.colliding(case)
            pathway = True
        
        return pathway
 
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
    ######


class Enemy(Person):

    aim = "goal"
    char = constants.ENEMY_CHAR
