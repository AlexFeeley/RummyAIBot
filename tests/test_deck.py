import unittest

# Import from src path
from src.card import *
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
        self.assertRaises(Exception, deck.insert(self.card), "Did not raise exception when trying \
                to overfill deck")

    def test_delete(self):
        deck = Deck(True)
        deck.delete(self.card)
        self.assertEqual(len(deck), 53, "Delete method did not update length size")

    def test_delete_zero_cards(self):
        deck = Deck()
        self.assertRaises(Exception, deck.delete(self.card), "Delete method did not raise \
                exeception if no cards in deck")

    def test_delete_card_does_not_exist(self):
        deck = Deck(True)
        deck.delete(self.card)
        self.assertRaises(Exception, deck.delete(self.card), "Delete method did not raise \
                exception if card deleted is not in deck")

    def test_draw_card(self):
        deck = Deck(True)
        self.assertIsInstance(type(self.card), deck.draw_card(), "Draw Card did not return a card type")

    def test_draw_card_size(self):
        deck = Deck(True)
        deck.draw_card()
        self.assertEqual(len(deck), 53, "Deck size not updated on draw_card")

    def test_return_deck(self):
        deck = Deck(True)
        a = []
        a.append(self.card)
        self.assertIsInstance(type(a), deck.return_deck())

    def test_pickup_cards(self):
        deck = Deck(True)
        deck.pickup_cards(card)
        self.assertNotEqual(52, len(deck), "Deck size did not shrink when pickup cards was called")

    def test_pickup_cards_type(self):
        a = []
        a.append(self.card)
        deck = Deck(True)
        self.assertIsInstance(type(a), deck.pickup_cards(self.card), "Pickup cards did not return \
                a list")

    def test_is_empty(self):
        deck = Deck(True)
        self.assertFalse(deck.is_empty(), "failed to assert false when deck is full")

    def test_is_empty_when_empty(self):
        deck = Deck()
        self.assertTrue(deck.is_empty(), "failed to assert true when deck is empty")


if __name__ == '__main__':
    unittest.main()
