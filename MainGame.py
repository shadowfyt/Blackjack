from blackjackmodule import random,Deck,Player,Hand,Dealer

suite = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}



def game():
    start_game = True
    player = Player(input('name?'))
    dealer = Dealer()
    while start_game == True:
        if input('(y)es to start game else (n)o')== 'y':
            hit = True
            dealer.intro()
            player.intro()
            while hit == True:
                if hit == True: 
                    player.hit_pass()
                else:
                    hit = False
            dealer.hit_pass()
        else:
            start_game = False

game()


        

