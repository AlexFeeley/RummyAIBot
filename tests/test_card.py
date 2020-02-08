import unittest

from src.card import *

# Tests the card class using standard unit tests
# from src.card import Card

class TestCard(unittest.TestCase):


    # Tests constructor returns valid suit and number of card created
    def test_constructor(self):
        card = Card("Hearts", 3)
        self.assertEqual(card.get_suit(), 'Hearts', "Card constructor did not create a card of the correct suit")
        self.assertEqual(card.get_number(), 3, "Card constructor did not create a card of the correct number")

    # Tests constructor throws correct errors for invalid card construction
    def test_constructor_bounds(self):
        with self.assertRaises(ValueError):
            Card("Hello World", 2)
        with self.assertRaises(ValueError):
            Card("Hearts", 0)
        with self.assertRaises(ValueError):
            Card("Hearts", 20)

    # Find correct syntax for comparing namedtuples
    # def test_get_card(self):
    #     card = Card("Hearts", 3)
    #     self.assertIsInstance(card.get_card(), Card())

    # Tests correct suit is returned
    def test_getSuit(self):
        card = Card("Hearts", 3)
        self.assertEqual(card.get_suit(), "Hearts", "Get suit returned the wrong suit")
        self.assertNotEqual(card.get_suit(), "Spades", "Get suit returned the wrong suit")

    # Tests corect number is returned
    def test_getNumber(self):
        card = Card("Hearts", 3)
        self.assertEqual(card.get_number(), 3, "Get number returned the wrong number")
        self.assertNotEqual(card.get_number(), 10, "Get number returned the wrong number")

    # Tests == for two equal cards
    def test_equals_true(self):
        card1 = Card("Hearts", 3)
        card2 = Card("Hearts", 3)
        self.assertTrue(card1 == card2, "Equals operator did not return true for equal cards")

    # Tests == for two unequal cards
    def test_equals_false(self):
        card1 = Card("Hearts", 3)
        card2 = Card("Spades", 3)
        card3 = Card("Hearts", 4)
        self.assertFalse(card1 == card2, "Equals operator did not return false for cards with different numbers")
        self.assertFalse(card1 == card3, "Equals operator did not return false for cards with different suits")