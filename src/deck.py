# Currently added compile lines so that my test file would run
# Obviously when you implemnent these, it will delete them

from src.card import *


class Deck:
    # builds inital deck of cards thats empty if no second param is passed. Otherwise construct full
    # deck.
    def __init__(self, initialize=None):
        if initialize is None:
            self.cards = []
        else:
            self.cards = []
            for s in ["Hearts", "Diamonds", "Spades", "Clubs"]:
                for v in ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]:
                    self.cards.append(Card(s, v))

            # Used to keep count of the number of cards in the deck
            global number_cards
            number_cards = 52

    # Returns the number of cards in the deck
    def __length__(self):
        return self.number_cards

    # Prints the deck in a clean way
    def __str__(self):
        for c in self.cards:
            c.__str__()

    # Checks if the deck contains a card
    def __contains__(self, card):
        print("compile line")

    # Inserts a card into the deck
    def insert(self, card):
        print("compile line")
        number_cards += 1

    # Deletes a card from the deck
    def delete(self, card):
        print("compile line")
        number_cards -= 1

    # Draws a card from the deck
    def draw_card(self):
        print("compile line")
        number_cards -= 1

    # Returns the array containing the deck
    def return_deck(self):
        print("compile line")

    # Returns an array with all cards passed a certain card. Mimics picking up at a number 
    def pickup_cards(self, card):
        print("compile line")

    # Returns true if a deck is empty
    def is_empty(self):
        if number_cards == 0:
            return True
        else:
            return False
