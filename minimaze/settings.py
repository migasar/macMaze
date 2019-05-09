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
nombre_sprite_cote = 15
taille_sprite = 40
cote_fenetre = nombre_sprite_cote * taille_sprite


# customization of the window
titre_fenetre = 'Mac Maze'
slogan_fenetre = 'Sauvez MacGyver, Sauvez mon projet'


# listing of ressources for the game
image_path = 'images/tile_path_resized40.png'
image_wall = 'images/tile_wall_resized40.png'
image_way = 'images/tile_point_resized40.png'

image_hero = 'images/perso_hero_resized40.png'
image_guardian = 'images/perso_enemy_resized40.png'

image_ether = 'images/item_ether_resized40.png'
image_needle = 'images/item_needle_resized40.png'
image_tube = 'images/item_tube_resized40.png'

image_syringe = 'images/item_syringe_resized40.png'


blueprint = '{}/board_01.txt'.format(
    os.path.dirname(__file__)
    )
