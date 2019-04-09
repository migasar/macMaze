"""
Fonctionnement
    le programme crée un labyrinthe avec des chemins, des murs, 3 équipements, 1 méchant qui garde la sortie, et 1 héros 
    l'utilisatur controle les mouvements du héros
    l'utilisateur gagne si son héros atteint la sortie après avoir récupéré les 3 équipements
    l'utilisatuer perd si le héros atteint la sortie (et son garde) avant d'avoir récupéré les 3 équipements

Le labyrinthe
    le programme crée une grille vide pour recevoir la structure du labyrinthe
    la structure du labyrinthe est reprise d'un fichier enregistré
        le labyrinthe se compose de plusieurs cases (1 case par sprite)
        ce labyrinthe aura 15 cases en longueur et 15 cases en largeur
    le type de cases varie selon les indications du fichier
        les cases peuvent être des murs ou des chemins
        les cases qui sont des chemins peuvent être juste des chemins, ou le départ, ou la sortie
        les cases qui sont des chemins peuvent contenir 1 équipement ou 1 personne 
    le programme fait apparaitre 3 équipements et 2 personnes dans le labyrinthe
        les 3 équipements apparaissent sur 3 cases différentes
            l'emplacement de la case de chaque équipement est choisie aléatoirement par toutes les cases qui sont juste des chemins
            chaque équipement disparait quand le héros rejoint l'emplacement de la case de l'équipement 
        les 2 personnes apparaissent chacun sur une case de chemin spécial qui leur est dédiée
            le garde apparait à l'emplacement de la case de chemin de sortie
            le héros apparait à l'emplacement de la case de chemin de départ

Le héros
    le héros peut se déplacer dans 4 directions(en haut, en bas, à gauche, )
        le héros change d'emplacement en passant à la case d'à coté si la nouvelle case est valide 
            la case est valide si elle n'est pas un mur
        si le nouvelle emplacement du héros est une case qui n'est pas vide, alors cela a un effet
            l'effet de la collision dépend de ce qui se trouvait sur la case:
                si c'était un équipement:
                    l'équipement disparait
                    le héros a un équipement en plus dans sa boite à outil
                    la case est désormais considérée comme vide (au cas ou le héros repasserait sur cette case)
                si c'est le garde:
                    le jeu est résolu et se termine
                        si le héros a rempli sa boite à outil (les 3 équipements ont été récupéré), l'utilisateur a gagné
                        si le héros n'a pas rempli sa boite à outil (il reste des équipements à récupérer dans le labyrinthe), l'utilisateur a perdu
"""


import settings as constants
from dataclasses import dataclass


class Position:

    def __init__(self, x, y):
        self.position = (x, y)

    # Magic Methods:
    def __repr__(self):
        return str(self.position)

    def __hash__(self):
        return hash(self.position)

    def __eq__(self, pos):
        return self.position == pos.position

    # Methods :
    # 4 moves (up, down, left, right)
    def up(self):
        """Brings a new position based on the previous position.
            The trick with this function is that it doesn't modify the instance position that is calling it
            It creates an entirely new instance position, with a modification of the data (x, y) stored in the previous instance position
            That's why the function starts by using an instance position and ends by using a class Position
        """
        # create new x and y by retrieving the coordinates of the instance
        x, y = self.position
        # create a new object position with modified coordinates
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

    # pass


@dataclass(order=True)
class Case:
    x : int
    y : int
    #position : tuple
    path : bool
    landing : str = ""
    toping : str = ""
#    visual : str


"""
class Case:

    # Attributes of the class :
    path = ["True", "False"]
    landing = [None, "start", "goal"]
    toping = [None, "hero", "enemy", "item1", "item2", "item3"]


    def __init__(self, position, path, landing=None, toping=None):
        self.position = position
        self.path = path
        self.landing = landing
        self.toping = toping
    # Attributes :
    # position (main attribute) - fixed
    # path (boolean) - fixed
    # landing: only one from the list ["regular", "start", "goal"] - fixed
    # toping: None or only one from the 3 equipments and the 2 persons - not fixed

    # Magic Methods :
    # __repr__
    # __str__

    # Properties :

    @property
    def path(self):
        return self.path

    # Methods :
    # def remove_toping(self, top):
    # def test_collision():
    # def solve_collision():
        # if collide with equipment:
            # load remove_toping()
            # modify count in toolbox of the hero
        # if collide with enemy --> showdown
            # if toolbox is completed, hero wins
            #  --> "winner, winner, needle dinner"
            # if toolbox is not completed, hero loses
            #  --> "these violent delights have violent ends"
    pass
"""


