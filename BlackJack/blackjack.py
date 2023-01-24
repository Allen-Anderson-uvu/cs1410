import random
import time

suits = ['Clubs', 'Spades', 'Hearts', 'Diamonds']
value = ['2','3', '4', '5', '6', '7', '8', '9', '10', 'A', 'K', 'Q', 'J']

class Card():
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        

class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for card in value:
                self.deck.append((card, suit))
    
    def shuffle(self):
        random.shuffle(self.deck)

class Player:
    def __init__(self, hand=[], points= 0, aces=0):
        self.hand = hand
        self.points = points
        self.aces = aces

    def calculate_points(self, newcard):
        if newcard[0] in ['1', '2', '3', '4', '5','6','7', '8', '9', '10']:
            self.points += int(newcard[0])
        elif newcard[0] in ['K', 'Q', 'J']:
            self.points += 10
        elif newcard[0] == 'A':
            self.points += 11


    def draw_hand(self):
        newcard = deck.deck[0]
        self.calculate_points(newcard)
        self.hand.append(newcard)

        if newcard[0] == 'A':
            self.aces += 1
        deck.deck.pop(0)

        newcard = deck.deck[0]
        self.calculate_points(newcard)
        self.hand.append(newcard)
        if newcard[0] == 'A':
            self.aces += 1
        deck.deck.pop(0)
    
    def hit(self):
        newcard = deck.deck[0]
        self.calculate_points(newcard)
        self.hand.append(newcard)
        if newcard[0] == 'A':
            self.aces += 1
        deck.deck.pop(0)
        print('Your new card is', newcard, 'Your new score is', player.points)

class Dealer(Player):
    def __init__(self, dealer_hand= [], hand=[], points= 0, hiddenscore= 0, hiddendealerhand = []):
        super().__init__(hand=[], points= 0, aces= 0)
        self.dealer_hand = dealer_hand
        self.hiddenscore = hiddenscore
        self.hiddendealerhand = hiddendealerhand

    def drawdealerhand(self):
        newcard = deck.deck[0]
        if newcard[0] == 'A':
            self.aces += 1      
        self.hiddendealerhand.append(newcard)
        self.hiddendealerhand.append('?')
        self.calculatehiddenpoints(newcard)
        self.calculate_points(newcard)
        self.dealer_hand.append(newcard)
        deck.deck.pop(0)
        newcard = deck.deck[0]
        if newcard[0] == 'A':
            self.aces += 1
        self.calculate_points(newcard)
        self.dealer_hand.append(newcard)
        deck.deck.pop(0)
    
    def calculatehiddenpoints(self, newcard):
        if newcard[0] in ['1', '2', '3', '4', '5','6','7', '8', '9', '10']:
            self.hiddenscore += int(newcard[0])
        elif newcard[0] in ['K', 'Q', 'J']:
            self.hiddenscore += 10
        elif newcard[0] == 'A':
            self.hiddenscore += 11

    def dealerhit(self):
        newcard = deck.deck[0]
        if newcard[0] == 'A':
            self.aces += 1
        self.calculate_points(newcard)
        self.dealer_hand.append(newcard)
        deck.deck.pop(0)
        print(newcard)

class Hand():
    def __init__(self, suit, number, mycard='', cardlist=''):
        self.suit = suit
        self.number = number
        self.mycard = mycard
        self.cardlist = cardlist
    
    def generate_card(self):

        if self.suit == 'Clubs':
            self.suit = '\u2667'
        elif self.suit == 'Hearts':
            self.suit = '\u2661'
        elif self.suit == 'Spades':
            self.suit = '\u2664'
        else:
            self.suit = '\u2662'

        self.mycard = f'''\
        .-------.
        |{self.number}      |
        |       |
        |   {self.suit}   |
        |       |
        |      {self.number}|
        `-------´
        '''.format(self.number, self.suit)


def splitcard(mytup):
    b = ''
    c = ''
    counter = 0
    for a in mytup:
        if counter == 0:
            b = a
            counter += 1
        else:
            c = a
        
    return c, b

def asciicards(a,b):
    spacing = ' ' * 5
    cards = a, b

    for pieces in zip(*(card.splitlines() for card in cards)):
        print(spacing.join(pieces))


deck = Deck()
deck.shuffle()
dealer = Dealer()
player = Player()

