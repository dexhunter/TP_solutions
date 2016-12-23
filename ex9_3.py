# This exercise is eaiser to do with regex
# An answer becomes very handy in this case:http://stackoverflow.com/questions/22506193/is-there-a-better-algorithm-for-exercise-9-3-in-think-python-how-to-think-like
'''
# previous version, changed after read the link
def avoids(word, forbid_string):
	for c in word:
		if c in forbid_string:
			return False
	return True
'''

def avoids(word, forbid_string):
	return set(forbid_string).isdisjoint(set(word))

# a combination of five forbidden letters that excludes the smallest number of words also means a combination contains the least amount of words
def avoids_count_modified(word):
	forbid_string = raw_input("Please enter a forbidden string: ")
	return sum(avoids(word, forbid_string) for c in word)

print avoids("Apple", "abcdA")
# I am not trying to write a function to return the combination, you can read the post with given link, that's a brilliant solution
# the answer is ['q', 'j', 'x', 'z', 'w'] if you are interested