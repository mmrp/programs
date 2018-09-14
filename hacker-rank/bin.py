#!/usr/bin/python
def binsearch(a, v):
    l = 0
    h = len(a) - 1
    while l <= h:
        m = (l+h)//2
        if v < a[m]:
            h = m -1
        elif v > a[m]:
            l = m + 1
        else:
            return a[m]
    return -1

a = list(map(int, input().strip().split(' ')))
v = int(input().strip())
a.sort()
print(binsearch(a, v))

        
