from src.hand import *
from src.deck import *

class Game:
    # init game with deck, discard deck, and player count
    def __init__(self, player_count):
        self.deck = Deck(True)
        self.discard = Deck()
        self.players = [] # Empty list to hold players hands
        for i in range(0, player_count):
            self.players.append(Hand(self.deck))

    # Resets the decks, allows another round to be player
    def reset(self, player_count):
        self.deck = Deck(True)
        self.discard = Deck()
        self.players = []
        for i in range(0, player_count):
            self.players.append(Hand(self.deck))

    # Adds score for a player
    def add_score(self, player):
        return self.players[player].points_down() - self.players[player].points_hand()

    # returns a tuple of player scores
    # from greatest to least
    def get_score(self):
        print("I compile")

    # check if a player has won
    # this may turn into a helper method
    def check_win(self):
        print("I compile")

    # declare a winner and end game
    def end_game(self):
        print("I compile")


