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
tile_number = 15
tile_size = 40
screen_width = tile_number * tile_size


# customization of the window
game_title = 'Mac Maze'
game_bid = 'Sauvez MacGyver, Sauvez mon projet'


# listing of ressources for the game
image_path = 'resources/images/tile_path_resized40.png'
image_wall = 'resources/images/tile_wall_resized40.png'
image_way = 'resources/images/tile_point_resized40.png'

image_hero = 'resources/images/perso_hero_resized40.png'
image_guardian = 'resources/images/perso_enemy_resized40.png'

image_ether = 'resources/images/item_ether_resized40.png'
image_needle = 'resources/images/item_needle_resized40.png'
image_tube = 'resources/images/item_tube_resized40.png'

image_syringe = 'resources/images/item_syringe_resized40.png'


blueprint = '{}/board_01.txt'.format(
    os.path.dirname(__file__)
    )
# TODO: learn path 
#   - to deal with call between files in different diretories of my project