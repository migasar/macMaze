# gere le personnage

class Hero :

    def __init__(self, board):
        self.board = board
        self.position = self.board.start

    def move(self, direction):
        """docstring.""""
        # getaatr can access an object property using a string
        new_position = getattr(self.position, direction)()
        if new_position in self.map:
            self.position = new_position

