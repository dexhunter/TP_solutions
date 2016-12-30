import bisect as bs
#import time #test
# list need to be sorted first!
if __name__ == '__main__':
	s = raw_input("What do yo wan to search? ")
	#s = "hey"
	#st = time.time()
	l = []
	with open('words.txt', 'r') as fin:
		for line in fin:
			word = line.strip()
			l.append(word)
		print bs.bisect(l, s) #count start from 1
		#bs.bisect(l, s)
		#et = time.time() - st
		#print et