import random
class Card:
    def __init__(self, key):
        self.code = key
    def __str__(self):
        valueKeys = {"2": "Two", "3" : "Three", "4" : "Four", "5" : "Five", "6" : "Six", "7" : "Seven", "8" : "Eigth", "9" : "Nine", "10" : "Ten", "J" : "Jack", "Q" : "Queen", "K" : "King", "A" : "Ace"}
        suitKeys = {"H" : "Hearts", "D" : "Diamonds", "C" : "Clubs", "S" : "Spades"}
        return valueKeys[self.code[:1]] + " of " + suitKeys[self.code[1:]]
    def getCode(self):
        return self.code



class Deck():
    def __init__(self):
        self.deck = [Card("2H"), Card("3H"), Card("4H"), Card("5H"), Card("6H"), Card("7H"), Card("8H"), Card("9H"), Card("10H"), Card("JH"), Card("QH"), Card("KH"), Card("AH"), 
                     Card("2D"), Card("3D"), Card("4D"), Card("5D"), Card("6D"), Card("7D"), Card("8D"), Card("9D"), Card("10D"), Card("JD"), Card("QD"), Card("KD"), Card("AD"), 
                     Card("2C"), Card("3C"), Card("4C"), Card("5C"), Card("6C"), Card("7C"), Card("8C"), Card("9C"), Card("10C"), Card("JC"), Card("QC"), Card("KC"), Card("AC"),
                     Card("2S"), Card("3S"), Card("4S"), Card("5S"), Card("6S"), Card("7S"), Card("8S"), Card("9S"), Card("10S"), Card("JS"), Card("QS"), Card("KS"), Card("AS")]
    def shuffle(self):
        random.shuffle(self.deck)
    def getCodeList(self):
        result = []
        for x in self.deck:
            result.append(x.getCode())
        return result
    
class Hand(Deck):
    def __init__(self, deck):
        self.deck = []
        for x in range(2):
            self.deck.append(deck.deck.pop(0))
    def displayDealer(self):
        print("The Dealer has:")
        print("A " + str(self.deck[0]) + " and a face down card")
    def displayPlayer(self):
        print("The player has:")
        for x in range(len(self.deck)):
            print("A " + str(self.deck[x]))
    def drawCard(self, deck):
        self.deck.append(deck.deck.pop(0))


mainDeck = Deck()
mainDeck.shuffle()

dealerHand = Hand(mainDeck)
playerHand = Hand(mainDeck)
dealerHand.displayDealer()
playerHand.displayPlayer()
playerHand.drawCard(mainDeck)
playerHand.displayPlayer()