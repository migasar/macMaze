#########
# IMPORTS
#########
"""
# import the pygame module
import pygame

# import pygame.locals for easier access to key coordinates
from pygame.locals import *
"""
# from config.settings import *
import config.settings as constants

#from .position import Position


#########
# CLASSES
#########

class Position:
    def __init__(self, x, y):
        self.position = (x, y)

    # methods to add this class to make it usable by the other classes
    # to complete the game
    def __repr__(self):
        # ???
        return str(self.position)

    def __hash___(self):
        # ???
        return hash(self.position)

    def __eq__(self, pos):
        # without this method, we can't compare 2 instances of position
        # this define that 2 positions are considered equals,
        # if their tuples are equal
        return self.position == pos.position

    def up(self):
        x, y = self.position
        return Position(x, y - 1)

    def down(self):
        x, y = self.position
        return Position(x, y + 1)

    def right(self):
        x, y = self.position
        return Position(x + 1, y)

    def left(self):
        x, y = self.position
        return Position(x - 1, y)


class Board:
    def __init__(self, blueprint):
        self.blueprint = constants.board_blueprint
        # exemple : blueprint is 'data/board-01.txt'
        # --> board = Board('data/board-01.txt')

        # pourquoi des sets?
        # listing des chemins praticables
        self.path = set()

        # l'attribut wall n'est pas forcément nécessaire
        # selon le mécanisme de mon programme
        self.wall = set()

        self.start = set()
        self.goal = set()

        self.load_from_file()

    def is_path_position(self, position):
        # check if a position is valid
        return position in self.path

    def load_from_file():
        with open(self.blueprint, "r") as infile:
            # ma 1ere boucle for va iterer sur mon fichier ligne par ligne
            # (ma ligne est x ou y dans mon cas?), (x or line)
            for line in enumerate(infile):
                # ma boucle va iterer sur chaque ligne colonne par colonne
                # (y or col)
                for col in enumerate(line):
                    if col == constants.PATH_CHAR:
                        self.path.add(Position(x, y))
                    elif col == constants.START_CHAR:
                        self.start.add(Position(x, y))
                        self.path.add(Position(x, y))
                    elif col == constants.GOAL_CHAR:
                        self.goal.add(Position(x, y))
                        self.path.add(Position(x, y))
                    else:
                        # This is a wall
                        pass


# Define our player object and call super to give it all the properties and methods of pygame.sprite.Sprite
# The surface we draw on the screen is now a property of 'player'

"""
class Hero(pygame.sprite.Sprite):
    def __init__(self):
        super(Hero, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()
"""

"""
class Hero(pygame.sprite.Sprite):
    def __init__(self):
        super(Hero, self).__init__()
        self.image = pygame.image.load(constants.image_hero).convert_alpha()
        #self.image.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.image.get_rect()
"""

class Hero:
    def __init__(self, position):
        self.position = position
        #self.image = pygame.image.load(constants.image_hero).convert_alpha()
        #self.rect = self.image.get_rect()

    def get_up(self):
        return self.position.up()

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

hero = Hero((0, 0))

print(hero.position)
hero.position = hero.position.up()
print(hero.position)

"""
here = Position(1, 1)
print(here)
here = here.up()
print(here)
"""