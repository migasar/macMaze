"""DOCSTRING"""


from dataclasses import dataclass


@dataclass(order=True)
class Case:
    x: int
    y: int
    #position : tuple
    walk: bool
    landing: str = ""
    toping: str = ""
