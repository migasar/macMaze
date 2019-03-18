"""
Dans la version simpliste du jeu, il me faut 2 classes: 
le niveau et le personnage
"""

class Board:
    def __init__(self, filename):
        self.filename = filename
        self.structure = 0

    def materialize(self):
        """Méthode permettant de générer le niveau en fonction du fichier.
        On crée une liste générale, contenant une liste par ligne à afficher"""
        with open(self.filename, "r") as filename:
            board_structure = []
            


class Hero:
    pass