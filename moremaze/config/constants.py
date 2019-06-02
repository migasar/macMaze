"""Settings of the game"""


import os

"""
import pygame
from pygame.compat import geterror

# Contains all game constants, parameters and main functions of the program

pygame.init()

def load_image(name, conv=True, colorkey=None):
    '''Functions to create  visual resources'''
    fullname = os.path.join('moremaze', 'data', 'images', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error:
        print('Cannot load image:', fullname)
        raise SystemExit(str(geterror()))
    if conv == True:
        image = image.convert_alpha()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    return image
"""


def reach_image(name):
    fullpath = os.path.join('moremaze', 'data', 'images', name)
    return fullpath

def reach_board(name):
    fullpath = os.path.join('moremaze', 'data', 'boards', name)
    return fullpath


# Representation of game elements

START_CHAR = 'S'
GOAL_CHAR = 'G'
PATH_CHAR = '.'
WALL_CHAR = '#'
HERO_CHAR = '@'
ENEMY_CHAR = 'X'
ITEM_1_CHAR = '1'
ITEM_2_CHAR = '2'
ITEM_3_CHAR = '3'


# Size elements

TILE_NUMBER = 15
TILE_SIZE = 40
PLAYTURF_HEIGHT = TILE_NUMBER * TILE_SIZE
TAILTURF_HEIGHT = 2 * TILE_SIZE
SCREEN_HEIGHT = PLAYTURF_HEIGHT + TAILTURF_HEIGHT
SCREEN_WIDTH = TILE_NUMBER * TILE_SIZE 


# Introduction of the game
GAME_TITLE = 'Mac Maze'
GAME_BID = 'Sauvez MacGyver, Sauvez mon projet'


# Image elements
PATH_IMAGE = 'tile_path.png'
WALL_IMAGE = 'tile_wall.png'
GATE_IMAGE = 'tile_gate.png'
HERO_IMAGE = 'perso_hero.png'
ENEMY_IMAGE = 'perso_enemy.png'
ETHER_IMAGE = 'item_ether.png'
NEEDLE_IMAGE = 'item_needle.png'
TUBE_IMAGE = 'item_tube.png'
SYRINGE_IMAGE = 'item_syringe.png'
WESTWORLD_MAZE = 'westworld_logo.png'


IMAGES_DICT = {
    'S': GATE_IMAGE,
    'G': GATE_IMAGE,
    '#': WALL_IMAGE,
    '.': PATH_IMAGE,
    '@': HERO_IMAGE,
    'X': ENEMY_IMAGE,
    '1': ETHER_IMAGE,
    '2': NEEDLE_IMAGE,
    '3': TUBE_IMAGE
}


BOARDS_LIST = [
    'board_01.txt', 'board_02.txt', 'board_03.txt'
]

BLUEPRINT = reach_board(BOARDS_LIST[0])



"""
BLUEPRINT = '{}/board_01.txt'.format(
    os.path.dirname(__file__)
    )
"""

# TODO: learn path 
#   - to deal with call between files in different diretories of my project
