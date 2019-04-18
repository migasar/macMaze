"""Gere les déplacements des objets"""


class Position:

    def __init__(self, x, y):
        self.position = (x, y)

    # Magic Methods:
    def __repr__(self):
        return str(self.position)

    def __hash__(self):
        return hash(self.position)

    def __eq__(self, pos):
        return self.position == pos.position

    @property
    def x(self):
        return self[0]
    
    @property
    def y(self):
        return self[1]

    # Methods :
    # 4 moves (up, down, left, right)
    def up(self):
        """Brings a new position based on the previous position.
            The trick with this function is that it doesn't modify the instance position that is calling it
            It creates an entirely new instance position, with a modification of the data (x, y) stored in the previous instance position
            That's why the function starts by using an instance position and ends by using a class Position
        """
        # create new x and y by retrieving the coordinates of the instance
        x, y = self.position
        # create a new object position with modified coordinates
        return Position(x, y+1)
        

    def down(self):
        x, y = self.position
        return Position(x, y-1)

    def right(self):
        x, y = self.position
        return Position(x+1, y)

    def left(self):
        x, y = self.position
        return Position(x-1, y)
