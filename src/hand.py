from src.deck import *
from src.card import Card.get_suit

class Hand:

    # Constructor shuffles deck and draws original 7 cards for each player
    def __init__(self, deck = None):
        self.hand = Deck()
        if deck is not None:
            for i in range(6):
                self.hand.insert(deck.draw_card())

    # Helper method, draws 7 cards from the deck
    def _startcards_(self, deck):
        for i in range(6):
            self.hand.insert(deck.draw_card())

    # Returns the number of cards in a hand
    def __len__(self):
        return len(self.hand)

    # Prints cards in hand
    def __str__(self):
        print(self.hand)

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

    # Checks if cards are in hand
    def __contains__(self, card):
        return card in self.hand

    # Verify set helper method
    def _verify_set(self, cards):
        suit = cards[i].get_suit()
        number = cards[i].get_number()
        for card in cards:
            if not card in self:
                raise ValueError("Card not in hand")
            else:
                if card.get_suit() != suit:
                    if card.get_number != number:
                        raise ValueError("Cards are not a valid set")
                    else:
                        return True

