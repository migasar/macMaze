"""docstring"""

from board import Board

class View:

    def __init__(self):
        self.board = board

    def visualize_text(self):
        visual_line = ""
        for block in self.board.grid:
            if block.toping == "hero":
                visual_line += "@"
            else:
                visual_line += block.visual
        visual_grid = [visual_line[i:i+15] for i in range(0, 225, 15)]
        for line in visual_grid:
            print(line)

    def display_title(self):
        print("\t******************************************************")
        print("\t***  macMaze - Sauvez MacGyver, sauvez mon projet  ***")
        print("\t******************************************************")
    
    def display_explanation(self):
        print("\tDirigez MacGyver jusqu'à la sortie du labyrinthe")
        print("\t  - pour aller en haut, appuyez sur Z")
        print("\t  - pour aller en bas, appuyez sur S")
        print("\t  - pour aller à gauche, appuyez sur A")
        print("\t  - pour aller à droite, appuyez sur E")
    
    def invitation(self):
        variable = input("Qu'allez vous faire ?  ")