def main():
    hitphase = False
    acecount = 0

    while True:
        if len(deck.deck) < 4:
            print('Not enough cards to continue playing. Dealer will draw a new deck and shuffle it.')
            break
        dealer.drawdealerhand()
        player.draw_hand()
        a,b = player.hand[0],player.hand[1]
        suit, number = splitcard(a)
        myhand = Hand(suit, number)
        myhand.generate_card()
        card1 = myhand.mycard
        suit, number = splitcard(b)
        myhand1 = Hand(suit, number)
        myhand1.generate_card()
        card2 = myhand1.mycard
        print('Your hand: ')
        print('****************************************************')
        asciicards(card1,card2)
        print('Your points: ', player.points)
        print('****************************************************')
        a, b = dealer.dealer_hand[0], dealer.dealer_hand[1]
        suit, number = splitcard(a)
        dealerhand = Hand(suit, number)
        dealerhand.generate_card()
        suit, number = splitcard(b)
        dealerhand2 = Hand(suit, number)
        dealerhand2.generate_card()
        c = '''
        ?????????
        ?????????
        ?????????
        ?????????
        ?????????
        ?????????
        '''
        print('Dealer known cards:')
        print('****************************************************')
        asciicards(dealerhand.mycard, c)
        print('Known dealer points:', dealer.hiddenscore)

        if player.points == 21:
            print('Black Jack! You win!')
            player.hand = []
            dealer.dealer_hand = []
            player.points = 0
            dealer.points = 0
            dealer.hiddendealerhand = []
            dealer.hiddenscore=0
        elif dealer.points == 21:
            player.hand = []
            dealer.dealer_hand = []
            player.points = 0
            dealer.points = 0
            dealer.hiddendealerhand = []
            dealer.hiddenscore=0
            print('Black Jack! Dealer wins!')
            main()
        else:
            hitphase = True

        while hitphase == True:
            hors = input('Would you like to hit or stand? (H/S)')
            if hors == 'H':
                player.hit()
                newcard = player.hand[-1]
                print(newcard)
                suit, number = splitcard(newcard)
                print(suit, number)
                hitcard = Hand(suit, number)
                print(hitcard)
                newcard = hitcard.generate_card
                print(hitcard.mycard)

            elif hors == 'S':
                break
            else:
                print('Syntax error: improper input.  Use H or S for input.')

            

            if player.points > 21:
                if player.aces > 0:
                    player.points -= 10
                    player.aces -= 1

            if player.points == 21:
                print('You win!')
                player.hand = []
                dealer.dealer_hand = []
                player.points = 0
                dealer.points = 0
                dealer.hiddendealerhand = []
                dealer.hiddenscore=0
                dealer.hiddendealerhand = []
                dealer.hiddenscore=0
                hitphase = False
                main()
            elif player.points > 21:
                print('Bust!  You lose!')
                player.hand = []
                dealer.dealer_hand = []
                player.points = 0
                dealer.points = 0
                dealer.hiddendealerhand = []
                dealer.hiddenscore=0
                hitphase = False
                main()
            
        print("Dealer's turn")
        time.sleep(1)
        dealer.hiddendealerhand = []
        print('Dealers cards', dealer.dealer_hand, 'Dealer points', dealer.points)
        time.sleep(2)

        while dealer.points < 17:
            print('Dealer hits!')
            dealer.dealerhit()
            print(dealer.points)
            time.sleep(2)

        if dealer.points > 21:
            if dealer.aces > 0:
                dealer.points -= 10
                dealer.aces -= 1

        if dealer.points == 21:
            print('Dealer wins!')
            dealer.dealer_hand = []
            player.hand = []
            player.points = 0
            dealer.points = 0
            

        elif dealer.points > 21:
            print('Dealer busts!  You win!')
            dealer.dealer_hand = []
            player.hand = []
            player.points = 0
            dealer.points = 0
            dealer.hiddendealerhand = []
            dealer.hiddenscore=0
            
            
        elif dealer.points > player.points:
            print('Dealer wins!')
            dealer.dealer_hand = []
            player.hand = []
            player.points = 0
            dealer.points = 0
            dealer.hiddendealerhand = []
            dealer.hiddenscore=0
            
        elif player.points > dealer.points:
            print('Player wins!')
            player.hand = []
            dealer.dealer_hand = []
            player.points = 0
            dealer.points = 0
            dealer.hiddendealerhand = []
            dealer.hiddenscore=0
            
        elif player.points == dealer.points:
            print("It's a push!  No winner!")
            dealer.hiddendealerhand = []
            dealer.hiddenscore=0            
            dealer.dealer_hand = []
            player.hand = []
            player.points = 0
            dealer.points = 0

if __name__ == "__main__":
    main()