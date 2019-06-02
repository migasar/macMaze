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
PATH_IMAGE = 'resources/images/tile_path_resized40.png'
WALL_IMAGE = 'resources/images/tile_wall_resized40.png'
GATE_IMAGE = 'resources/images/tile_point_resized40.png'

HERO_IMAGE = 'resources/images/perso_hero_resized40.png'
ENEMY_IMAGE = 'resources/images/perso_enemy_resized40.png'

ETHER_IMAGE = 'resources/images/item_ether_resized40.png'
NEEDLE_IMAGE = 'resources/images/item_needle_resized40.png'
TUBE_IMAGE = 'resources/images/item_tube_resized40.png'

SYRINGE_IMAGE = 'resources/images/item_syringe_resized40.png'

WESTWORLD_MAZE = 'resources/images/westworld_labyrinth_thin.png'


# dictionnary of images of the game
IMAGESDICT = {
    'path_image': 'resources/images/tile_path_resized40.png',
    'wall_image': 'resources/images/tile_wall_resized40.png',
    'gate_image': 'resources/images/tile_point_resized40.png',
    'hero_image': 'resources/images/perso_hero_resized40.png',
    'enemy_image': 'resources/images/perso_enemy_resized40.png',
    'ether_image': 'resources/images/item_ether_resized40.png',
    'needle_image': 'resources/images/item_needle_resized40.png',
    'tube_image': 'resources/images/item_tube_resized40.png',
    'syringe_image': 'resources/images/item_syringe_resized40.png'
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

BLUEPRINT = '{}/board_01.txt'.format(
    os.path.dirname(__file__)
    )
