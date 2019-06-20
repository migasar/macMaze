"""
Manage the personas
"""

from macmaze.models.position import Position
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

    ######
    # methods for every move of the hero on the board
    def move(self, next_step):
        """Method to initiate every move of the hero"""

        # clean the square of the previous position
        back_step = Position(self.position.x_pos, self.position.y_pos)
        back = self.board.get_coordinates(
            'x_square', 'y_square', back_step.x_pos, back_step.y_pos
            )
        back.toping = ''

        # change the position of the hero
        self.position = next_step

        return self.position

    def move_up(self):
        return Position(self.position.x_pos, self.position.y_pos - 1)

    def move_down(self):
        return Position(self.position.x_pos, self.position.y_pos + 1)

    def move_left(self):
        return Position(self.position.x_pos - 1, self.position.y_pos)

    def move_right(self):
        return Position(self.position.x_pos + 1, self.position.y_pos)


class Guard(Person):

    aim = 'goal'
    char = constants.GUARD_CHAR
