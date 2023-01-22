'''
Project: Twenty One Game:
Course:
Name: 
Due Date:

Description:
<put your description here>

This is skeleton starter code for the Twenty-One Game.

Typical pseudocode for such a game would be:
1. initial deal
2. player's turn 
3. If player gets twenty-one, immediate win 
4. dealer's turn 
5. check for winner
6. print results
'''

import os
import random

class Card:
    def __init__(self, value, suit, faceup= True):
        self.value = value
        self.suit = suit
        self.faceup = faceup

    def printcard(self):
        
        if self.suit == 'clubs':
            self.suit = '\u2667'
        elif self.suit == 'hearts':
            self.suit = '\u2661'
        elif self.suit == 'spades':
            self.suit = '\u2664'
        else:
            self.suit = '\u2662'

        if self.value == 'Ace':
            self.value = 'A'
        elif self.value == 'King':
            self.value = 'K'
        elif self.value == 'Queen':
            self.value = 'Q'
        elif self.value == 'Joker':
            self.value = 'J'

        if self.faceup == True:
            print(" ----------------------")
            print("|                      |")
            if self.value == 10:
                print(f"| {self.value}                   |".format(self.value))
            else:
                print(f"| {self.value}                    |".format(self.value))
            print("|                      |")
            print("|                      |")
            print("|                      |")
            print("|                      |")
            print("|                      |")
            print(f"|           {self.suit}          |".format(self.suit))
            print("|                      |")
            print("|                      |")
            print("|                      |")
            print("|                      |")
            print("|                      |")
            if self.value == 10:
                print(f"|                   {self.value} |".format(self.value))  
            else:  
                print(f"|                    {self.value} |".format(self.value))
            print("|                      |")
            print(" ----------------------")

mycard = Card(10, 'hearts')
hiscard = Card(5, 'diaomonds')
mycard.printcard()
hiscard.printcard()

class Deck:
    def __init__(self, suits= ['spades', 'clubs', 'diamonds', 'hearts'], value= ['Ace', 'King', 'Queen', 'Joker', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], deck = []):
        
        self.suits = suits
        self.value = value
        self.deck = deck

    def createdeck(self):
        for i in self.suits:
            for ii in self.value:
                self.deck.append(str(i) + ' ' + str(ii))

class Hand:
    pass

class Dealer:
    def __innit__(self, hand= [], points= 0):
        self.hand = hand
        self.points = points

    def dealerdraw(self):
        pass



class Player:
    pass

class Game:

    def run(self):
        pass

def clear():
   """Clear the console."""
   # for windows
   if os.name == 'nt':
      _ = os.system('cls')
   # for mac and linux, where os.name is 'posix'
   else:
      _ = os.system('clear')

def main():
    pass

if __name__ == '__main__':
    main()

