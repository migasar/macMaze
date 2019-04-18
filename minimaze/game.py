"""DOCSTRING"""


from board import Board
from person import Hero
from position import Position

import settings as constants


class Game:

    def __init__(self):
        self.board = None
        self.hero = None

    def start(self):
        self.board = Board.load_blueprint(constants.blueprint)
        self.hero = Hero(self.board)
        #self.view = View(self.board)


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
            print("\t**********************************************")
            print(
                "\t  " + constants.titre_fenetre 
                + " - " + constants.slogan_fenetre
                )
            print("\t**********************************************")

    def display_explanation(self):
        print("\t Dirigez MacGyver jusqu'à la sortie du labyrinthe")
        print("\t  - pour aller en haut, appuyez sur Z")
        print("\t  - pour aller en bas, appuyez sur S")
        print("\t  - pour aller à gauche, appuyez sur A")
        print("\t  - pour aller à droite, appuyez sur E")
        print("\t  - pour quitter le jeu, appuyez sur Q")
    
    def invitation(self):
        self.new_order = input("Qu'allez vous faire ?  ")
        return self.new_order

    def new_turn(self):
        self.visualize_text()
        self.display_explanation()
        self.invitation()

    def turn_solver(self):

        if self.new_order == "q":
            print(
                """
                Vous quittez le jeu.
                Le labyrinthe n'était sans doute pas fait pour vous,
                mais nous vous remercions d'avoir essayé.
                """
                )
        
        elif self.new_order == "z":
            return self.hero.move.up()
        
        elif self.new_order == "s":
            return self.hero.move.down()

        elif self.new_order == "a":
            return self.hero.move.left()
        
        elif self.new_order == "e":
            return self.hero.position.right()
        
        else:
            print(
                """
                
                Désolé, commande non valide
                
                """
                )
            return self.new_turn()

def main():

    game = Game()
    game.start()

    game.display_title()
    game.visualize_text()
    game.display_explanation()

    """
    game.invitation()
    game.turn_solver()
    """

    #game.hero.up() 

    game.hero.up()
    print(game.hero.position)


if __name__ == "__main__":
    main()

