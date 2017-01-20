#!/usr/bin/python3


import os
import glob #The glob module finds all the pathnames matching a specified pattern according to the rules used by the Unix shell, although results are returned in arbitrary order. No tilde expansion is done, but *, ?, and character ranges expressed with [] will be correctly matched. 

# The author asked to write a md5sum check to find duplicate without providing anymore information. It is interesting to learn how md5sum actually works. So for reference: https://en.wikipedia.org/wiki/Md5sum
import hashlib
import itertools

#following code is copied from http://stackoverflow.com/questions/3431825/generating-an-md5-checksum-of-a-file
def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()
	
def main():
	d = {}
	rev_d = {}
	for filename in glob.glob('./**/*.py',recursive = True):
		print(os.path.abspath(filename))
		print(md5(os.path.abspath(filename)))
		d[filename] = md5(os.path.abspath(filename))
	
	for k, v in d.items():
		rev_d.setdefault(v, set()).add(k)
	print ("Are there any duplicate files?")
	'''
	for k, v in rev_d.items():
		if len(v) > 1:
			print ("Yes, and they are:")
			print (v)
	'''
	print(set(itertools.	chain.from_iterable(values for key, values in rev_d.items() if len(values) > 1)))
	
if __name__ == '__main__':
	main()
		