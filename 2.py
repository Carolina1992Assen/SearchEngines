#!/usr/bin/python3
# This program will take an identifier of a tweet as input
# and will print the corresponding words to standard output
# Author: Carlijn Assen
# Date 08/09/2018

import pickle
import sys


def main():
    docs = pickle.load(open('docs.pickle', 'rb'))
    for line in sys.stdin:
        line = line.rstrip()
        print(docs[line][2])

if __name__ == "__main__":
    main()
