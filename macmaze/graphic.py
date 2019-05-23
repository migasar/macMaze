"""Manage the display of every elements of the game"""


import pygame
from pygame.locals import *
# from pygame import display
# from pygame import Surface
# from pygame import image
# from pygame import Rect
# from pygame import event

from models.board import Board

from config import settings as constants



# TODO: Pygame GUI
#   - create another class View based on pygame for a version with a GUI


class GUIview:

    def __init__(self, board):
        self.board = board



def main():

    pygame.init()

    #Ouverture de la fenêtre Pygame
    screen = pygame.display.set_mode((600, 680)) 

    play_turf = pygame.Surface((600, 600))

    tail_turf = pygame.Surface((600, 80))
    tail_turf.fill((225, 225, 225))

    #Chargement et collage du fond
    #background = pygame.image.load("background.jpg").convert()
    #screen.blit(fond, (0,0))

    # not used
    square = pygame.Surface((40, 40))


    path = pygame.image.load(constants.image_path).convert()
    # path_rect = path.get_rect()
    wall = pygame.image.load(constants.image_wall).convert()
    # wall_rect = wall.get_rect()
    way = pygame.image.load(constants.image_way).convert()
    # way_rect = way.get_rect()


    hero = pygame.image.load(constants.image_hero).convert()
    # hero_rect = hero.get_rect()
    guardian = pygame.image.load(constants.image_guardian).convert()
    # guardian_rect = guardian.get_rect()

    ether = pygame.image.load(constants.image_ether).convert()
    # ether_rect = ether.get_rect()
    needle = pygame.image.load(constants.image_needle).convert()
    # needle_rect = needle.get_rect()
    tube = pygame.image.load(constants.image_tube).convert_alpha() 
    # tube_rect = tube.get_rect()

    syringe = pygame.image.load(constants.image_syringe).convert_alpha() 
    # syringe_rect = syringe.get_rect()


    screen.blit(play_turf, (0, 0))
    screen.blit(tail_turf, (0, 600))

    """
    play_turf.blit(path, (40, 40))
    play_turf.blit(wall, (80, 40))
    play_turf.blit(way, (120, 40))

    play_turf.blit(hero, (40, 120))
    play_turf.blit(guardian, (120, 120))

    play_turf.blit(ether, (40, 200))
    play_turf.blit(needle, (80, 200))
    play_turf.blit(tube, (120, 200))

    play_turf.blit(syringe, (80, 280))
    """

    screen.blit(path, (40, 0))
    screen.blit(wall, (0, 40))
    screen.blit(way, (0, 0))

    screen.blit(hero, (40, 120))
    screen.blit(hero, (0, 0))
    screen.blit(guardian, (120, 120))

    screen.blit(ether, (40, 200))
    screen.blit(needle, (80, 200))
    screen.blit(tube, (120, 200))

    screen.blit(syringe, (80, 280))

    #Rafraîchissement de l'écran
    pygame.display.flip()


    #INFINTE LOOP
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
    

#pygame.event.get()


if __name__ == "__main__":
    main()



