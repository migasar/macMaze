"""DOCSTRING"""


from board import Board
from person import Hero

import settings as constants


class Game:

    def __init__(self):
        self.board = None
        self.hero = None

    def start(self):
        self.board = Board.load_blueprint(constants.blueprint)
        self.hero = Hero(self.board)

    def move(self, direction):
        self.hero.move(direction)

    def visualize_text(self):
        visual_line = ""
        for block in self.board.grid:
            if block.toping == "hero":
                visual_line += "@"
            else:
                visual_line += block.visual
        visual_grid = [ visual_line[i:i+15] for i in range(0, 225, 15) ]
        for line in visual_grid:
            print(line)

def main():
    game = Game()
    game.start()
    game.visualize_text()
    print(len(game.board.grid))
    print(game.hero.position)

if __name__ == "__main__":
    main()

