# Currently added compile lines so that my test file would run
# Obviously when you implemnent these, it will delete them

class Deck:
    # builds inital deck of cards thats empty if no second param is passed. Otherwise construct full
    # deck.
    def __init__(self, initialize = None):
        print("compile line")

    # returns the length of the deck
    def __length__(self):
        print("compile line")

    # Prints the deck in a clean way
    def __str__(self):
        print("compile line")

    # Checks if the deck contains a card
    def __contains__(self, card):
        print("compile line")

    # Inserts a card into the deck
    def insert(self, card):
        print("compile line")

    # Deletes a card from the deck
    def delete(self, card):
        print("compile line")

    # Draws a card from the deck
    def draw_card(self):
        print("compile line")

    # Returns the array containing the deck
    def return_deck(self):
        print("compile line")

    # Returns an array with all cards passed a certain card. Mimics picking up at a number 
    def pickup_cards(self, card):
        print("compile line")

    # Returns if a deck is empty
    def is_empty(self):
        print("compile line")








