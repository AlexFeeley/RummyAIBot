from src.deck import *


class Hand:

    # Constructor shuffles deck and draws original 7 cards for each player
    def __init__(self, deck = None):
        self.hand = Deck()
        self.points = 0  # Records number of points laid down
        if deck is not None:
            deck.shuffle_deck()
            self.__startcards_(deck)

    # Helper method, draws 7 cards from the deck
    def __startcards_(self, deck):
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
        return str(self.hand)

    # Draws one card from the deck, adding one card to your hand
    def draw_card(self, deck):
        self.hand.insert(deck.draw_card())

    # Puts down one card to pile
    def put_down(self, deck, card):
        if card in self.hand:
            self.hand.delete(card)
            deck.insert(card)
        else:
            raise ValueError("Card not in hand")

    # Checks if cards are in hand
    def __contains__(self, card):
        return card in self.hand

    # Verify set helper method
    def verify_set(self, cards):
        suit = cards[0].get_suit()
        number = cards[0].get_number()
        if self.same_number(cards):
            return True
        elif self.consecutive(cards) and self.same_suit(cards):
            return True
        else:
            return False

    # Helper method if three cards are of consecutive numbers
    # Doesn't allow for use of ace as a low card
    def consecutive(self, cards):
        integers = []
        for card in cards:
            integers.append(card.get_number())
        return sorted(integers) == list(range(min(integers), max(integers)+1))

    # Helper method to check if all cards have the same number
    def same_number(self, cards):
        return all(card == cards[0] for card in cards)

    # Helper method to check if all cards are of the same suit
    def same_suit(self, cards):
        return all(card.get_suit() == cards[0].get_suit() for card in cards)

    # Lays down more than one card to pile if possible
    def lay_down(self, deck, cards):
        if self.verify_set(cards):
            for card in cards:
                if card not in self:
                    raise ValueError("Cards are not in hand")
                deck.insert(card)
                self.hand.delete(card)
                self.points += card.return_points()
        else:
            raise Exception("You cannot lay down cards that are not a set")

    # Returns number of points that have been laid down
    def points_down(self):
        return self.points

    # Returns number of points in hand
    # How do you do this :(
    def points_hand(self, cards):
        points = 0
        for i in range(len(cards)):
            card = self.hand.__contains__(cards[i])
            points += card.return_points()
        return points

    # Inserts one specific card into hand
    def insert_card(self, deck, card):
        if card in deck:
            self.hand.insert(card)
        else:
            raise Exception("Cannot insert card into hand that is not in pile")

    # Inserts more than one card into hand
    def insert_cards(self, deck, cards):
        allin = True
        for card in cards:
            if card not in deck:
                allin = False
        if allin:
            for card in cards:
                self.hand.insert(card)
        else:
            raise Exception("Cannot insert cards into hand that are not in pile")
