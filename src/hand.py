from src.deck import *
from src.card import *

class Hand:

    # Constructor shuffles deck and draws original 7 cards for each player
    def __init__(self, deck = None):
        self.hand = Deck()
        if deck is not None:
            self._startcards_(deck)

    # Helper method, draws 7 cards from the deck
    def _startcards_(self, deck):
        if len(deck) > 6:
            for i in range(7):
                self.hand.insert(deck.draw_card())
        else:
            raise Exception("Cannot draw a hand from a deck with less than 7 cards")

    # Returns the number of cards in a hand
    def __len__(self):
        return len(self.hand)

    # Prints cards in hand
    def __str__(self):
        return self.hand.__str__()

    # Draws one card from the deck
    def draw_card(self, deck):
        self.hand.insert(deck.draw_card())

    # Puts down one card to deck
    def put_down(self, deck, card):
        if card in self:
            self.hand.delete(card)
            deck.insert(card)
        else:
            raise ValueError("Card not in hand")

    # Lays down cards if possible
    def lay_down(self, deck, cards):
        if _verify_set(cards):
            for card in cards:
                if card not in self:
                    raise ValueError("Cards are not in hand")
            for card in cards:
                deck.insert(card)
                self.hand.delete(card)

    # Checks if cards are in hand
    def __contains__(self, card):
        return card in self.hand

    # Verify set helper method
    def _verify_set(self, cards):
        suit = cards[i].get_suit()
        number = cards[i].get_number()
        for card in cards:
            if card.get_suit() != suit:
                if card.get_number != number:
                    return False
                # elif _same_number(cards):
                #     return True
                # else _consecutive(cards):
                #     return True
        return False

    # # Helper method to identify if three numbers are consectuive. Additionally checks they do not
    # # loop
    # def _consectutive(self, cards):
    #     integers = []
    #     for card in cards:
    #         integers.append(card.get_number())
    #     if sorted(integers) == list(range(min(integers), max(integers)+1)):
    #         return True
    #     else:
    #         1 if x==13 else x for x in integers
    #         return sorted(integers) == list(range(min(integers), max(integers)_1))
    #
    # # helper method to check if all cards have the same number
    # def _same_number(cards):
    #     number = cards[1].get_number()
    #     for card in cards:
    #         if card.number() != number:
    #             return False
    #     return True

    # Insert specific card into hand

    # Insert array of cards into hand