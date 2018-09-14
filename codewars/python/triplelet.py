"""
ecret = "whatisup"
triplets = [
  ['t','u','p'],
  ['w','h','i'],
  ['t','s','u'],
  ['a','t','s'],
  ['h','a','p'],
  ['t','i','s'],
  ['w','h','s']
]

There is a secret string which is unknown to you. Given a collection of random triplets from the string, recover the original string.

A triplet here is defined as a sequence of three letters such that each letter occurs somewhere before the next in the given string. "whi" is a triplet for the string "whatisup".

As a simplification, you may assume that no letter occurs more than once in the secret string.

You can assume nothing about the triplets given to you other than that they are valid triplets and that they contain sufficient information to deduce the original string. In particular, this means that the secret string will never contain letters that do not occur in one of the triplets given to you.
"""


#!/usr/bin/python
import string
def recoverSecret(triplets):
    dct = { e:set() for e in string.lowercase}
    right = set([])
    left  = set([])
    for t in triplets:
        dct[t[0]].add(t[1])
        dct[t[0]].add(t[2])
        dct[t[1]].add(t[2])
        right.add(t[1])
        right.add(t[2])
        left.add(t[0])
        left.add(t[1])
    
   # print left, right
    ne = list(right - left)[0]
    str = []
    while len(dct) > 0:
        str.append(ne)
        e = ne
        dct = {k:v for k, v in dct.items() if v}
        for k, v in dct.items():
            if e in v:
                dct[k].remove(e)
            if not dct[k]:
                ne = k
    return ''.join(str[::-1])

triplets = [
  ['t','u','p'],
  ['w','h','i'],
  ['t','s','u'],
  ['a','t','s'],
  ['h','a','p'],
  ['t','i','s'],
  ['w','h','s']
]

print recoverSecret(triplets)
import itertools
v = [list(i) for i in itertools.combinations("abcd", 3)]
print recoverSecret(v)
