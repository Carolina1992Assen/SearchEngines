#!/usr/bin/python3
# This program builds a dictionary,
# where the identifier of the tweet is the key
# and where the value is a tuple containing user, text and words.
# It will save this dictionary in a pickle file
# Author: Carlijn Assen
# Date: 08/09/2018

import sys
import pickle


def main():
    docs = {}
    file = open("tweets.txt", "r")
    for line in file:
        line = line.rstrip()
        line = line.split("\t")
        docs[line[0]] = (line[1], line[2], line[3])
    with open('docs.pickle', 'wb') as f:
        pickle.dump(docs, f)

if __name__ == "__main__":
    main()
