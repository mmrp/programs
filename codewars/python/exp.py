#!/usr/bin/python3

import math

def digits(s):
    s = str(s)
    if '.' in s:
        return len(s) - 1
    else:
        return len(s)

def exponent(x, d):
    s = 1
    c = 1
    m = x/c
#    while digits(s+m) <= d:
    for i in range(20):
        s += m
        c += 1
        m *= x/c
        print(s, m)
    return(s, s+m, digits(s+m), digits(s), digits(m))

print(math.exp(3), exponent(3, 10)) 
