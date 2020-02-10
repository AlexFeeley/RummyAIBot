from src.hand import *

card = Card("Spades", 13)

# Why does this print none after listing the card?
print(card.__str__(),"\n")

# Why is there one none after printing all the cards despite it using the card classes' string?
# deck = Deck(True)
# print(deck.__str__())

hand = Hand(Deck(True))
print(hand.__str__())