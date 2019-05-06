"""Gere les cases du plateau de jeu et leurs contenus"""


from dataclasses import dataclass


@dataclass(order=True)
class Case:

    x: int
    y: int

    walk: bool
    landing: str = ""
    toping: str = ""
    visual: str = ""
