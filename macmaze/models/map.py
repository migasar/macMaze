import config.settings as constants

class Map():

    def __init__(self, filename):
        self.filename = filename

        self.paths = set()
        # listing des chemis praticables
        # pourquoi des sets?
        self.walls = set()
        # pas forcément  nécessaire
        self.start = set()
        self.goal = set()

    def load_from_file():

        with open(self.filename) as infile:
            for x, line in enumerate(infile):
            # ma 1ere boucle for va iterer sur mon fichier ligne par ligne 
            # (ma ligne est x ou y dans mon cas?)
                for y, col in enumerate(line):
                # ma 2nde boucle va iterer sur chaque ligne colonne par colonne 
                    if c == constants.PATH_CHAR:
                        self.path.add(Position(x, y))
                    elif #...