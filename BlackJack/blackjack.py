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
    def __init__(self, hand=[], points= 0):
        self.hand = hand
        self.points = points

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
        deck.deck.pop(0)
        newcard = deck.deck[0]
        self.calculate_points(newcard)
        self.hand.append(newcard)
        deck.deck.pop(0)
    
    def hit(self):
        newcard = deck.deck[0]
        self.calculate_points(newcard)
        self.hand.append(newcard)
        deck.deck.pop(0)
        print('Your new card is', newcard, 'Your new score is', player.points)

class Dealer(Player):
    def __init__(self, dealer_hand= [], hand=[], points= 0, ):
        super().__init__(hand=[], points= 0)
        self.dealer_hand = dealer_hand

    def drawdealerhand(self):
        newcard = deck.deck[0]
        self.calculate_points(newcard)
        self.dealer_hand.append(newcard)
        deck.deck.pop(0)
        newcard = deck.deck[0]
        self.calculate_points(newcard)
        self.dealer_hand.append(newcard)
        deck.deck.pop(0)

    def dealerhit(self):
        newcard = deck.deck[0]
        self.calculate_points(newcard)
        self.dealer_hand.append(newcard)
        deck.deck.pop(0)

deck = Deck()
deck.shuffle()
dealer = Dealer()
player = Player()

def main():
    hitphase = False
    global dealerphase
    dealerphase = False

    while True:
        dealer.drawdealerhand()
        player.draw_hand()
        print(dealer.dealer_hand, 'Dealer points: ', dealer.points)
        print(player.hand, 'Your points: ', player.points)
        if player.points == 21:
            print('You win!')
            player.hand = []
            dealer.dealer_hand = []
            player.points = 0
            dealer.points = 0
        elif dealer.points == 21:
            player.hand = []
            dealer.dealer_hand = []
            player.points = 0
            dealer.points = 0
            print('Dealer wins!')
        else:
            hitphase = True

        while hitphase == True:
            player.hit()
            print(dealer.dealer_hand, 'Dealer points: ', dealer.points)
            print(player.hand, 'Your points ', player.points)

            hors = input('Would you like to hit or stand? (H/S)')
            if hors == 'H':
                player.hit()
            elif hors == 'S':
                pass
            else:
                print('Syntax error: improper input.  Use H or S for input.')

            if player.points == 21:
                print('You win!')
                player.hand = []
                dealer.dealer_hand = []
                player.points = 0
                dealer.points = 0
                hitphase = False
            elif player.points > 21:
                print('Bust!  You lose!')
                player.hand = []
                dealer.dealer_hand = []
                player.points = 0
                dealer.points = 0
                hitphase = False
            
        
        print('Dealers turn!')
            

if __name__ == "__main__":
    main()