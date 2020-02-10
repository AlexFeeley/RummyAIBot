from src.hand import *

card = Card("Spades", 9)

# Why does this print none after listing the card?
print(card)
# Why is there one none after printing all the cards despite it using the card classes' string?
#deck = Deck(True)
#print(deck)

hand = Hand(Deck(True))
print(hand)

