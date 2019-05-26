"""
"""

import sys
# FIXME: module sys (not sure it is needed)

import pygame
from pygame.locals import *
"""
from pygame import display
from pygame import Surface
from pygame import image
from pygame import Rect
from pygame import event
"""

from models.board import Board
from config import settings as constants


pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('MacMaze : save McGyver, save my project')

while True: # main game loop

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

            sys.exit()
            # FIXME: module sys (not sure it is needed)

    pygame.display.update()

