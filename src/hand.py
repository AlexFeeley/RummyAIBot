class Hand:

    # Constructor shuffles deck and draws original 7 cards for each player
    def __init__(self, deck = None):

    # Helper method, draws 7 cards from the deck
    def _startcards_(self, deck):

    # Returns the number of cards in a hand
    def __len__(self):

    # Prints cards in hand
    def __str__(self):

    # Draws one card from the deck
    def draw_card(self, deck):

    # Puts down one card to deck
    def put_down(self, deck):

    # Checks if cards are valid to put down
    def _valid_set_(self):

    # Lays down cards
    def laydown(self):
