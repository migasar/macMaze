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
PATH_IMAGE = 'resources/images/tile_path_resized40.png'
WALL_IMAGE = 'resources/images/tile_wall_resized40.png'
GATE_IMAGE = 'resources/images/tile_point_resized40.png'

HERO_IMAGE = 'resources/images/perso_hero_resized40.png'
ENEMY_IMAGE = 'resources/images/perso_enemy_resized40.png'

ETHER_IMAGE = 'resources/images/item_ether_resized40.png'
NEEDLE_IMAGE = 'resources/images/item_needle_resized40.png'
TUBE_IMAGE = 'resources/images/item_tube_resized40.png'

SYRINGE_IMAGE = 'resources/images/item_syringe_resized40.png'


blueprint = '{}/board_01.txt'.format(
    os.path.dirname(__file__)
    )
