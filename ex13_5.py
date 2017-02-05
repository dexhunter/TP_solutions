'''This is Dex's solution to exercise 13_5 of Think Python '''

def choose_from_hist(hist):
	'''
	Generate a hist list according to frequency
	then choose randomly one from the list 
	WARN: this is low effiency
	'''
	l = []
	for key, value in hist.items():
		l.extend([key] * value) #word needs to be inside a list
	return random.choice(l)
	
	
	
import random
from ex13_4 import *

if __name__ == '__main__':
	hist = load_word_as_dict('words.txt')
	print(choose_from_hist(hist)) 