#!/usr/bin/env python

def permute(a, s, n):
    if s == n:
        print(a)
        return

    for i in range(s, n, 1):
        a[s], a[i] = a[i], a[s]
        permute(a, s+1, n)
        a[s], a[i] = a[i], a[s]

    return

n = int(raw_input())
permute(range(1, n+1), 0, n)
