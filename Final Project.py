import random
import time

seeDealerCards = False # Set to true to see dealers cards for testing
winCounter = 0

#Card class for easy formated printing of cards
class Card:
    #Card constructor
    def __init__(self, key):
        self.code = key
    
    #Formatted card printing
    def __str__(self):
        valueKeys = {"2": "Two", "3" : "Three", "4" : "Four", "5" : "Five", "6" : "Six", "7" : "Seven", "8" : "Eigth", "9" : "Nine", "10" : "Ten", "J" : "Jack", "Q" : "Queen", "K" : "King", "A" : "Ace"}
        suitKeys = {"H" : "Hearts", "D" : "Diamonds", "C" : "Clubs", "S" : "Spades"}
        return valueKeys[self.code[:-1]] + " of " + suitKeys[self.code[-1:]]
    
    #returns code for value calculations
    def getCode(self):
        return self.code

#Deck class for storing cards in deck and randomized order
class Deck():
    #Deck constructor
    def __init__(self):
        self.deck = [Card("2H"), Card("3H"), Card("4H"), Card("5H"), Card("6H"), Card("7H"), Card("8H"), Card("9H"), Card("10H"), Card("JH"), Card("QH"), Card("KH"), Card("AH"), 
                     Card("2D"), Card("3D"), Card("4D"), Card("5D"), Card("6D"), Card("7D"), Card("8D"), Card("9D"), Card("10D"), Card("JD"), Card("QD"), Card("KD"), Card("AD"), 
                     Card("2C"), Card("3C"), Card("4C"), Card("5C"), Card("6C"), Card("7C"), Card("8C"), Card("9C"), Card("10C"), Card("JC"), Card("QC"), Card("KC"), Card("AC"),
                     Card("2S"), Card("3S"), Card("4S"), Card("5S"), Card("6S"), Card("7S"), Card("8S"), Card("9S"), Card("10S"), Card("JS"), Card("QS"), Card("KS"), Card("AS")]
    
    #Randomly shuffles deck
    def shuffle(self):
        random.shuffle(self.deck)
    
    #Get list of card codes in order
    def getCodeList(self):
        result = []
        for x in self.deck:
            result.append(x.getCode())
        return result

#Class for hand of player and dealer, handles drawing cards, displaying whole hands, and calculating value of hands
class Hand(Deck):
    #Hand constructor, returns true if opening hand is blackjack
    def __init__(self, deck):
        self.deck = []
        for x in range(2):
            self.deck.append(deck.deck.pop(0))
        return blackJackCheck(self.deck)
    
    #Displays dealers hand without showing facedown card, has option to always show dealers facedown card for testing
    def displayDealer(self):
        print("The Dealer has:")
        for x in range(len(self.deck)-1):
            print("A " + str(self.deck[x]))
        if seeDealerCards:
            print("And a " + str(self.deck[len(self.deck)-1]))
        else:
            print("And a face down card")
        print("")
    
    def displayPlayer(self):
        print("You have:")
        for x in range(len(self.deck)-1):
            print("A " + str(self.deck[x]))
        print("And a " + str(self.deck[len(self.deck)-1]))
        print("")

    def displayHand(self):
        for x in range(len(self.deck)-1):
            print("A " + str(self.deck[x]))
        print("And a " + str(self.deck[len(self.deck)-1]))
        print("")

    def drawCard(self, deck):
        card = deck.deck.pop(0)
        self.deck.append(card)
        return card
    
    def getValue(self):
        values = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10, "A":11}
        ace = False
        handValue = 0
        for x in self.deck:
            code = x.code[:-1]
            if code == "A":
                ace = True
            handValue += values[code]
        if ace and handValue > 21:
            handValue -= 10
        return handValue
    
    def blackJackCheck(deck):
        hand = {}
        blackJack = {"10", "J", "Q", "K", "A"}
        for x in deck:
            hand.append(x.code[:-1])
        if 
            
            
