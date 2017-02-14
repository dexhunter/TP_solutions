"""Adapeted from Think Python website

Copyright 2017 Dex D. Hunter

License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

from Card import Hand, Deck


class PokerHand(Hand):
	"""Represents a poker hand.
	
	Inherited from Hand
	"""

	def suit_hist(self):
		"""Builds a histogram of the suits that appear in the hand.

		Stores the result in attribute suits.
		"""
		self.suits = {}
		for card in self.cards:
			self.suits[card.suit] = self.suits.get(card.suit, 0) + 1
		print(self.suits)
		
	def rank_hist(self):
		"""Builds a histogram of the rank that appear in the hand.

		Stores the result in attribute rank.
		"""
		self.ranks = {}
		for card in self.cards:
			self.ranks[card.rank] = self.ranks.get(card.rank, 0) + 1
		print(self.ranks)

	def has_flush(self):
		"""Returns True if the hand has a flush, False otherwise.
	  
		Note that this works correctly for hands with more than 5 cards.
		
		flush: 5 cards with the same suit
		"""
		self.suit_hist()
		for val in self.suits.values():
			if val >= 5:
				return True
		return False
		
	def has_pair(self, other):
		'''pair: two cards with the same rank'''
		self.rank_hist()
		for val in self.ranks.values():
			if val >= 2:
				return True
		return False
		
	
	def has_twopair(self):
		''' has two pairs of cards with the same rank '''
		self.rank_hist()
		count = 0
		for val in self.ranks.values():
			if val >= 2:
				count += 1
				
		if count >=2:
			return True
		return False
		
	def classify(self):
		'''
		straight: five cards with ranks in sequence
		
		flush: five cards with the same suit
		'''
		label = ['pari', 'two pair', 'three of a kind', 'striaght', 'flush', 'full house', 'four of a kind', 'straight flush']
		


if __name__ == '__main__':
	# make a deck
	deck = Deck()
	deck.shuffle()

	# deal the cards and classify the hands
	h = PokerHand()
	deck.move_cards(h, 10)
	h.suit_hist()
	print(h)
	'''
	for i in range(7):
		hand = PokerHand()
		deck.move_cards(hand, 7)
		hand.suit_hist
		hand.sort()
		print(hand)
		print(hand.has_flush())
		print('')
	'''