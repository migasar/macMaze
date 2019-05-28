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
    
    def display_board(self, screen):

        for y, line in enumerate(self.board.grid):

            for tile in self.board.grid[y]:
                x = tile.x_case * constants.TILE_SIZE
                y = tile.y_case * constants.TILE_SIZE

                tile_image = constants.TILES_MAPPING[tile.visual]
                screen.blit(tile_image, (x,y))
