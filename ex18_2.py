import random

class Card:
	''' class represents suit of cars, encoding with numbers 
	
	Attributes:
		suit;
		rank;
	
	sapdes -> 3
	hearts -> 2
	diamonds -> 1
	clubs -> 0
	
	jack -> 11
	queen -> 12
	king -> 13
	
	
	'''
	# Attribute
	suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
	rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
	
	def __init__(self, suit=0, rank=2):
		self.suit = suit
		self.rank = rank
		
	def __str__(self):
		return '%s of %s' % (Card.rank_names[self.rank], Card.suit_names[self.suit])
	
	def __lt__(self, other):
		# first compare suit
		if self.suit < other.suit: return True
		if self.suit > other.suit: return False
		
		# if suit is the same then compare rank
		return self.rank < other.rank
		
		
class Deck:
	'''class represents deck
	
	Attributes:
		cards: list
	'''
	
	def __init__(self):
		self.cards = []
		for suit in range(4):
			for rank in range(1, 14):
				card = Card(suit, rank)
				self.cards.append(card)
	
	def __str__(self):
		res = []
		for card in self.cards:
			res.append(str(card))
		return '\n'.join(res)
		
	def pop_card(self):
		'''remove the last card from the deck'''
		return self.cards.pop()
		
	def add_card(self, card):
		''' add a card to the last position of deck (using veneer methods)'''
		self.cards.append(card)
		
	def shuffle(self):
		'''shuffle the deck randomly'''
		random.shuffle(self.cards)
		
	def sort(self):
		'''sort the deck in descending ordoer'''
		self.cards.sort()
		
	def move_card(self, hand, num):
		'''move card(s) to another Hand or Deck'''
		for i in range(num):
			hand.add_card(self.pop_card())
			
	def deal_hands(self, num_of_hands, num_of_cards_per_hand):
		'''deal hands
		
		num_of_hands: int
		num_of_cards_per_hand: list
		
		'''
		hand_list = []
		for i in range(num_of_hands):
			h = Hand("Hand No. %d" % i)
			self.move_card(h, num_of_cards_per_hand)
			hand_list.append(h)
		return hand_list
		
		
class Hand(Deck):
	'''class represents cards on hand, inherited from deck '''
	
	def __init__(self, label=''):
		'''initialize cards on hand, and label which hand is using'''
		self.cards = []
		self.label = label
		
if __name__ == '__main__':
	king_of_spades = Card(3, 13) # test
	print(king_of_spades)
	d = Deck() #test
	print('\n---initial result---')
	print(d)
	d.shuffle()
	print('\n---shuffle result---')
	print(d)
	d.sort()
	print('\n---sort result---')
	print(d)
	print('\n---deal_hand test result---')
	li = d.deal_hands(5,4)
	for h in li:
		print (h.label)
		print (h)
		