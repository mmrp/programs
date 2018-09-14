#!/usr/bin/python

def pow_mod(a, p, n):
    b = 1
    while p:
        if p & 1:
            b = (b*a) % n
        p = p >> 1
        a = (a*a) % n
    return b

print((pow_mod(2, 7830457, 10**10) * 28433) % 10**10) 

