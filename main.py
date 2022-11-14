import random

## 1) Creating the deck

suits = ['hearts', 'spades', 'clubs', 'diamonds']
#for suit in suits: 
#   print(suit)

ranks = [
        { 'rank': 'A', 'value': 1},
        { 'rank': '2', 'value': 2},
        { 'rank': '3', 'value': 3},
        { 'rank': '4', 'value': 4},
        { 'rank': '5', 'value': 5},
        { 'rank': '6', 'value': 6},
        { 'rank': '7', 'value': 7},
        { 'rank': '8', 'value': 8},
        { 'rank': '9', 'value': 9},
        { 'rank': '10', 'value': 10},
        { 'rank': 'J', 'value': 10},
        { 'rank': 'Q', 'value': 10},
        { 'rank': 'K', 'value': 10},
]
#for rank in ranks: 
#    print(rank)

cards = []

## 2) Before we star the game, we need to assign each suit to a specific rank, and that will be our card

for suit in suits: 
    for rank in ranks:
        # print([suit, rank]) #
        cards.append([suit, rank])

## 3) Shuffle the cards
def shuffle():
    random.shuffle(cards)
    return cards

##4) Choose a card from the deck
def choose(number):
    cards_chosen = []

    for x in range(number):
        card = cards.pop()
        cards_chosen.append(card)
 
    return cards_chosen

## 5) Now we get just one card (or as many cards as we want)

shuffle()
cards_chosen = choose(1)[0]
print(cards_chosen)
print(cards_chosen[1]['value'])

