import unittest

# Import from source path
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
        self.hand = Hand()
        self.hand.insert_card(Deck(True), Card("Hearts", 3))
        self.hand.put_down(Deck(), Card("Hearts", 3))
        self.assertFalse(self.hand.__contains__(Card("Hearts", 3)))

    def test_putDown_length(self):
        self.hand = Hand()
        self.hand.insert_card(Deck(True), Card("Hearts", 3))
        self.hand.put_down(Deck(), Card("Hearts", 3))
        self.assertEqual(len(self.hand), 0, "Laying down one card decreased the size of the hand by one")

    def test_putDown_exception(self):
        self.hand = Hand()
        with self.assertRaises(ValueError):
            self.hand.put_down(Deck(), Card("Hearts", 9))

    def test_layDown(self):
        self.hand = Hand()
        cards = [Card("Clubs", 9), Card("Clubs", 8)]
        self.hand.insert_cards(Deck(True), cards)
        self.hand.lay_down(Deck(), cards)
        self.assertFalse(self.hand.__contains__(Card("Clubs", 9)))

    def test_layDown_nonConsecutive(self):
        self.hand = Hand(Deck(True))
        cards = [Card("Clubs", 9), Card("Clubs", 11)]
        with self.assertRaises(Exception):
            self.hand.lay_down(Deck(), cards)

    def test_layDown_diffSuits(self):
        self.hand = Hand(Deck(True))
        for i in range(0, 10):
            self.hand.draw_card(Deck(True))
        cards = [Card("Clubs", 11), Card("Spades", 11)]
        with self.assertRaises(Exception):
            self.hand.lay_down(Deck(), cards)

    def test_layDown_notThere(self):
        self.hand = Hand(Deck(True))
        cards = [Card("Hearts", 2), Card("Hearts", 3)]
        with self.assertRaises(ValueError):
            self.hand.lay_down(Deck(), cards)

    def test_insertCard(self):
        self.hand = Hand()
        card = Card("Hearts", 3)
        deck = [Card("Hearts", 3)]
        self.hand.insert_card(deck, card)
        self.assertTrue(self.hand.__contains__(card))

    def test_insertCard_length(self):
        self.hand = Hand(Deck(True))
        card = Card("Hearts", 3)
        deck = [Card("Hearts", 3)]
        self.hand.insert_card(deck, card)
        self.assertEqual(len(self.hand), 8, "Insert card did not update the length of the hand")

    def test_insertCard_exception(self):
        self.hand = Hand()
        deck = Deck()
        with self.assertRaises(Exception):
            self.hand.insert_card(deck, Card("Hearts", 3))

    def test_insertCards(self):
        self.hand = Hand()
        cards = [Card("Hearts", 2), Card("Hearts", 3), Card("Hearts", 4)]
        deck = [Card("Hearts", 2), Card("Hearts", 3), Card("Hearts", 4)]
        self.hand.insert_cards(deck, cards)
        self.assertTrue(self.hand.__contains__(Card("Hearts", 2)))
        self.assertTrue(self.hand.__contains__(Card("Hearts", 3)))
        self.assertTrue(self.hand.__contains__(Card("Hearts", 4)))

    def test_insertCards_length(self):
        self.hand = Hand()
        cards = [Card("Hearts", 2), Card("Hearts", 3), Card("Hearts", 4)]
        deck = [Card("Hearts", 2), Card("Hearts", 3), Card("Hearts", 4)]
        self.hand.insert_cards(deck, cards)
        self.assertEqual(len(self.hand), 3, "Insert cards did not update the size of the hand "
                                            "by the appropiate amount")

    def test_insertCards_exception(self):
        self.hand = Hand()
        cards = [Card("Hearts", 2), Card("Hearts", 3), Card("Hearts", 4)]
        with self.assertRaises(Exception):
            self.hand.insert_cards(Deck(), cards)


if __name__ == '__main__':
    unittest.main()
