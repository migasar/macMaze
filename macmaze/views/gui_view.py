"""
Manage the display of every elements of the game
"""

import pygame
from pygame.locals import *

from models.person import Hero
from config import constants


class GUIview:

    def __init__(self, board, hero):
        self.board = board
        self.hero = hero

    
    def draw_board(self, screen):

        for y, line in enumerate(self.board.grid):
            for tile in self.board.grid[y]:

                x = tile.x_square * constants.TILE_SIZE
                y = tile.y_square * constants.TILE_SIZE

                tile_image = constants.reach_image(
                    constants.IMAGES_DICT[tile.visual]
                    )
                tile_surf = pygame.image.load(tile_image).convert()

                screen.blit(tile_surf, (x,y))

                if tile.toping:

                    toping_image = constants.reach_image(
                        constants.IMAGES_DICT[tile.toping]
                        )
                    toping_surf = pygame.image.load(toping_image).convert()

                    screen.blit(toping_surf, (x, y))

    def draw_menu(self, screen):

        #draw the background for the menu
        background_image = constants.reach_image(constants.RIBBON_IMAGE)
        background_surf = pygame.image.load(background_image).convert()
        screen.blit(background_surf, (0, constants.PLAYTURF_HEIGHT))

        for i, item in enumerate(self.hero.toolbox):

            x = constants.SCREEN_WIDTH - (i * constants.TILE_SIZE)
            y = constants.PLAYTURF_HEIGHT

            item_image = constants.reach_image(constants.IMAGES_DICT[str(item)])
            item_surf = pygame.image.load(item_image).convert()

            screen.blit(item_surf, (x, y))
            pygame.display.flip()
