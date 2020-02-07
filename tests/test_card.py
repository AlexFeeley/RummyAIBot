import unittest

from src.card import *

# Tests the card class using standard unit tests
from src.card import Card

class TestCard(unittest.TestCase):


    def test_default_constructor(self):
        card = Card("Hearts", 3)
        self.assertEqual(card.get_suit(), 'Hearts', "Card constructor did not create a card of the correct suit")
        self.assertEqual(card.get_number(), 3, "Card constructor did not create a card of the correct number")

        try:
            card = Card("Hello World", 2)
        except ValueError:
            print("ValueError thrown when invalid suit was used")
        except:
            print("ValueError was not thrown when invalid suit was used")

        try:
            card = Card("Hearts", 15)
        except ValueError:
            print("ValueError thrown when invalid number was used")
        except:
            print("ValueError was not thrown when invalid number was used")

    def test_get_card(self):
        card = Card("Hearts", 3)
        # myCard = collections.namedtuple('Card', [card.get_suit(), card.get_number()])
        # print(testCard.suit)
        # self.assertEqual(testCard, myCard, "GetCard() did not return the correct namedtuple")