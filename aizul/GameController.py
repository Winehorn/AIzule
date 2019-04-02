import aizul.gameobjects as go

class GameController:
    def __init__(self, num_players=4):
        if num_players > 4:
            raise ValueError("Number of players too large!")
        if num_players < 2:
            raise ValueError("Number of players too small!")
        self.num_players = num_players

        self.bag = go.Bag()

        self.num_factories = num_players * 2 + 1
        self.factories = [go.Factory() for _ in range(self.num_factories)]
        for factory in self.factories:
            factory.tiles = self.bag.draw_tiles(4)