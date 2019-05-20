"""Manage the flow of the game"""


from models.board import Board
from models.person import Hero, Enemy
from models.equipment import Ether, Needle, Tube
from models.position import Position

from views.textview import TextView
from event import TextEvent

from config import settings as constants


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

        self.view = TextView(self.board)
        self.event = TextEvent(self.board, self.hero, self.view)

    def starter(self):
        self.event.starter()


def main():

    game = Game()
    game.starter()
    

if __name__ == "__main__":
    main()

