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
    
    def draw_board(self, screen):

        for y, line in enumerate(self.board.grid):

            for tile in self.board.grid[y]:
                x = tile.x_square * constants.TILE_SIZE
                y = tile.y_square * constants.TILE_SIZE

                tile_image = constants.TILEMAPPING[tile.visual]
                tile_surf = pygame.image.load(tile_image).convert()
                screen.blit(tile_surf, (x,y))

                if tile.toping:
                    toping_image = constants.ITEMSMAPPING[tile.toping]
                    toping_surf = pygame.image.load(toping_image).convert()
                    screen.blit(toping_surf, (x, y))

