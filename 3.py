#!/usr/bin/python3
# This program will build a postings list
# where the key is a word
# and where the values are the tweet identifiers in which that word occurs
# Author: Carlijn Assen
# Date: 08/09/2018

import sys
import pickle


def main():
    post_dict = {}
    l1 = []
    docs = pickle.load(open('tweets.txt', 'r'))
 
    for key, value in sorted(docs.items()):
        try:
            words = str(value[2]).split()
            l1.append(words)
            
        except:
            continue
    print(l1)
      
    
 
    
      
    

    
        
if __name__ == "__main__":
    main()
