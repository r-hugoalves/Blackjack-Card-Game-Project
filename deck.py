import random

class Deck:

    def __init__(self):
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

        self.cards = []

        ## 2) Before we start the game, we need to assign each suit to a specific rank, and that will be our card

        for suit in suits: 
            for rank in ranks:
                # print([suit, rank]) #
                self.cards.append([suit, rank])

    ## 3) Shuffle the cards
    def shuffle(self):
        if len(self.cards > 1): 
            random.shuffle(self.cards)
        
        return self.cards

    ##4) Choose a card from the deck
    def choose(self, number):
        cards_chosen = []

        for x in range(number):
            if len(self.cards) > 0:
                card = self.cards.pop()
                cards_chosen.append(card)
    
        return cards_chosen

    ## 5) Now we get just one card (or as many cards as we want)

    #shuffle()

    #print('Getting more than one\n')
    #cards_chosen = choose(2)
    #print(cards_chosen)

    #print('\n Getting just the first one \n')
    #cards_chosen = choose(2)[0]
    #print(cards_chosen)
    #print(cards_chosen[1]['value'])

deck1 = Deck()
print('\nTesting deck')
print(deck1.cards)

deck2 = Deck()
deck2.shuffle
print('\nTesting deck')
print(deck2.cards)