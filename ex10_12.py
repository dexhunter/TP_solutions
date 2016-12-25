'''
I tried to writw something but found that I misunderstood the question (alternating)
Then I looked up on Internet
The result is amazing!
Check this out:http://stackoverflow.com/questions/5523058/how-to-optimize-this-python-code-from-thinkpython-exercise-10-10

'''

words = set(line.strip() for line in open("words.txt"))
for w in words:
    even, odd = w[::2], w[1::2]
    if even in words and odd in words:
        print even, odd
	print "The word is %s" % (w)