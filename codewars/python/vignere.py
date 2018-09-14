#!/usr/bin/python

class VigenereCipher (object):
    def __init__(self, key, alphabet):
        self.key = key
        self.alphabet = alphabet

    def encode(self, str):
        key = self.key * (len(str)/len(self.key))
        key += self.key[:len(str) - len(key)]
        
        res = ''.join([chr((ord(key[p]) + ord(c) - 2 * ord('A')) % 26 + ord('A')) for p, c in enumerate(str)]) 
            
        print(key)
        return res

    def decode(self, str):
        key = self.key * (len(str)/len(self.key))
        key += self.key[:len(str) - len(key)]
        res = ''.join([chr((ord(c) - ord(key[p])) % 26 + ord('A')) for p, c in enumerate(str)]) 
        return res
        

        

import string
v = VigenereCipher('LEMON', string.lowercase)
r = v.encode('ATTACKATDAWN')
print(v.decode(r), r)


