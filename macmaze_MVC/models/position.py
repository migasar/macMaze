
class Position:

    def __init__(self, x, y):
        self.position = (x, y)

    def __repr__(self):
        # ???
        return str(self.position)

    def __hash___(self):
        # ???
        return hash(self.position)

    def __eq__(self, pos):
        # without this method, we can't compare 2 instances of position
        # this define that 2 positions are considered equals,
        # if their tuples are equal
        return self.position == pos.position

    def up(self):
        x, y = self.position
        return Position(x, y-1)

    def down(self):
        x, y = self.position
        return Position(x, y+1)

    def right(self):
        x, y = self.position
        return Position(x+1, y)

    def left(self):
        x, y = self.position
        return Position(x-1, y)
