"""
Manage the squares of the board and their content
"""

from dataclasses import dataclass


@dataclass(order=True)
class Square:

    x_square: int
    y_square: int

    walk: bool
    toping: str = ''
    landing: str = ''
    visual: str = ''

    @property
    def free(self):
        # check if the square is empty
        return self.walk == True and self.toping == '' and self.landing == ''
