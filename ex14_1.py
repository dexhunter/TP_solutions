from string import maketrans

def sed(s, replace_string, input, output):
	fin = open(input, 'r')
	fout = open(output, 'w')

	trantab = maketrans(s, replace_string) # translate table


	for word in fin:
		re_word = word.translate(trantab)
		fout.write(re_word)

	fin.close()
	fout.close()


if __name__ == '__main__':
	sed('p', 'q', 'test.txt', 'output.txt') #success with this one
