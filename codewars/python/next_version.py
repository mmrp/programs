#!/usr/bin/python

def next_version(str1):

    n = map(int, str1.split("."))[::-1]
    c = 1
    for p, v in enumerate(n[:-1]):
        if v + c == 10:
            n[p] = 0
            c = 1
        else:
            n[p] = v + c
            c = 0
    n[p+1] = n[p+1] + c
    return '.'.join(map(str, n[::-1]))


print next_version("10.8.9")
