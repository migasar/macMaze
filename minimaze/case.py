"""Gere les cases du plateau de jeu et leurs contenus"""


from dataclasses import dataclass, field


@dataclass(order=True)
class Case:
    x: int
    y: int
    #position : tuple
    walk: bool
    landing: str = ""
    toping: str = ""
    visual: str = ""

