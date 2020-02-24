import random

suite = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
          'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}


class Deck:
    '''
    creates the 52 card deck object
    '''

    def __init__(self):
        self.deck = []
        self.create_deck()
        random.shuffle(self.deck)

    def create_deck(self):
        for s in suite:
            for r in ranks:
                self.deck.append((r, s))

    def s_deck(self):
        print(self.deck)


class Hand:

    def __init__(self):
        self.num = 0
        self.c_h = []
        self.show_cards = []
        self.total = []

    '''
    display cards in hand
    '''

    def show_hand(self):
        print(self.show_cards)
        print(sum(self.total))

        '''
        grabs the first card on the deck and removes it from deck
        '''
        #           hard coded in the deck.. not the best way

    def grab_card(self, n=1):
        i = 0
        n = n
        while i < n:
            self.c_h.append(deck.deck[0])
            self.show_cards.append(f"{self.c_h[self.num][0]} of {self.c_h[self.num][1]}")
            self.sum_hand()
            remove_card()
            i += 1
            self.num += 1
        '''
            gets the value of cards and sums it
        '''

    def sum_hand(self):
        self.total.append(values[self.c_h[self.num][0]])


def remove_card():
    deck.deck.pop(0)


deck = Deck()


class Player(Hand):
    '''
    create a player object that can,
    place bets,
    hit: ask for another card or pass,
    works with the Hand object?
    '''

    def __init__(self, name, money=0):
        super().__init__()
        self.name = name
        self.money = money
        self.bet_amt = 500
        # Hand.grab_card(self, n=2)

    def bet(self):
        self.bet_amt = int(input('bet amt?'))
        print(f' you bet: ${self.bet_amt}')

    def hit_pass(self):
        hit = True
        while hit:
            if input('hit or pass') == 'hit':
                print(self.name)
                Hand.grab_card(self)
                Hand.show_hand(self)
                if self.check_bust():
                    print('BUST')
                    hit = False
            else:
                print('PASSED!!')
                hit = False

    def check_bust(self):

        if sum(self.total) > 21:
            return True
        elif sum(self.total) == 21:
            print('BLACKJACK')

    def intro(self):
        print(self.name)
        Hand.grab_card(self, n=2)
        Hand.show_hand(self)

    def reset_hand(self):
        self.c_h = []
        self.show_cards = []
        self.total = []
        self.num = 0


class Dealer(Hand):
    '''
    create Dealer object
    show only 1 card
    inherit from Hand class
    must hit if sum for card less then 14
    '''

    def __init__(self, name='Dealer'):
        super().__init__()
        self.name = name
        Hand.grab_card(self, n=2)

    def hit_pass(self):
        while sum(self.total) <= 14:
            Hand.grab_card(self)
        if sum(self.total) > 21:
            print(self.name)
            print('BUST!')
            Hand.show_hand(self)
        elif sum(self.total) == 21:
            print(self.name)
            print('BLACKJACK')
            Hand.show_hand(self)
        else:
            print(self.name)
            Hand.show_hand(self)

    def intro(self):
        print(self.name)
        print(f'{self.show_cards[0]}, HIDDEN')


'''
create a Game object that sets up the blackjack game
num of players?
checks for winner?
'''


def check_winner(a, b):
    if sum(a.total) > 21:
        print(f'{b.name}, IS THE WINNER')
    elif sum(b.total) > 21:
        print(f'{a.name}, IS THE WINNER')
    elif sum(a.total) == sum(b.total):
        print('TIED GAME')
    elif sum(a.total) > sum(b.total):
        print(f'{a.name}, IS THE WINNER')
    else:
        print(f'{b.name}, IS THE WINNER')


def game():
    start_game = True
    player = Player(input('name?'))
    dealer = Dealer()
    while start_game:
        player.reset_hand()
        if input('(y)es to start game else (n)o') == 'y':
            dealer.intro()
            player.intro()
            player.hit_pass()
            dealer.hit_pass()
            check_winner(player, dealer)
        else:
            start_game = False


game()


