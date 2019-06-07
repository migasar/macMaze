"""
Manage the flow of the game
and the interactions between the components of the project
"""

from models.board import Board
from models.person import Hero, Guard
from models.equipment import Ether, Needle, Tube
from views.cli_view import CLIview
from config import constants


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
            next_step = self.hero.move_up()
            if self.check_move(next_step) is False:
                self.view.display_no_motion()
            else:
                self.hero.move(next_step)
            return self.turn_solver()
        elif self.view.new_order == "x":
            next_step = self.hero.move_down()
            if self.check_move(next_step) is False:
                self.view.display_no_motion()
            else:
                self.hero.move(next_step)
            return self.turn_solver()
        elif self.view.new_order == "w":
            next_step = self.hero.move_left()
            if self.check_move(next_step) is False:
                self.view.display_no_motion()
            else:
                self.hero.move(next_step)
            return self.turn_solver()
        elif self.view.new_order == "c":
            next_step = self.hero.move_right()
            if self.check_move(next_step) is False:
                self.view.display_no_motion()
            else:
                self.hero.move(next_step)
            return self.turn_solver()

        else:
            return self.repeat_turn()

    def turn_solver(self):
        # check if it is the last turn
        if self.hero.terminus is True:
            if self.game_over() is True:
                return self.view.display_victory()
            else:
                return self.view.display_defeat()
        else:
            return self.new_turn()

    ######
    # methods to solve the collisions
    def check_move(self, next_step):
        """Method to verify if the next move is possible"""

        motion = True

        # check that the new position is still inside the board
        if self.board.inside(next_step) is False:
            motion = False
        else:
            blockade = self.board.get_coordinates(
                'x_square', 'y_square', next_step.x_pos, next_step.y_pos
                )

            # manage potential collision with other elements on the next square
            if self.check_path(blockade) is False:
                motion = False

        return motion

    def check_path(self, block):
        """
        Check the attributes of the square on the next position,
        and initiate the methods in case of collisions
        """

        pathway = False

        if block.free is True:
            # check that the new position is not a wall
            block.toping = constants.HERO_CHAR
            pathway = True

        elif block.landing == 'start':
            # check if the hero came back to starting square
            block.toping = constants.HERO_CHAR
            pathway = True

        elif block.toping != '':
            # check if there is already something on the next position
            self.colliding(block)
            pathway = True

        return pathway

    def colliding(self, block):
        """Determine the type of collision and the method to solve it"""

        if block.toping == constants.GUARD_CHAR:
            self.showdown(block)
        else:
            self.toolup(block)

    def toolup(self, block):
        """
        Put an item in the inventory of the hero,
        when he gets in collision with it
        """

        if block.toping == constants.ITEM_1_CHAR:
            self.hero.toolbox.append(1)  # ether
        elif block.toping == constants.ITEM_2_CHAR:
            self.hero.toolbox.append(2)  # needle
        elif block.toping == constants.ITEM_3_CHAR:
            self.hero.toolbox.append(3)  # tube

        block.toping = constants.HERO_CHAR

    def showdown(self, block):
        """Decide of the issue when the hero and the guard collide"""

        self.hero.terminus = True
        if len(self.hero.toolbox) == 3:
            # WIN
            block.toping = constants.HERO_CHAR
            # else:
            # LOSE --> phantom walk
            # FIXME: phantom walk defeat
            # I should find a way to clarify how the game understand
            # that the hero has lost in front of the guard

    ######
    # method to know how the game ends
    def game_over(self):
        """Check if the hero has won the game"""

        end = self.board.get_square('landing', 'goal')
        return end.toping == constants.HERO_CHAR


class CLIgame:

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
