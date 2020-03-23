# inherits from game class
# this is because we need the players to access methods such as the score
class Player(Game):
    # initialize hand with games deck
    def __init__(self, game):
        print("I compile")

    # lay down, should just call players hand easily
    # put down a full set, or add to a set that is already laid down
    def lay_down(self):
        print("I compile")

    # decides whether to go out
    def go_out(self):
        print("I compile")

    # put down one card to discard pile
    def discard(self):
        print("I compile")

    # pickup from deck
    def pick_up(self):
        print("I compile")

    # pickup from discard deck
    def pick_up_discards(self):
        print("I compile")

    # prints hand
    def __str__(self):
        print("I compile")

    # shows sets all players have laid down
    def show_laydown(self):
        print("I compile")

