"""Manage the commands of the gamer"""


from models.board import Board
from models.person import Hero, Guard

from models.equipment import Ether, Needle, Tube
from models.position import Position

from views.cli_view import CLIview

import config.constants as constants


class CLIcontroller:

    def __init__(self, board, hero, view):
        self.board = board
        self.hero = hero
        self.view = view
    
    
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


class Game:

    def __init__(self):
        
        self.board = Board.load_blueprint(pick=False)

        self.hero = Hero(self.board)
        self.guard = Guard(self.board)
        
        self.ether = Ether(self.board)
        self.needle = Needle(self.board)
        self.tube = Tube(self.board)

        self.view = CLIview(self.board)
        self.controller = CLIcontroller(self.board, self.hero, self.view)


"""
def main():

    game = Game()
    game.controller.start()

if __name__ == "__main__":
    main()
"""
