"""
Manage the display of every elements of the game
"""

import pygame

from config import constants


class GUIview:

    def __init__(self, board, hero):
        self.board = board
        self.hero = hero

    ######
    # methods to display screens of the game
    def draw_board(self, screen):
        """draw the board of the game and the elements to play a party"""

        for y, line in enumerate(self.board.grid):
            for tile in self.board.grid[y]:

                x = tile.x_square * constants.TILE_SIZE
                y = tile.y_square * constants.TILE_SIZE

                tile_image = constants.reach_image(
                    constants.IMAGES_DICT[tile.visual]
                    )
                tile_surf = pygame.image.load(tile_image).convert()

                screen.blit(tile_surf, (x, y))

                if tile.toping:

                    toping_image = constants.reach_image(
                        constants.IMAGES_DICT[tile.toping]
                        )
                    toping_surf = pygame.image.load(toping_image).convert()

                    screen.blit(toping_surf, (x, y))

    def draw_menu(self, screen):
        """draw the menubar at the bottom of the window"""

        # draw the background for the menubar
        background_image = constants.reach_image(constants.RIBBON_IMAGE)
        background_surf = pygame.image.load(background_image).convert()
        screen.blit(background_surf, (0, constants.PLAYTURF_HEIGHT))

        if len(self.hero.toolbox) == 3:
            # draw the syringe on the menubar
            # when all items have been collected

            x = constants.SCREEN_WIDTH - constants.TILE_SIZE
            y = constants.PLAYTURF_HEIGHT
            item_image = constants.reach_image(constants.SYRINGE_IMAGE)
            item_surf = pygame.image.load(item_image).convert()

            screen.blit(item_surf, (x, y))
            pygame.display.flip()

        else:
            for i, item in enumerate(self.hero.toolbox):
                # draw the items that have been colected on the menubar

                x = constants.SCREEN_WIDTH - ((i + 1) * constants.TILE_SIZE)
                y = constants.PLAYTURF_HEIGHT
                item_image = constants.reach_image(
                    constants.IMAGES_DICT[str(item)]
                    )
                item_surf = pygame.image.load(item_image).convert()

                screen.blit(item_surf, (x, y))
                pygame.display.flip()

    ######
    # methods to display visuals in the game
    def draw_outcome(self, screen):
        """draw visuals in the menubar to indicate the issue of the game"""

        # check if the game has reached its end
        if self.hero.terminus is True:
            x = 0
            y = constants.PLAYTURF_HEIGHT

            font = pygame.font.Font(None, 48)

            if len(self.hero.toolbox) == 3:
                item_image = constants.reach_image(constants.STAIRS_IMAGE)
                text = font.render("MacGyver s'est échappé", 1, (10, 10, 10))
            else:
                item_image = constants.reach_image(constants.RIP_IMAGE)
                text = font.render("MacGyver a échoué", 1, (10, 10, 10))

            item_surf = pygame.image.load(item_image).convert()

            screen.blit(item_surf, (x, y))
            screen.blit(text, (2 * constants.TILE_SIZE, y))
            pygame.display.flip()
