import unittest
from .context import aizul
from aizul import gameobjects as go
from aizul.GameController import GameController


class TestGameControllerClass(unittest.TestCase):

    def test_gamecontroller_playernumber(self):
        with self.assertRaises(ValueError):
            GameController(num_players=5)
        with self.assertRaises(ValueError):
            GameController(num_players=1)
        with self.assertRaises(ValueError):
            GameController(num_players=-3)

        gc = GameController(num_players=3)
        self.assertEqual(gc.num_players, 3)

if __name__ == '__main__':
    unittest.main()