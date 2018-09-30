from enum import Enum

class Color(Enum):
    BLUE = 1
    ORANGE = 2
    RED = 3
    BLACK = 4
    WHITE = 5


class Bag:
    pass

class Tile:
    def __init__(self, color: Color):
        if(isinstance(color, Color)):
            self.color = color
        else:
            raise TypeError("Tile color has to be of type Color")


class Location:
    pass