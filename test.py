def contain(word, letters):
    return not set(letters).isdisjoint(set(word))
	
def ncont(words, letters):
    return sum(contain(word, letters) for word in words)
	

import itertools
import string
def minimum_letter_set(words, n):
    # build a lookup table for each letter to the set of words it features in
    by_letter = {
        letter: {
            word
            for word in words
            if letter in word
        }
        for letter in string.ascii_lowercase
    }

    # allowing us to define a function that finds words that match multiple letters
    def matching_words(letters):
        return set.union(*(by_letter[l] for l in letters))

    # find all 5 letter combinations
    attempts = itertools.combinations(string.ascii_lowercase, n)

    # and return the one that matches the fewest words
    return min(attempts, key=lambda a: len(matching_words(a)))
	
	
if __name__ == '__main__':

    with open('words.txt', 'r') as fin:
        words = [line.strip() for line in fin]

    print (minimum_letter_set(words, 5))