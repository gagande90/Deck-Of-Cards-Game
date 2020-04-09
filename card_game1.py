import random
from pprint import pprint

suits = ['Clubs', 'Spades', 'Hearts', 'Diamonds']

deck = [ (suit, rank) for suit in suits for rank in range(1, 14) ]      # list comprehension

pprint(deck)

random.shuffle(deck)

print()
print()
print()
print("Lets's shuffle the cards")
pprint(deck)

card = deck.pop()
print()
print()
print('card drawn from top of deck is: ', card)

random_card = deck.pop(random.randint(0, len(deck) -1))
print()
print()
print('random card drawn is: ', random_card)





