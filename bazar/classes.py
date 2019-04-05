"""
Dans la version simpliste du jeu, il me faut 3 classes : 
le niveau, le personnage, et la position 
(je gère la position en-dehors du personnage
 car elle va me servir aussi pour les items par la suite)
"""

import settings as constants


class Position:
    def __init__(self, x, y):
        self.position = (x,y)
    
    """ 
    # methods to add this class to make it usable by the other classes 
    # to complete the game
    def __repr__(self):
        # ???
        return str(self.position)

    def __hash___(self):
        # ???
        return hash(self.position)

    def __eq__(self, pos):
        # without this method, we can't compare 2 instances of position
        # this define that 2 positions are considered equals,
        # if their tuples are equal
        return self.position == pos.position
    """

    def up(self):
        x, y = self.position
        return Position(x, y-1)

    def down(self):
        x, y = self.position
        return Position(x, y+1)

    def right(self):
        x, y = self.position
        return Position(x+1, y)

    def left(self):
        x, y = self.position
        return Position(x-1, y)


class Board:
    def __init__(self, filename):
        self.filename = filename
        # exemple : filename is 'data/board-01.txt'
        # --> board = Board('data/board-01.txt')

        # pourquoi des sets?
        # listing des chemins praticables
        self.path = set()

        # l'attribut wall n'est pas forcément nécessaire
        # selon le mécanisme de mon programme
        self.wall = set()

        self.start = set()
        self.goal = set()

        self.load_from_file()

    def is_path_position(self, position):
        # check if a position is valid
        return position in self.path

    def load_from_file():
        with open(self.filename, "r") as infile:
            # ma 1ere boucle for va iterer sur mon fichier ligne par ligne
            # (ma ligne est x ou y dans mon cas?), (x or line)
            for line in enumerate(infile):
                # ma boucle va iterer sur chaque ligne colonne par colonne
                # (y or col) 
                for col in enumerate(line):
                    if col == constants.PATH_CHAR:
                        self.path.add(Position(x, y))
                    elif col == constants.START_CHAR:
                        self.start.add(Position(x, y))
                        self.path.add(Position(x, y))
                    elif col == constants.GOAL_CHAR:
                        self.goal.add(Position(x, y))
                        self.path.add(Position(x, y))
                    else:
                        # This is a wall
                        pass


class Hero:
    """Classe permettant de créer un personnage"""
    def __init__(self, image, position, board):
        # image du personnage
        self.image = pygame.image.load('resources/macguy.truc').convert_alpha()
        self.position = Position(0, 0)
