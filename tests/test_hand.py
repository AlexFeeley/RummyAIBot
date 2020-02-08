import unittest

# Import from source path
# from src.card import  Card.get_suit()
from src.hand import *


class TestDeck(unittest.TestCase):

    def test_default_constructor(self):
        self.hand = Hand()
        self.assertEqual(len(self.hand), 0, "Default constructor did not create a 0 sized hand")

    def test_overloaded_constructor(self):
        self.hand = Hand(Deck(True))
        self.assertEqual(len(self.hand), 7, "Overloaded constructor did not create a hand of 7 cards")

    def test_overloaded_constructor_exception(self):
        deck = Deck()
        card = Card("Hearts", 3)
        for i in range(6):
            deck.insert(card)
        with self.assertRaises(Exception):
            Hand(deck)

    def test_drawCard_size(self):
        self.hand = Hand(Deck(True))
        self.hand.draw_card(Deck(True))
        self.assertEqual(len(self.hand), 8, "Draw card increased the size of the hand by one")

    def test_putDown(self):
        deck = Deck()
        self.hand = Hand(Deck(True))
        self.hand.put_down(deck, Card("Clubs", 8))
        self.assertFalse(self.hand.__contains__(Card("Clubs", 8)))

    # def test_layDown(self):
    #     deck = Deck()
    #     self.hand = Hand(Deck(True))


if __name__ == '__main__':
    unittest.main()
