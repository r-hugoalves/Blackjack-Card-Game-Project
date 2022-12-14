import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank['rank'] + ' of ' + self.suit
        # we can also write:
        # return f"{self.rank['rank']} of {self.suit}"

#card1 = Card('hearts', {'rank': 'A', 'value': 1})
# print(card1)


class Deck:

    def __init__(self):
        # 1) Creating the deck

        suits = ['hearts', 'spades', 'clubs', 'diamonds']
        # for suit in suits:
        #   print(suit)

        ranks = [
            {'rank': 'A', 'value': 1},
            {'rank': '2', 'value': 2},
            {'rank': '3', 'value': 3},
            {'rank': '4', 'value': 4},
            {'rank': '5', 'value': 5},
            {'rank': '6', 'value': 6},
            {'rank': '7', 'value': 7},
            {'rank': '8', 'value': 8},
            {'rank': '9', 'value': 9},
            {'rank': '10', 'value': 10},
            {'rank': 'J', 'value': 10},
            {'rank': 'Q', 'value': 10},
            {'rank': 'K', 'value': 10},
        ]
        # for rank in ranks:
        #    print(rank)

        self.cards = []

        # 2) Before we start the game, we need to assign each suit to a specific rank, and that will be our card

        for suit in suits:
            for rank in ranks:
                # print([suit, rank]) #
                self.cards.append(Card(suit, rank))

    # 3) Shuffle the cards
    def shuffle(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)

        return self.cards

    # 4) Choose a card from the deck
    def choose(self, number):
        cards_chosen = []

        for x in range(number):
            if len(self.cards) > 0:
                card = self.cards.pop()
                cards_chosen.append(card)

        return cards_chosen

    # 5) Now we get just one card (or as many cards as we want)

    # shuffle()

    #print('Getting more than one\n')
    #cards_chosen = choose(2)
    # print(cards_chosen)

    #print('\n Getting just the first one \n')
    #cards_chosen = choose(2)[0]
    # print(cards_chosen)
    # print(cards_chosen[1]['value'])

# TESTING THE CLASS DECK #

#deck1 = Deck()
#print('\nTesting deck')
# print(deck1.cards)

#deck2 = Deck()
# deck2.shuffle
#print('\nTesting deck')
# print(deck2.cards)


class Hand:
    def __init__(self, dealer=False):
        self.cards = []
        self.value = 0
        self.dealer = dealer

    def add_card(self, card_list):
        self.cards.extend(card_list)

    def calculate_value(self):
        self.value = 0
        has_ace = False

        for card in self.cards:
            card_value = int(card.rank['value'])
            self.value += card_value
            if card.rank['rank'] == 'A':
                has_ace = True

        if has_ace and self.value > 21:
            self.value -= 10

    def get_value(self):
        self.calculate_value()
        return self.value

    def is_blackjack(self):
        return self.get_value() == 21

    def display(self, show_all_dealer_cards=False):
        print(f'''{"Dealer's" if self.dealer else "Your"} hand: ''')
        for index, card in enumerate(self.cards):
            if index == 0 and self.dealer and not show_all_dealer_cards and not self.is_blackjack():
                print('Hidden')
            else:
                print(card)

        if not self.dealer:
            print(f'Value: {self.get_value()}')

# TESTING THE CLASS HAND #

#deck = Deck()
# deck.shuffle

#hand = Hand()
# hand.add_card(deck.choose(2))
#print(f'{hand.cards[0]} and,\n{hand.cards[1]}')

# hand.display()


class Game:
    def play(self):
        game_number = 0
        games_to_play = 0

        while games_to_play <= 0:
            try:
                games_to_play = int(input('How many games do you want to play?'))
            except:
                print('You must enter a number!')

        while game_number < games_to_play:
            game_number += 1

            deck = Deck()
            deck.shuffle()

            player_hand = Hand()
            dealer_hand = Hand(dealer=True)

            for i in range(2):
                player_hand.add_card(deck.choose(1))
                dealer_hand.add_card(deck.choose(1))

            print()
            print('*' * 30)
            print(f'Game number: {game_number} of {games_to_play}')
            print('*' * 30)
            player_hand.display()
            dealer_hand.display()

            if self.check_winner(player_hand, dealer_hand):
                continue

            choice = ''
            while player_hand.get_value() < 21 and choice not in ['s', 'stand']:
                choice = input("Please, choose 'Hit' or 'Stand: ").lower()
                print()
                while choice not in ['s', 'stand', 'h', 'hit']:
                    choice = input("Please, choose 'Hit' or 'Stand' (or 'H/S') ").lower()
                    print()
                if choice in ['h', 'hit']:
                    player_hand.add_card(deck.choose(1))
                    player_hand.display()

            if self.check_winner(player_hand, dealer_hand):
                continue

            player_hand_value = player_hand.get_value()
            dealer_hand_value = dealer_hand.get_value()

            while dealer_hand_value < 17:
                dealer_hand.add_card(deck.choose(1))
                dealer_hand_value = dealer_hand.get_value()
            
            dealer_hand.display(show_all_dealer_cards=True)

            if self.check_winner(player_hand, dealer_hand):
                continue

            print('Final Results: ')
            print(f'Your hand: {player_hand_value}')
            print(f"Dealer's hand: {dealer_hand_value}")

            self.check_winner(player_hand, dealer_hand, True)

        print('Thanks for playing :)')

    def check_winner(self, player_hand, dealer_hand, game_over=False):
        if not game_over:
            if player_hand.get_value() > 21:
                print('You busted! Dealer wins!')
                return True
            elif dealer_hand.get_value() > 21:
                print('Dealer busted! You win!')
                return True
            elif player_hand.is_blackjack() and dealer_hand.is_blackjack():
                print('Both hands are blackjack! It is a tie!')
                return True
            elif player_hand.is_blackjack():
                print('You got a blackjack! You win!')
                return True
            elif dealer_hand.is_blackjack():
                print('Dealer got a blackjack! You lost!')
                return True
            else:
                if player_hand.get_value() > dealer_hand.get_value():
                    print('You win!')
                elif player_hand.get_value() == dealer_hand.get_value():
                    print('It is a tie!')
                else:
                    print('Dealer wins!')
                return True
                
        return False


new_game = Game()
new_game.play()
