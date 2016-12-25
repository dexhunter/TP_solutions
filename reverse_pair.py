"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division


from inlist import in_bisect, make_word_list


def reverse_pair(word_list, word):
    """Checks whether a reversed word appears in word_list.

    word_list: list of strings
    word: string
    """
    rev_word = word[::-1]
    return in_bisect(word_list, rev_word)
        
import time
if __name__ == '__main__':
	st = time.time()
	word_list = make_word_list()
	ctr = 0
	for word in word_list:
		if reverse_pair(word_list, word):
			ctr = ctr + 1
			#print(word, word[::-1])
	et = time.time() - st
print (ctr)
print (et)

