#!/usr/bin/python

def value(a, i, n, cost, shares):
    #print(i, cost, shares)
    if i == n:
        return cost
    #print(i, cost, shares)
    v = 0
    if shares > 0:
        v = max(value(a, i+1, n, cost + j * a[i], shares - j) for j in range(1, shares+1))
    return max(value(a, i+1, n, cost, shares), value(a, i+1, n, cost - a[i], shares + 1), v)
q = int(input().strip())
for i in range(q):
    n = int(input().strip())
    a = list(map(int, input().strip().split(" ")))
    print(value(a, 0, len(a), 0, 0))
