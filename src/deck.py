from src.card import *
import random

class Deck:
    # Builds inital deck of cards that's empty if no parameter is passed. Otherwise constructs full
    # deck.
    def __init__(self, initialize = None, number_cards = 0):
        if initialize is None:
            # Initialize an empty deck with 0 cards
            self.deck = []
            self.number_cards = 0
        else:
            # Initialize a full deck with 52 cards
            self.deck = []
            for s in ["Hearts", "Diamonds", "Spades", "Clubs"]:
                for v in range(2, 15):
                    self.deck.append(Card(s, v))
            self.number_cards = 52

    # Returns the number of cards in the deck
    def __len__(self):
        return self.number_cards

    # Prints the deck in a clean way
    def __str__(self):
        s = ""
        for c in self.deck:
            s += "{}\n".format(str(c))
        return s[:-2]
            

    # Checks if the deck contains a card
    def __contains__(self, card):
        return card in self.deck

    # Inserts a card into the deck
    def insert(self, card):
        if self.number_cards < 52:
            self.deck.append(card)
            self.number_cards += 1
        else:
            raise Exception('Cannot insert a card into a full deck')

    # Deletes a card from the deck
    def delete(self, card):
        if self.number_cards > 0 and self.deck.__contains__(card):
            self.deck.remove(card)
            self.number_cards -= 1
        else:
            raise Exception('Cannot delete a card from an empty deck')

    # Draws a card from the deck
    def draw_card(self):
        if self.number_cards > 0:
            card = self.deck[self.number_cards - 1]    # Draws from top of deck
            self.deck.remove(card)
            self.number_cards -= 1
            return card
        else:
            raise Exception('Cannot draw a card from an empty deck')

    # Returns the array containing the deck
    def return_deck(self):
        return self.deck

    # Returns an array with all cards past a certain card, mimicing picking up from a certain card
    def pickup_cards(self, card):
        temp = self.deck.index(card)
        self.number_cards = temp
        self.deck = self.deck[0:temp]
        return self.deck[temp:len(self.deck)]

    # Returns true if a deck is empty
    def is_empty(self):
        if self.number_cards == 0:
            return True
        else:
            return False

    # Shuffle deck
    def shuffle_deck(self):
        return random.shuffle(self.deck)
