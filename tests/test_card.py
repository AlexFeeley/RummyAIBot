import unittest

from src.card import *

# Tests the card class using standard unit tests
from src.card import Card


class TestCard(unittest.TestCase):

    def test_default_constructor(self):
        card = Card("Hearts", 3)
        # self.assertEqual(get_suit(card), 'Hearts', "Card constructor did not create a card of the correct suit")
        # self.assertEqual(get_number(card), 3, "Card constructor did not create a card of the correct number")