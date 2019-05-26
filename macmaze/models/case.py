"""Manage the cases of the board and their content"""


from dataclasses import dataclass


@dataclass(order=True)
class Case:

    x_case: int
    y_case: int

    walk: bool
    toping: str = ''
    landing: str = ''
    visual: str = ''

    @property
    def free(self):
        # check if the case is empty
        return self.walk == True and self.toping == '' and self.landing == ''
