import bisect as bs
# list need to be sorted first!
if __name__ == '__main__':
	s = raw_input("What do yo wan to search? ")
	l = []
	with open('words.txt', 'r') as fin:
		for line in fin:
			word = line.strip()
			l.append(word)
		print bs.bisect(l, s) #count start from 1