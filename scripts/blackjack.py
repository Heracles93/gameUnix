import random
import pdb

suits = ("Hearts","Diamonds", "Spades", "Clubs")
ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")
values = {"Two":2, "Three":3, "Four":4, "Five":5, "Six":6, "Seven":7, "Eight":8, "Nine":9, "Ten":10, "Jack":10, "Queen":10, "King":10, "Ace":11}

playing = False
bet = 1
restartPhrase = "Press 'd' to deal the cards again, or press 'q' to quit"

class Card:

	def __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank
		
	def __str__(self):
		return self.rank + " of " + self.suit

	def getSuit(self):
		return self.suit
    
	def getRank(self):
		return self.rank
    
	def draw(self):
		print(self.suit + self.rank)

class Deck:

	def __init__(self):
		''' Create a deck in order '''
		self.deck = []
		for suit in suits:
			for rank in ranks:
				self.deck.append(Card(suit, rank))
				
	def __str__(self):
		deckComp = ""
		for card in self.deck:
			deckComp += "\n" + card.__str__()
		return "The deck has " + deckComp
		
	def shuffle(self):
		''' Shuffle the deck, python actually already has a shuffle method in its random lib '''
		random.shuffle(self.deck)
		
	def deal(self):
		''' Grab the first item in the deck '''
		return self.deck.pop()
		
# test_deck = Deck()
# print(test_deck)


class Hand:

	def __init__(self):
		self.cards = []
		self.value = 0
		self.aces = 0

	def __str__(self):
		''' Return a string of current hand composition '''
		handComp = ""
        
        # Better way to do this? List comprehension?
		for card in self.cards:
			cardName = card.__str__()
			handComp += " " + cardName
		return 'The hand has %s' %handComp

	def addCard(self, card):
		self.cards.append(card)
		# card passed in
		# from Deck.deal() --> singleCard(suit, rank)
		self.value += values[card.rank]
		# trach aces
		if card.rank is "Ace":
			self.aces += 1
	
	# def adjustForAce(self):
	# 	while self.value > 21 and self.aces > 0:
	# 		self.value -= 10
	# 		self.aces += 1

	def calcVal(self):
		'''Calculate the value of the hand, make aces an 11 if they don't bust the hand'''
		if (self.aces > 0 and self.value < 12):
			return self.value + 10
		else:
			return self.value
        
	def draw(self,hidden):
		if hidden == True and playing == True:
            #Don't show first hidden card
			startingCard = 1
		else:
			startingCard = 0
		for x in range(startingCard,len(self.cards)):
			self.cards[x].draw()

