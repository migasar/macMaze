# modèle principal quie va enrober/ orchestrer les interactions entre les modèles

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


class Game:

    pass


