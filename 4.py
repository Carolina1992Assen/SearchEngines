#!/usr/bin/python3
# This program will read one word from standard input,
# it will print the tweets containing that word to standard output.
# Date: 08/09/2018
# Author: Carlijn Assen

import sys
import pickle


def main():
    docs = pickle.load(open('docs.pickle', 'rb'))
    post_dict = pickle.load(open('post_dict.pickle', 'rb'))
    post_list = []

    try:
        for line in sys.stdin:
            line = line.rstrip()
            words = line.split()

        if len(words) == 1:
            post_list = post_dict[line]

            for item in post_list:
                print(docs[item][0], docs[item][1])

        else:
            print("Please enter one word.", file=sys.stderr)
        exit(-1)
    except KeyError:
        print("No tweets can be found.", file=sys.stderr)
    exit(-1)

if __name__ == "__main__":
    main()
