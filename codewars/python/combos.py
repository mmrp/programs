#!/usr/bin/python

def combos1(n):
    if n == 1:
        return 1
    d = 1
    for i in range(1, n/2+1):
        d += combos(i) * combos(n-i)
    return d



p = {1: [[1]]}
def partition(n):
    if n in p:
        return p[n]

    r = [[n]]
    for i in range(n-1, 0, -1):
        f = i
        s = partition(n - i)
        for e in s:
            if e[0] <= f:
                r.append([f] + e)

    p[n] = r
    return r

print(partition(4))

