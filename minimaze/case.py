"""Gere les cases du plateau de jeu et leurs contenus"""


from dataclasses import dataclass


@dataclass(order=True)
class Case:

    x: int
    y: int

    walk: bool
    toping: str = ""
    landing: str = ""
    visual: str = ""

    @property
    def free(self):
    #check if the case is empty
        return self.walk == True and self.toping == "" and self.landing == ""
