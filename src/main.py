from src.hand import *

card = Card("Clubs", 9)
card2 = Card("Spades", 9)
card3 = Card("Hearts", 9)
cards = [card, card2, card3]
deck = Deck(True)
hand = Hand(deck)
for i in range(0, 45):
    hand.draw_card(deck)

empty_deck = Deck()
hand.lay_down(empty_deck, cards)
print(hand)

