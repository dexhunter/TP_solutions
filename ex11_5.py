def rotate_letter(letter, n):
    """Rotates a letter by n places.  Does not change other chars.

    letter: single-letter string
    n: int

    Returns: single-letter string
    """
    if letter.isupper():
        start = ord('A')
    elif letter.islower():
        start = ord('a')
    else:
        return letter

    c = ord(letter) - start
    i = (c + n) % 26 + start
    return chr(i)


def rotate_word(word, n):
    """Rotates a word by n places.

    word: string
    n: integer

    Returns: string
    """
    res = ''
    for letter in word:
        res += rotate_letter(letter, n)
    return res
	
import bisect as bs

def exist_check(a, x):
    '''
	Checks if a is in x.
	a: string
	x: list
	
	Returns: bool
	'''
	#https://docs.python.org/2/library/bisect.html
    i = bs.bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return True
    return False

def rotate_pair(l):
	'''Returans a list containing all rotate pairs of a wordlist
	
	l: wordlist
	
	Returns: rotate_list
	'''
	rl = {}
	for word in l:
		for num in range(1,14):
			if exist_check(l, rotate_word(word, num)):
				rl[word] = str(num) + rotate_word(word, num)
	return rl
	

if __name__ == '__main__':

	with open('words.txt', 'r') as fin:
		words = [line.strip() for line in fin]
		print rotate_pair(words)
	
	