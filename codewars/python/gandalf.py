#!/usr/bin/python

def tongues(code):
    low_conso = ['b', 'k', 'x', 'z', 'n', 'h', 'd', 'c', 'w', 'g', 'p', 'v', 'j', 'q', 't', 's', 'r', 'l', 'm', 'f']
    upp_conso = ['B', 'K', 'X', 'Z', 'N', 'H', 'D', 'C', 'W', 'G', 'P', 'V', 'J', 'Q', 'T', 'S', 'R', 'L', 'M', 'F']
    low_vowels  = ['a', 'i', 'y', 'e', 'o', 'u']
    upp_vowels = ['A', 'I', 'Y', 'E', 'O', 'U']

    newcode=[]
    for c in code:
        if c in low_conso:
            v = low_conso[(low_conso.index(c) + 10) % 20]
        elif c in low_vowels:
            v = low_vowels[(low_vowels.index(c) + 3) % 6]
        elif c in upp_conso:
            v = upp_conso[(upp_conso.index(c) + 10) % 20]
        elif c in upp_vowels:
            v = upp_vowels[(upp_vowels.index(c) + 3) % 6]
        else:
            v = c
        newcode.append(v)
    return ''.join(newcode)


print tongues('Ita dotf ni dyca nsaw ecc.')
