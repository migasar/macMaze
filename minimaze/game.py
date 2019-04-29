"""DOCSTRING"""


from board import Board
from person import Hero
from position import Position
from view import View

import settings as constants


class Game:

    def __init__(self):
        self.board = None
        self.hero = None
        self.view = None


    def start(self):
        self.board = Board.load_blueprint(constants.blueprint)
        self.hero = Hero(self.board)
        self.view = View(self.board)

    def onboarding(self):
        self.view.display_title()
        self.view.display_board()
        #self.view.display_explanation()
        #self.turn_action()


    def new_turn(self):
        self.view.display_board()
        self.turn_action()


    def turn_action(self):

        #invit de commande
        self.view.display_invitation()

        print(self.view.new_order)
        print("")

        if self.view.new_order == "q":
            return self.view.display_goodbye()

        elif self.view.new_order == "s":
            return self.hero.move_up()
        elif self.view.new_order == "x":
            return self.hero.move_down()
        elif self.view.new_order == "w":
            return self.hero.move_left()
        elif self.view.new_order == "c":
            return self.hero.move_right()

        else:
            self.view.display_failure_input()
            self.view.display_explanation()
            return self.turn_action()

    def turn_solver(self):
        pass

def main():

    game = Game()
    game.start()
    game.onboarding()



    
    #game.view.display_invitation()
    #game.turn_action()
    
    #game.hero.move_right()
    #game.hero.move_down()
    print(game.hero.position)

    #game.view.display_board()
    #print(game.board.height)

if __name__ == "__main__":
    main()

