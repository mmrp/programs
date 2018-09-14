#!/usr/bin/env python


def val(v, p):
    return (v**(p-1)-1)/(v-1)

def findbase(n):
    l = 1
    h = 9007199254740991
    while l <= h:
        m = (l+h)/2
        v = val(n, m)
        if l >
