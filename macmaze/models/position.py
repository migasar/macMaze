
class Position:

    def __init__(self, x, y):
        self.position = (x, y)

    def __repr__(self):
        # ???
        return str(self.position)

    def __hash___(self):
        # ???
        return hash(self.position)

    def up(self):
        return Position(x, y-1)

    def down(self):
        return Position(x, y+1)

    def right(self):
        return Position(x+1, y)

    def left(self):
        return Position(x-1, y)