class Board:

    def __init__(self, grid, pathway, starting, ending, width, height):

        self.grid = grid

        self.pathway = pathway
        self.starting = starting
        self.ending = ending

        self.width = width
        self.height = height

        #self.load_from_file()

    # Methods:
    # create an empty grid (a list of list --> 15 * 15)
    # load the structure of the board from a file
    # the data fetched from the file will be used as a blueprint
    # with each element from the file, 
    # #we will create an object case per element of the list to populate the grid
    @classmethod
    def load_blueprint(cls, filename):
        #grid = {}
        grid = []
        pathway = []
        starting = None
        ending = None
        width = 0
        height = 0

        with open(filename) as infile:
            #k = 0
            for y, line in enumerate(infile):
                for x, col in enumerate(line):
                    #k += 1

                    if col == "S":
                        #f"case_{k}" = Case(x, y, path=True, landing="start")
                        #grid[Position(x, y)] = f"case_{k}"
                        grid.append(Case(x, y, path=True, landing="start"))
                        pathway.append(Position(x, y))
                        starting = Position(x, y)

                    elif col == "G":
                        #f"case_{k}" = Case(x, y, path=True, landing="goal")
                        #grid[Position(x, y)] = f"case_{k}"
                        grid.append(Case(x, y, path=True, landing="goal"))
                        pathway.append(Position(x, y))
                        ending = Position(x, y)

                    elif col == ".":
                        #f"case_{k}" = Case(x, y, path=True)
                        #grid[Position(x, y)] = f"case_{k}"
                        grid.append(Case(x, y, path=True))
                        pathway.append(Position(x, y))

                    else :
                        #f"case_{k}" = Case(x, y, path=False)
                        #grid[Position(x, y)] = f"case_{k}"
                        grid.append(Case(x, y, path=False))
                        
        return cls(grid, pathway, starting, ending, x+1, y+1)

    #pass


class Hero:

    # def __init__()
    def __init__(self, board):
    # Attributes :
    # position (main attribute --> begin with the position on the case "start")
    # toolbox (start empty --> counter full at 3)
        self.board = board
        # self.position = self.board.start

    # Magic Methods :
    # __repr__

    # Methods :
    # def move(self, direction):
        """this method permits the movement of the hero by verifying if the position is a valid one, and by solving eventual collisions with any object standing on the case"""
        # test if the new position doesn't put the hero outside of the board
        # test if the new position is not a wall
        # test if the new position is an empty case
        # if the case is not empty
            # solve the collision between the hero
            # and the object standing on the case
    pass


class Enemy:
    #Enemy et Hero pouraient avoir une classe parent (la classe Person)

    # def __init__()

    # Attributes :
    # position (main attribute)
    pass


class Equipment:

    # def __init__()

    # Attributes :
    # position (main attribute)
    pass


def main():

    """
    bazar():
        point1 = Position(0, 1)
        case1 = Case(0, 0, True, )
        case2 = Case(0, 1, True, "start", "hero")

        myDict = {(0, 0): case1}
        
        q = 1
        z = 2
        #k = q + z
        
        #case + str(q+z) = 10
        yourDict = {}
        a = 1 
        b = 1
        
        for i in range(3):
            yourDict[f"case_{a}"] = b
            a += 1
            b = b * 2

        print(yourDict)

        a = [i for i in range(10)]
        b = [i for i in range(10)]
        c = []
        for j in a:
            for i in b:
                k = i + j
                c.append(k)
        d = set(c)

        print(c[5 : 15])
    """
    
    board = Board.load_blueprint("board-01.txt")


main()
