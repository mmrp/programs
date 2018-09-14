#!/usr/bin/python

def fact(n):
    return ((n * fact(n-1)) if n > 1 else 1)


print(fact(int(raw_input("n : "))))
