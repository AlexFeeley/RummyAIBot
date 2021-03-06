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

    # Accessor method for suit
    def get_suit(self):
        return self.suit

    # Accessor method for number of card (11-14 are face cards)
    def get_number(self):
        return self.number

    # Checks if two cards are equal
    def __eq__(self, other):
        return self.suit == other.suit and self.number == other.number

    # Returns instance of one card: Card(suit, number)
    def get_card(self):
        return collections.namedtuple('Card', [self.suit, self.number])

    def __str__(self):
        if self.number == 11:
            return "Jack of {}".format(self.suit)
        elif self.number == 12:
            return "Queen of {}".format(self.suit)
        elif self.number == 13:
            return "King of {}".format(self.suit)
        elif self.number == 14:
            return "Ace of {}".format(self.suit)
        else:
            return "{0} of {1}".format(self.number, self.suit)

    # returns the number of points a card is worth. Return an ace as 15 but we need to solve the 1
    # later
    def return_points(self):
        if self.number == 11 or self.number == 12 or self.number == 13:
            return 10
        elif self.number == 14:
            return 15
        else:
            return self.number
