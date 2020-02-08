import unittest

# Import from src path
from src.deck import *


# Tests the deck class using standard unit tests. Integration tests are not used.
class TestDeck(unittest.TestCase):

    def setUp(self):
        self.card = Card("Spades", 13)

    def test_default_constructor(self):
        deck = Deck()
        self.assertEqual(len(deck), 0, "Initial Deck constructor did not create a zero sized deck")

    def test_overload_constructor(self):
        deck = Deck(True)
        self.assertEqual(len(deck), 52, "Initial Deck overloaded constructor did not create a \
                full deck")

    def test_insert(self):
        deck = Deck()
        deck.insert(self.card)
        self.assertEqual(len(deck), 1, "Insert method did not update length size")

    def test_insert_max_size(self):
        deck = Deck(True)
        with self.assertRaises(Exception):
            deck.insert(self.card)

    def test_delete(self):
        deck = Deck(True)
        deck.delete(self.card)
        self.assertEqual(len(deck), 51, "Delete method did not update length size")

    def test_delete_zero_cards(self):
        deck = Deck()
        with self.assertRaises(Exception):
            deck.delete(self.card)

    def test_delete_card_does_not_exist(self):
        deck = Deck(True)
        deck.delete(self.card)
        with self.assertRaises(Exception):
            deck.delete(self.card)

    def test_draw_card(self):
        deck = Deck(True)
        card = deck.draw_card()
        self.assertFalse(deck.__contains__(card), "Deck still contains card that was drawn")

    def test_draw_card_size(self):
        deck = Deck(True)
        deck.draw_card()
        self.assertEqual(len(deck), 51, "Deck size not updated on draw_card")

    def test_return_deck(self):
        deck = Deck(True)
        self.assertIsInstance(deck.return_deck(), list)

    def test_pickup_cards(self):
        deck = Deck(True)
        deck.pickup_cards(self.card)
        self.assertEqual(37, len(deck), "Deck size did not shrink when pickup cards was called")
        self.assertFalse(deck.__contains__(self.card), "Deck still contains card that was picked up from")

    def test_pickup_cards_type(self):
        deck = Deck(True)
        self.assertIsInstance(deck.pickup_cards(self.card), list)

    def test_is_empty(self):
        deck = Deck(True)
        self.assertFalse(deck.is_empty(), "failed to assert false when deck is full")

    def test_is_empty_when_empty(self):
        deck = Deck()
        self.assertTrue(deck.is_empty(), "failed to assert true when deck is empty")

if __name__ == '__main__':
    unittest.main()
