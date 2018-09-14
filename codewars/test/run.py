#!/usr/bin/env python3

import math

def valid_number(n, divisors):
    #print(n, divisors)
    for p in divisors:
        v = math.log((((n-1)*(p-1)/p)+1), p)
        if int(v) == v:
            return p
    return -1

def divisors(n):
    m = int(math.sqrt(n))+1
    l = int(math.sqrt(n))+1
    if n % 2 == 0:
        s = 2
    else:
        s = 3
    divisors = []
    while s < l:
        if n % s == 0:
            c = n // s
            divisors.append(s)
            if c != s:
                divisors.append(c)
            l = c
        s += 2
    divisors.append(n)
    return sorted(divisors)

def get_smallest(n):
    return valid_number(n, divisors(n-1))

import sys
if __name__ == '__main__':
    if (len(sys.argv) != 2):
        print('Usage: {} number'.format(sys.argv[0]))
        sys.exit(1)
    print(sys.argv[1], get_smallest(int(sys.argv[1])))
