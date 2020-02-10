import collections

class Card:
    # Initializes a card and checks for intial value errors. A card without the suit or number is
    # a useless. 
    def __init__(self, suit, number):
        if suit.lower() != "spades" and suit.lower() != "hearts" and suit.lower() != "clubs" \
            and suit.lower() != "diamonds": 
            raise ValueError('Enter a valid suit')
        elif number > 14 or number < 2:
            raise ValueError('Enter a valid number')
        else:
            self.suit = suit
            self.number = number

    def get_card(self):
        # Why do we use a named tuple here?
        return collections.namedtuple('Card', [self.suit, self.number])

    def get_suit(self):
        return self.suit

    def get_number(self):
        return self.number

    # Checks if two cards are equal
    def __eq__(self, other):
        if self.suit == other.suit and self.number == other.number:
            return True
        return False

    def __str__(self):
        if self.number == 11:
            return("Jack of {}".format(self.suit))
        elif self.number == 12:
            return("Queen of {}".format(self.suit))
        elif self.number == 13:
            return("King of {}".format(self.suit))
        elif self.number == 14:
            return("Ace of {}".format(self.suit))
        else:
            return("{0} of {1}".format(self.number, self.suit))
