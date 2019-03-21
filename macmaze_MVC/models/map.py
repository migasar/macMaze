import config.settings as constants
from .position import Position

class Map():

    def __init__(self, filename):
        self.filename = filename

        self.path = set()
        # listing des chemins praticables
        # pourquoi des sets?
        self.walls = set()
        # pas forcément  nécessaire
        self.start = set()
        self.goal = set()

        self.load_from_file()

    def is_path_position(self, position):
        # check if a position is valid
        return position in self.path

    def load_from_file():

        with open(self.filename) as infile:
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


###
### The following lines are only used to test my code
###
"""
def main():
    map = Map('data/maps/map-01.txt')

    p = Position(-1, 0)
    print(map.is_valid_position(p))

if __name__ == "__main__":
    pass
"""