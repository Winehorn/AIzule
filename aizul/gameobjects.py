from enum import Enum
import random

class Color(Enum):
    BLUE = 1
    ORANGE = 2
    RED = 3
    BLACK = 4
    WHITE = 5


class Bag:
    def __init__(self):
        self.max_tiles = 100
        self.tiles = []
        self.used_tiles = []

        for color in Color:
            for _ in range(20):
                self.tiles.append(Tile(color))
        random.shuffle(self.tiles)

    def print_remaining(self):
        '''Prints color of remaining tiles.'''
        for tile in self.tiles:
            print(tile)

    def draw_tiles(self, number=4):
        tiles = []
        for _ in range(number):
            if len(self.tiles) == 0:
                self.refill()
            tiles.append(self.tiles.pop())
        return tiles

    def refill(self):
        if not self.used_tiles:
            raise IndexError("No used tiles!")
        else:
            self.tiles.extend(self.used_tiles)
            random.shuffle(self.tiles)

    def return_tiles(self, tiles):
        '''
        Return tiles to the used tiles list.

        Keyword arguments:
        tiles -- list of tiles to return
        '''
        for tile in tiles:
            if type(tile) is not Tile:
                raise TypeError("Only Tile type allowed!")
        self.used_tiles.extend(tiles)

class Tile:
    def __init__(self, color: Color):
        if(isinstance(color, Color)):
            self.color = color
        else:
            raise TypeError('Tile color has to be of type Color')

    def __repr__(self):
        return self.color.name


class Factory:
    def __init__(self):
        self.tiles = []