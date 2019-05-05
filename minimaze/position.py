"""Gere les déplacements des objets"""


from collections import namedtuple

Position = namedtuple('Position', ['x', 'y'])


"""

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
        return self.position[0]
    
    @property
    def y(self):
        return self.position[1]

"""

