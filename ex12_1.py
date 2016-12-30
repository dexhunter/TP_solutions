import collections

def most_frequent(s):
	return collections.Counter(s).most_common()
	
if __name__ == '__main__':
	# emma.txt is provided from author's code
	with open('emma.txt', 'r') as fin:
		string = fin.read()
		print most_frequent(string)