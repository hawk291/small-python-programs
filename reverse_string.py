#!/usr/bin/python3.7

# reverses the given string

def reverse(w):
   reversed_word = []
   explode_word = list(w)
   for i in range(len(explode_word)):
       reversed_word.append(explode_word.pop())
   print('Your string ' + w + ' has been reversed to', end=' ')
   print(*reversed_word)

word = 'alice'
reverse(word)
