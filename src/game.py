from src.hand import *

class Game:
    # init game with deck, discard deck, and player count
    def __init__(self, player_count, game_points):
        game_deck = Deck(True)
        discard_deck = Deck()
        number_players = player_count
        max_points = game_points

        hands = []

        for i in range(0, player_count):
            hands.append(Hand(game_deck))

    # resets the deck
    def reset(self, number_players, hands):
        game_deck = Deck(True)
        discard_deck = Deck()

        hands = []
        for i in range(0, number_players):
            hands.append(Hand(game_deck))

    # returns a tuple of player scores
    # from greatest to least
    def get_score(self):
        print("I compile")

    # Check if a player has reached MAX_POINTS
    # If multiple players reach this, whoever has most points wins
    def check_win(self):
        print("I compile")

    # Uses check win to see if a player has won, and returns the player that has won
    def end_game(self):
        print("I compile")

    # When the deck is empty or someone goes out, use add_score
    # to add points to every player
    def end_round(self):
        print("I compile")

    # If MAX_POINTS is not reached and 'round' not over, start a new round
    # Probably a helper method eventually once we have the game just loop until it's done
    def start_round(self):
        print("I compile")

    # Prints all cards that have been put down by each player
    def __str__(self):
        print("I compile")

    # Shows discard pile
    def show_discard(self):
        print("I compile")