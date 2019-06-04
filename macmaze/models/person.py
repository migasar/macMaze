"""
Manage the personas
"""

from models.position import Position
from config import constants


class Person:

    def __init__(self, board):
        self.board = board
        self.position = None
        self.homing(self.aim, self.char)


    def homing(self, aim, char):
        """Initialize the starting position of the person"""

        home = self.board.get_square('landing', aim)
        home.toping = char
        self.position = Position(home.x_square, home.y_square)
        return self.position


class Hero(Person):

    aim = 'start'
    char = constants.HERO_CHAR

    # a list containing the items collected by the hero
    toolbox = []
    # a boolean inidcating if the hero has reached the end of the maze
    terminus = False


    # Methods for every move of the hero on the board

    def move(self, next_step):
        """Method to initiate every move of the hero"""
        
        back_step = Position(self.position.x_pos, self.position.y_pos)
        motion = True

        # check that the new position is still inside the board
        if self.board.inside(next_step) == False:
            motion = False
        
        else:
            blockade = self.board.get_coordinates(
                'x_square', 'y_square', next_step.x_pos, next_step.y_pos
                )

            # manage potential collision with other elements on the next square
            if self.check_path(blockade) is False:
                motion = False
            
            else:
                # clean the square of the previous position
                back = self.board.get_coordinates('x_square', 'y_square', back_step.x_pos, back_step.y_pos)
                back.toping = ''

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


    # Methods to solve the collisions
   
    def check_path(self, square):
        """Check the attributes of the square on the next position"""
        """nitiate the methods in case of collisions"""

        pathway = False

        if square.free is True:
            # check that the new position is not a wall
            square.toping = constants.HERO_CHAR
            pathway = True

        elif square.landing == 'start':
            # check if the hero came back to starting square
            square.toping = constants.HERO_CHAR
            pathway = True

        elif square.toping != '':
            # check if there is already something on the next position
            self.colliding(square)
            pathway = True
        
        return pathway
 
    def colliding(self, square):
        # determine the type of collision and the method to solve it

        if square.toping == constants.GUARD_CHAR:
            self.showdown(square)
        else:
            self.toolup(square)

    def toolup(self, square):
        # manage collision between the hero and the equipment

        if square.toping == constants.ITEM_1_CHAR:
            self.toolbox.append(1)  # ether
        elif square.toping == constants.ITEM_2_CHAR:
            self.toolbox.append(2)  # needle
        elif square.toping == constants.ITEM_3_CHAR:
            self.toolbox.append(3)  # tube

        square.toping = constants.HERO_CHAR 

    def showdown(self, square):
        # manage collision between the hero and the guard

        self.terminus = True
        if len(self.toolbox) == 3:
            # WIN
            square.toping = constants.HERO_CHAR
            # else: 
                # LOSE --> phantom walk
                # FIXME: phantom walk defeat
                #   - I should find a way to clarify how the game understand that the hero has lost in front of the guard


class Guard(Person):

    aim = 'goal'
    char = constants.GUARD_CHAR
