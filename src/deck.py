from src.card import *

class Deck:
    # Builds inital deck of cards that's empty if no parameter is passed. Otherwise constructs full
    # deck.
    def __init__(self, initialize = None, number_cards = 0):
        if initialize is None:
            # Initialize an empty deck with 0 cards
            self.cards = []
            self.number_cards = 0
        else:
            # Initialize a full deck with 52 cards
            self.cards = []
            for s in ["Hearts", "Diamonds", "Spades", "Clubs"]:
                for v in range(2, 15):
                    self.cards.append(Card(s, v))
            self.number_cards = 52

    # Returns the number of cards in the deck
    def __len__(self):
        return self.number_cards

    # Prints the deck in a clean way
    def __str__(self):
        for c in self.cards:
            c.__str__()

    # Checks if the deck contains a card
    def __contains__(self, card):
        for c in self.cards:
            if c == card:
                return True
        return False

    # Inserts a card into the deck
    def insert(self, card):
        self.cards.append(card)
        self.number_cards += 1

    # Deletes a card from the deck
    def delete(self, card):
        if self.__contains__(card):
            self.cards.remove(card)
            self.number_cards -= 1
        else:
            print("Card to be deleted was not found in deck")

    # Deck shuffle command??

    # Draws a card from the deck
    def draw_card(self):
        if self.number_cards != 0:
            card = self.cards[self.number_cards - 1]    # Draws from top of deck
            self.cards.remove(card)
            self.number_cards -= 1
            return card
        else:
            print("Cannot draw a card from an empty deck")

    # Returns the array containing the deck
    def return_deck(self):
        return self.cards

    # Returns an array with all cards passed a certain card. Mimics picking up at a number?
    def pickup_cards(self, card):
        print("compile line")

    # Returns true if a deck is empty
    def is_empty(self):
        if self.number_cards == 0:
            return True
        else:
            return False
