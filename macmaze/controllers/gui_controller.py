"""
Manage the flow of the game
and the interactions between the components of the project
"""

import pygame
from pygame.locals import *

from models.board import Board
from models.person import Hero, Guard
from models.equipment import Ether, Needle, Tube
from views.gui_view import GUIview
from config import constants


class GUIcontroller:

    def __init__(self, board, hero, view):
        self.board = board
        self.hero = hero
        self.view = view

        self.window_maker()

    def window_maker(self):
        """Initialize the main object for Pygame"""

        # Pygame initialization
        pygame.init()

        # Pygame window setup
        self.screen = pygame.display.set_mode(
            (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
            )
        pygame.display.set_caption('MacMaze')

        self.view.draw_board(self.screen)
        self.view.draw_menu(self.screen)

        # variable to maintain the loop as long as it is True
        self.running = True

        pygame.display.update()

    def start(self):
        """Manage the Pygame loop"""

        # Pygame main loop
        while self.running:

            # limit the speed of the loop
            pygame.time.Clock().tick(30)

            # for loop through the event queue
            for event in pygame.event.get():

                # check for QUIT event; if QUIT, set running to false
                # QUIT is a constant defined in pygame.locals
                if event.type == QUIT:
                    self.running = False

                # check for KEYDOWN event;
                # KEYDOWN is a constant defined in pygame.locals
                elif event.type == KEYDOWN:

                    # if the Esc key has been pressed
                    # set running to false to exit the main loop
                    if event.key == K_ESCAPE:
                        self.running = False

                    # keys for the movement of the hero
                    elif event.key == K_RIGHT:
                        next_step = self.hero.move_right()
                        if self.check_move(next_step) is True:
                            self.hero.move(next_step)
                    elif event.key == K_LEFT:
                        next_step = self.hero.move_left()
                        if self.check_move(next_step) is True:
                            self.hero.move(next_step)
                    elif event.key == K_UP:
                        next_step = self.hero.move_up()
                        if self.check_move(next_step) is True:
                            self.hero.move(next_step)
                    elif event.key == K_DOWN:
                        next_step = self.hero.move_down()
                        if self.check_move(next_step) is True:
                            self.hero.move(next_step)

            self.view.draw_board(self.screen)
            self.view.draw_menu(self.screen)
            self.view.draw_outcome(self.screen)
            pygame.display.update()

    ######
    # methods to solve the collisions
    def check_move(self, next_step):
        """Method to verify if the next move is possible"""

        # check if the game should have ended
        if self.hero.terminus is True:
            self.running = False

        motion = True

        # check that the new position is still inside the board
        if self.board.inside(next_step) is False:
            motion = False
        else:
            blockade = self.board.get_coordinates(
                'x_square', 'y_square', next_step.x_pos, next_step.y_pos
                )

            # manage potential collision with other elements on the next square
            if self.check_path(blockade) is False:
                motion = False

        return motion

    def check_path(self, block):
        """
        Check the attributes of the square on the next position,
        and initiate the methods in case of collisions
        """

        pathway = False

        if block.free is True:
            # check that the new position is not a wall
            block.toping = constants.HERO_CHAR
            pathway = True

        elif block.landing == 'start':
            # check if the hero came back to starting square
            block.toping = constants.HERO_CHAR
            pathway = True

        elif block.toping != '':
            # check if there is already something on the next position
            self.colliding(block)
            pathway = True

        return pathway

    def colliding(self, block):
        """Determine the type of collision and the method to solve it"""

        if block.toping == constants.GUARD_CHAR:
            self.showdown(block)
        else:
            self.toolup(block)

    def toolup(self, block):
        """
        Put an item in the inventory of the hero,
        when he gets in collision with it
        """

        if block.toping == constants.ITEM_1_CHAR:
            self.hero.toolbox.append(1)  # ether
        elif block.toping == constants.ITEM_2_CHAR:
            self.hero.toolbox.append(2)  # needle
        elif block.toping == constants.ITEM_3_CHAR:
            self.hero.toolbox.append(3)  # tube

        block.toping = constants.HERO_CHAR

    def showdown(self, block):
        """Decide of the issue when the hero and the guard collide"""

        self.hero.terminus = True

        if len(self.hero.toolbox) == 3:
            # WIN
            block.toping = constants.HERO_CHAR
            # else:
            # LOSE --> phantom walk
            # FIXME: phantom walk defeat
            # I should find a way to clarify how the game understand
            # that the hero has lost in front of the guard

    ######
    # method to know how the game ends
    def game_over(self):
        """Check if the hero has won the game"""

        end = self.board.get_square('landing', 'goal')
        return end.toping == constants.HERO_CHAR


class GUIgame:

    def __init__(self):
        self.board = Board.load_blueprint(pick=False)

        self.hero = Hero(self.board)
        self.guard = Guard(self.board)
        self.ether = Ether(self.board)
        self.needle = Needle(self.board)
        self.tube = Tube(self.board)

        self.view = GUIview(self.board, self.hero)
        self.controller = GUIcontroller(self.board, self.hero, self.view)
