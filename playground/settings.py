"""Constantes du jeu de Labyrinthe Mac Maze"""


START_CHAR = 'S'
GOAL_CHAR = 'G'
PATH_CHAR = '.'
WALL_CHAR = '#'

ITEM_CHAR = 'I'
ENEMY_CHAR = 'E'
HERO_CHAR = 'H'

blueprint = "board-01.txt"

# Paramètres de la fenêtre
nombre_sprite_cote = 15
taille_sprite = 40
cote_fenetre = nombre_sprite_cote * taille_sprite

# Personnalisation de la fenêtre
titre_fenetre = "Mac Maze"
slogan_fenetre = "Save MacGyver, Save my project"

# Listes des images du jeu
image_path = "images/tile_path_resized40.png"
image_wall = "images/tile_wall_resized40.png"
image_way = "images/tile_point_resized40.png"

image_hero = "images/perso_hero_resized40.png"
image_guardian = "images/perso_enemy_resized40.png"

image_ether = "images/item_ether_resized40.png"
image_needle = "images/item_needle_resized40.png"
image_tube = "images/item_tube_resized40.png"

image_syringe = "images/item_syringe_resized40.png"

