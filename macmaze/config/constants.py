"""
Settings of the game
Contains all the game constants and the parameters of the program
"""

import os


def reach_image(name):
    """Method to create the path to load an image"""

    fullpath = os.path.join('macmaze', 'data', 'images', name)
    return fullpath

def reach_board(name):
    """Method to create the path to load the scheme of the board"""

    fullpath = os.path.join('macmaze', 'data', 'boards', name)
    return fullpath


# representation of game elements
START_CHAR = 'S'
GOAL_CHAR = 'G'
PATH_CHAR = '.'
WALL_CHAR = '#'
HERO_CHAR = '@'
GUARD_CHAR = 'X'
ITEM_1_CHAR = '1'
ITEM_2_CHAR = '2'
ITEM_3_CHAR = '3'


# size elements
TILE_NUMBER = 15
TILE_SIZE = 40
PLAYTURF_HEIGHT = TILE_NUMBER * TILE_SIZE
TAILTURF_HEIGHT = 2 * TILE_SIZE
SCREEN_HEIGHT = PLAYTURF_HEIGHT + TAILTURF_HEIGHT
SCREEN_WIDTH = TILE_NUMBER * TILE_SIZE 


# introduction of the game
GAME_TITLE = 'Mac Maze'
GAME_BID = 'Sauvez MacGyver, Sauvez mon projet'


# image elements
PATH_IMAGE = 'tile_path.png'
WALL_IMAGE = 'tile_wall.png'
GATE_IMAGE = 'tile_gate.png'
HERO_IMAGE = 'perso_hero.png'
GUARD_IMAGE = 'perso_guard.png'
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
    'X': GUARD_IMAGE,
    '1': ETHER_IMAGE,
    '2': NEEDLE_IMAGE,
    '3': TUBE_IMAGE
}


# board elements
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
