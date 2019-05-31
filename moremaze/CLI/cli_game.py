"""Manage the flow of the game"""


from CLI.board import Board
from CLI.person import Hero, Enemy
from CLI.equipment import Ether, Needle, Tube
from CLI.position import Position

from CLI.cli_view import CLIview
from CLI.cli_event import CLIevent

import config.constants as constants


import pygame 
from pygame.locals import *


class Game:

    def __init__(self):

        self.board = Board.load_blueprint(constants.BLUEPRINT)
        # TODO: randomize blueprint
            #   - create a method to randomize the choice of the file used as a blueprint
            #   - it will be a way to generate different mazes
            #   - this method could also be in the class Board

        self.hero = Hero(self.board)
        self.enemy = Enemy(self.board)
        
        self.ether = Ether(self.board)
        self.needle = Needle(self.board)
        self.tube = Tube(self.board)

        """
        self.view = CLIview(self.board)
        self.event = CLIevent(self.board, self.hero, self.view)
        """
        self.view = GUIview(self.board)

    def start(self):
        self.event.starter()


def main():

    game = Game()
    #game.start()


    ######
    ## pygame LOOP

    pygame.init()

    #Ouverture de la fenêtre pygame
    screen = pygame.display.set_mode((600, 640)) 

    #Titre
    pygame.display.set_caption('MacMaze')

    """
    #Icone
    icon = pygame.image.load(constants.WESTWORLD_MAZE)
    pygame.display.set_icon(icon)
    """
    # FIXME: the image for the icon can't be loaded


    game.view.draw_board(screen)
    pygame.display.flip()


    ######
    # MAIN LOOP

    running = True
    while running:

		#Limitation de vitesse de la boucle
        pygame.time.Clock().tick(30)

        # for loop through the event queue
        for event in pygame.event.get():

            # Check for QUIT event; if QUIT, set running to false
            if event.type == QUIT:
                running = False

            # Check for KEYDOWN event; KEYDOWN is a constant defined in pygame.locals, which we imported earlier
            
            elif event.type == KEYDOWN:

                # If the Esc key has been pressed set running to false to exit the main loop
                if event.key == K_ESCAPE:
                    running = False

            	#Touches de déplacement de Donkey Kong
                elif event.key == K_RIGHT:
                    game.hero.move_right()
                    print(game.hero.position)
                elif event.key == K_LEFT:
                    game.hero.move_left()
                elif event.key == K_UP:
                    game.hero.move_up()
                elif event.key == K_DOWN:
                    game.hero.move_down()	
                # FIXME: hero changes of position internally,
                #    but his image doesn't move on the screen
    
        game.view.draw_board(screen)
        pygame.display.flip()

    ######
    ######
    

if __name__ == "__main__":
    main()

