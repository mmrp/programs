#!/usr/bin/python
def find_index(a, v):
    if not a:
        return 0
    
    l = 0
    h = len(a)-1
    if v < a[l]:
        return l
    if v > a[h]:
        return h+1
    
    while l < h:
        m = (l + h)//2
        if a[m] <= v and v <= a[m+1]:
            return m+1
        elif v < a[m]:
            h = m  - 1
        elif v > a[m+1]:
            l = m + 1
            
        if v < a[l]:
            return l
        if v > a[h]:
            return h+1
    
    if a[l] <= v and v <= a[l+1]:
        return l+1  
    
def insort1(a, v):
    a.insert(find_index(a, v), v)

import random
import bisect
a = range(2000) * 2
random.shuffle(a)
print(a)
b = []
import time
t1 = time.time()
for e in a:
    insort1(b, e)
    if sorted(b) != b:
        print("secrew")
        break
print(time.time()-t1)

print(sorted(b) == b)
