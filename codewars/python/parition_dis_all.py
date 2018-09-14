#!/usr/bin/python

def partition(n):
    if n == 1:
        return [[1]]

    l = [[n]]
    for i in range(1, n):
        for j in partition(n-i):
            l += [[i] + j]
    return l

print partition(5)
print partition(6)
