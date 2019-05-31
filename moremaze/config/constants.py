"""Settings of the game"""

import os


START_CHAR = 'S'
GOAL_CHAR = 'G'
PATH_CHAR = '.'
WALL_CHAR = '#'

ITEM_CHAR = 'I'
ITEM_1_CHAR = '1'
ITEM_2_CHAR = '2'
ITEM_3_CHAR = '3'

ENEMY_CHAR = 'X'
HERO_CHAR = '@'


# parameters of the window
TILE_NUMBER = 15
TILE_SIZE = 40

SCREEN_WIDTH = TILE_NUMBER * TILE_SIZE 
PLAYTURF_HEIGHT = TILE_NUMBER * TILE_SIZE
TAILTURF_HEIGHT = 2 * TILE_SIZE
SCREEN_HEIGHT = PLAYTURF_HEIGHT + TAILTURF_HEIGHT


# customization of the window
GAME_TITLE = 'Mac Maze'
GAME_BID = 'Sauvez MacGyver, Sauvez mon projet'


# listing of ressources for the game
PATH_IMAGE = 'data/images/tile_path.png'
WALL_IMAGE = 'data/images/tile_wall.png'
GATE_IMAGE = 'data/images/tile_gate.png'

HERO_IMAGE = 'data/images/perso_hero.png'
ENEMY_IMAGE = 'data/images/perso_enemy.png'

ETHER_IMAGE = 'data/images/item_ether.png'
NEEDLE_IMAGE = 'data/images/item_needle.png'
TUBE_IMAGE = 'data/images/item_tube.png'

SYRINGE_IMAGE = 'data/images/item_syringe.png'

WESTWORLD_MAZE = 'data/images/westworld_logo.png'


# dictionnary of images of the game
IMAGESDICT = {
    'path_image': 'data/images/tile_path.png',
    'wall_image': 'data/images/tile_wall.png',
    'gate_image': 'data/images/tile_gate.png',
    'hero_image': 'data/images/perso_hero.png',
    'enemy_image': 'data/images/perso_enemy.png',
    'ether_image': 'data/images/item_ether.png',
    'needle_image': 'data/images/item_needle.png',
    'tube_image': 'data/images/item_tube.png',
    'syringe_image': 'data/images/item_syringe.png'
}

TILEMAPPING = {
    'S': IMAGESDICT['gate_image'],
    'G': IMAGESDICT['gate_image'],
    '#': IMAGESDICT['wall_image'],
    '.': IMAGESDICT['path_image']
}

ITEMSMAPPING = {
    '@': IMAGESDICT['hero_image'],
    'X': IMAGESDICT['enemy_image'],
    '1': IMAGESDICT['ether_image'],
    '2': IMAGESDICT['needle_image'],
    '3': IMAGESDICT['tube_image']
}

"""
BOARD_1 = os.path.join('data', 'boards', 'board_01.txt')
BOARD_2 = os.path.join('data', 'boards', 'board_02.txt')
BOARD_3 = os.path.join('data', 'boards', 'board_03.txt')

BLUEPRINT = BOARD_1
"""
BLUEPRINT = '{}/board_01.txt'.format(
    os.path.dirname(__file__)
    )

# TODO: learn path 
#   - to deal with call between files in different diretories of my project
