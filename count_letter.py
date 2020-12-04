#!/usr/bin/python3.7

import re

def count_letter(words, letter):
    wc = 0
    for i in range(len(words)):
        match = re.search(letter, words[i])
        if match:
            wc += 1
    print('Letter ' + letter + ' matched in ' + str(wc) + ' ' + 'words')

strings = ['alpha', 'bravo', 'charlie']
count_letter(strings, 'r')
