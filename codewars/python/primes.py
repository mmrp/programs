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

print(get_primes(int(sys.argv[1])))
