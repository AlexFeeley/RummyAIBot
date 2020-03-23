from src.game import Game


# inherits from game class
# this is because we need the players to access methods such as the score
class Player(Game):
    # initialize hand with games deck
    # should we make local variables from the constructor s.t each player
    # has access to game deck, discard deck, and max points
    def __init__(self, game_deck):
        print("I compile")

    # lay down, should just call players hand easily
    # put down a full set, or add to a set that is already laid down
    def lay_down(self):
        print("I compile")

    # decides whether to go out
    # According to Wiki, when you go out you're supposed to say rummy
    def rummy(self):
        print("I compile")

    # put down one card to discard pile
    def discard(self, discard_deck):
        print("I compile")

    # pickup from deck
    def pick_up(self, game_deck):
        print("I compile")

    # pickup from discard deck
    def pick_up_discards(self, discard_deck):
        print("I compile")

    # prints hand
    def __str__(self):
        print("I compile")

    # shows sets all players have laid down
    def show_laydown(self):
        print("I compile")

    # Calculate score of cards
    # + points for cards laid down, - points for cards in hand
    def get_score(self):
        print("I compile")