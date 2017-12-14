#!/usr/bin/env python3

"""wcount.py: count words from an Internet file.

__author__ = "Cai Jiaji"
__pkuid__  = "1700017797"
__email__  = "jiajicaiyp@pku.edu.cn"
"""

import sys
from urllib.request import urlopen

def clean(word):
    alphabet = 'qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM'
    better = ''
    for char in word:
        if char in alphabet:
            better = better + char
    return better

def wcount(lines, topn=10):
    """count words from lines of text string, then sort by their counts
    in reverse order, output the topn (word count), each in one line. 
    """
    lst = lines.split()
    
    for (i,word) in enumerate(lst):
        lst[i] = clean(word)
        
    alphabet = 'qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM'
    raw_english = []
    for word in lst:
        if set(word).issubset(set(alphabet)):
            raw_english.append(word)
            
    english = []
    for word in raw_english:
        temp = word.lower()
        english.append(temp)
        
    vocab = list(set(english))
    
    freq = []
    for word in vocab:
        time = english.count(word)
        freq.append(time)
        
    corr = {}
    for i in range(len(freq)):
        corr[freq[i]] = vocab[i]
        
    freq.sort(reverse = True)
    out_freq = freq[:topn]
    
    out_vocab = []
    for time in out_freq:
        out_vocab.append(corr[time])
        
    for i in range(topn):
        print(out_vocab[i],'  ',out_freq[i])
        
    pass

if __name__ == '__main__':

    if  len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)

    try:
        topn = 10
        if len(sys.argv) == 3:
            topn = int(sys.argv[2])
    except ValueError:
        print('{} is not a valid topn int number'.format(sys.argv[2]))
        sys.exit(1)

    try:
        with urlopen(sys.argv[1]) as f:
            contents = f.read()
            lines   = contents.decode()
            wcount(lines, topn)
    except Exception as err:
        print(err)
        sys.exit(1)
