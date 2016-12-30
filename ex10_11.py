''' #due to poor effiency I abort this method
def find_reverse(l):
	ctr = 0
	for i in range(len(l)):
		for j in range(i+1, len(l)):
			if l[i] == l[j][::-1]:
				ctr += 1
				print (l[i], l[j])
	return ctr			
				
if __name__ == '__main__':
	l = []
	with open('words.txt', 'r') as fin:
		for line in fin:
			word = line.strip()
			l.append(word)
		print find_reverse(l)
'''
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

	
import time
if __name__ == '__main__':
	l = []
	ctr = 0
	st = time.time()
	with open('words.txt', 'r') as fin:
		for line in fin:
			word = line.strip()
			l.append(word)
		for i in l:
			if exist_check(l,i[::-1]):
				ctr += 1
				#print (i, i[::-1])
		#This one is much faster than author's, I think it's because bisect module uses a better implementation.
		#The original time used: 71.5869998932
		#This method time used: 0.22100019455
		et = time.time() - st
		print ctr
		print et
		print len(l)
				
				
	