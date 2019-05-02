"""Gere le deroulement du jeu"""


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
        self.view.display_explanation()
        self.turn_action()


    def new_turn(self):
        self.view.display_board()
        self.turn_action()
    
    def repeat_turn(self):
        self.view.display_failure_input()
        self.view.display_explanation()
        self.turn_action()


    def turn_action(self):

        #invit de commande
        self.view.display_invitation()

        print(self.view.new_order)
        print("")

        if self.view.new_order == "q":
            return self.view.display_goodbye()

        elif self.view.new_order == "s":
            self.hero.move_up()
            return self.turn_solver()
        elif self.view.new_order == "x":
            self.hero.move_down()
            return self.turn_solver()
        elif self.view.new_order == "w":
            self.hero.move_left()
            return self.turn_solver()
        elif self.view.new_order == "c":
            self.hero.move_right()
            return self.turn_solver()

        else:
            return self.repeat_turn()

    def turn_solver(self):
        if self.board.targeting() is True:
            return self.view.display_victory()
        else:
            return self.new_turn()


def main():

    game = Game()
    game.start()
    game.onboarding()

    #print(game.hero.position)


if __name__ == "__main__":
    main()

