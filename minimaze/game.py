"""Manage the flow of the game"""


from board import Board
from person import Hero, Enemy
from equipment import Ether, Needle, Tube
from position import Position
from view import View_text

import settings as constants


class Game:

    def __init__(self):

        self.board = Board.load_blueprint(constants.blueprint)
        # TODO: randomize blueprint
        #   - create a method to randomize the choice of the file used as a blueprint
        #   - it will be a way to generate different mazes
        #   - this method could also be in the class Board

        self.hero = Hero(self.board)
        self.enemy = Enemy(self.board)
        
        self.ether = Ether(self.board)
        self.needle = Needle(self.board)
        self.tube = Tube(self.board)

        self.view = View_text(self.board)


    def start(self):
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

        # invit de commande
        self.view.display_invitation()

        # FIXME: print(self.view.new_order)
        #   - maybe, I should delete that line
        print(self.view.new_order)
        print("")

        if self.view.new_order == "q":
            return self.view.display_goodbye()

        elif self.view.new_order == "s":
            if self.hero.move_up() == False:
                self.view.display_no_motion()
            return self.turn_solver()
        elif self.view.new_order == "x":
            if self.hero.move_down() == False:
                self.view.display_no_motion()
            return self.turn_solver()
        elif self.view.new_order == "w":
            if self.hero.move_left() == False:
                self.view.display_no_motion()
            return self.turn_solver()
        elif self.view.new_order == "c":
            if self.hero.move_right() == False:
                self.view.display_no_motion()
            return self.turn_solver()

        else:
            return self.repeat_turn()

    def turn_solver(self):
        # check if it is the last turn
        if self.hero.terminus is True:
            if self.board.game_over() is True:
                return self.view.display_victory()
            else:
                return self.view.display_defeat()
        else:
            return self.new_turn()


def main():

    game = Game()
    game.start()


if __name__ == "__main__":
    main()
