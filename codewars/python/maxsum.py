#!/usr/bin/python

def msum(arr):
    maxsofar = 0
    maxsum = 0
    for a in arr:
        if a + maxsofar < 0:
            maxsofar = 0
        else:
            maxsofar += a
        if maxsofar > maxsum:
            maxsum = maxsofar
    return maxsum

print(msum([25, -21, 12, 6, 92, -11, 17, 2, 2, 2, -7, 2, -9, 16, 2, -11]))