class Game:


	def __init__(self):
		self.hello = "HELLO"
		self.playing = True # ???
		
		
	def intro(self):
		statement = '''Welcome to BlackJack! Get as close to 21 as you can without going over!
		Dealer hits until she reaches 17. Aces count as 1 or 11.
		Card output goes a letter followed by a number of face notation'''
		print(statement)		

	# First Bet
	def makeBet(self):
		''' Ask the player for the bet amount and '''
		
		global bet
		bet = 0
		
		print(' What amount of chips would you like to bet? (Enter whole integer please) ')
		
		# While loop to keep asking for the bet
		while bet == 0:
		    betComp = input() # Use betComp as a checker
		    betComp = int(betComp)
		    # Check to make sure the bet is within the remaining amount of chips left.
		    if betComp >= 1 and betComp <= 100:#chipPool:
		        bet = betComp
		    else:
		        print("Invalid bet, you only have " + str(chipPool) + " remaining")

	def dealCards(self):
		''' This function deals out cards and sets up round '''
		
		# Set up all global variables
		global result, playing, deck, playerHand, dealerHand, chipPool, bet
		
		# Create a deck
		deck = Deck()
		
		#Shuffle it
		deck.shuffle()
		
		#Set up bet
		self.makeBet()
		
		# Set up both player and dealer hands
		playerHand = Hand()
		dealerHand = Hand()
		
		# Deal out initial cards
		playerHand.addCard(deck.deal())
		playerHand.addCard(deck.deal())
		
		dealerHand.addCard(deck.deal())
		dealerHand.addCard(deck.deal())
		
		result = "Hit or Stand? Press either h or s: "
		
		if playing == True:
		    print('Fold, Sorry')
		    chipPool -= bet
		
		# Set up to know currently playing hand
		playing = True 
		self.gameStep()



	def hit(self):
		
		''' Implement the hit button '''
		global playing,chipPool,deck,playerHand,dealerHand,result,bet
		chidPool = 100 # test debug
		# If hand is in play add card
		if playing:
		    if playerHand.calcVal() <= 21:
		        playerHand.addCard(deck.deal())
		    
		    print("Player hand is %s" %playerHand)
		    
		    if playerHand.calcVal() > 21:
		        result = 'Busted! '+ restartPhrase
		        
		        # chipPool -= bet
		        chidPool = 999
		        playing = False
		
		else:
		    result = "Sorry, can't hit" + restartPhrase
		
		self.gameStep()



	def stand(self):
		# global playing,chipPool,deck,playerHand,dealerHand,result,bet
		''' This function will now play the dealers hand, since stand was chosen '''
		
		if playing == False:
		    if playerHand.calcVal() > 0:
		        result = "Sorry, you can't stand!"
		        
		# Now go through all the other possible options
		else:
		    
		    # Soft 17 rule
		    while dealerHand.calcVal() < 17:
		        dealerHand.addCard(deck.deal())
		        
		    # Dealer Busts    
		    if dealerHand.calcVal() > 21:
		        result = 'Dealer busts! You win!' + restartPhrase
		        chipPool += bet
		        playing = False
		        
		    #Player has better hand than dealer
		    elif dealerHand.calcVal() < playerHand.calcVal():
		        result = 'You beat the dealer, you win!' + restartPhrase
		        chipPool += bet
		        playing = False
		    
		    # Push
		    elif dealerHand.calcVal() == playerHand.calcVal():
		        result = 'Tied up, push!' + restartPhrase
		        playing = False
		    
		    # Dealer beats player
		    else:
		        result = 'Dealer Wins!' + restartPhrase
		        chipPool -= bet
		        playing = False
		self.gameStep()

	def gameStep(self):
		'Function to printgame step/status on output'
		
		#Display Player Hand
		print("")
		print('Player Hand is: ')
		playerHand.draw(hidden =False)
		
		print('Player hand total is: '+str(playerHand.calcVal()))
		
		#Display Dealer Hand
		print('Dealer Hand is: '),
		dealerHand.draw(hidden=True)
		
		# If game round is over
		if playing == False:
		    print( " --- for a total of " + str(dealerHand.calcVal() ))
		    chipPool = 3000 # test debug
		    print("Chip Total: " + str(chipPool))
		# Otherwise, don't know the second card yet
		else: 
		    print(" with another card hidden upside down")
		
		# print(result of hit or stand.
		print(result)
		
		self.playerInput()

	def gameExit(self):
		print('Thanks for playing!')
		exit()

	def playerInput(self):
		''' Read user input, lower case it just to be safe'''
		#pdb.set_trace()
		plin = 'h' # test debug
		# plin = input().lower()
		#pdb.set_trace()
		
		if plin == 'h':
		    self.hit()
		elif plin == 's':
		    stand()
		elif plin == 'd':
		    dealCards()
		elif plin == 'q':
		    gameExit()
		else:
		    print("Invalid Input...Enter h, s, d, or q: ")
		    self.playerInput()



def main():
	'''The following code will initiate the game! (Note: Need to Run all Cells)'''

	# Create a Deck
	deck = Deck()
	#Shuffle it
	deck.shuffle()
	# Create player and dealer hands
	playerHand = Hand()
	dealerHand = Hand()
	#print(the intro
	game = Game()
	#pdb.set_trace()
	print(game.hello)
	print(game.playing)
	game.intro()
	# Deal out the cards and start the game!
	game.dealCards()

main()
