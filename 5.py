#!/usr/bin/python3
# This program will read either one or two words from standard input,
# it will print the tweets in which the word(s) occur to standard output.
# Author: Carlijn Assen
# Date: 08/09/2018

import pickle
import sys


def forin(alist, blist):
    return [obj for obj in blist if obj in alist]


def main():
    docs = pickle.load(open('docs.pickle', 'rb'))
    post_dict = pickle.load(open('post_dict.pickle', 'rb'))
    try:
        for line in sys.stdin:
            line = line.rstrip()
            words = line.split()

        if len(words) == 1:
            post_list = post_dict[line]

            for item in post_list:
                print(docs[item][0], docs[item][1])

        if len(words) == 2:
            word1 = words[0]
            word2 = words[1]

            word1_list = post_dict[word1]
            word2_list = post_dict[word2]
            id_list = (forin(word1_list, word2_list))

            for item in id_list:
                print(docs[item][0], docs[item][1])

        else:
            print("Please enter either one or two words.", file=sys.stderr)
        exit(-1)
    except KeyError:
        print("No tweets can be found.", file=sys.stderr)
    exit(-1)

if __name__ == "__main__":
    main()
