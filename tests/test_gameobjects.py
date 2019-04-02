import unittest
from .context import aizul
from aizul import gameobjects as go


class TestTileClass(unittest.TestCase):

    def test_tile_has_color(self):
        tile = go.Tile(go.Color.BLUE)
        self.assertTrue(isinstance(tile.color, go.Color))

    def test_tile_exception_with_no_color(self):
        with self.assertRaises(TypeError):
            go.Tile("this is not a color")

    def test_tile_string_representation(self):
        tile = go.Tile(go.Color.BLUE)
        self.assertTrue(str(tile) == "BLUE")

class TestColorEnum(unittest.TestCase):
    def test_number_of_colors(self):
        self.assertEqual(len(go.Color),5,"Number of Colors is not 5")

class TestBagClass(unittest.TestCase):
    def test_refill_error_with_no_unused_tiles(self):
        bag = go.Bag()
        with self.assertRaises(IndexError):
            bag.refill()

    def test_draw(self):
        bag = go.Bag()
        tiles = bag.draw_tiles(5)
        self.assertEqual(len(tiles), 5)
        self.assertIsInstance(tiles[0], go.Tile)

        with self.assertRaises(IndexError):
            tiles = bag.draw_tiles(101)

if __name__ == '__main__':
    unittest.main()