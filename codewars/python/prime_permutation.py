#!/usr/bin/env python3

from primes import get_primes
import sys
def kperm(N, C):
    C += 1
    primes = get_primes(N)
    print([int(''.join(sorted(str(p)))) for p in primes])
    cprimes = dict()
    for p in primes:
        e = ''.join(sorted(str(p)))
        if e not in cprimes:
            cprimes[e] = []
        cprimes[e].append(p)
    print(cprimes)
    s = sorted([cprimes[k][0] for  k in cprimes if len(cprimes[k]) == C])
    print(s)
    if len(s) >= 2:
        return [len(s), s[0], s[-1]]
    else:
        return [0, 0, 0]

print(kperm(int(sys.argv[1]), int(sys.argv[2])))
