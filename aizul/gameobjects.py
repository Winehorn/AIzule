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
        '''Print color of remaining tiles.'''
        for tile in self.tiles:
            print(tile)

    def draw_tiles(self, number=4):
        '''Return tiles and refills the bag if it gets empty.'''
        tiles = []
        for _ in range(number):
            if len(self.tiles) == 0:
                self.refill()
            tiles.append(self.tiles.pop())
        return tiles

    def refill(self):
        '''Put unused tiles in the bag.'''
        if not self.used_tiles:
            raise IndexError("No used tiles!")
        else:
            self.tiles.extend(self.used_tiles)
            random.shuffle(self.tiles)

    def return_tiles(self, tiles):
        '''
        Return tiles to the used tiles list.

        Arguments:
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
            raise TypeError('Tile color has to be of type Color!')

    def __repr__(self):
        return self.color.name


class Factory:
    def __init__(self):
        self.tiles = []

    def pick_tiles(self, color: Color, remove_all=True):
        '''Return tuple of tiles of specified color and remaining tiles.'''
        picked_tiles = [tile for tile in self.tiles if tile.color == color]

        if not picked_tiles:
            raise ValueError('You can only pick available tiles!')

        remaining_tiles = [tile for tile in self.tiles if tile.color != color]

        if remove_all:
            self.tiles = []
        else:
            self.tiles = remaining_tiles
        return picked_tiles, remaining_tiles