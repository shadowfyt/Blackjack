import random


suite = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}


class Deck():
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
                self.deck.append((r,s))
                
    def s_deck(self):
        print(self.deck)
    
class Hand():
    num = 0
    
    def __init__(self,c_h =[]):
        self.c_h = c_h
        self.show_cards = []
        self.sum = []
        
    '''
    display cards in hand
    '''    
    def show_hand(self):
        print(self.show_cards)
        print(sum(self.sum))
            
        '''
        grabs the first card on the deck and removes it from deck
        '''  
        #           hard coded in the deck.. not the best way
    def grab_card(self,deck=deck,n = 1):
        i = 0
        
        while i < n:
            self.c_h.append(deck.deck[0])
            self.show_cards.append(f"{self.c_h[Hand.num][0]} of {self.c_h[Hand.num][1]}")
            deck.deck.pop(0)
            Hand.num += 1
            i  += 1
        
            self.sum_hand()
        '''
            gets the value of cards and sums it
        '''       
    def sum_hand(self):
        
        self.sum.append(values[self.c_h[Hand.num - 1][0]])
        
class Player(Hand):
    '''
    create a player object that can,
    place bets,
    hit: ask for another card or pass,
    works with the Hand object?
'''
    
    def __init__(self,name,money = 0):
        super().__init__()
        self.name = name
        self.money = money
        self.bet_amt = 0
        Hand.grab_card(self,n = 2,deck =deck)
        
    def bet(self):
        self.bet_amt = int(input('bet amt?'))
        print(f' you bet: ${self.bet_amt}')
    
    def hit_pass(self):
        hit = True
        while hit == True:
            if input('hit or pass') =='hit':
                print(self.name)
                Hand.grab_card(self,deck=deck)
                Hand.show_hand(self)
                self.check_bust()
            else:
                print('PASSED!!')
                hit = False
                
    def check_bust(self):
        
        if sum(self.sum) > 21:
            print('BUST!')
        elif sum(self.sum) == 21:
            print('BLACKJACK')
            
    def intro(self):
        print(self.name)
        Hand.show_hand(self)
        
class Dealer(Hand):
    '''
    create Dealer object
    show only 1 card
    inherit from Hand class
    must hit if sum for card less then 14
    '''  
    
    def __init__(self,name = 'Dealer'):
        super().__init__() 
        self.name = name
        Hand.grab_card(self,n =2,deck=deck)

        
    def hit_pass(self):
        while sum(self.sum) <= 14:
            Hand.grab_card(self,deck=deck)
        if sum(self.sum) > 21:
            print(self.name)
            print('BUST!')
            Hand.show_hand(self)
        elif sum(self.sum) == 21:
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


def check_winner(a,b):
    if sum(a.sum) > sum(b.sum):
        print(f'{a.name}, IS THE WINNER')
    else:
        print(f'{b.name}, IS THE WINNER')

deck = Deck()

def game():
    start_game = True
    player = Player(input('name?'))
    dealer = Dealer()
    while start_game == True:
        if input('(y)es to start game else (n)o')== 'y':
            dealer.intro()
            player.intro()
            player.hit_pass()
            dealer.hit_pass()
        else:
            start_game = False


game()
len(deck.deck)