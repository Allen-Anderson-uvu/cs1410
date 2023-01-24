import random
import time
import os

class Card:
    '''This sets the values that the Deck class is created from'''
    def __init__(self):
        self.values = ['2','3', '4', '5', '6', '7', '8', '9', '10', 'A', 'K', 'Q', 'J']
        self.suits = ['Clubs', 'Spades', 'Hearts', 'Diamonds']


class Deck:
    '''This creates the deck by instantiating a Card class'''
    def __init__(self):
        self.deck = []

        card = Card()
        for i in card.suits:
            for ii in card.values:
                self.deck.append([(ii, i)])
        random.shuffle(self.deck)


class Hand:
    def __init__(self):
        self.hand = []
        self.score = 0
        self.aces = 0

    def createhand(self, deck):
        for i in range(2):
            newcard = deck.deck[0]
            self.hand.append(deck.deck[0])
            self.calculatescore(newcard)
            deck.deck.pop(0)

    def hit(self, deck):
        newcard = deck.deck[0]
        self.hand.append(newcard)
        self.calculatescore(newcard)
        deck.deck.pop(0)

    def calculatescore(self, data):
        newcard = data[0]
        if newcard[0] in ['1', '2', '3', '4', '5','6','7', '8', '9', '10']:
            self.score+= int(newcard[0])
        elif newcard[0] in ['K', 'Q', 'J']:
            self.score+= 10
        elif newcard[0] == 'A':
            self.score += 11
            self.aces += 1
    
    def checkaces(self):
        while self.score > 21:
            if self.aces > 0:
                self.score -= 10
                self.aces -= 1
                print('Changing ace from 11 to 1')
            else:
                break

    def asciicard(self, card):
        newcard = card[0]
        number = newcard[0]
        suit = newcard[1]

        if suit == 'Clubs':
            suit = '\u2667'
        elif suit == 'Hearts':
            suit = '\u2661'
        elif suit == 'Spades':
            suit = '\u2664'
        else:
            suit = '\u2662'
        return f'''\
        .-------.
        |{number}      |
        |       |
        |   {suit}   |
        |       |
        |      {number}|
        `-------´
        '''.split('\n')

    def display_hand(self):
        cards = [self.asciicard(card) for card in self.hand]
        for lines in zip(*cards):
            print(' '.join(lines))

class DealerHand(Hand):
    def __init__(self):
        super().__init__()
        self.card2 = f'''\ 
        ?????????
        ?????????
        ?????????
        ?????????
        ?????????
        ?????????
        '''.split('\n')
        
    def createonecard(self):
        data = self.hand[0]
        card1 = data[0]
        number = card1[0]
        suit = card1[1]

        if suit == 'Clubs':
            suit = '\u2667'
        elif suit == 'Hearts':
            suit = '\u2661'
        elif suit == 'Spades':
            suit = '\u2664'
        else:
            suit = '\u2662'
        return f'''\
        .-------.
        |{number}      |
        |       |
        |   {suit}   |
        |       |
        |      {number}|
        `-------´
        '''.split('\n')

        
    def showdealercards(self):
        card1 = self.createonecard()
        spacing = ' ' * 5
        for pieces in zip(card1, self.card2):
            print(spacing.join(pieces))


        
def clear():
   """Clear the console."""
   # for windows
   if os.name == 'pos':
      _ = os.system('cls')
   # for mac and linux, where os.name is 'posix'
   else:
      _ = os.system('clear')


def main():
    deck = Deck()
    dealerphase = False

    while True:
        hitphase = True
        playerhand = Hand()
        dealerhand = DealerHand()
        playerhand.createhand(deck)
        dealerhand.createhand(deck)
        print("Dealer's hand: ")
        dealerhand.showdealercards()

        print('-------------------------------------------------------------------------')
        print('Your hand: ')
        playerhand.display_hand()
        print('Your score is ', playerhand.score)
    
        while hitphase == True:
            hors = input('Would you like to hit? H/S ')
            if hors == 'H':
                clear()
                playerhand.hit(deck)
                playerhand.display_hand()
                print('Your new score is', playerhand.score)
            elif hors == 'S':
                hitphase = False
            else:
                print('Invalid input, please use "H" or "S"')

            playerhand.checkaces()

            if playerhand.score == 21:
                print('You won!')
                hitphase = False
                time.sleep(1)
            elif playerhand.score > 21:
                print('Bust!  You lose!')
                hitphase = False
                time.sleep(1)
            else:
                dealerphase = True

        while dealerphase == True:
            clear()
            time.sleep(1)
            print('The dealer reveals his hand')
            dealerhand.display_hand()
            print('Your hand: ')
            playerhand.display_hand()
            time.sleep(5)

            while dealerhand.score < 17:
                dealerhand.hit(deck)
                clear()
                print("Dealer hits")
                dealerhand.display_hand()
                print('Dealer points: ', dealerhand.score)
                time.sleep(2)

            dealerhand.checkaces()
            clear()
            time.sleep(1)
            dealerhand.display_hand()
            print('-------------------------------------------------------')
            playerhand.display_hand()
            print('Player points: ', playerhand.score)
            print('Dealer points: ', dealerhand.score)
            time.sleep(5)

            if dealerhand.score > 21:
                print('Dealer busts!')
                dealerphase = False
                break
             
            if dealerhand.score == 21:
                print('Dealer wins!')
                dealerphase = False

            elif dealerhand.score > playerhand.score:
                print('Dealer wins')
                dealerphase = False
            
            elif dealerhand.score < playerhand.score:
                print('Player wins!')
                dealerphase = False

            elif dealerhand.score == playerhand.score:
                print("It's a tie!")
                dealerphase = False

        time.sleep(5)
        clear()


if __name__ == "__main__":
    main()




