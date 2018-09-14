#!/usr/bin/python

""" given a set of numbers and sum s find
whether  exist a subset which sums to s"""


def subset(a, gs, minsum = False):
    a.sort()
    ns = sum([i for i in a if i <  0])
    ps = sum([i for i in a if i >= 0])
    if ns != 0:
        S = ps - ns + 1
    else:
        S = ps

    N  = len(a) 
    D = [[False] * (N + 1) for _ in range(S+1)]
    #print(len(D), len(D[0]))
    start = ns 
    end   = ps
    for s in range(start+1, end+1):
        for i in range(1, N + 1):
            p = s - start   
            D[p][i] = D[p][i-1] or (a[i-1] == s) or (D[s-a[i-1]][i-1] if s >= a[i-1] else False)
    #print(D)

    if minsum:
        s = min([(abs(S - 2*s), s) for s in range(S+1) if D[s][N] is True])[1]
        print('min s', s, S-s)
    else:
        s = gs - start 
    k = N
    A = set([])
    B = set(a)
    while s != 0:
        if D[s][k] == False:
            return []
        while D[s][k] == True:
            k -= 1
        A.add(a[k]) # values of array a are zero indexed but the k is already decreased in above
        s = s - a[k]
    print('sets: ', A, B - A)
import random
a = range(random.randint(100, 200))
random.shuffle(a)
print('total sum', sum(a))
subset(a, 43, True)
