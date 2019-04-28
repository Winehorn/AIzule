import aizul.gameobjects as go
from aizul.gameobjects import Color

class GameController:
    def __init__(self, num_players=4):
        if num_players > 4:
            raise ValueError("Number of players too large!")
        if num_players < 2:
            raise ValueError("Number of players too small!")
        self.num_players = num_players

        self.bag = go.Bag()
        self.table = go.Factory(is_table=True)

        self.num_factories = num_players * 2 + 1
        self.factories = [go.Factory() for _ in range(self.num_factories)]
        for factory in self.factories:
            factory.tiles = self.bag.draw_tiles(4)

    def get_full_factories(self):
        full_factories = []
        for i, factory in enumerate(self.factories):
            if len(factory.tiles) == 4:
                full_factories.append(i)
        return full_factories

    def print_table(self):
        print("Factories:")
        full_factories = self.get_full_factories()
        
        for factory in full_factories:
            print("[{}]: {x[0]}, {x[1]}, {x[2]}, {x[3]}".format(factory, x=self.factories[factory].tiles))
        print("")
        print("Table:")
        for color in Color:
            index = self.num_factories - 1 + color.value
            num_color_tiles = self.table.tiles.count(color)
            print("[{index}]: {color}: {num_color_tiles}".format(index=index, color= color.name, num_color_tiles=num_color_tiles))