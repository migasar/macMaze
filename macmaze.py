#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""
Jeu Labyrinthe de MacGyver
Version simpliste du jeu (sans les objets à collecter), 
où on doit déplacer MacGyver jusqu'au gardien

"""

#Importation des bibliothèques nécessaires
import pygame
from pygame.locals import *

from classes import *
from settings import *


#Initialisation de la bibliothèque Pygame
pygame.init()


#Ouverture de la fenêtre Pygame (zone)
zone = pygame.display.set_mode((int, int), RESIZABLE)

#Chargement et collage du fond (background)
background = pygame.image.load("filenamebackground.jpg").convert()
zone.blit(background, (int,int))

#Rafraîchissement de l'écran
pygame.display.flip()

#Variable qui continue la boucle si = 1, stoppe si = 0
keep_on = 1
#Boucle infinie
while keep_on:
    keep_on = int(input()) #Je place continue ici pour pouvoir relancer la boucle infinie
                 #mais il est d'habitude remplacé par une suite d'instructions


def main():
    #gère le déroulement du jeu
    #affiche la zone de jeu
    pass

if __name__ == "__main__":
    main()
