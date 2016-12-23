#test run for exercise 9-3
import string

def findmincomb(num_letter, words, alphabet):
    global min_num, min_comb
    # find miniset in resurcive way
    def mincomb(remain, alphabet, comb, pre_set):
        global min_num, min_comb
        # get enough letters
        if remain <= 0:
            pre_num = len(pre_set)
            if pre_num < min_num: # update
                min_num = pre_num
                min_comb = comb.copy()
                print(min_num, min_comb)
        else:
            comb.append(None)
            for i in range(len(alphabet)):
                letter = alphabet[i]
                cur_set = pre_set | cont[letter]
                print(comb, letter, len(cur_set))
                # only when current set small the minimum set, get next letter
                if len(cur_set) < min_num:
                    comb[-1] = letter
                    mincomb(remain-1, alphabet[i+1:], comb, cur_set)
            comb.pop()

    # build dictionary for every letter in alphabet
    # key: letter, value: set of words contain letter
    cont = {
        letter : {
            word
            for word in words
            if letter in word
        }
        for letter in alphabet
    }

    # get a temporay minset
    min_tuple = sorted(cont.items(), key = lambda  x: len(x[1]))[:num_letter]
    min_comb = [item[0] for item in min_tuple]
    min_num = len(set.union(*(item[1] for item in min_tuple)))
    print(min_num, min_comb)

    # do the really work
    mincomb(num_letter, alphabet, [], set())

if __name__ == '__main__':
    with open('words.txt', 'r') as fin:
        words = [line.strip() for line in fin]
    global min_num, min_comb
    findmincomb(5, words, string.ascii_lowercase)
    print(min_num, min_comb)