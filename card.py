class card:
    def __init__(self, suit = None, number = None):
        if suit is None and number is None:
            self.suit = ""
            self.number = 0;
        else:
            if suit.lower() != "spades" and suit.lower() != "hearts" and suit.lower() != "clubs" \
                and suit.lower() != "diamonds": 
                raise ValueError('Enter a valid suit')
            elif number > 13 or number < 2:
                raise ValueError('Enter a valid number')
            else:
                self.suit = suit
                self.number = number

    def get_card(self):


    def get_suit(self):

    def get_number(self):

    
        
