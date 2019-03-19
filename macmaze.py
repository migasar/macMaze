#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""
Jeu Labyrinthe de MacGyver
Version simpliste du jeu (sans les objets à collecter), 
où on doit déplacer MacGyver jusqu'au gardien

"""

# Importation des bibliothèques nécessaires
import pygame
from pygame.locals import *

from classes import *
import settings as constants

# Initialisation de la bibliothèque Pygame
pygame.init()

# Ouverture de la fenêtre Pygame (screen)
screen = pygame.display.set_mode((800, 800), RESIZABLE)

"""
# Chargement et collage du fond (background)
background = pygame.image.load("filenamebackground.jpg").convert()
screen.blit(background, (int,int))

# Rafraîchissement de l'écran
pygame.display.flip()
"""

# Variable qui continue la boucle si = True, stop si = False  
running = True

# Boucle principale (infinie)
while running:
    # for loop through the event queue
    for event in pygame.event.get():
        # check for KEYDOWN event;
        #KEYDOWN is a constant defined in pygame.locals
        if event.type == KEYDOWN:
            # if the ESC key is pressed, 
            # it sets running to False to exit the main loop
            if event.key == K_ESCAPE:
                running = False
        # check for QUIT event; 
        # if QUIT, set running to false
        elif event.type == QUIT:
            running = False

    """
    running = int(input()) # Je place continue ici pour pouvoir relancer la boucle infinie
                 # mais il est d'habitude remplacé par une suite d'instructions
    """             

"""
def main():
    # gère le déroulement du jeu
    # affiche la zone de jeu
    pass

if __name__ == "__main__":
    main()
"""