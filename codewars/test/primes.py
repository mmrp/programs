#!/usr/bin/env python3
import sys
import math
def get_primes(N):
    primes = [2, 3, 5, 7, 11, 13, 17, 19]
    p = primes[-1] + 1
    while p <= N:
        e = int(math.sqrt(p)) + 1
        i = 0
        isprime = True
        while e >= primes[i]:
            if p % primes[i] == 0:
                isprime = False
                break
            i += 1
        if isprime:
            primes.append(p)
        p += 1
    return primes

def seive(m = 2**27):
    last = int(math.sqrt(m)+1)
    primes = [True] * m
    for i in range(2, last):
        if primes[i]:
            j = i * i
            while j < m:
                primes[j] = False
                j += i
    return primes
import time
t1 = time.time()
get_primes(int(sys.argv[1]))
#seive(94906265)
t2 = time.time()
print(t2-t1)
