#!/usr/bin/python

def squaring(a, n):
    c = 1 
    b = a 
    while n > 1:
        if n % 2 != 0:
            c = c * b 
        b = b * b 
        n = n /2

    return c * b 



def solve(v, n):
    x0 = 0
    x1 = 1
    while abs((x1-x0)*1.0/x1) > 0.000001:
        print x1
        x0 = x1
#        s = squaring(x0, n-1)
        print x0, n-1
        s = x0**(n-1)
        x1 = (x0 * (n -1)/n) +  ((v * 1.0)/(n * s))
        raw_input()
    return x1

a = 860333223084000000000
b = 47
#print(solve(12200631968304670122098443514908031282380605686988661304109249007588992531473634756816383252952495298687, 49))
print(solve(a, b))
