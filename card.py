import collections

class card:
    # Initializes a card and checks for intial value errors. A card without the suit or number is
    # a useless. 
    def __init__(self, suit, number):
        if suit.lower() != "spades" and suit.lower() != "hearts" and suit.lower() != "clubs" \
            and suit.lower() != "diamonds": 
            raise ValueError('Enter a valid suit')
        elif number > 13 or number < 2:
            raise ValueError('Enter a valid number')
        else:
            self.suit = suit
            self.number = number

    def get_card(self):
        return collections.namedtuple('Card', [self.suit, self.number])

    def get_suit(self):
        return self.suit

    def get_number(self):
        return self.number

    
        
