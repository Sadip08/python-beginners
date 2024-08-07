import random

def encode(self,word):
    l = len(word)
    if l < 3:
        return word.reverse()
    else:
        return word[1:] + word[0]