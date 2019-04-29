"""docstring"""

from board import Board

import settings as constants

class View:

    def __init__(self, board):
        self.board = board

    def display_board(self):
        visual_line = ""
        for block in self.board.grid:
            if block.toping:
                visual_line += block.toping
            else:
                visual_line += block.visual
        visual_grid = [visual_line[i:i+15] for i in range(0, 225, 15)]
        for line in visual_grid:
            print(line)


    def display_title(self):
        print("\t**********************************************")
        print(
            "\t  " + constants.titre_fenetre 
            + " - " + constants.slogan_fenetre
            )
        print("\t**********************************************")

    def display_goodbye(self):
        print("\t Vous quittez le jeu.")
        print("\t Le labyrinthe n'était sans doute pas fait pour vous, ")
        print("\t mais nous vous remercions d'avoir essayé.")

    
    def display_victory(self):
        print(" ")
        print("\t**********************************************")
        print(" ")
        print("\t Bravo, vous avez trouvé le chemin du labyrinthe.")
        print("\t Mais ces jeux violents auront une fin violante.")
        print("")

    def display_failure_input(self):
        print("\t Désolé, votre commande n'est pas valide.")

    def display_explanation(self):
        print("\t Dirigez MacGyver jusqu'à la sortie du labyrinthe")
        print("\t  - pour aller en haut, appuyez sur S")
        print("\t  - pour aller en bas, appuyez sur X")
        print("\t  - pour aller à gauche, appuyez sur W")
        print("\t  - pour aller à droite, appuyez sur C")
        print("\t  - pour quitter le jeu, appuyez sur Q")
    
    def display_invitation(self):
        self.new_order = input("Qu'allez vous faire ?  ")
        return self.new_order
