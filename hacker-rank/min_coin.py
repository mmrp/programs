#!/usr/bin/python

n = int(input().strip())
a = list(map(int, input().strip().split(" ")))
s = int(input().strip())

m = [0] * (s+1)
for i in range(min(a)):
    m[i] = 0

for i in range(min(a), s+1):
    k = 10000000
    for j in range(len(a)):
        v = i - a[j] 
        if v >= 0:
            k = min(m[v] + 1, k)
    m[i] = k 
    print(i, m[i])
print(m[n])
    
