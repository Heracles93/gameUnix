import random

suits = ("Hearts","Diamonds", "Spades", "Clubs")
ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")
values = {"Two":2, "Three":3, "Four":4, "Five":5, "Six":6, "Seven":7, "Eight":8, "Nine":9, "Ten":10, "Jack":10, "Queen":10, "King":10, "Ace":11}

playing = True

class Card:

	def __init__(self, suit, rank)):
		self.suit = suit
		self.rank = rank
		
	def __str__(self):
	return self.rank + " of " + self.suit

class Deck:

	def __init__(self):
		self.deck = []
		for suit in suits:
			for rank in ranks:
				self.deck.append(Card(suit, rank))
				
	def __str__(self):
		deck_comp = ""
			for card in self.deck:
			deckComp += "\n" + card.__str__()
		return "The deck has " + deckComp
		
	def shuffle(self):
		random.shuffle(self.deck)
		
	def deal(self)
		return self.deck.pop()
		
# test_deck = Deck()
# print(test_deck)


class Hand:

	def __init__(self):
		self.cards = []
		self.value = 0
		self.aces = 0

	def addCard(self, card):
		self.cards.append(card)
		# card passed in
		# from Deck.deal() --> single_Card(suit, rank)
		self.value += values[card.rank]
		# trach aces
		if card.rank is "Ace":
			self.aces += 1
	
	def adjustForAce(self):
		while self.value > 21 and self.aces > 0:
			self.value -= 10
			self.aces += 1

class Chips:

	def __init__(self, total = 100):
		self.total = total
		self.bet = 0

	def winBet(self):
		self.total += self.bet

	def loseBet(self):
		self.total -= self.bet

def hitOrStand(deck, hand):
	global playing
		while playing:
			x = str(input("Hit or Stand ? enter h or s")).lower()
			if x[0] == "h":
				hit(deck, hand)
			elif x[0] =="s":
				print("Player Stands Dealer's Turn")
				playing = False
			else:
				print("Sorry, I did no understand that, Please enter h or s only !")
				continue
			break

def hit(deck, hand):
	singleCard = deck.deal()
	hand.addCard(singleCard)
	hand.adjustForAce()

def playerBusts(player, dealer, chips):
	print("BUST PLAYER")
	chips.loseBet()

def playerWins(player, dealer, chips):
	print("PLAYER WINS!")
	chips.winBet()

def dealerBusts(player, dealer, chips):
	print("PLAYER WINS! DEALER BUSTED")
	chips.winBet()

def dealerWins(player, dealer, chips):
	print("DEALER WINS!")
	chips.loseBet()

def push(player, dealer):
	print("Dealer and player tie! PUSH")

def showSome(player, dealer):

def showAll(player, dealer):
