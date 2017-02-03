'''This is Dex's solution to exercise 13_5 of Think Python '''

def choose_from_hist(hist):
	l = []
	for key, value in hist.items():
		l.extend([key] * value) #word needs to be inside a list
	return random.choice(l)
	
	
	
import random
from ex13_4 import *

if __name__ == '__main__':
	hist = load_word_as_dict('words.txt')
	print(choose_from_hist(hist))