def printTitle():
    print(" ______                 _                      _______                       _                _  ")
    print("(_____ \           _   | |                    (_______)                     (_)              | | ")
    print(" _____) ) _   _  _| |_ | |__    ___   ____        _     _____   ____  ____   _  ____   _____ | | ")
    print("|  ____/ | | | |(_   _)|  _ \  / _ \ |  _ \      | |   | ___ | / ___)|    \ | ||  _ \ (____ || | ")
    print("| |      | |_| |  | |_ | | | || |_| || | | |     | |   | ____|| |    | | | || || | | |/ ___ || | ")
    print("|_|       \__  |   \__)|_| |_| \___/ |_| |_|     |_|   |_____)|_|    |_|_|_||_||_| |_|\_____| \_)")
    print("         (____/                                                                                  ")
    print("              ______   _                 _        _                _      _ ")
    print("             (____  \ | |               | |      (_)              | |    | |")
    print("              ____)  )| |  _____   ____ | |  _    _  _____   ____ | |  _ | |")
    print("             |  __  ( | | (____ | / ___)| |_/ )  | |(____ | / ___)| |_/ )|_|")
    print("             | |__)  )| | / ___ |( (___ |  _ (   | |/ ___ |( (___ |  _ (  _ ")
    print("             |______/  \_)\_____| \____)|_| \_) _| |\_____| \____)|_| \_)|_|")
    print("                                               (__/                         ")
    input("Press Enter to Continue")
    print("")

def printWin():
    global winCounter
    winCounter += 1

def printLoss():
    global winCounter
    winCounter = 0

def choiceCheck(choice):
    isValid = False
    while(not isValid):
        choice = choice.strip()
        choice = choice.lower()
        # print(choice)
        if choice == "h" or choice == "hit":
            return "hit"
            isValid = True
            # print("1")
        elif choice == "s" or choice == "stand":
            return "stand"
            isValid = True
            # print("2")
        else:
            print("Sorry your input was invalid")
            choice = input("Please choose \"H\" or \"Hit\" to hit or \"S\" or \"Stand\" to stand: ")
            # print("3")

while True:
    #game set up
    sleepTime = 0.7
    if winCounter == 5:
        print("You have won 5 times in a row")
        print("The pit boss suspects you of cheating and has kick you out of the casino")
        print("Congratulations!")
        input("")
        break

    gameOver = False
    printTitle()

    mainDeck = Deck()
    mainDeck.shuffle()
    dealerHand = Hand(mainDeck)
    playerHand = Hand(mainDeck)

    print("The dealer has delt the cards.")
    print("")
    time.sleep(sleepTime)
    dealerHand.displayDealer()
    time.sleep(sleepTime)
    playerHand.displayPlayer()
    time.sleep(sleepTime)
    
    #Player chooses hit or stand
    isStanding = False
    while(not isStanding):
        if(choiceCheck(input("Would you like to hit or stand: ")) == "hit"):
            print("")
            
            print("The dealer hands you a " + str(playerHand.drawCard(mainDeck)))
            print("")
            time.sleep(sleepTime)
            playerHand.displayPlayer()
            time.sleep(sleepTime)
            if playerHand.getValue() > 21:
                gameOver = True
                print("You went over 21 (" + str(playerHand.getValue()) + ") and busted out")
                break
        else:
            isStanding = True
    if gameOver:
        time.sleep(sleepTime)
        printLoss()
        print("Game Over")
        input("Press enter to start a new game")
        continue
    
    #Dealer draws cards
    if dealerHand.getValue() < 17 :
        print("The dealer will now draw cards, the deal must stand on 17. (Soft 17 rules)")
        print("")
        time.sleep(sleepTime)
        print("The dealer has:")
        dealerHand.displayHand()

        while(True):
            if dealerHand.getValue() < 17 :
                time.sleep(sleepTime)
                print("The dealer drew a " + str(dealerHand.drawCard(mainDeck)))
                print("")
            else:
                break
    else:
        time.sleep(sleepTime)
        print("The dealer has:")
        dealerHand.displayHand()

    #See who wins
    playerValue = playerHand.getValue()
    dealerValue = dealerHand.getValue()
    time.sleep(sleepTime)
    if dealerValue > 21:
        print("The dealer went over 21 and busted")
        printWin()
        print("You win!")
    elif dealerValue < playerValue:
        printWin()
        print("You Win!")
    elif dealerValue > playerValue:
        printLoss()
        print("You lose :(")
    else:
        print("Tie")

    print("")
        
    time.sleep(sleepTime)
    print("Your cards value was: " + str(playerValue))
    print("The dealers card value was: " + str(dealerValue))
    input("Press any key to restart")
        
    

