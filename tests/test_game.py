import unittest

from src.game import *


class TestGame(unittest.TestCase):

    def test_default_contructor(self):
        game = Game(2)

if __name__ == '__main__':
    unittest.main()