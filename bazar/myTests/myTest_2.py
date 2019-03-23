#########
# IMPORTS
#########

"""
# import the pygame module
import pygame
# import pygame.locals for easier access to key coordinates
from pygame.locals import *
"""

import config.settings as constants
#from .position import Position


#########
# CLASSES
#########


# gere les déplacements des objets
class Position:

    def __init__(self, x, y):
        self.position = (x, y)

    def __repr__(self):
        return str(self.position)

    def __hash__(self):
        return hash(self.position)

    def __eq__(self, pos):
        return self.position == pos.position

    def up(self):
        x, y = self.position
        return Position(x, y-1)

    def down(self):
        x, y = self.position
        return Position(x, y+1)

    def right(self):
        x, y = self.position
        return Position(x+1, y)

    def left(self):
        x, y = self.position
        return Position(x-1, y)


# gere la map des objets
class Board:

    def __init__(self, filename):
        self.filename = filename

        self._paths = set()
        self._start = set()
        self._goal = set()
        self._walls = set()

        self.load_from_file()

    @property
    def start(self):
        return list(self._start)[0]

    def __contains__(self, position):
        return position in self._paths

    def load_from_file():
            with open(self.filename) as infile:
                for y, line in enumerate(infile):
                    for x, col in enumerate(line):
                        if col == constants.PATH_CHAR:
                            self._paths.add(Position(x, y))
                        elif col == constants.START_CHAR:
                            self._start.add(Position(x, y))
                            self._paths.add(Position(x, y))
                        elif col == constants.GOAL_CHAR:
                            self._goal.add(Position(x, y))
                            self._paths.add(Position(x, y))
                        else :
                            self._walls.add(Position(x, y))


# gere le personnage
class Hero:

    def __init__(self, board):
        self.board = board
        self.position = self.board.start

    def move(self, direction):
        """docstring."""
        # getattr can access an object property using a string
        new_position = getattr(self.position, direction)()
        if new_position in self.map:
            self.position = new_position




"""
############
# GAME START
############

# initialize pygame
pygame.init()

# create the screen object
# here we pass it a size of 800x600
screen = pygame.display.set_mode((600, 600))

# instantiate our player; right now he's just a rectangle
hero = Hero()

print(hero.position.__repr__)

###########
# MAIN LOOP
###########

# Variable to keep our main loop running
running = True

# Our main loop!
while running:
    # for loop through the event queue
    for event in pygame.event.get():
        # Check for KEYDOWN event; KEYDOWN is a constant defined in pygame.locals, which we imported earlier
        if event.type == KEYDOWN:
            # If the Esc key has been pressed set running to false to exit the main loop
            if event.key == K_ESCAPE:
                running = False
        # Check for QUIT event; if QUIT, set running to false
        elif event.type == QUIT:
            running = False

    # Draw the player to the screen
    screen.blit(hero.image, (0, 0))
    # Update the display
    pygame.display.flip()

"""



#def main():
board = Board(constants.board_blueprint)
hero = Hero(board)
print(hero.position)



"""
if __name__ == "__main__":
    main()
"""
