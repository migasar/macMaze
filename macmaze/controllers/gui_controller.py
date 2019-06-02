# -*- coding: utf-8 -*-
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



class GUIcontroller:

    def __init__(self, board, hero, view):
        self.board = board
        self.hero = hero
        self.view = view
    
    def start(self):

        # Pygame initialization
        pygame.init()

        # Pygame window setup
        screen = pygame.display.set_mode((600, 640)) 

        pygame.display.set_caption('MacMaze')

        """
        #Icone
        icon = pygame.image.load(constants.WESTWORLD_MAZE)
        pygame.display.set_icon(icon)
        """
        # FIXME: the image for the icon can't be loaded

        self.view.draw_board(screen)
        pygame.display.flip()


        # Pygame main loop
        running = True

        while running:

            # limit the speed of the loop
            pygame.time.Clock().tick(30)

            # for loop through the event queue
            for event in pygame.event.get():

                # check for QUIT event; if QUIT, set running to false
                if event.type == QUIT:
                    running = False

                # check for KEYDOWN event; 
                # KEYDOWN is a constant defined in pygame.locals
                
                elif event.type == KEYDOWN:

                    # if the Esc key has been pressed set running to false to exit the main loop
                    if event.key == K_ESCAPE:
                        running = False

                    # keys for the movement of the hero
                    elif event.key == K_RIGHT:
                        self.hero.move_right()
                    elif event.key == K_LEFT:
                        self.hero.move_left()
                    elif event.key == K_UP:
                        self.hero.move_up()
                    elif event.key == K_DOWN:
                        self.hero.move_down()	
                    # FIXME: hero changes of position internally,
                    #    but his image doesn't move on the screen
        
            self.view.draw_board(screen)
            pygame.display.flip()


class Game:

    def __init__(self):

        self.board = Board.load_blueprint(pick=False)

        self.hero = Hero(self.board)
        self.guard = Guard(self.board)
        
        self.ether = Ether(self.board)
        self.needle = Needle(self.board)
        self.tube = Tube(self.board)

        self.view = GUIview(self.board)
        self.controller = GUIcontroller(self.board, self.hero, self.view)


"""
def main():

    game = Game()
    game.controller.start()

if __name__ == "__main__":
    main()

"""
