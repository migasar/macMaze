# import the pygame module
import pygame

# import random for random numbers!
# import random

# import pygame.locals for easier access to key coordinates
from pygame.locals import *
####

# Classes

# initialize pygame
pygame.init()
####

# create the screen object
# here we pass it a size of 800x600
screen = pygame.display.set_mode((800, 600))
####

my_image = pygame.image.load("resources\aiguille.png").convert()

surf = pygame.Surface((800, 600))
surf.blit( my_image, (0, 0), (10, 10, 10, 10) )

####
####


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

