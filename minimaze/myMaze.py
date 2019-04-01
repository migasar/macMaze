
"""
le programme crée un labyrinthe avec des chemins, des murs, 3 équipements, 1 méchant qui garde la sortie, et 1 héros 
l'utilisatur controle les mouvements du héros
l'utilisateur gagne si son héros atteint la sortie après avoir récupéré les 3 équipements
l'utilisatuer perd si le héros atteint la sortie (et son garde) avant d'avoir récupéré les 3 équipements
"""

"""
le labyrinthe
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
"""

"""
le héros
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


class Position:

    def __init__(self, x, y):
        self.position = (x, y)
    
    # Magic Methods:
    # __repr__
    # __eq__

    # Methods : 
    # 4 moves (up, down, left, right)



class Case:

    # def __init__(self, position, wall, landing, toping)

    # Attributes : 
    # position (main attribute) - fixed
    # is_path (boolean) - fixed
    # type_of_path: only one from the list ["regular", "start", "goal"] - fixed
    # toping: None or only one from the 3 equipments and the 2 persons - not fixed

    # Magic Methods :
    # __repr__
    # __str__

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



class Board:

    # def __init__()

    # Methods:
    # create an empty grid (a list of list --> 15 * 15)
    # load the structure of the board from a file
    # the data fetched from the file will be used as a blueprint
    # with each element from the file, we will create an object case per element of the list to populate the grid

    pass



class Hero:

    # def __init__()

    # Attributes :
    # position (main attribute --> begin with the position on the case "start")
    # toolbox (start empty --> counter full at 3)

    # Magic Methods :
    # __repr__

    # Methods :
    # def move(self, direction):
        """this method permits the movement of the hero by verifying if the position is a valid one, and by solving eventual collisions with any object standing on the case"""
        # test if the new position doesn't put the hero outside of the board
        # test if the new position is not a wall
        # test if the new position is an empty case
        # if the case is not empty, solve the collision between the hero and the object standing on the case

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



